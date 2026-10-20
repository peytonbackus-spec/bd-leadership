# Results: Before and After

> Self-reported figures from an anonymized enterprise procurement and compliance SaaS company (2025–2026), where I led sales development and then GTM systems. Each figure is tagged **Measured** or **Estimated**. These are before-and-after comparisons, not controlled tests. Several changes ran at the same time, so "Related work" shows what I built in that period, not a proven single cause. No company revenue figures are shown.

| Metric | Before | After | Timeframe | Tag | Related work |
|---|---|---|---|---|---|
| Enterprise meetings per week | 4 (when I joined) | 8 | First 30 days | Measured | A sharper first 30 seconds of the cold call (a clear reason for calling), calling only validated mobiles to cut the wrong-number rate, and re-tiering and scoring each rep's book of business so time went to better accounts. Repo reconstructions: [account scoring](../01-strategy-and-operations/02-icp-and-account-scoring/score_accounts.py), [signal decay](../01-strategy-and-operations/03-signals-and-research/decay_calculator.py) |
| Signal-sourced share of pipeline | ~50% | ~80% | | Before: **Estimated** (not tracked before I joined). After: Measured | Previous users and evaluators, and aged MQLs, added as source-of-opportunity options at opportunity creation. Clay signals synced to Salesforce: website visits, connections to subject-matter experts, previous users and evaluators, lost, derailed or rejected opportunities, aged MQLs, new hires, promotions, job postings |
| SDR conversations per rep per week | ~7–8 | ~10 | | Measured | The same call-opening and validated-mobile changes, plus Clay and weekly 1:1 coaching ([coaching framework](../03-team-and-enablement/05-coaching/README.md)) |
| New-business win rate | ~7% | ~9% | One quarter | Measured | Better lead quality plus flows and agents: intro-call transcripts scored to fill pain, priority, authority and budget fields in Salesforce (more discovery and demo prep time for AEs), and a risk-scoring agent across stages, especially past demo and presentation. Not attributed to a single change |
| Speed-to-lead (inbound) | 30 minutes | 5 minutes | | Measured | Scoring and routing together: reps only saw qualified leads and had the first email ready to go ([cross-functional playbook](../03-team-and-enablement/10-cross-functional/cross-functional-playbook.md)). Repo reconstruction: [speed-to-lead proof of concept](../02-execution-and-workflows/08-ai-workflows/speed-to-lead-README.md) |
| AE customer-facing time | Baseline | +1–2 hours per week | | **Estimated** (from conversations with AEs) | Notion request intake, transcript-filled qualification fields, and mutual action plan and BVA agents that gave time back to customers and solution consultants |
| Win rate on closed deals | ~10% | ~15% | | Measured | A mix of lead quality and tooling: deal-risk scoring, plus mutual action plan and BVA agents that freed rep time for customers and strategy |
| Security questionnaire and RFP turnaround | 1.5–3 weeks | Under 2 days | | Measured | AI drafting plus a changed process: solution consultants and AEs only reviewed the parts the agent was about 80% confident on, and their confirmations were logged so confidence rose next time |

## How these were tracked
I was told to show revenue impact, not activity or tool output. From then on I reported before-and-after numbers for every build and tracked baselines, which is where this table comes from, and leadership reviews moved to pipeline and win rate. The full story is in [How I use critical feedback](../03-team-and-enablement/06-hiring-and-onboarding/hiring-and-coachability.md).

## Team results (FP&A SaaS)
Hiring and ramp results from my SDR manager role (team grown from 7 to 12, all five new hires producing at least one meeting a week after two weeks) are on the [hiring page](../03-team-and-enablement/06-hiring-and-onboarding/hiring-and-coachability.md).

## What these numbers are not
- Not audited. They are my reported figures from the role.
- Not produced by the code in this repo. The scripts here are sample-data reconstructions of the approach.
- See the [case study](./case-studies/enterprise-procurement-saas-sdr-function.md) for context and the [cross-functional playbook](../03-team-and-enablement/10-cross-functional/cross-functional-playbook.md) for how the work ran with AEs, Sales Ops, CS and marketing.
