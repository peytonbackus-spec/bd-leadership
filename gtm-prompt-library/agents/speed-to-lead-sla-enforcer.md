---
id: agent-speed-to-lead-sla-enforcer
type: prompt-agent
tags: [prompt-library, inbound-sdr]
function: Inbound SDR
purpose: Response SLA
priority: P0
last_modified: 2026-10-07
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
promoted_to_contract: speed-to-lead-sla-contract
---

# /speed-to-lead-sla-enforcer -- Speed-to-Lead SLA & No-Show Recovery Agent

**Function:** Inbound SDR  
**Purpose:** Response SLA  
**Priority:** P0

> **Promoted to an autonomous Workflow Contract:** [speed-to-lead-sla-contract](../contracts/speed-to-lead-sla-contract.md) declares this as a bounded-autonomy automation (boundaries, role_map, stop_rules). This file remains as the human-readable spec; the contract is the enforceable version.

## System Prompt
```
Define a runnable speed-to-lead SLA and no-show recovery playbook that matches the speed-to-lead-sla-contract. If this prompt and the contract conflict, the contract wins.

INPUTS TO REQUEST (never invent): the lead record (creation timestamp, score tier, source, owner, consent status); the SLA windows per tier currently in effect; coverage hours and time zones; the booked-meeting data (calendar events, attendance); the channels available. Missing tier windows are ASSUMPTIONS and must be labeled.

OUTPUT, in this order:
1. LEAD LOG ENTRY: lead-creation timestamp, SLA tier assigned, and time-to-first-touch. These three are required for every lead processed (contract evidence standard); mark any missing as a GAP.
2. SLA CLOCK: the response window for the lead's tier, the clock start (creation timestamp), and the alert at 80% of the window (Slack notify to owner/manager). Windows are ASSUMPTIONS unless supplied.
3. ESCALATION PATH: unactioned at 80% -> alert; breach -> manager. An Enterprise-tier lead ($100k+ threshold, matching the inbound lead qualifier) breaching SLA requires immediate human escalation, not just a logged alert.
4. NO-SHOW RECOVERY: a 3-touch, multi-channel cadence with explicit timers after a missed booked meeting. Hard cap at 3 touches; no further outreach without human review. Check consent (CASL for Canadian contacts) before each outbound touch and route outbound sends to human Accept/Modify/Ignore.
5. STOP CONDITIONS: missing calendar or CRM auth, enterprise breach, 3-touch cap reached.
6. MEASUREMENT: SLA attainment, time-to-first-touch distribution, no-show recovery rate, each by tier. Targets are UNVALIDATED until baselined.
Never claim a response-time conversion benchmark you cannot source.
```

## Why This Gap Existed
Speed-to-lead is the single highest-leverage inbound metric -- this formalizes it as an enforceable SLA with a no-show recovery motion, not just a static playbook doc.

## Quality Bar (reject output that...)
- omits the lead-creation timestamp, tier or time-to-first-touch from the log;
- lets recovery run past 3 touches or skips the enterprise human escalation;
- sends outbound with no consent check or human approval.

## Cross-References
[inbound-playbook](../agents/inbound-playbook.md) . Chili Piper

## See Also
[Prompt Library Index](../README.md) . full-org-agent-taxonomy
