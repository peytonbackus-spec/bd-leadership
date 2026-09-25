---
id: agent-inbound-lead-qualifier
type: prompt-agent
tags: [prompt-library, inbound-sdr]
function: Inbound SDR
purpose: Intake & Qualification
priority: P0
last_modified: 2026-09-25
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
promoted_to_contract: inbound-lead-qualifier-contract
---

# /inbound-lead-qualifier -- Inbound Lead Intake & Qualification Orchestrator

**Function:** Inbound SDR  
**Purpose:** Intake & Qualification  
**Priority:** P0

> **Promoted to an autonomous Workflow Contract:** [inbound-lead-qualifier-contract](../contracts/inbound-lead-qualifier-contract.md) declares this as a bounded-autonomy automation (boundaries, role_map, stop_rules). This file remains as the human-readable spec; the contract is the enforceable version.

**Status: net-new, identified via full-org gap research** -- not among the original 25 or the first 7 research additions.

## System Prompt
```
Given a new inbound lead record, enrich firmographic data, compare against the defined ICP, check for duplicate/existing account records, determine correct owner via territory rules, and calculate a lead score. Output a routing decision (MQL/SAL/disqualify) with the evidence for each factor, before any human review.
```

## Why This Gap Existed
The full inbound intake job -- broader than pure scoring: enrichment + dedup + ownership + score in one pass, matching how top RevOps teams actually automate lead intake.

## Cross-References
[lead-scoring](lead-scoring.md) . [icp-builder](icp-builder.md) . revops-schema

## See Also
00-Prompt-Library-Index . full-org-agent-taxonomy
