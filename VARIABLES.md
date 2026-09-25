# Universal Variable Substitution Guide — GTM Prompt Library

This repository's prompt agents are designed as company-agnostic templates. Substitute the bracketed variables below in the System Prompts across `gtm-prompt-library/agents/` to customize for any target company -- ported from the same convention used in the full `gtm-revops-toolkit` library this repo's prompt agents are curated from.

| Variable Tag | Description | Example Values |
| :--- | :--- | :--- |
| `[COMPANY_NAME]` | Target enterprise or client organization | ACME Corp, SaaS Corp |
| `[TARGET_BUYER_PERSONA]` | Core decision maker titles | VP Engineering, CFO, Head of RevOps |
| `[PRIMARY_PRODUCT_SUITE]` | Core software or service offering | Enterprise Analytics, Predictive Maintenance |
| `[PRIMARY_PARTNER_ECOSYSTEM]` | Primary OEM or channel integration | Salesforce, AWS, Siemens |
| `[ACV_RANGE]` | Average Contract Value brackets | $50k - $150k ARR |
| `[SALES_CYCLE_LENGTH]` | Standard conversion timeline | 60 - 90 Days |
| `[PRIMARY_SIGNAL_TRIGGERS]` | Intent and enrichment triggers | Executive hires, Job posts, FX Volatility |

## Where This Is Used

These tags appear directly in the System Prompt of the agents below, so running one only requires filling in the bracketed values -- no rewriting the prompt itself:

- [`gtm-prompt-library/agents/icp-builder.md`](gtm-prompt-library/agents/icp-builder.md)
- [`gtm-prompt-library/agents/competitive-battlecard.md`](gtm-prompt-library/agents/competitive-battlecard.md)

Any other agent in [`gtm-prompt-library/agents/`](gtm-prompt-library/agents/) can adopt the same tags as it's extended -- these two are the ones with a System Prompt built to consume them directly today (the same two that carry this wiring in the source `gtm-revops-toolkit` library; the other three wired agents there -- `positioning-framework`, `gtm-motion-selector`, `pricing-packaging-optimizer` -- aren't part of this repo's curated BDR/SDR-leadership subset).

## Worked Example

Filling in the table for a hypothetical mid-market target, "Northwind Analytics" (a supply-chain intelligence SaaS vendor):

| Variable Tag | Filled Value |
| :--- | :--- |
| `[COMPANY_NAME]` | Northwind Analytics |
| `[TARGET_BUYER_PERSONA]` | VP Supply Chain Operations, Director of RevOps |
| `[PRIMARY_PRODUCT_SUITE]` | Supply Chain Intelligence Platform |
| `[PRIMARY_PARTNER_ECOSYSTEM]` | NetSuite, SAP |
| `[ACV_RANGE]` | $40k - $120k ARR |
| `[SALES_CYCLE_LENGTH]` | 45 - 75 Days |
| `[PRIMARY_SIGNAL_TRIGGERS]` | ERP migration announcements, new VP Supply Chain hires, warehouse expansion press releases |

Dropped into [`gtm-prompt-library/agents/icp-builder.md`](gtm-prompt-library/agents/icp-builder.md)'s System Prompt, the generic "provided account characteristics" becomes a concrete ask: *"Build a quantitative ICP Definition Matrix for Northwind Analytics' Supply Chain Intelligence Platform, targeting VP Supply Chain Operations / Director of RevOps buyers with a typical deal size of $40k-$120k ARR..."* -- the same prompt, now scoped to an actual deal instead of an abstraction.

## See Also
[gtm-prompt-library/README](gtm-prompt-library/README.md)
