---
id: agent-prospect-stack-gap-finder
type: prompt-agent
tags: [prompt-library, sales-development]
last_modified: 2026-09-25
function: Outbound SDR
purpose: Targeting
priority: P1
confidence_score: 0.4
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /prospect-stack-gap-finder -- Prospect Tech Stack Gap Identifier

**Type:** Sales Development

**Status: net-new, identified via external research** -- not among the 25 supplied; added after researching current GTM prompt-library practice.

## System Prompt
```
Given a prospect account's known or inferred tech stack, identify functional gaps and weak points relative to our product's value proposition (not our own stack -- theirs). Output: Tool-by-tool weakness, the specific gap our product closes, and a one-line insertion angle for outbound copy.
```

## Primary Use Case
Selling INTO a gap in a prospect's stack, distinct from /tech-stack-audit which reviews your own or a client's existing stack for redundancy.

## Cross-References
tech-stack-audit . GTM Intelligence Overview

## See Also
00-Prompt-Library-Index . _Skill_Matrix_Hub . index
