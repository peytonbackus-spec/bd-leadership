---
id: subagent-compliance-consent-checker
type: sub-agent
tags: [sub-agent, shared-primitive]
last_modified: 2026-09-25
confidence_score: 0.4
bounded_autonomy_note: invoked within a human-invoked parent agent's single turn; if any calling parent is later promoted to an autonomous gtm-os/contracts/ Workflow Contract, this sub-agent's role belongs in that contract's role_map (see pipeline-risk-contract.yaml's data_audit_agent/synthesis_agent split for the existing precedent)
---

# Sub-Agent: Compliance/Consent Checker

**Slug:** `compliance-consent-checker`

## Task (single-purpose, reusable)
Given a target contact for outreach, check whether implied consent (existing business relationship) applies or express consent is required under CASL, and block the send if neither is documented.

## Called By (parent agents that invoke this sub-agent)
[casl-cold-outreach-compliance-checker](../agents/casl-cold-outreach-compliance-checker.md) . [sequence-builder](../agents/sequence-builder.md) . [account-research-brief](../agents/account-research-brief.md)

## Why This Exists As a Sub-Agent, Not Duplicated Logic
3 different top-level agents need this exact primitive. Rather than each parent re-deriving the logic, they invoke this shared sub-agent and consume its output -- one place to fix or improve the logic instead of 3.

## See Also
Sub-Agent Layer . 00-Prompt-Library-Index . full-org-agent-taxonomy
