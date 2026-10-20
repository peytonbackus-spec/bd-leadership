# Case Study: Building the Enterprise SDR Function (Enterprise Procurement SaaS, 2025-2026)

> Outcomes below are self-reported. Company details are anonymized. Before-and-after figures, each tagged measured or estimated, are on the [Results page](../results.md).

## Executive Summary
Led the outbound SDR function at an enterprise procurement and compliance SaaS company (2025–2026). Established core GTM infrastructure, data enrichment pipelines, and AI-assisted research workflows. Later moved into a GTM systems role covering the full revenue org, from SDR through Customer Success.

## Key Outcomes (self-reported)
- **Measured results:** speed-to-lead from 30 to 5 minutes; enterprise meetings from 4 to 8 per week in the first 30 days; new-business win rate from ~7% to ~9% in one quarter. [All eight figures](../results.md).
- **Cross-functional partnership:** stage gates and lead routing with AEs and Sales Ops, renewal handoffs with Customer Success, and MQL and event work with marketing. See the [cross-functional playbook](../../03-team-and-enablement/10-cross-functional/cross-functional-playbook.md).
- **Infrastructure & Stack Buildout:** Operationalized a multi-channel outbound stack (Salesforce, Outreach, Orum, ZoomInfo, Clay) and established data governance standards.
- **AI-Assisted Workflows:** Built prompt frameworks and automation for pre-call research and personalized opening lines.
- **Global Compliance Guardrails:** Implemented regional routing and consent controls across North American and international outbound (GDPR, CASL, CAN-SPAM).

## How This Repo Relates
The scripts in this repo are sample-data reconstructions of the approach, not the production systems used in the role:
- [`score_accounts.py`](../../01-strategy-and-operations/02-icp-and-account-scoring/score_accounts.py): account scoring with a signal requirement and a geo compliance gate
- [`pipeline.py`](../../02-execution-and-workflows/08-ai-workflows/pipeline.py): templated hook drafts with a human review queue (no LLM call)
- [Capacity calculator](../docs/capacity-calculator.html): headcount and activity planning
