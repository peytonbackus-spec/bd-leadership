---
id: gtm-prompt-library-index
type: hub
tags: [hub, prompt-library]
last_modified: 2026-09-25
---

# GTM Prompt Library — Index

The curated BDR/SDR-leadership prompt library for this repo: 15 top-level agents, 5 shared sub-agents, 2 skill references, and 3 Workflow Contracts promoted to bounded-autonomy automations. This is the hub every agent's "See Also" points back to.

## Agents

### Inbound SDR
| Agent | Purpose | Priority |
|---|---|---|
| [inbound-lead-qualifier](agents/inbound-lead-qualifier.md) | Intake & Qualification — promoted to [inbound-lead-qualifier-contract](contracts/inbound-lead-qualifier-contract.md) | P0 |
| [inbound-playbook](agents/inbound-playbook.md) | Response SLA | P0 |
| [lead-scoring](agents/lead-scoring.md) | Qualification | P0 |
| [speed-to-lead-sla-enforcer](agents/speed-to-lead-sla-enforcer.md) | Response SLA — promoted to [speed-to-lead-sla-contract](contracts/speed-to-lead-sla-contract.md) | P0 |

### Outbound SDR
| Agent | Purpose | Priority |
|---|---|---|
| [icp-builder](agents/icp-builder.md) | Targeting | P0 |
| [sequence-builder](agents/sequence-builder.md) | Outreach Execution | P0 |
| [account-research-brief](agents/account-research-brief.md) | Research & Prep | P0 |
| [casl-cold-outreach-compliance-checker](agents/casl-cold-outreach-compliance-checker.md) | Legal Compliance — promoted to [casl-compliance-gate-contract](contracts/casl-compliance-gate-contract.md) | P0 |
| [cold-call-script](agents/cold-call-script.md) | Outreach Execution | P1 |
| [competitive-battlecard](agents/competitive-battlecard.md) | Objection Handling | P1 |
| [email-optimizer](agents/email-optimizer.md) | Outreach Execution | P1 |
| [prospect-stack-gap-finder](agents/prospect-stack-gap-finder.md) | Targeting | P1 |
| [win-back-reactivation-sequence-builder](agents/win-back-reactivation-sequence-builder.md) | Pipeline Recovery | P1 |
| [linkedin-social-selling-script](agents/linkedin-social-selling-script.md) | Outreach Execution | P2 |
| [voicemail-script](agents/voicemail-script.md) | Outreach Execution | P2 |

## Sub-Agents

5 shared, single-purpose sub-agents that multiple top-level agents call, instead of each re-deriving the same logic — mirrors the `role_map` pattern used in the Workflow Contracts below.

| Sub-Agent | Called By (within this repo) |
|---|---|
| [ICP Fit Scorer](sub-agents/icp-fit-scorer.md) | icp-builder, lead-scoring, inbound-lead-qualifier, prospect-stack-gap-finder, account-research-brief |
| [Competitive Intel Lookup](sub-agents/competitive-intel-lookup.md) | competitive-battlecard, prospect-stack-gap-finder |
| [Objection Mapper](sub-agents/objection-mapper.md) | cold-call-script, competitive-battlecard, sequence-builder |
| [Compliance/Consent Checker](sub-agents/compliance-consent-checker.md) | casl-cold-outreach-compliance-checker, sequence-builder, account-research-brief |
| [Trigger Event Detector](sub-agents/trigger-event-detector.md) | account-research-brief, win-back-reactivation-sequence-builder, icp-builder |

Some sub-agents are also called by agents that live only in the full `gtm-revops-toolkit` library (not curated into this repo) — those parents are named in each sub-agent's own "Called By" section as plain text, not links, since they have no file here.

## Skills

| Skill | Covers |
|---|---|
| [sales-development-strategy](skills/sales-development-strategy.md) | Outbound sequencing, territory/capacity planning, objection handling, IC-level tactics |
| [sales-development-leadership](skills/sales-development-leadership.md) | Hiring/ramp, activity metrics, coaching cadence, comp design, career ladder — team management |

## Workflow Contracts

Three agents above have been promoted from human-invoked prompts to autonomous, bounded-autonomy Workflow Contracts (boundaries, role_map, stop_rules defined in each contract's YAML; the `.md` file is the human-readable companion):

- [casl-compliance-gate-contract](contracts/casl-compliance-gate-contract.md) — promoted from casl-cold-outreach-compliance-checker
- [inbound-lead-qualifier-contract](contracts/inbound-lead-qualifier-contract.md) — promoted from inbound-lead-qualifier
- [speed-to-lead-sla-contract](contracts/speed-to-lead-sla-contract.md) — promoted from speed-to-lead-sla-enforcer

## See Also
[README](../README.md)
