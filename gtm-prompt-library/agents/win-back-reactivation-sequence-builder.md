---
id: agent-win-back-reactivation-sequence-builder
type: prompt-agent
tags: [prompt-library, outbound-sdr]
function: Outbound SDR
purpose: Pipeline Recovery
priority: P1
last_modified: 2026-09-25
confidence_score: 0.45
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /win-back-reactivation-sequence-builder -- Closed-Lost & Dormant Account Reactivation Builder

**Function:** Outbound SDR  
**Purpose:** Pipeline Recovery  
**Priority:** P1

**Status: net-new, identified via second-pass gap research.**

## System Prompt
```
Given a list of closed-lost or dormant accounts, segment by original loss reason (not uniformly), check for reactivation triggers (leadership change, funding event, champion moved companies, regulatory change), and build a standardized reactivation sequence per loss category that leads with the fresh trigger context (why now) rather than a generic check-in.
```

## Why This Gap Existed
Closed-lost pipeline is a common, high-ROI, and previously uncovered source of new pipeline -- distinct from both outbound prospecting (cold, no prior relationship) and renewal (still-active customer).

## Cross-References
win-loss-analyzer . [account-research-brief](account-research-brief.md)

## Sources
Closed-Lost Reactivation Research

## See Also
00-Prompt-Library-Index . full-org-agent-taxonomy . Sub-Agent Layer . index
