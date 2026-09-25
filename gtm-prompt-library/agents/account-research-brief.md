---
id: agent-account-research-brief
type: prompt-agent
tags: [prompt-library, sales-development]
last_modified: 2026-09-25
function: Outbound SDR
purpose: Research & Prep
priority: P0
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /account-research-brief -- Prospect Trigger-Event & Pain Compiler

**Type:** Sales Development

**Status: net-new, identified via external research** -- not among the 25 supplied; added after researching current GTM prompt-library practice.

## System Prompt
```
Given a target account/contact, compile a research brief covering: digital footprint summary (recent posts, role changes), job-posting-derived business initiatives and pain signals, hiring/funding trigger events, and an evidence-based deal-likelihood score with cited sources for each claim. Flag any claim that cannot be sourced.
```

## Primary Use Case
Pre-call/pre-sequence research so outbound leads with a real trigger event instead of a generic pitch.

## Cross-References
[icp-builder](icp-builder.md) . clay-waterfall

## See Also
[gtm-prompt-library/README](../README.md)
