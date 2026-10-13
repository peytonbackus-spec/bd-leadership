"""Outbound hook pipeline: geo-gate, build a human-review queue, then (dry-run) enroll.

`build` joins contacts to accounts, applies the geography policy (the same
geo-policy.csv that score_accounts.py uses), and writes a templated opening hook
per allowed contact to approval_queue.csv for human review. Contacts at `block`
accounts are skipped; contacts at `review` (or unknown-geography) accounts go to
compliance_hold.csv with the reason. Every skip and hold is logged.

The hook is a fixed string template, not an LLM call; prompts/first_line.md is
the prompt a live version would send. `enroll` is a dry run: it makes no API
call to any sequencer.
"""
import importlib.util
import sys
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ACCOUNTS = REPO_ROOT / 'sample-data' / 'accounts.csv'
DEFAULT_CONTACTS = REPO_ROOT / 'sample-data' / 'contacts.csv'
SCORE_ACCOUNTS = REPO_ROOT / '01-strategy-and-operations' / '02-icp-and-account-scoring' / 'score_accounts.py'

# Reuse the scorer's geo-policy loader so both scripts apply one policy.
_spec = importlib.util.spec_from_file_location("score_accounts", SCORE_ACCOUNTS)
_scoring = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_scoring)


def build_hooks(accounts: pd.DataFrame, contacts: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(contacts, accounts, on='account_id', how='inner')
    merged['generated_hook'] = merged.apply(
        lambda r: f"Hi {r['first_name']}, saw your focus on {r['title']} at {r['account_name']}. Worth connecting on modernizing your pipeline stack?",
        axis=1
    )
    return merged


def apply_geo_gate(merged: pd.DataFrame, geo_policy_file=_scoring.DEFAULT_GEO_POLICY):
    """Split contacts into (allowed, held, blocked), each with geo_status and geo_reason columns."""
    statuses = _scoring.load_geo_policy(geo_policy_file)
    reasons = _scoring.load_geo_policy(geo_policy_file, field="reason")
    merged = merged.copy()
    for col in ("country", "region"):
        if col not in merged:
            merged[col] = ""
        merged[col] = merged[col].fillna("").astype(str)
    codes = [_scoring.geo_match(c, r, statuses) for c, r in zip(merged['country'], merged['region'])]
    merged['geo_status'] = [statuses[c] if c else "review" for c in codes]
    merged['geo_reason'] = [
        f"{c}: {reasons[c] or statuses[c]}" if c else "geography missing from geo policy"
        for c in codes
    ]
    allowed = merged[merged['geo_status'] == "allow"]
    held = merged[merged['geo_status'] == "review"]
    blocked = merged[merged['geo_status'] == "block"]
    return allowed, held, blocked


def run_pipeline(mode, accounts_file=DEFAULT_ACCOUNTS, contacts_file=DEFAULT_CONTACTS,
                 output_file='approval_queue.csv', hold_file='compliance_hold.csv',
                 geo_policy_file=_scoring.DEFAULT_GEO_POLICY):
    print(f"=== Running Hook Pipeline in [{mode.upper()}] Mode ===")
    if mode not in ('build', 'enroll'):
        raise ValueError(f"Unknown mode '{mode}'; use 'build' or 'enroll'.")

    merged = build_hooks(pd.read_csv(accounts_file), pd.read_csv(contacts_file))
    allowed, held, blocked = apply_geo_gate(merged, geo_policy_file)
    for _, r in blocked.iterrows():
        print(f"SKIP  {r['first_name']} {r['last_name']} @ {r['account_name']} - geo block ({r['geo_reason']})")
    for _, r in held.iterrows():
        print(f"HOLD  {r['first_name']} {r['last_name']} @ {r['account_name']} - compliance review ({r['geo_reason']})")

    if mode == 'build':
        allowed.to_csv(output_file, index=False)
        held.to_csv(hold_file, index=False)
        print(f"Generated {len(allowed)} prospect hooks. Pending human review in '{output_file}'.")
        print(f"Held {len(held)} for compliance review in '{hold_file}'; skipped {len(blocked)} blocked.")
    else:
        print(f"DRY RUN: would enroll {len(allowed)} reviewed records into sequences "
              f"({len(held)} held, {len(blocked)} blocked).")
        print("No sequencer API is called; wire one in after the pre-send compliance gate.")
    return allowed


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'build'
    run_pipeline(mode)
