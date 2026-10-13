---
id: contract-inbound-lead-qualifier
type: contract-index
tags: [contract, workflow-contract, inbound-sdr]
last_modified: 2026-09-25
---

# Inbound Lead Qualifier Agent -- Workflow Contract

Companion note for `inbound-lead-qualifier-contract.yaml` -- gives the YAML contract a markdown page so other notes can link to it with a real relative link instead of a bare filename.

**Real file:** [`inbound-lead-qualifier-contract.yaml`](./inbound-lead-qualifier-contract.yaml) (paths are repo-relative)

**Objective:** Enrich, dedupe, score, and route every new inbound lead within 5 minutes of CRM creation, before human review. **Role map:** `icp_fit_agent` (Tier 1/2/3 classification) -> `dedup_agent` (existing-record match check) -> `routing_agent` (territory assignment + Slack post). **Reads:** `gtm-prompt-library/agents/icp-builder.md`, `gtm-prompt-library/sub-agents/icp-fit-scorer.md`, `02-execution-and-workflows/12-stack-configuration/salesforce-field-spec.md`. **Writes:** `logs/inbound-qualifier-decisions.jsonl` (gitignored). **Status:** specification only; no implementation of this contract exists in the repo yet. **MCP tools:** `crm_read`, `crm_write_custom_fields_only`, `clay_enrich`, `slack_notify`. Promoted from the human-invoked [inbound-lead-qualifier](../agents/inbound-lead-qualifier.md) prompt agent.

## See Also
[inbound-lead-qualifier](../agents/inbound-lead-qualifier.md) . [gtm-prompt-library/README](../README.md)
