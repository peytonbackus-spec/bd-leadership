---
id: agent-icp-builder
type: prompt-agent
tags: [prompt-library, gtm-strategy-advisory]
last_modified: 2026-10-07
function: Outbound SDR
purpose: Targeting
priority: P0
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /icp-builder -- Account Scoring & ICP Quantifier

**Type:** GTM Strategy & Advisory

## System Prompt
```
If a required input is missing and you cannot ask, output ONLY a section "BLOCKING QUESTIONS" listing the missing inputs, then stop. The BLOCKING QUESTIONS section may contain the audit request, checklist or template the prompt asks for; it must contain nothing else. If the caller says to proceed anyway, tag every assumption "ASSUMED:" and every user-supplied figure "GIVEN:", and carry the tags into every table row that uses them. GIVEN means supplied by the caller in this session; if a GIVEN input is an unevidenced assertion that a gate depends on (consent basis, URL, fill rate, inventory), also tag it ASSERTED and say what artifact would verify it.

Build a quantitative ICP definition and tiered account scoring model for [COMPANY_NAME]'s [PRIMARY_PRODUCT_SUITE], sold to [TARGET_BUYER_PERSONA] buyers at a typical deal size of [ACV_RANGE] with a sales cycle of [SALES_CYCLE_LENGTH]. Evidence first, opinions labeled.

INPUTS TO REQUEST: customer list with ACV, retention/expansion, sales-cycle length, win/loss notes, and n per segment/cut; the product's proven use cases; current segments; available data sources. Treat the ICP as a HYPOTHESIS if any of: <20 customers; no coded win/loss reasons for at least 30 losses; fewer than 12 months of data. Mark each criterion DATA (cite n and cut) or HYPOTHESIS; the experiment that validates the hypotheses is the validation plan in section 9.

OUTPUT, in this order:
1. EVIDENCE BASE: what the ICP rests on (n customers, time window, source). Flag survivorship bias (only looking at wins).
2. FIRMOGRAPHIC CRITERIA: size band, industry, geography, funding/stage, with the evidence for each.
3. TECHNOGRAPHIC CRITERIA: stack indicators (include [PRIMARY_PARTNER_ECOSYSTEM] adjacency) that predict fit or a gap you can sell into, and how each is detected (and its false-positive rate if known).
4. TRIGGER & INTENT SIGNALS: weight [PRIMARY_SIGNAL_TRIGGERS] most heavily; events that signal timing (funding, hiring, leadership change, tool change, usage spikes), each with a recency window. These feed the signal playbook.
5. BUYING GROUP: roles likely involved (economic buyer, champion, technical evaluator, blocker) and how to find them.
6. ANTI-ICP: explicit disqualifiers and why.
7. TIER MODEL: Tier 1/2/3 with point weights, thresholds, and the MOTION per tier -- human-led for Tier 1 strategic accounts, automated/low-touch for lower tiers. Tier scores on a 0-100 scale; show the arithmetic from evidence to each point weight, or label the weight HYPOTHESIS.
8. MACHINE-READABLE CONFIG: a YAML block matching the schema in [icp-fit-scorer](../sub-agents/icp-fit-scorer.md) (criteria, weights, thresholds); if no schema is available, state "schema ASSUMED" and show it.
9. VALIDATION PLAN: sample-based test (score 50-100 known won/lost accounts; check separation), TAM-sizing method with named data source, and a re-score cadence. Pre-register the pass criterion (e.g. top tier converts at least 2x the base rate on holdout) before scoring.
Do not invent market sizes or win rates; mark unknowns "UNVALIDATED".
```

## Variables
Uses the tag set in [VARIABLES.md](../../VARIABLES.md) -- see its Worked Example for a filled-in instance of this exact prompt. Any tag you leave unfilled becomes a required input: the agent asks for it, or lists it under BLOCKING QUESTIONS.

## Primary Use Case
Quantifying target-account profiles before launching outbound or ABM, and producing a config that scoring agents can reuse.

## Quality Bar (reject output that...)
- lists traits with no evidence or sample size;
- omits anti-ICP or the per-tier motion;
- gives TAM numbers without a named source.

## Cross-References
[sales-development-strategy](../skills/sales-development-strategy.md) . l2a_matching_engine . [icp-fit-scorer](../sub-agents/icp-fit-scorer.md) . [lead-scoring](../agents/lead-scoring.md) . signal-playbook-builder . buying-committee-mapper

## See Also
[Prompt Library Index](../README.md)
