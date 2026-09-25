---
id: contract-casl-compliance-gate
type: contract-index
tags: [contract, workflow-contract, compliance]
last_modified: 2026-09-25
---

# CASL Compliance Gate Agent -- Workflow Contract

Companion note for `casl-compliance-gate-contract.yaml` -- resolves `[casl-compliance-gate-contract](casl-compliance-gate-contract.md)` wikilinks.

**Real file:** `gtm-os/contracts/casl-compliance-gate-contract.yaml`

**Objective:** Block any outbound cold-email send to a Canadian contact that fails CASL consent or formatting requirements before it leaves the sequencer -- a gate, not a sender. **Reads:** `raw-sources/articles/gap-and-subagent-research/01-casl-compliance`. **Writes:** `intelligence/logs/decision-log.md`. **MCP tools:** `consent_db_read`, `sequencer_read_draft`, `slack_notify`. Promoted from the human-invoked [casl-cold-outreach-compliance-checker](../agents/casl-cold-outreach-compliance-checker.md) prompt agent -- directly relevant to Peyton's own Ontario-registered cold-outbound consulting practice, not hypothetical.

## See Also
[casl-cold-outreach-compliance-checker](../agents/casl-cold-outreach-compliance-checker.md) . [gtm-prompt-library/README](../README.md)
