# Outbound Regulatory Compliance Guardrails

> **Guardrails, not legal advice.** This is an operating checklist for a BDR team, written by a sales leader rather than a lawyer. Laws change and vary with the facts, so confirm every rule here with qualified counsel before relying on it. Sources were last checked on 2026-10-13 and are listed at the end.

How to use this page: the [geo policy](./geo-policy.csv) decides whether a geography can be prospected at all. The channel rules below decide *how* to contact it. The [pre-send gate](../../02-execution-and-workflows/12-stack-configuration/outreach-sequence-design.md#pre-send-compliance-gate) is where both get enforced before any touch goes out.

---

## 1. Email: baseline by jurisdiction

| Jurisdiction | Cold B2B email basis | Every message must include | Opt-out deadline |
|---|---|---|---|
| **US (CAN-SPAM)** | Opt-out regime; no prior consent needed | Accurate header and subject, ad identification, valid physical postal address, working opt-out | 10 business days |
| **Canada (CASL)** | Express consent, or implied consent: an existing business relationship, or an address *conspicuously published* with no "no solicitation" statement and the message relevant to the person's role | Sender name and business, mailing address, plus phone, email or web contact; working unsubscribe | 10 business days |
| **EU (GDPR + ePrivacy)** | Lawful basis under GDPR (usually legitimate interest, see §2), **plus** the member state's ePrivacy rule for email, which varies by country | Sender identity, a clear opt-out in every message, privacy notice (Art. 14) within one month of collecting the data | Without undue delay |
| **UK (UK GDPR + PECR)** | Depends on subscriber type, see §3 | Sender identity, valid opt-out address | Promptly |
| **Germany (UWG §7)** | **Opt-in only**, see §4 | Imprint (Impressum) details, opt-out | Immediately |

CASL penalties reach C$10M per violation for organizations (C$1M for individuals), so a CASL failure is a business risk as well as a deliverability one. The [casl-compliance-gate-contract](../../gtm-prompt-library/contracts/casl-compliance-gate-contract.md) holds the block-by-default rules for Canadian sends.

---

## 2. GDPR / ePrivacy: legitimate interest

Under GDPR Art. 6(1)(f), cold B2B outreach usually relies on **legitimate interest**. Recital 47 recognizes direct marketing as a possible legitimate interest. That basis only holds if a documented Legitimate Interest Assessment (LIA) passes all three tests, and it covers the *data processing* only. The separate ePrivacy rule for the email itself still applies (§1, §4).

### LIA template (one per campaign or segment)

| Section | Answer |
|---|---|
| **Campaign / segment** | e.g. "VP Finance at 250–5,000-employee manufacturers in NL, IE, FR" |
| **Owner and date** | Named person; review date (at most 12 months out) |
| **1. Purpose test.** What is the interest? Is it lawful and specific? | e.g. "Offer a relevant B2B product to people whose role makes it relevant" |
| **2. Necessity test.** Is processing needed for that purpose? Is there a less intrusive way? | Data minimized to name, title, work email, company. No personal email, no personal phone, no sensitive data |
| **3. Balancing test.** Would the person reasonably expect this? What is the impact? | Role-relevant message to a work address; easy opt-out; no profiling beyond firmographics |
| **Safeguards** | Opt-out in every touch; suppression list checked before send; Art. 14 notice with source of data; retention limit (e.g. purge non-responders after 12 months) |
| **Data source** | Vendor name, its lawful-basis statement, and when you checked it |
| **Outcome** | Pass / Pass with conditions / Fail |
| **Approved by** | Privacy lead or counsel |

---

## 3. UK PECR: corporate vs individual subscribers

PECR splits recipients by **subscriber type**, not by job title:

| Recipient | Email / SMS | Live calls |
|---|---|---|
| **Corporate subscriber** (limited company, LLP, Scottish partnership, government body) | Allowed without consent; must identify sender and give an opt-out | Allowed unless the number is on the Corporate TPS (CTPS) or has objected |
| **Individual subscriber** (sole trader, some partnerships) | Needs consent, unless the "soft opt-in" applies (existing customer, similar products) | Allowed unless on TPS or has objected |

UK GDPR still applies to named people at corporate subscribers, so the LIA in §2 is still required. The Data (Use and Access) Act 2025 aligned PECR fines with UK GDPR levels (up to £17.5M or 4% of global turnover). Confirm how far its commencement has reached before relying on older guidance.

---

## 4. Germany: UWG §7, treat email as opt-in only

UWG §7(2) No. 2 treats advertising email sent without the recipient's **prior express consent** as an unreasonable nuisance. **This applies to B2B as well as B2C.** There is no corporate-subscriber carve-out like the UK's.

- **Email:** do not cold-email German contacts. Only email people with a documented opt-in (form fill, event badge scan with consent text, explicit reply asking to be contacted).
- **Phone:** B2B cold calls need at least *presumed* consent (mutmaßliche Einwilligung). That means a concrete reason to believe the business would want the call. Document the reason per account.
- **LinkedIn / InMail:** treat as a manual, low-volume channel, and record what prompted each message.
- Austria is believed to have similarly strict consent rules for email, including B2B. **Unverified, confirm with counsel.** Its row in [geo-policy.csv](./geo-policy.csv) is `review` for that reason.

---

## 5. US state privacy, including California B2B contacts

- **California (CCPA as amended by CPRA):** the B2B and employee exemptions **expired on 1 January 2023**. Business contact data about California residents is now personal information. If the company meets the CCPA thresholds, it must give notice at collection, honor delete/know/correct requests, and honor opt-out of "sale or sharing" (including Global Privacy Control signals on web properties). Many contact-data vendors are registered data brokers under California's Delete Act, so deletion requests can reach them through the state's centralized deletion mechanism. Check vendor contracts for how they pass deletions back to you.
- **Other comprehensive state laws** (Virginia, Colorado, Connecticut, Texas, and others) mostly exclude people acting in a commercial or employment context. Check each new state law for a B2B carve-out instead of assuming one.
- **Operational rule:** store `state` on every US contact. Route California deletion and opt-out requests through a single intake with a 45-day SLA.

---

## 6. Do-Not-Call rules

| Regime | Rule for B2B callers |
|---|---|
| **US TCPA** (47 CFR 64.1200) | Live, manually dialed calls to business lines are generally allowed. Autodialed or prerecorded calls and texts to **mobile numbers** need prior express consent, even for B2B. Mobile numbers used for business can still be treated as residential. Calling hours are **8 AM–9 PM** in the recipient's local time. Keep an internal DNC list and honor requests within 10 business days. |
| **US TSR** (16 CFR 310) | Most B2B calls are exempt. Retail sales of nondurable office or cleaning supplies are not. |
| **US National DNC Registry** | Covers residential numbers. Scrub anyway, because personal mobiles end up in B2B data. |
| **US state "mini-TCPA" laws** | Some are stricter. Florida, for example, limits calls to 8 AM–8 PM and caps attempts. Apply the strictest rule for the recipient's state. |
| **Canada: CRTC Unsolicited Telecommunications Rules** | B2B calls are **exempt from the National DNCL** but **not** from the Telemarketing Rules. The caller must register with the National DNCL operator, keep an internal do-not-call list, identify the caller and the purpose, and respect calling hours (see [time-zone model](../14-global-coverage/time-zone-model.md)). Whether the calling-hour limits bind B2B calls: **Unverified, confirm with counsel.** |
| **UK** | Screen against TPS and CTPS before every call block. |
| **France** | Since **11 Aug 2026**, telephone prospecting of consumers needs **prior explicit consent** (loi n° 2025-594, art. 13; décret n° 2026-662 of 23 July 2026). Consent is valid for at most one year, and the caller must be able to prove it (DGCCRF: keep proof for at least 3 years). This replaces Bloctel opt-out. The rule is consumer-facing and B2B treatment is less clear: **apply the consent rule whenever a contact's status is doubtful** (sole traders, personal mobiles). Consumer calls remain limited to weekdays 10:00–13:00 and 14:00–20:00 (consumer's time zone, excluding public holidays), with at most four calls to the same consumer in 30 days ([DGCCRF guide](https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/demarchage-telephonique-professionnels-mettez-vous-en-conformite-avec-la-reglementation), checked 2026-10-13). B2B treatment is not addressed by that guide. |

