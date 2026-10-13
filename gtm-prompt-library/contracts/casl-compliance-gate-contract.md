---
id: contract-casl-compliance-gate
type: contract-index
tags: [contract, workflow-contract, compliance]
last_modified: 2026-09-25
---

# CASL Compliance Gate Agent -- Workflow Contract

Companion note for `casl-compliance-gate-contract.yaml` -- gives the YAML contract a markdown page so other notes can link to it with a real relative link instead of a bare filename.

**Real file:** [`casl-compliance-gate-contract.yaml`](./casl-compliance-gate-contract.yaml) (paths are repo-relative)

**Objective:** Block any outbound cold-email send to a Canadian contact that fails CASL consent or formatting requirements before it leaves the sequencer -- a gate, not a sender. **Role map:** `consent_check_agent` (implied consent via existing relationship or conspicuous publication, or express consent) -> `format_check_agent` (sender-ID, unsubscribe, subject-line checks). **Reads:** `raw-sources/01-casl-compliance.md`, `04-compliance-and-coverage/13-compliance/outbound-compliance.md`. **Writes:** `logs/casl-gate-decisions.jsonl` (gitignored). **Status:** specification only; no implementation of this contract exists in the repo yet. **MCP tools:** `consent_db_read`, `sequencer_read_draft`, `slack_notify`. Promoted from the human-invoked [casl-cold-outreach-compliance-checker](../agents/casl-cold-outreach-compliance-checker.md) prompt agent.

## See Also
[casl-cold-outreach-compliance-checker](../agents/casl-cold-outreach-compliance-checker.md) . [gtm-prompt-library/README](../README.md)
