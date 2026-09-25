---
id: subagent-icp-fit-scorer
type: sub-agent
tags: [sub-agent, shared-primitive]
last_modified: 2026-09-25
bounded_autonomy_note: invoked within a human-invoked parent agent's single turn; if any calling parent is later promoted to an autonomous gtm-os/contracts/ Workflow Contract, this sub-agent's role belongs in that contract's role_map (see pipeline-risk-contract.yaml's data_audit_agent/synthesis_agent split for the existing precedent)
---

# Sub-Agent: ICP Fit Scorer

**Slug:** `icp-fit-scorer`

## Task (single-purpose, reusable)
Score an account against the defined ICP's firmographic and technographic criteria, returning a Tier 1/2/3 classification with the specific criteria met and missed.

## Called By (parent agents that invoke this sub-agent)
[icp-builder](../agents/icp-builder.md) . [lead-scoring](../agents/lead-scoring.md) . [inbound-lead-qualifier](../agents/inbound-lead-qualifier.md) . [prospect-stack-gap-finder](../agents/prospect-stack-gap-finder.md) . [account-research-brief](../agents/account-research-brief.md)

## Why This Exists As a Sub-Agent, Not Duplicated Logic
5 different top-level agents need this exact primitive. Rather than each parent re-deriving the logic, they invoke this shared sub-agent and consume its output -- one place to fix or improve the logic instead of 5.

## See Also
Sub-Agent Layer . 00-Prompt-Library-Index . full-org-agent-taxonomy
