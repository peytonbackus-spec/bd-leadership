"""Score target accounts on ICP fit plus a time-decayed signal, gated by geo policy.

Fit (employees, revenue, Salesforce in stack) is worth up to 80 points. The
account's most recent signal (signal_type + signal_date) adds up to 20 points,
decayed by decay_calculator.py's half-lives. Tier 1 requires an *active* signal:
decayed strength at or above --min-signal-strength (default 0.5, i.e. within one
half-life). Fit-only accounts cap at Tier 2.

Accounts in a geography marked `block` in geo-policy.csv score 0 and are
excluded. `review` geographies keep their score but are flagged for compliance
sign-off before any outreach. A missing or unknown geography is treated as
`review`.

Usage:
    python3 score_accounts.py [input.csv] [--output out.csv] [--geo-policy policy.csv]
                              [--as-of YYYY-MM-DD] [--min-signal-strength 0.5]
"""
import argparse
import importlib.util
from datetime import datetime
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = REPO_ROOT / "sample-data" / "accounts.csv"
DEFAULT_OUTPUT = REPO_ROOT / "sample-data" / "scored_accounts.csv"
DEFAULT_GEO_POLICY = REPO_ROOT / "04-compliance-and-coverage" / "13-compliance" / "geo-policy.csv"
DECAY_CALCULATOR = REPO_ROOT / "01-strategy-and-operations" / "03-signals-and-research" / "decay_calculator.py"

GEO_STATUSES = {"allow", "review", "block"}
EXCLUDED_TIER = "Excluded (geo block)"
SIGNAL_MAX_POINTS = 20
DEFAULT_MIN_SIGNAL_STRENGTH = 0.5

# Load the decay model by file path (its directory name is not importable).
_spec = importlib.util.spec_from_file_location("decay_calculator", DECAY_CALCULATOR)
_decay = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_decay)
calculate_decayed_score = _decay.calculate_decayed_score


def load_geo_policy(path=DEFAULT_GEO_POLICY, field="status") -> dict:
    """Map ISO country codes and ISO 3166-2 region codes to a policy column (status by default)."""
    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    unknown = set(df["status"]) - GEO_STATUSES
    if unknown:
        raise ValueError(f"Unknown geo policy status in {path}: {sorted(unknown)}")
    policy = {}
    for row in df.to_dict("records"):
        code = (row["region_code"] or row["country_code"]).strip().upper()
        policy[code] = row[field]
    return policy


def geo_match(country: str, region: str, policy: dict) -> str:
    """Return the policy code that applies; a region row (e.g. UA-43) overrides its country row (e.g. UA)."""
    for code in (region, country):
        code = str(code or "").strip().upper()
        if code and code in policy:
            return code
    return ""


def geo_status(country: str, region: str, policy: dict) -> str:
    code = geo_match(country, region, policy)
    return policy[code] if code else "review"


def fit_points(row):
    score = 0
    # Firmographic Fit
    employees = float(row.get('employees', 0))
    if 250 <= employees <= 5000:
        score += 30
    elif employees > 5000:
        score += 20

    revenue = float(row.get('revenue_m', 0))
    if 50 <= revenue <= 1000:
        score += 30
    elif revenue > 1000:
        score += 20

    # Tech Stack Fit
    if str(row.get('has_salesforce', '')).strip().lower() in ['true', '1', 'yes']:
        score += 20

    return score


def signal_strength(signal_type, signal_date, as_of: datetime) -> float:
    """Decayed weight of the signal (1.0 = fresh, 0.5 = one half-life old, 0.0 = none or unparseable)."""
    signal_type = str(signal_type or "").strip()
    signal_date = str(signal_date or "").strip()
    if not signal_type or not signal_date:
        return 0.0
    try:
        return calculate_decayed_score(1.0, signal_type, signal_date, as_of)
    except ValueError:
        return 0.0


def assign_tier(score: int, status: str, active_signal: bool = True) -> str:
    if status == "block":
        return EXCLUDED_TIER
    if score >= 80 and active_signal:
        return 'Tier 1'
    if score >= 50:
        return 'Tier 2'
    return 'Tier 3'


def score_frame(df: pd.DataFrame, policy: dict, as_of: datetime = None,
                min_signal_strength: float = DEFAULT_MIN_SIGNAL_STRENGTH) -> pd.DataFrame:
    as_of = as_of or datetime.now()
    df = df.copy()
    for col in ("country", "region", "signal_type", "signal_date"):
        if col not in df:
            df[col] = ""
        df[col] = df[col].fillna("").astype(str)
    df['geo_status'] = [geo_status(c, r, policy) for c, r in zip(df['country'], df['region'])]
    df['signal_strength'] = [signal_strength(t, d, as_of) for t, d in zip(df['signal_type'], df['signal_date'])]
    df['active_signal'] = df['signal_strength'] >= min_signal_strength
    df['signal_points'] = (df['signal_strength'] * SIGNAL_MAX_POINTS).round().astype(int)
    df['fit_score'] = df.apply(fit_points, axis=1) + df['signal_points']
    df.loc[df['geo_status'] == "block", 'fit_score'] = 0
    df['tier'] = [assign_tier(s, g, a) for s, g, a in zip(df['fit_score'], df['geo_status'], df['active_signal'])]
    return df


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("input", nargs="?", default=str(DEFAULT_INPUT))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--geo-policy", default=str(DEFAULT_GEO_POLICY))
    parser.add_argument("--as-of", help="Reference date for signal decay (YYYY-MM-DD); defaults to today")
    parser.add_argument("--min-signal-strength", type=float, default=DEFAULT_MIN_SIGNAL_STRENGTH,
                        help="Decayed signal strength (0-1) required for Tier 1")
    args = parser.parse_args(argv)

    try:
        df = pd.read_csv(args.input)
    except Exception as e:
        print(f"Error loading {args.input}: {e}")
        return

    if "hiring_signal" in df and "signal_type" not in df:
        print("Note: 'hiring_signal' is no longer scored; provide signal_type and signal_date columns.")

    as_of = datetime.strptime(args.as_of, "%Y-%m-%d") if args.as_of else None
    scored = score_frame(df, load_geo_policy(args.geo_policy), as_of, args.min_signal_strength)

    print("=== Account Scoring Summary ===")
    print(scored[['account_name', 'country', 'signal_type', 'signal_strength', 'geo_status', 'fit_score', 'tier']].to_string(index=False))
    review = scored[scored['geo_status'] == "review"]
    if not review.empty:
        print(f"\n{len(review)} account(s) need compliance review before outreach: "
              + ", ".join(review['account_name']))
    scored.to_csv(args.output, index=False)
    print(f"\nSaved scored output to {args.output}")


if __name__ == '__main__':
    main()
