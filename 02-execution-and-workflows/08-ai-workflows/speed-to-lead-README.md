---
id: mcp-speed-to-lead-readme
type: automation
tags: [mcp, automation, proof-of-concept]
last_modified: 2026-09-25
---

# Speed-to-Lead SLA MCP Server (Proof of Concept)

The first real implementation of the "L2 Automation" layer this repo's architecture has promised since CLAUDE.md was written -- see the 2026-09-25 audit, Critical Finding #3: every Workflow Contract declared `allowed_mcp_tools` but none of them existed as actual code. This closes that gap for one contract, [speed-to-lead-sla-contract](../../gtm-prompt-library/contracts/speed-to-lead-sla-contract.md), as a template for the other three.

**Run the smoke test (works with no setup, no credentials):**
```bash
python3 gtm-os/mcp/speed-to-lead/speed_to_lead_server.py --selftest
```
This reads `mock_data.json`, evaluates each lead against the SLA windows, and logs mock Slack/sequencer actions to `notification_log.jsonl` (gitignored -- see below).

## What's real vs. mocked
| Tool | Status |
|---|---|
| `evaluate_sla_breach` | **Real logic.** Tier -> deadline -> OK/AT_RISK/BREACHED, sourced from the same SLA windows [sales-development-strategy](../../gtm-prompt-library/skills/sales-development-strategy.md) and [inbound-playbook](../../gtm-prompt-library/agents/inbound-playbook.md) document. |
| `crm_read_new_leads` | Mocked -- reads `mock_data.json`. Replace with a Salesforce SOQL query. |
| `calendar_read_no_shows` | Mocked -- reads `mock_data.json`. Replace with a Calendar/Chili Piper API read. |
| `slack_notify` | Mocked -- appends to `notification_log.jsonl` + prints to stderr. Replace with `slack_sdk.WebClient.chat_postMessage`. |
| `sequencer_enqueue` | Mocked -- appends to `notification_log.jsonl`. Replace with an Outreach/Salesloft API call. |

## Wiring real data
1. Get a Salesforce API user (or Connected App OAuth) with read access to Lead/Contact; replace `crm_read_new_leads`'s body with a `simple-salesforce` SOQL query on `CreatedDate`.
2. Same pattern for a calendar/Chili Piper API in `calendar_read_no_shows`.
3. Add a Slack bot token scoped only to the channel(s) this contract's `boundaries.allowed_mcp_tools` permit; swap `slack_notify`'s body for a real `chat_postMessage` call.
4. Add Outreach/Salesloft API credentials for `sequencer_enqueue` -- **route every call through the CASL compliance gate first** ([casl-compliance-gate-contract](../../gtm-prompt-library/contracts/casl-compliance-gate-contract.md)) before it goes live, since this contract alone doesn't check consent.
5. Register the server with an MCP client (`claude mcp add speed-to-lead-sla -- python3 gtm-os/mcp/speed-to-lead/speed_to_lead_server.py`) once `pip install mcp` succeeds somewhere with PyPI access -- note this failed on Peyton's own device during this build (network egress blocked the PyPI proxy), so this step needs either a network exception or running the server from a machine/container that has one.

## Why this one contract first
Speed-to-lead is the highest-leverage automation in the whole prompt library to get right: the SLA windows are minutes, not days, so a human-in-the-loop chat invocation is structurally too slow to enforce it. `pipeline-risk` and `inbound-lead-qualifier` are the next-best candidates to wire up using this same pattern.

## See Also
00-Automation-Layer-Index . [speed-to-lead-sla-contract](../../gtm-prompt-library/contracts/speed-to-lead-sla-contract.md) . [speed-to-lead-sla-enforcer](../../gtm-prompt-library/agents/speed-to-lead-sla-enforcer.md) . Tool I/O Schema
