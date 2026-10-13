---
id: mcp-speed-to-lead-readme
type: automation
tags: [mcp, automation, proof-of-concept]
last_modified: 2026-09-25
---

# Speed-to-Lead SLA MCP Server (Proof of Concept)

A working proof of concept for one of the three Workflow Contracts, [speed-to-lead-sla-contract](../../gtm-prompt-library/contracts/speed-to-lead-sla-contract.md): the contract's tools exist as callable MCP tools, with SLA evaluation as real logic and data access mocked. It is a template for wiring the other two contracts. It has not been run against a live CRM.

**Run the smoke test (works with no setup, no credentials):**
```bash
python3 02-execution-and-workflows/08-ai-workflows/speed_to_lead_server.py --selftest
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

**Tool names vs. the contract YAML:** the contract's `allowed_mcp_tools` lists exactly the five tools this server registers. [tests/test_speed_to_lead_contract.py](../../tests/test_speed_to_lead_contract.py) fails if the two drift apart.

## Wiring real data
1. Get a Salesforce API user (or Connected App OAuth) with read access to Lead/Contact; replace `crm_read_new_leads`'s body with a `simple-salesforce` SOQL query on `CreatedDate`.
2. Same pattern for a calendar/Chili Piper API in `calendar_read_no_shows`.
3. Add a Slack bot token scoped only to the channel(s) this contract's `boundaries.allowed_mcp_tools` permit; swap `slack_notify`'s body for a real `chat_postMessage` call.
4. Add Outreach/Salesloft API credentials for `sequencer_enqueue` -- **route every call through the CASL compliance gate first** ([casl-compliance-gate-contract](../../gtm-prompt-library/contracts/casl-compliance-gate-contract.md)) before it goes live, since this contract alone doesn't check consent.
5. Register the server with an MCP client (`claude mcp add speed-to-lead-sla -- python3 02-execution-and-workflows/08-ai-workflows/speed_to_lead_server.py`) after `pip install mcp`. Without the `mcp` package the script falls back to `--selftest`. Live MCP-client registration has not been tested in this repo.

## Why this one contract first
Speed-to-lead is the highest-leverage automation in the prompt library to get right. The SLA windows are minutes, not days, so a human-in-the-loop chat invocation is too slow to enforce them. [inbound-lead-qualifier](../../gtm-prompt-library/contracts/inbound-lead-qualifier-contract.md) is the next candidate for the same pattern.

## See Also
[speed-to-lead-sla-contract](../../gtm-prompt-library/contracts/speed-to-lead-sla-contract.md) . [speed-to-lead-sla-enforcer](../../gtm-prompt-library/agents/speed-to-lead-sla-enforcer.md) . [Tool I/O Schema](../../gtm-prompt-library/schemas/speed-to-lead-sla.schema.json) . [AI workflows index](./README.md)
