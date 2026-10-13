---
id: contract-speed-to-lead-sla
type: contract-index
tags: [contract, workflow-contract, inbound-sdr]
last_modified: 2026-09-25
---

# Speed-to-Lead SLA Agent -- Workflow Contract

Companion note for `speed-to-lead-sla-contract.yaml` -- gives the YAML contract a markdown page so other notes can link to it with a real relative link instead of a bare filename.

**Real file:** [`speed-to-lead-sla-contract.yaml`](./speed-to-lead-sla-contract.yaml) (paths are repo-relative)

**Objective:** Enforce SLA response windows on inbound leads by score tier, and trigger no-show recovery cadences for missed booked meetings. **Role map:** `sla_timer_agent` (per-tier SLA clock + escalation) -> `noshow_recovery_agent` (3-touch recovery cadence via milestone-sequencer). **Reads:** `gtm-prompt-library/agents/inbound-playbook.md`, `02-execution-and-workflows/09-gtm-tool-evaluation/Chili Piper.md`, `02-execution-and-workflows/08-ai-workflows/mock_data.json`. **Writes:** `02-execution-and-workflows/08-ai-workflows/notification_log.jsonl` (gitignored). **MCP tools:** `crm_read_new_leads`, `calendar_read_no_shows`, `evaluate_sla_breach`, `slack_notify`, `sequencer_enqueue` (a test checks these match the server). Promoted from the human-invoked [speed-to-lead-sla-enforcer](../agents/speed-to-lead-sla-enforcer.md) prompt agent.

> **Automation built (proof of concept):** the speed-to-lead MCP server implements this contract's tools -- 1 of 5 is real logic, 4 are mocked pending CRM/calendar/Slack/sequencer credentials. See [speed-to-lead-README](../../02-execution-and-workflows/08-ai-workflows/speed-to-lead-README.md).

## See Also
[speed-to-lead-sla-enforcer](../agents/speed-to-lead-sla-enforcer.md) . [gtm-prompt-library/README](../README.md)
