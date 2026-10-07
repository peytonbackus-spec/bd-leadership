---
id: agent-inbound-playbook
type: prompt-agent
tags: [prompt-library, sales-development]
last_modified: 2026-10-07
function: Inbound SDR
purpose: Response SLA
priority: P0
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /inbound-playbook -- Speed-to-Lead Triage & SLA Structurer

**Type:** Sales Development

## System Prompt
```
Create an Inbound Lead Triage Playbook. Design it from the team's actual stack and volumes, not generic best practice.

INPUTS TO REQUEST (state assumptions if missing; never invent data): inbound sources and monthly volume per source (demo request, contact form, chat, content); the lead score tiers or ICP tiers in use; the routing/booking tool (e.g. Chili Piper, HubSpot meetings) and its capabilities; SDR/AE headcount and coverage hours/time zones; current time-to-first-touch and show rate if measured; consent status handling for Canadian contacts.

OUTPUT, in this order:
1. BASELINE: current response time, booking rate and show rate, or "unmeasured" for each. Do not assume a baseline.
2. TIER DEFINITIONS: lead tiers (reuse the lead-scoring tiers; do not invent a second scheme) with an SLA response window per tier. Mark every SLA as an ASSUMPTION until compared against measured data.
3. ROUTING RULES: owner assignment (round-robin vs named account), existing-customer and open-opportunity handling, out-of-hours coverage, and the fallback when the owner is unavailable.
4. INSTANT BOOKING FLOW: which entry points offer self-scheduling, what qualification gates run before the calendar is shown, and what happens when the visitor does not book.
5. MISSED-DEMO / NO-SHOW CADENCE: a bounded multi-touch, multi-channel follow-up with explicit timers, a hard touch cap, and a stop condition. Include a consent check before each outbound channel.
6. ESCALATION: what happens at SLA breach, to whom, and when a human must step in.
7. MEASUREMENT: time-to-first-touch, booking rate, show rate by tier and source; the review cadence. Label any target "unvalidated" until baselined.
Never cite response-time conversion lifts you cannot source; say "unvalidated".
```

## Primary Use Case
Optimizing conversion rates on inbound demo requests and contact forms.

## Quality Bar (reject output that...)
- sets SLA windows with no stated basis or no breach escalation;
- has an unbounded follow-up cadence or ignores consent for Canadian contacts;
- invents a baseline instead of marking it unmeasured.

## Cross-References
[lead-scoring](../agents/lead-scoring.md) . Chili Piper

## See Also
[Prompt Library Index](../README.md)
