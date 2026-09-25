---
id: agent-icp-builder
type: prompt-agent
tags: [prompt-library, gtm-strategy-advisory]
last_modified: 2026-09-25
function: Outbound SDR
purpose: Targeting
priority: P0
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /icp-builder -- Account Scoring & ICP Quantifier

**Type:** GTM Strategy & Advisory

**Status: net-new** -- no equivalent exists elsewhere in this repo yet.

## System Prompt
```
Build a quantitative ICP Definition Matrix based on provided account characteristics. Define: 1) Firmographic Criteria, 2) Technographic Triggers, 3) Intent Signals, and 4) An explicit Tier 1 / Tier 2 / Tier 3 Account Scoring Model with point weightings.
```

## Primary Use Case
Quantifying target account profiles before launching outbound pipeline generation campaigns.

## Cross-References
[sales-development-strategy](../skills/sales-development-strategy.md) . l2a_matching_engine

## See Also
[gtm-prompt-library/README](../README.md)
