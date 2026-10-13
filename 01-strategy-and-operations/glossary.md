# Outbound GTM Glossary & System Taxonomy

This document serves as the single source of truth for terminology, lifecycle stages, field schemas, and tech stack definitions used across the `bd-leadership` operating system.

---

## 1. Core Outbound Tech Stack

| Function | Standard Tool | Notes |
| :--- | :--- | :--- |
| **System of Record (CRM)** | **Salesforce** | Primary customer database, opportunity pipeline, and reporting source. |
| **Engagement Platform** | **Outreach** | Sequence execution, automated email cadences, and task management. |
| **Parallel Dialer** | **Orum** | High-velocity live call execution, disposition sync, and call recording. |
| **Data & Signal Enrichment** | **Clay** | Signal waterfall aggregation, contact enrichment, and AI prompt input preparation. |

---

## 2. Account Tiers & Scoring

* **Tier 1 (Score 80–100):** Top-priority target accounts. Tight ICP fit **plus an active intent signal** (decayed strength within one half-life by default). Fit-only accounts cap at Tier 2; see the [ICP scoring README](./02-icp-and-account-scoring/README.md). Assigned to senior BDRs; receive 1:1 hyper-personalized multi-channel research.
* **Tier 2 (Score 50–79):** Core target accounts. Solid ICP fit with standard intent signals. Semi-automated sequence tracks with personalized opening hooks.
* **Tier 3 (Score < 50):** Long-tail accounts or low intent. Programmatic email nurturing or deprioritized until new intent signals fire.
* **Excluded (geo block):** Account sits in a `block` geography in the [geo policy](../04-compliance-and-coverage/13-compliance/geo-policy.csv). Score forced to 0; never sequenced.

---

## 3. Outbound Pipeline Lifecycle Stages

1. **Prospecting / Uncontacted:** Account/Contact assigned to BDR in Salesforce and staged in Outreach.
2. **Active Sequence:** Multi-touch cadences running across Email, Phone (Orum), and LinkedIn.
3. **Meeting Set:** Outbound prospect confirmed a scheduled meeting on the calendar.
4. **Meeting Held:** Meeting completed. BDR and AE confirm prospect attended and met baseline criteria.
5. **Sales Qualified Opportunity (SQO):** AE accepts the prospect into active sales pipeline under formal criteria (MEDDPICC / BANT light).

**Terms used in this repo:** BDR and SDR mean the same role. "Handoff" means a Meeting Held that the AE accepts or rejects against written criteria. Older drafts called this a "SAL"; use "Meeting Held" for the stage and "accepted" or "rejected" for the AE decision. "Meeting Booked" means Meeting Set.

---

## 4. Standardized Salesforce & Outreach Field Mapping

To ensure programmatic consistency across all scripts and documentation:

| Field Label | API Name | Type | Value Options / Format |
| :--- | :--- | :--- | :--- |
| **Account Tier** | `Account_Tier__c` | Picklist | `Tier 1`, `Tier 2`, `Tier 3`, `Excluded (geo block)` |
| **Geo Policy Status** | `Geo_Policy_Status__c` | Picklist | `allow`, `review`, `block` |
| **Decayed Signal Score** | `Signal_Score_Decayed__c` | Number(3,0) | `0` to `100` |
| **Disqualification Reason** | `Outbound_Disqualification_Reason__c` | Picklist | `Bad Data`, `No Budget`, `Competitor Locked`, `No Need`, `Unresponsive` |
| **Email Opt-Out** | `HasOptedOutOfEmail` | Boolean | `True` / `False` *(Applies ONLY to email)* |
| **Phone Opt-Out** | `DoNotCall` | Boolean | `True` / `False` *(Applies ONLY to phone calls)* |

---

## 5. Compliance Rules

* **Email Opt-Out (`HasOptedOutOfEmail = True`):** Instantly unsubscribes contact from Outreach email cadences. **Does NOT set `DoNotCall` to True.** Reps remain compliant to call prospects unless explicit verbal/written phone opt-out is requested.
* **Phone Opt-Out (`DoNotCall = True`):** Instantly blocks Orum dialer tasks and marks phone field DNC.
