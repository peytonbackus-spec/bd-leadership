# Cross-Functional Playbook: What I Ran

> Everything on this page is **Done**: I ran it at an anonymized enterprise procurement and compliance SaaS company (2025–2026) unless marked FP&A SaaS. The proposed SLAs on the [cross-functional README](./README.md) are separate and remain starting targets. Results are self-reported; figures are on the [Results page](../../05-proof-and-tools/results.md).

**Context.** I reported to the VP Growth (later VP GTM Strategy and Operations). I led 5 SDRs with cross-functional oversight of 9 Sales Ops and 8 AEs, then moved into a GTM systems role covering the full revenue org, from SDR through Customer Success.

## Who I partnered with, on what

| Partner | What we owned together | How we worked |
|---|---|---|
| AEs and Sales Ops | Stage gates, lead routing, closed-lost data | Rules reviewed with AE and Sales Ops leads before launch; change log kept |
| Customer Success | Renewals and existing-customer inbound | Renewal opportunity auto-created and owned by the named CSM |
| Marketing | MQL handoff, aged-MQL recycling, event campaigns | One scored handoff process for new and recycled MQLs |
| Revenue org requests | CRM and systems work | Requests submitted through Notion forms and prioritized |
| My manager | Priorities and reporting | Weekly priority list; before-and-after numbers for every build |

## 1. Stage gates (AEs and Sales Ops)
- **PANT before Discovery:** Pain, Authority, Need and Timeline required before an opportunity enters Discovery.
- **"Demo Occurred" before Presentation:** required to pass Presentation, and ticked automatically when a Gong recording shows a screenshare with a solutions consultant on the call.
- **Closed-lost reason:** a reason plus background required on every closed-lost opportunity.
- **Rollout:** reviewed with AE and Sales Ops leads before launch, with a change log. Result: fewer rollbacks and complaints, and AEs adopted PANT and "Demo Occurred" without pushback.

## 2. Lead routing and MQL handoff (AEs, CS, marketing)
- **Routing:** an inbound lead from an account with an open opportunity goes to that AE; an existing-customer inbound goes to the named CSM.
- **MQL handoff:** the lead is scored, the SDR gets an AI-generated subject line and email body, the SDR qualifies further by phone, and books the meeting for the AE. Speed-to-lead went from 30 to 5 minutes.
- **FP&A SaaS (earlier role):** the SDR qualified the MQL and booked the call for the AE.

## 3. Renewal handoff (Customer Success)
- A closed-won opportunity automatically creates a renewal opportunity. The named CSM becomes the owner and the external contacts are associated.

## 4. Marketing
- **Aged-MQL recycling:** aged MQLs are tiered by the type of event, re-enriched to confirm the person is still in role and at the company, then sent through the same MQL handoff so an SDR starts outreach.
- **Event campaign:** I built and enriched the lists (priority accounts and contacts) and designed the campaign; SDRs executed it; I tracked progress, including replies from event attendees.

## 5. Feedback loops (Gong and Clay)
- **Objections:** a Gong objection-tracking feedback loop, and Clay extracts objections into opportunity and account fields, with tasks.
- **Call context in the CRM:** a Gong "Most Recent Call" field in Salesforce.
- **Data sync:** Clay to Salesforce sync of leads, contacts, accounts and opportunities.
- **Alerts:** n8n sends Clay alerts to Slack for expansion intent and role changes.
- **Trust in AI output:** reps pushed back on the accuracy of AI-drafted emails. The fix was prompt enablement plus validated sources. Reps adopted the AI drafts and made fewer manual rewrites.

## 6. Request intake and priorities
- **Intake:** CRM and systems requests came in through Notion forms so they could be prioritized. Turnaround got faster, and this was part of how AEs gained 1–2 customer-facing hours a week.
- **Priorities:** after feedback that I was spread too thin between running the team and running systems, I agreed a weekly priority list with my manager, with fixed coaching time and fixed build time. Coaching time held every week and fewer builds were left half-finished.

## FP&A SaaS (earlier role)
- Strict handoff criteria and weekly deal reviews with AE leadership.
- I ask AEs for feedback on meeting quality and handoffs as a standing practice.

See also: [How I hire and use feedback](../06-hiring-and-onboarding/hiring-and-coachability.md) · [Operating model and rules of engagement](../../01-strategy-and-operations/01-operating-model/README.md)
