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
Build a quantitative ICP Definition Matrix for [COMPANY_NAME]'s [PRIMARY_PRODUCT_SUITE], targeting [TARGET_BUYER_PERSONA] buyers with a typical deal size of [ACV_RANGE]. Define: 1) Firmographic Criteria, 2) Technographic Triggers (including [PRIMARY_PARTNER_ECOSYSTEM] adjacency), 3) Intent Signals (weighting [PRIMARY_SIGNAL_TRIGGERS] most heavily), and 4) An explicit Tier 1 / Tier 2 / Tier 3 Account Scoring Model with point weightings.
```

## Variables
Uses the tag set in [VARIABLES.md](../../VARIABLES.md) -- see its Worked Example for a filled-in instance of this exact prompt.

## Primary Use Case
Quantifying target account profiles before launching outbound pipeline generation campaigns.

## Cross-References
[sales-development-strategy](../skills/sales-development-strategy.md) . l2a_matching_engine

## See Also
[gtm-prompt-library/README](../README.md)
