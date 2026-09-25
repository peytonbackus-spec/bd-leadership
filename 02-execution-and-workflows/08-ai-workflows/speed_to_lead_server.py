"""
Speed-to-Lead SLA MCP Server -- Proof of Concept
==================================================

Implements the `allowed_mcp_tools` declared in
gtm-os/contracts/speed-to-lead-sla-contract.yaml as real, callable MCP
tools, closing the "zero automation layer" gap flagged in the
2026-09-25 vault audit (intelligence/weekly/vault-audit-2026-09-25.md,
Critical Finding #3).

STATUS: proof of concept. The contract's real objective is enforcing SLA
response windows against a live CRM + calendar + sequencer. This server
implements the correct TOOL SHAPES (names, inputs, outputs) so an MCP
client (e.g. this Claude session, via `claude mcp add`) can call them
today, but three of the four tools currently read from
`gtm-os/mcp/speed-to-lead/mock_data.json` instead of a real Salesforce/
calendar/sequencer API. Swap the `_mock_*` functions for real API calls
(see gtm-os/mcp/speed-to-lead/README.md, "Wiring real data") without
changing the tool signatures the contract already declares.

Run standalone for a smoke test:
    python3 speed_to_lead_server.py --selftest

Run as an MCP server (stdio transport) once `pip install mcp` succeeds
in an environment with network access to PyPI:
    python3 speed_to_lead_server.py
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from typing import Any

try:
    from mcp.server.fastmcp import FastMCP
    _HAVE_MCP = True
except ImportError:
    _HAVE_MCP = False

    class FastMCP:  # minimal no-op shim so --selftest works without the mcp package installed
        def __init__(self, *_args, **_kwargs):
            pass

        def tool(self):
            def _decorator(fn):
                return fn
            return _decorator

        def run(self):
            raise RuntimeError(
                "The 'mcp' package is not installed in this environment. "
                "Run 'pip install mcp' somewhere with PyPI access, then run this "
                "server there (or use --selftest here, which works without it)."
            )

MOCK_DATA_PATH = os.path.join(os.path.dirname(__file__), "mock_data.json")

mcp = FastMCP("speed-to-lead-sla")

# SLA windows by score tier, per wiki/skills/sales-development-strategy.md
# and the inbound-playbook agent -- centralized here so the contract's
# enforcement logic and the human-readable docs can't silently diverge.
SLA_MINUTES_BY_TIER = {
    "Tier 1 (Hot)": 5,
    "Tier 2 (Warm)": 30,
    "Tier 3 (Cold)": 1440,  # next business day
}


def _load_mock_data() -> dict:
    with open(MOCK_DATA_PATH) as f:
        return json.load(f)


def _parse_iso(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


@mcp.tool()
def crm_read_new_leads(since_minutes: int = 60) -> list:
    """
    Read leads created in the CRM within the last `since_minutes` minutes.

    MOCK: reads gtm-os/mcp/speed-to-lead/mock_data.json's "leads" array.
    Real implementation: replace with a Salesforce SOQL query against
    Lead/Contact `CreatedDate`, filtered to your inbound record types.
    """
    data = _load_mock_data()
    cutoff = datetime.now(timezone.utc) - timedelta(minutes=since_minutes)
    return [
        lead for lead in data.get("leads", [])
        if _parse_iso(lead["created_at"]) >= cutoff
    ]


@mcp.tool()
def calendar_read_no_shows(lookback_hours: int = 24) -> list:
    """
    Read booked meetings within `lookback_hours` that were marked as
    no-shows and have not yet had a recovery cadence triggered.

    MOCK: reads gtm-os/mcp/speed-to-lead/mock_data.json's "meetings"
    array. Real implementation: replace with a Calendar/Chili Piper API
    read, joined against CRM activity to detect the no-show flag.
    """
    data = _load_mock_data()
    cutoff = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
    return [
        m for m in data.get("meetings", [])
        if m.get("status") == "no_show"
        and not m.get("recovery_triggered", False)
        and _parse_iso(m["scheduled_at"]) >= cutoff
    ]


@mcp.tool()
def evaluate_sla_breach(lead: dict) -> dict:
    """
    Given a lead record (as returned by crm_read_new_leads), determine
    its SLA tier, deadline, and whether it is currently breached or
    approaching breach (within 20% of its window).

    Real logic, not mocked -- SLA_MINUTES_BY_TIER above is the single
    source of truth the contract enforces against, matching what
    wiki/skills/sales-development-strategy.md and inbound-playbook
    document.
    """
    tier = lead.get("score_tier", "Tier 3 (Cold)")
    window_minutes = SLA_MINUTES_BY_TIER.get(tier, SLA_MINUTES_BY_TIER["Tier 3 (Cold)"])
    created_at = _parse_iso(lead["created_at"])
    deadline = created_at + timedelta(minutes=window_minutes)
    now = datetime.now(timezone.utc)
    minutes_remaining = (deadline - now).total_seconds() / 60

    if minutes_remaining < 0:
        status = "BREACHED"
    elif minutes_remaining <= window_minutes * 0.2:
        status = "AT_RISK"
    else:
        status = "OK"

    return {
        "lead_id": lead.get("id"),
        "tier": tier,
        "sla_window_minutes": window_minutes,
        "deadline_utc": deadline.isoformat(),
        "minutes_remaining": round(minutes_remaining, 1),
        "status": status,
    }


@mcp.tool()
def slack_notify(channel: str, message: str) -> dict:
    """
    Post an SLA breach/at-risk/no-show-recovery alert to Slack.

    MOCK: prints to stderr and appends to
    gtm-os/mcp/speed-to-lead/notification_log.jsonl instead of calling
    the real Slack API. Real implementation: replace with a
    `slack_sdk.WebClient.chat_postMessage` call using a bot token scoped
    to only the channels this contract's boundaries permit.
    """
    entry = {"channel": channel, "message": message, "sent_at": datetime.now(timezone.utc).isoformat()}
    log_path = os.path.join(os.path.dirname(__file__), "notification_log.jsonl")
    with open(log_path, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"[MOCK slack_notify] #{channel}: {message}", file=sys.stderr)
    return {"ok": True, "mock": True, **entry}


@mcp.tool()
def sequencer_enqueue(contact_id: str, cadence_name: str) -> dict:
    """
    Enqueue a contact into a named outreach cadence (e.g. a no-show
    recovery sequence).

    MOCK: appends to gtm-os/mcp/speed-to-lead/notification_log.jsonl.
    Real implementation: replace with an Outreach/Salesloft API call to
    add the prospect to the named sequence. In production this should be
    gated by the casl-compliance-gate-contract's consent check first --
    see CLAUDE.md section 2's router note that contracts share the same
    lookup/enforcement discipline as human-invoked agents.
    """
    entry = {
        "action": "sequencer_enqueue", "contact_id": contact_id,
        "cadence_name": cadence_name, "enqueued_at": datetime.now(timezone.utc).isoformat(),
    }
    log_path = os.path.join(os.path.dirname(__file__), "notification_log.jsonl")
    with open(log_path, "a") as f:
        f.write(json.dumps(entry) + "\n")
    return {"ok": True, "mock": True, **entry}


def _selftest() -> None:
    print("=== crm_read_new_leads ===")
    leads = crm_read_new_leads(since_minutes=10_000_000)
    print(json.dumps(leads, indent=2))

    print("\n=== evaluate_sla_breach (each lead) ===")
    for lead in leads:
        result = evaluate_sla_breach(lead)
        print(json.dumps(result, indent=2))
        if result["status"] in ("BREACHED", "AT_RISK"):
            slack_notify(
                "revops-alerts",
                f"Lead {result['lead_id']} is {result['status']} "
                f"({result['tier']}, {result['minutes_remaining']} min remaining)",
            )

    print("\n=== calendar_read_no_shows ===")
    no_shows = calendar_read_no_shows(lookback_hours=10_000_000)
    print(json.dumps(no_shows, indent=2))
    for m in no_shows:
        sequencer_enqueue(m["contact_id"], "no-show-recovery-v1")

    print("\nSelf-test complete. See notification_log.jsonl for mock side effects.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest or not _HAVE_MCP:
        _selftest()
    else:
        mcp.run()
