---
id: agent-competitive-battlecard
type: prompt-agent
tags: [prompt-library, gtm-strategy-advisory]
last_modified: 2026-09-25
function: Outbound SDR
purpose: Objection Handling
priority: P1
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /competitive-battlecard -- Market Intelligence & Trap-Setting

**Type:** GTM Strategy & Advisory

**Status: partial overlap** -- related material already exists elsewhere in this repo; this note captures the reusable prompt form specifically.

## System Prompt
```
Analyze [COMPANY_NAME] (competitor) against our [PRIMARY_PRODUCT_SUITE] positioning for [TARGET_BUYER_PERSONA] buyers. Output a B2B Competitive Battlecard containing: Competitor Strengths/Weaknesses, Landmine Questions to Plant in Discovery, Feature-by-Feature Gap Analysis (including [PRIMARY_PARTNER_ECOSYSTEM] integration depth), and Exact Pivot Scripts for Sales Reps.
```

## Variables
Uses the tag set in [VARIABLES.md](../../VARIABLES.md) -- here `[COMPANY_NAME]` refers to the competitor being profiled, not the seller.

## Primary Use Case
Equipping sales development reps and account executives with objection handling against market incumbents.

## Cross-References
[sales-development-strategy](../skills/sales-development-strategy.md) . [Buyer Objections Heatmap](../../02-execution-and-workflows/09-gtm-tool-evaluation/Buyer Objections Heatmap.md)

## See Also
[gtm-prompt-library/README](../README.md)
