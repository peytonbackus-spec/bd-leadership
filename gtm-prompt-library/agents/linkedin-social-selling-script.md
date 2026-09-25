---
id: agent-linkedin-social-selling-script
type: prompt-agent
tags: [prompt-library, outbound-sdr]
function: Outbound SDR
purpose: Outreach Execution
priority: P2
last_modified: 2026-09-25
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /linkedin-social-selling-script -- LinkedIn Social Selling Touch Builder

**Function:** Outbound SDR  
**Purpose:** Outreach Execution  
**Priority:** P2

**Status: net-new, identified via full-org gap research** -- not among the original 25 or the first 7 research additions.

## System Prompt
```
Write a 3-touch LinkedIn engagement sequence (connection request note, value-add comment/DM, direct ask) for the given persona and trigger event. Keep each touch under platform character limits and avoid language that reads as automated.
```

## Why This Gap Existed
Channel-specific script -- sequence-builder covers LinkedIn generically as one touch in a multi-channel sequence; this is the dedicated LinkedIn-only motion for reps leaning heavily on social.

## Cross-References
[sequence-builder](sequence-builder.md)

## See Also
00-Prompt-Library-Index . full-org-agent-taxonomy