The Salesforce `DoNotCall` flag is channel-specific: it blocks phone only (see the [glossary](../../01-strategy-and-operations/glossary.md#5-compliance-rules)). Every DNC request is logged with date and source.

---

## 7. Other regimes to check before entering a market

| Regime | What changes for outbound |
|---|---|
| **Quebec Law 25** (Act respecting the protection of personal information in the private sector) | Section 1 provides that Divisions II (collection) and III (confidentiality) do not apply to personal information concerning the performance of duties within an enterprise, such as name, title and duties, and the address, email and telephone number of the person's place of work ([P-39.1, s.1](https://www.legisquebec.gouv.qc.ca/en/document/cs/P-39.1), checked 2026-10-13); other provisions of the Act still apply. Anything beyond that needs consent, a privacy officer, and a privacy impact assessment before transfer outside Quebec. CASL still governs the email itself. Fines reach C$25M or 4% of worldwide turnover. |
| **Brazil LGPD** | Legitimate interest is a valid basis (Art. 7 IX). The ANPD published guidance on it in 2024. Document an LIA (§2 template works), give data-subject rights, and keep a record of the data source. |
| **China PIPL** | There is **no legitimate-interest basis**. Consent is generally required. Exporting personal data collected in China needs a CAC security assessment, standard contract, or certification, unless a 2024 exemption applies. Status is `review`. Do not bulk-import Chinese contact data into a US CRM without counsel sign-off. |

---

## 8. Sanctions and restricted-geography policy

Sales outreach is not itself a sanctioned transaction, but it is the first step toward one. Prospecting a blocked geography wastes capacity and creates a paper trail of intent to deal. The policy below is encoded in [geo-policy.csv](./geo-policy.csv), and [score_accounts.py](../../01-strategy-and-operations/02-icp-and-account-scoring/score_accounts.py) scores blocked accounts to **0**.

### Block (no outreach, score 0)

| Geography | Why |
|---|---|
| Cuba, Iran, North Korea | Comprehensive US embargoes (OFAC) |
| Crimea (incl. Sevastopol); so-called DNR and LNR regions of Ukraine (Donetsk, Luhansk oblasts) | Region-level comprehensive OFAC sanctions (EO 13685, EO 14065), mirrored by the EU, UK and Canada |
| Russia | **Policy choice, not a comprehensive embargo.** Russia is not under a comprehensive embargo, but US, EU, UK and Canadian restrictions are broad. They include the US ban (from 12 Sept 2024) on providing IT consultancy and certain enterprise software to anyone in Russia. Counsel can override per account. |
| Belarus | **Policy choice, not a comprehensive embargo.** Belarus is under extensive US, EU, UK and Canadian sanctions aligned with the Russia measures. |

### Review (compliance sign-off before any outreach; no auto-sequencing)

| Geography | Why |
|---|---|
| Syria | OFAC ended the comprehensive Syria program on 1 July 2025 (EO 14312). The Caesar Act was repealed on 18 Dec 2025, and the State Sponsor of Terrorism designation was rescinded on 24 Aug 2026. Targeted SDN designations and some export controls remain, so screen every party. **Verify current status with OFAC and the State Department before each policy review**, because this program changed three times in 14 months. |
| Venezuela | The government-blocking order and targeted designations remain. 2026 general licenses changed the program, so check them. |
| Myanmar | Targeted sanctions on the military and state-owned entities. |
| Zaporizhzhia and Kherson oblasts (Ukraine) | EU and UK restrictions on areas not controlled by the Ukrainian government. |
| China | PIPL data-export rules (§7). US export controls, including the BIS Entity List and Military End-User rules, can restrict specific counterparties. Hong Kong and Macau are treated the same for screening. |
| Austria | Strict email consent rules (§4). **Unverified, confirm with counsel.** |
| Any geography missing from the policy file | Unknown means review, not allow. |

### Canadian sanctions

Canada imposes its own sanctions under the Special Economic Measures Act (SEMA) and the Justice for Victims of Corrupt Foreign Officials Act. Its lists do not match OFAC's. A Canadian entity, or a US entity selling from Canada, screens against the **Consolidated Canadian Autonomous Sanctions List** as well as OFAC.

### Denied-party screening (every account, every time)

Geography is only a coarse filter. A company in an `allow` country can still be owned by a sanctioned party (OFAC's 50% rule). Before first touch, screen the **account legal name and the contact** against:

- the US Consolidated Screening List (trade.gov: OFAC SDN, BIS Entity List, and others)
- the UK Sanctions List
- the EU consolidated financial sanctions list
- the Canadian consolidated list

The step-by-step gate is in [outreach-sequence-design.md](../../02-execution-and-workflows/12-stack-configuration/outreach-sequence-design.md#pre-send-compliance-gate).

> **Status:** geo blocking in `score_accounts.py` is implemented and tested against sample data. Denied-party screening is a **documented process, not code** in this repo. It would normally be done through a screening vendor or the trade.gov CSL API.

---

## 9. Record-keeping (what makes the rest defensible)

- Consent records (CASL, UWG, PECR individual subscribers): type, timestamp, source, and IP or form ID where relevant.
- One LIA per EU/UK/Brazil segment, with a review date.
- Screening results per account: date, lists checked, hit or no hit, who cleared any hit.
- Suppression lists (email opt-out, DNC, objection to processing) are synced to every sending tool before every send.

---

## Verification status

Everything here is a researched guardrail. These items are **not independently verified** and must not be relied on as fact:

| Item | Status |
|---|---|
| Austria B2B email consent | **Unverified, confirm with counsel.** |
| Japan: published-address exception to email opt-in | **Unverified, confirm with counsel.** |
| India DPDP Rules: scope and timing | **Unverified, confirm with counsel.** |
| Canada CRTC calling hours for B2B calls | **Unverified, confirm with counsel.** |
| France: 2022 calling hours and four-call cap alongside the consent rule | Checked 2026-10-13 against the [DGCCRF guide](https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/demarchage-telephonique-professionnels-mettez-vous-en-conformite-avec-la-reglementation) |
| Quebec Law 25: work-contact information exclusion (s.1) | Checked 2026-10-13 against the [Act](https://www.legisquebec.gouv.qc.ca/en/document/cs/P-39.1) |
| Australia 2017 telemarketing standard: in force, hours, no business-number carve-out, scheduled sunset 1 Apr 2027 | Checked 2026-10-13 against the [Federal Register entry](https://www.legislation.gov.au/F2017L00323/latest) |
| Syria: terrorism-sponsor status | Checked 2026-10-13 against [State](https://www.state.gov/state-sponsors-of-terrorism/) and [OFAC](https://ofac.treasury.gov/faqs/topic/1571) |

Items marked "Checked" were read against the cited primary source on that date. That is a research check, not legal advice: laws change, so confirm with counsel before relying on any of it.

Syria status and the Russia/Belarus framing are stated as policy: Syria is `review`, Russia and Belarus are `block` as policy choices, and current status should be checked with OFAC and the State Department before each policy review.

## Sources

| Topic | Source |
|---|---|
| CASL | [Act, s.20 penalties](https://laws-lois.justice.gc.ca/eng/acts/E-1.6/) · [CRTC CASL FAQ](https://crtc.gc.ca/eng/com500/faq500.htm) |
| CAN-SPAM | [FTC compliance guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business) |
| GDPR / ePrivacy | [GDPR (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [ePrivacy Directive Art. 13](https://eur-lex.europa.eu/eli/dir/2002/58/oj) · [EDPB Guidelines 1/2024 on legitimate interest](https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2024/guidelines-12024-processing-personal-data-based_en) |
| UK | [ICO: legitimate interests](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/legitimate-interests/) · [ICO: direct marketing and PECR](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/) · [Data (Use and Access) Act 2025](https://www.legislation.gov.uk/ukpga/2025/18) |
| Germany | [UWG §7](https://www.gesetze-im-internet.de/uwg_2004/__7.html) |
| California | [CPPA](https://cppa.ca.gov/) · [CA AG: CCPA](https://oag.ca.gov/privacy/ccpa) |
| US calling | [47 CFR 64.1200 (TCPA)](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200) · [16 CFR 310 (TSR)](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-310) |
| France calling | [DGCCRF: démarchage téléphonique, professionals' compliance guide](https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/demarchage-telephonique-professionnels-mettez-vous-en-conformite-avec-la-reglementation) |
| Canada calling | [CRTC telemarketing rules](https://crtc.gc.ca/eng/phone/telemarketing/reg.htm) · [CRTC business alerts (B2B exemption)](https://crtc.gc.ca/eng/phone/telemarketing/biz.htm) |
| Quebec | [P-39.1 private sector act](https://www.legisquebec.gouv.qc.ca/en/document/cs/P-39.1) · [CAI](https://www.cai.gouv.qc.ca/) |
| Brazil | [LGPD (Lei 13.709)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) |
| China | [PIPL (NPC English text)](http://en.npc.gov.cn.cdurl.cn/2021-12/29/c_694559.htm) |
| Sanctions | [OFAC programs](https://ofac.treasury.gov/sanctions-programs-and-country-information) · [OFAC Syria FAQs](https://ofac.treasury.gov/faqs/topic/1571) · [State Dept: State Sponsors of Terrorism](https://www.state.gov/state-sponsors-of-terrorism/) · [Trade.gov Consolidated Screening List](https://www.trade.gov/consolidated-screening-list) · [UK Sanctions List](https://www.gov.uk/government/publications/the-uk-sanctions-list) · [EU Sanctions Map](https://www.sanctionsmap.eu/) · [Canada: current sanctions](https://www.international.gc.ca/world-monde/international_relations-relations_internationales/sanctions/current-actuelles.aspx?lang=eng) |
