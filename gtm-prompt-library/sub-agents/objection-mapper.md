---
id: subagent-objection-mapper
type: sub-agent
tags: [sub-agent, shared-primitive]
last_modified: 2026-09-25
bounded_autonomy_note: invoked within a human-invoked parent agent's single turn; if any calling parent is later promoted to an autonomous gtm-os/contracts/ Workflow Contract, this sub-agent's role belongs in that contract's role_map (see pipeline-risk-contract.yaml's data_audit_agent/synthesis_agent split for the existing precedent)
---

# Sub-Agent: Objection Mapper

**Slug:** `objection-mapper`

## Task (single-purpose, reusable)
Given a target persona or account, pull the most frequent relevant objections from the Buyer Objections Heatmap and Friction Heatmap data and rank them by frequency for this specific context.

## Called By (parent agents that invoke this sub-agent)
[cold-call-script](../agents/cold-call-script.md) . [competitive-battlecard](../agents/competitive-battlecard.md) . [sequence-builder](../agents/sequence-builder.md) . positioning-framework

## Why This Exists As a Sub-Agent, Not Duplicated Logic
4 different top-level agents need this exact primitive. Rather than each parent re-deriving the logic, they invoke this shared sub-agent and consume its output -- one place to fix or improve the logic instead of 4.

## See Also
Sub-Agent Layer . 00-Prompt-Library-Index . full-org-agent-taxonomy
