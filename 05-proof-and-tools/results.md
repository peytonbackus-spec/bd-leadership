# Results: Before and After

> Self-reported figures from an anonymized enterprise procurement and compliance SaaS company (2025–2026), where I led sales development and then GTM systems. Each figure is tagged **Measured** or **Estimated**. These are before-and-after comparisons, not controlled tests. Several changes ran at the same time, so "Related work" shows what I built in that period, not a proven single cause. No company revenue figures are shown.

| Metric | Before | After | Timeframe | Tag | Related work |
|---|---|---|---|---|---|
| Enterprise meetings per week | 4 (when I joined) | 8 | First 30 days | Measured | Signal-based account tiering and outreach. Repo reconstructions: [account scoring](../01-strategy-and-operations/02-icp-and-account-scoring/score_accounts.py), [signal decay](../01-strategy-and-operations/03-signals-and-research/decay_calculator.py) |
| Signal-sourced share of pipeline | ~50% | ~80% | | Before: **Estimated** (not tracked before I joined). After: Measured | Clay signals synced to Salesforce: website visits, connections to subject-matter experts, previous users and evaluators, lost, derailed or rejected opportunities, aged MQLs, new hires, promotions, job postings |
| SDR conversations per rep per week | ~7–8 | ~10 | | Measured | Weekly 1:1 call review and coaching ([coaching framework](../03-team-and-enablement/05-coaching/README.md)) |
| New-business win rate | ~7% | ~9% | One quarter | Measured | Not attributed to a single change |
| Speed-to-lead (inbound) | 30 minutes | 5 minutes | | Measured | Lead scoring and routing, with an AI-drafted email ready for the SDR ([cross-functional playbook](../03-team-and-enablement/10-cross-functional/cross-functional-playbook.md)). Repo reconstruction: [speed-to-lead proof of concept](../02-execution-and-workflows/08-ai-workflows/speed-to-lead-README.md) |
| AE customer-facing time | Baseline | +1–2 hours per week | | Measured | Request intake through Notion forms to prioritize CRM and systems work |
| Win rate on closed deals | ~10% | ~15% | | Measured | Deal-risk scoring |
| Security questionnaire and RFP turnaround | 1.5–3 weeks | Under 2 days | | Measured | AI-assisted drafting, with parts kept under human review |

## How these were tracked
I was told to show revenue impact, not activity or tool output. From then on I reported before-and-after numbers for every build and tracked baselines, which is where this table comes from, and leadership reviews moved to pipeline and win rate. The full story is in [How I use critical feedback](../03-team-and-enablement/06-hiring-and-onboarding/hiring-and-coachability.md).

## Team results (FP&A SaaS)
Hiring and ramp results from my SDR manager role (team grown from 7 to 12, all five new hires producing at least one meeting a week after two weeks) are on the [hiring page](../03-team-and-enablement/06-hiring-and-onboarding/hiring-and-coachability.md).

## What these numbers are not
- Not audited. They are my reported figures from the role.
- Not produced by the code in this repo. The scripts here are sample-data reconstructions of the approach.
- See the [case study](./case-studies/enterprise-procurement-saas-sdr-function.md) for context and the [cross-functional playbook](../03-team-and-enablement/10-cross-functional/cross-functional-playbook.md) for how the work ran with AEs, Sales Ops, CS and marketing.
