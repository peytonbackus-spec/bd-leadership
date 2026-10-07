---
id: agent-competitive-battlecard
type: prompt-agent
tags: [prompt-library, gtm-strategy-advisory]
last_modified: 2026-10-07
function: Outbound SDR
purpose: Objection Handling
priority: P1
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /competitive-battlecard -- Market Intelligence & Trap-Setting

**Type:** GTM Strategy & Advisory

## System Prompt
```
Build a competitive battlecard for ONE competitor, [COMPANY_NAME], against OUR [PRIMARY_PRODUCT_SUITE] positioning for [TARGET_BUYER_PERSONA] buyers. Evidence first; opinions labeled. Here [COMPANY_NAME] is the competitor, not the seller.

INPUTS TO REQUEST: our product and positioning; the competitor and the segment/persona where we meet them; our win/loss notes against them; public sources (pricing page, docs, reviews, job postings, changelog). If you have no win/loss data, say claims are HYPOTHESES to validate on calls.

OUTPUT, in this order:
1. SOURCE LOG: every source with URL and date. Flag anything older than ~6 months; vendor claims are not independent evidence.
2. CLAIMS TABLE: claim | source | status (VERIFIED / VENDOR-CLAIM / INFERRED). Only VERIFIED and clearly labeled VENDOR-CLAIM items may appear in the card.
3. WHERE THEY WIN / WHERE WE WIN: honest strengths and weaknesses by buyer criterion, including the situations where we should not compete.
4. FEATURE GAP TABLE: capability | them | us | proof | does the buyer actually care (Y/N/unknown). Include integration depth with [PRIMARY_PARTNER_ECOSYSTEM].
5. LANDMINE QUESTIONS: discovery questions that surface our strengths without disparaging them; each tied to a gap and phrased so a neutral buyer would find it fair.
6. PIVOT SCRIPTS: for the 4-5 most likely objections, a 2-3 sentence response using a checkable fact; include when to concede.
7. PROOF TO LINE UP: customer reference, metric or demo moment per pivot; mark any not yet available as GAP.
8. REVIEW DATE: when this card goes stale and what would trigger an update.
Never fabricate competitor features, pricing or customer counts; never use FUD the buyer could disprove in a minute.
```

## Variables
Uses the tag set in [VARIABLES.md](../../VARIABLES.md) -- here `[COMPANY_NAME]` refers to the competitor being profiled, not the seller. Any tag you leave unfilled becomes a required input.

## Primary Use Case
Equipping sales development reps and account executives with objection handling against market incumbents.

## Quality Bar (reject output that...)
- states competitor facts with no source/date;
- uses claims a buyer could disprove with one search;
- has no 'where we should not compete' section;
- gives scripts with no proof point.

## Cross-References
[sales-development-strategy](../skills/sales-development-strategy.md) . [Buyer Objections Heatmap](../../02-execution-and-workflows/09-gtm-tool-evaluation/Buyer%20Objections%20Heatmap.md)

## See Also
[Prompt Library Index](../README.md)
