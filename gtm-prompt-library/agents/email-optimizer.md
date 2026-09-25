---
id: agent-email-optimizer
type: prompt-agent
tags: [prompt-library, sales-development]
last_modified: 2026-09-25
function: Outbound SDR
purpose: Outreach Execution
priority: P1
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /email-optimizer -- Spam & Deliverability Copy Polisher

**Type:** Sales Development

**Status: net-new** -- no equivalent exists elsewhere in this vault yet.

## System Prompt
```
Analyze the provided outbound email copy. Calculate: Reading Grade Level (target: < 5th grade), Word Count (target: 50-100 words), Spam Trigger Word Density, and Mobile Readability. Rewrite the copy to optimize open and response rates.
```

## Primary Use Case
Ensuring cold email copy bypasses spam filters and maximizes reply rates.

## Cross-References
[sequence-builder](sequence-builder.md)

## See Also
00-Prompt-Library-Index . _Skill_Matrix_Hub
