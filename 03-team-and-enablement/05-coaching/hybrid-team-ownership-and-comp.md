# Hybrid Team Ownership & Quality-Gated Comp

How to run a BDR team where AI agents handle part of the outbound motion: who owns which metric, what variable pay should key on, and what to demand from any vendor that prices agents on outcomes. These are starting frameworks, not benchmarks, and no figure here is a claim about any company.

## Principle
Hold agents accountable for inputs they can be measured on. Hold people accountable for the downstream outcomes that require judgment. Pay on what you can verify.

## Ownership matrix

| Metric | Owner | Evidence source | Pay-relevant? |
|---|---|---|---|
| Touches sent | Agent | Sequencer log, per agent ID | No (activity) |
| Reply rate, positive replies | Agent | Reply classification, sampled and audited weekly | No (input) |
| Meetings set | Shared | Calendar event with a named source | Partly |
| Meetings held | Human | Held flag after the call, not on booking | Yes |
| Sales-qualified opportunities (SQO) | Human | AE acceptance against written criteria | Yes |
| Handoff quality | Human | Manager review of a sample, with a rubric | Yes (quality gate) |

The funnel is the same one used elsewhere in this repo: Meeting Set, then Meeting Held, then SQO.

## Quality gate on variable pay
Agents can inflate meetings booked at near-zero marginal cost, so any plan keyed to booked meetings is gameable. Key variable pay to held meetings and accepted SQOs, and have the manager sample handoffs against the rubric before a result counts. [ASSUME: sample size and rubric thresholds are set per team; start small and tighten.]

## Weekly sampled review (manager, 30 minutes)
- [ ] Sample agent-classified replies; note misclassifications and tune the rules.
- [ ] Sample agent-set meetings; check ICP fit and whether the buyer knew why they were meeting.
- [ ] Review 1-2 handoffs per rep against the rubric; feed findings into the next 1:1 (see [coaching](./README.md)).
- [ ] Record what changed in the agent's rules or prompts, and who approved it.

## One-page governance for each agent
| Field | Answer |
|---|---|
| Owner | One named person |
| Objective | The measurable input it owns |
| Boundaries | What it may and may not send or write |
| Evidence | Where its activity is logged |
| Stop rule | When it halts and hands back to a person |
| Review cadence | Weekly sample, monthly rules review |

## If a vendor prices on outcomes
Ask four questions before signing: who defines "qualified", who counts it, who checks a sample, and what happens in a dispute. If the answer to the first is "our default," you are buying the vendor's definition of success.

## See also
[Unit economics](../../01-strategy-and-operations/07-metrics-and-forecasting/unit-economics.md) · [Coaching framework](./README.md) · [Compliance](../../04-compliance-and-coverage/13-compliance/outbound-compliance.md)
