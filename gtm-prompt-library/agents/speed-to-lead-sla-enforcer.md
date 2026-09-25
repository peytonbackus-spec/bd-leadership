---
id: agent-speed-to-lead-sla-enforcer
type: prompt-agent
tags: [prompt-library, inbound-sdr]
function: Inbound SDR
purpose: Response SLA
priority: P0
last_modified: 2026-09-25
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
promoted_to_contract: speed-to-lead-sla-contract
---

# /speed-to-lead-sla-enforcer -- Speed-to-Lead SLA & No-Show Recovery Agent

**Function:** Inbound SDR  
**Purpose:** Response SLA  
**Priority:** P0

> **Promoted to an autonomous Workflow Contract:** [speed-to-lead-sla-contract](../contracts/speed-to-lead-sla-contract.md) declares this as a bounded-autonomy automation (boundaries, role_map, stop_rules). This file remains as the human-readable spec; the contract is the enforceable version.

**Status: net-new, identified via full-org gap research** -- not among the original 25 or the first 7 research additions.

## System Prompt
```
Given a newly booked or newly created inbound lead, define the SLA response window by lead score tier, the escalation path if the SLA is missed, and a no-show recovery cadence (3-touch, multi-channel) for any booked demo the prospect misses. Output as a runnable playbook with explicit timers.
```

## Why This Gap Existed
Speed-to-lead is the single highest-leverage inbound metric -- this formalizes it as an enforceable SLA with a no-show recovery motion, not just a static playbook doc.

## Cross-References
[inbound-playbook](inbound-playbook.md) . [Chili Piper](../../02-execution-and-workflows/09-gtm-tool-evaluation/Chili Piper.md)

## See Also
[gtm-prompt-library/README](../README.md)
