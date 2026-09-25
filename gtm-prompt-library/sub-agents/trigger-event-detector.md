---
id: subagent-trigger-event-detector
type: sub-agent
tags: [sub-agent, shared-primitive]
last_modified: 2026-09-25
bounded_autonomy_note: invoked within a human-invoked parent agent's single turn; if any calling parent is later promoted to an autonomous gtm-os/contracts/ Workflow Contract, this sub-agent's role belongs in that contract's role_map (see pipeline-risk-contract.yaml's data_audit_agent/synthesis_agent split for the existing precedent)
---

# Sub-Agent: Trigger Event Detector

**Slug:** `trigger-event-detector`

## Task (single-purpose, reusable)
Scan available signals (funding, hiring, leadership change, regulatory change) for a given account and return the single strongest trigger event with its source and recency, or explicitly return 'no trigger found' rather than fabricating one.

## Called By (parent agents that invoke this sub-agent)
[account-research-brief](../agents/account-research-brief.md) . [win-back-reactivation-sequence-builder](../agents/win-back-reactivation-sequence-builder.md) . [icp-builder](../agents/icp-builder.md)

## Why This Exists As a Sub-Agent, Not Duplicated Logic
3 different top-level agents need this exact primitive. Rather than each parent re-deriving the logic, they invoke this shared sub-agent and consume its output -- one place to fix or improve the logic instead of 3.

## See Also
[gtm-prompt-library/README](../README.md)
