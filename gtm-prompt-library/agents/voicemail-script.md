---
id: agent-voicemail-script
type: prompt-agent
tags: [prompt-library, outbound-sdr]
function: Outbound SDR
purpose: Outreach Execution
priority: P2
last_modified: 2026-09-25
confidence_score: 0.45
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /voicemail-script -- Cold Voicemail Script Generator

**Function:** Outbound SDR  
**Purpose:** Outreach Execution  
**Priority:** P2

**Status: net-new, identified via full-org gap research** -- not among the original 25 or the first 7 research additions.

## System Prompt
```
Write a 20-second cold voicemail script for the given persona and pain point. Include a specific reason for the call (not generic), a callback number stated twice, and a follow-up email reference so the prospect has two ways to respond.
```

## Why This Gap Existed
High-frequency micro-skill for dial-heavy outbound (Orum/parallel dialing) -- distinct enough from the full cold-call-script to warrant its own reusable prompt.

## Cross-References
[cold-call-script](cold-call-script.md) . [Orum](../../02-execution-and-workflows/09-gtm-tool-evaluation/Orum.md)

## See Also
00-Prompt-Library-Index . full-org-agent-taxonomy . index
