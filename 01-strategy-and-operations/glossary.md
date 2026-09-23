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

* **Tier A (Score 80–100):** Top-priority target accounts. High intent signals + tight ICP fit. Assigned to senior BDRs; receive 1:1 hyper-personalized multi-channel research.
* **Tier B (Score 50–79):** Core target accounts. Solid ICP fit with standard intent signals. Semi-automated sequence tracks with personalized opening hooks.
* **Tier C (Score < 50):** Long-tail accounts or low intent. Programmatic email nurturing or deprioritized until new intent signals fire.

---

## 3. Outbound Pipeline Lifecycle Stages

1. **Prospecting / Uncontacted:** Account/Contact assigned to BDR in Salesforce and staged in Outreach.
2. **Active Sequence:** Multi-touch cadences running across Email, Phone (Orum), and LinkedIn.
3. **Meeting Set:** Outbound prospect confirmed a scheduled meeting on the calendar.
4. **Meeting Held:** Meeting completed. BDR and AE confirm prospect attended and met baseline criteria.
5. **Sales Qualified Opportunity (SQO):** AE accepts the prospect into active sales pipeline under formal criteria (MEDDPICC / BANT light).

---

## 4. Standardized Salesforce & Outreach Field Mapping

To ensure programmatic consistency across all scripts and documentation:

| Field Label | API Name | Type | Value Options / Format |
| :--- | :--- | :--- | :--- |
| **Account Tier** | `Account_Tier__c` | Picklist | `Tier A`, `Tier B`, `Tier C` |
| **Decayed Signal Score** | `Signal_Score_Decayed__c` | Number(3,0) | `0` to `100` |
| **Disqualification Reason** | `Outbound_Disqualification_Reason__c` | Picklist | `Bad Data`, `No Budget`, `Competitor Locked`, `No Need`, `Unresponsive` |
| **Email Opt-Out** | `HasOptedOutOfEmail` | Boolean | `True` / `False` *(Applies ONLY to email)* |
| **Phone Opt-Out** | `DoNotCall` | Boolean | `True` / `False` *(Applies ONLY to phone calls)* |

---

## 5. Compliance Rules

* **Email Opt-Out (`HasOptedOutOfEmail = True`):** Instantly unsubscribes contact from Outreach email cadences. **Does NOT set `DoNotCall` to True.** Reps remain compliant to call prospects unless explicit verbal/written phone opt-out is requested.
* **Phone Opt-Out (`DoNotCall = True`):** Instantly blocks Orum dialer tasks and marks phone field DNC.
