---
id: agent-sequence-builder
type: prompt-agent
tags: [prompt-library, sales-development]
last_modified: 2026-09-25
function: Outbound SDR
purpose: Outreach Execution
priority: P0
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /sequence-builder -- Multi-Channel Outbound Campaign Architect

**Type:** Sales Development

**Status: partial overlap** -- related material already exists elsewhere in this vault; this note captures the reusable prompt form specifically.

## System Prompt
```
Build a 14-day, 6-touch multi-channel outbound sequence (Email, LinkedIn, Phone) targeting the defined persona. Include: Cold email copies with dynamic enrichment placeholders (Clay/RB2B), cold call scripts, LinkedIn touchpoints, and objection handling pivots.
```

## Primary Use Case
Designing outbound sequences for SDR/BDR campaigns.

## Cross-References
[sales-development-strategy](../skills/sales-development-strategy.md)

## See Also
00-Prompt-Library-Index . _Skill_Matrix_Hub
