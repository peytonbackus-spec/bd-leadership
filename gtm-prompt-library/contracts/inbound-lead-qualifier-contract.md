---
id: contract-inbound-lead-qualifier
type: contract-index
tags: [contract, workflow-contract, inbound-sdr]
last_modified: 2026-09-25
---

# Inbound Lead Qualifier Agent -- Workflow Contract

Companion note for `inbound-lead-qualifier-contract.yaml` -- resolves `[inbound-lead-qualifier-contract](inbound-lead-qualifier-contract.md)` wikilinks.

**Real file:** `gtm-os/contracts/inbound-lead-qualifier-contract.yaml`

**Objective:** Enrich, dedupe, score, and route every new inbound lead within 5 minutes of CRM creation, before human review. **Reads:** `wiki/skills/icp-builder`, `wiki/concepts/gtm-tool-data-models`. **Writes:** `intelligence/daily/`. **MCP tools:** `crm_read`, `crm_write_custom_fields_only`, `clay_enrich`, `slack_notify`. Promoted from the human-invoked [inbound-lead-qualifier](../agents/inbound-lead-qualifier.md) prompt agent.

## See Also
[inbound-lead-qualifier](../agents/inbound-lead-qualifier.md) . 00-Agent-Router . full-org-agent-taxonomy
