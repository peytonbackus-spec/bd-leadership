---
id: contract-speed-to-lead-sla
type: contract-index
tags: [contract, workflow-contract, inbound-sdr]
last_modified: 2026-09-25
confidence_score: 1.0
---

# Speed-to-Lead SLA Agent -- Workflow Contract

Companion note for `speed-to-lead-sla-contract.yaml` -- resolves `[speed-to-lead-sla-contract](speed-to-lead-sla-contract.md)` wikilinks.

**Real file:** `gtm-os/contracts/speed-to-lead-sla-contract.yaml`

**Objective:** Enforce SLA response windows on inbound leads by score tier, and trigger no-show recovery cadences for missed booked meetings. **Reads:** `wiki/skills/inbound-playbook`, `wiki/competitive/Chili Piper`. **Writes:** `intelligence/daily/`. **MCP tools:** `calendar_read`, `crm_read`, `slack_notify`, `sequencer_enqueue`. Promoted from the human-invoked [speed-to-lead-sla-enforcer](../agents/speed-to-lead-sla-enforcer.md) prompt agent.

> **Automation built (proof of concept):** the speed-to-lead MCP server implements this contract's tools -- 1 of 5 is real logic, 4 are mocked pending CRM/calendar/Slack/sequencer credentials.

## See Also
[speed-to-lead-sla-enforcer](../agents/speed-to-lead-sla-enforcer.md) . 00-Agent-Router . full-org-agent-taxonomy
