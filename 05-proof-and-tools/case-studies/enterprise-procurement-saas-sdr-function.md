# Case Study: Building the Enterprise SDR Function (Enterprise Procurement SaaS, 2025-2026)

> Outcomes below are self-reported and qualitative. Company details are anonymized, and no figures are claimed.

## Executive Summary
Led the outbound SDR function at an enterprise procurement and compliance SaaS company (2025–2026). Established core GTM infrastructure, data enrichment pipelines, and AI-assisted research workflows.

## Key Outcomes (self-reported)
- **Infrastructure & Stack Buildout:** Operationalized a multi-channel outbound stack (Salesforce, Outreach, Orum, ZoomInfo, Clay) and established data governance standards.
- **AI-Assisted Workflows:** Built prompt frameworks and automation for pre-call research and personalized opening lines.
- **Global Compliance Guardrails:** Implemented regional routing and consent controls across North American and international outbound (GDPR, CASL, CAN-SPAM).

## How This Repo Relates
The scripts in this repo are sample-data reconstructions of the approach, not the production systems used in the role:
- [`score_accounts.py`](../../01-strategy-and-operations/02-icp-and-account-scoring/score_accounts.py): account scoring with a signal requirement and a geo compliance gate
- [`pipeline.py`](../../02-execution-and-workflows/08-ai-workflows/pipeline.py): templated hook drafts with a human review queue (no LLM call)
- [Capacity calculator](../docs/capacity-calculator.html): headcount and activity planning
