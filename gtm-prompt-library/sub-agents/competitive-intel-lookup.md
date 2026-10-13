---
id: subagent-competitive-intel-lookup
type: sub-agent
tags: [sub-agent, shared-primitive]
last_modified: 2026-09-25
---

# Sub-Agent: Competitive Intel Lookup

**Slug:** `competitive-intel-lookup`

## Task (single-purpose, reusable)
Given a named competitor, retrieve and synthesize the relevant profile from [09-gtm-tool-evaluation](../../02-execution-and-workflows/09-gtm-tool-evaluation/README.md) (tool profile, friction/objection heatmap data) into a 3-bullet strengths/weaknesses summary for the specific deal context.

## Called By (parent agents that invoke this sub-agent)
account-brief-generator . [competitive-battlecard](../agents/competitive-battlecard.md) . rfp-proposal-generator . positioning-framework . [prospect-stack-gap-finder](../agents/prospect-stack-gap-finder.md)

## Why This Exists As a Sub-Agent, Not Duplicated Logic
5 different top-level agents need this exact primitive. Rather than each parent re-deriving the logic, they invoke this shared sub-agent and consume its output -- one place to fix or improve the logic instead of 5.

## See Also
[gtm-prompt-library/README](../README.md)
