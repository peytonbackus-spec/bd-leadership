---
id: agent-lead-scoring
type: prompt-agent
tags: [prompt-library, revenue-operations]
last_modified: 2026-09-25
function: Inbound SDR
purpose: Qualification
priority: P0
confidence_score: 0.4
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /lead-scoring -- Behavioral & Demographic Scoring Engine

**Type:** Revenue Operations

**Status: net-new** -- no equivalent exists elsewhere in this vault yet.

## System Prompt
```
Construct a dual-axis Lead Scoring Engine. Axis A (Demographic/Firmographic Fit: 0-50 pts) and Axis B (Intent/Behavioral Engagement: 0-50 pts). Define point thresholds for MQL, SAL, and immediate SDR routing.
```

## Primary Use Case
Optimizing inbound lead triage and inbound-to-outbound routing rules.

## Cross-References
meddpicc_health_engine . [icp-builder](icp-builder.md)

## See Also
00-Prompt-Library-Index . _Skill_Matrix_Hub . index
