# Time-Zone Routing & Calling-Hours Model

Three rules drive everything below:

1. **Schedule in the prospect's local time, never the rep's.** Store an IANA time zone (e.g. `America/Chicago`) on every contact. Derive it from the contact's address first, then the account HQ, then the phone area code. Never store a fixed UTC offset, because offsets change with DST.
2. **A call or send is allowed only inside the stricter of the legal window and the team window**, on a local business day that is not a public holiday.
3. **Geography status comes first.** Accounts that are `block` in [geo-policy.csv](../13-compliance/geo-policy.csv) never enter a call block. `review` accounts enter one only after sign-off (see [outbound-compliance.md](../13-compliance/outbound-compliance.md)).

---

## 1. North America: separate zones, separate windows

The team's best-connect windows are **8:30–11:30 AM and 1:30–4:30 PM in the prospect's local time**. The table shows when those windows fall for a rep working in Eastern time.

| Zone | IANA zone | UTC offset (std / DST) | Prospect-local window | Same window in ET |
|---|---|---|---|---|
| Eastern (ET) | `America/New_York` | −5 / −4 | 8:30–11:30, 1:30–4:30 | 8:30–11:30, 1:30–4:30 |
| Central (CT) | `America/Chicago` | −6 / −5 | 8:30–11:30, 1:30–4:30 | 9:30–12:30, 2:30–5:30 |
| Mountain (MT) | `America/Denver` | −7 / −6 | 8:30–11:30, 1:30–4:30 | 10:30–1:30, 3:30–6:30 |
| Arizona (no DST) | `America/Phoenix` | −7 all year | 8:30–11:30, 1:30–4:30 | Same as MT in winter, same as PT in summer |
| Pacific (PT) | `America/Los_Angeles` | −8 / −7 | 8:30–11:30, 1:30–4:30 | 11:30–2:30, 4:30–7:30 |
| Atlantic (Canada) | `America/Halifax` | −4 / −3 | 9:00–11:30, 1:30–4:30 | 8:00–10:30, 12:30–3:30 |
| Newfoundland | `America/St_Johns` | −3:30 / −2:30 | 9:00–11:30, 1:30–4:30 | 7:30–10:00, 12:00–3:00 |
| Saskatchewan (no DST) | `America/Regina` | −6 all year | 9:00–11:30, 1:30–4:30 | Same as CT in winter, same as MT in summer |

Canadian windows start at 9:00 AM local to match the CRTC Telemarketing Rules (see §4; whether those hours bind B2B calls is **Unverified, confirm with counsel.**).

**Pod design:** an East pod (ET and CT territories) and a West pod (MT and PT). The West pod starts and ends later, so PT afternoons are covered without overtime. A single national pod running on ET loses roughly two PT hours a day.

---

## 2. EMEA and APAC

| Region | IANA zone (examples) | UTC offset (std / DST) | Coverage model |
|---|---|---|---|
| UK & Ireland | `Europe/London`, `Europe/Dublin` | 0 / +1 | EMEA pod, 9:00–17:00 local |
| Central Europe | `Europe/Berlin`, `Europe/Paris`, `Europe/Amsterdam` | +1 / +2 | EMEA pod, 9:00–17:00 local (France calls 10:00–13:00, 14:00–17:30, see §4) |
| Eastern Europe | `Europe/Helsinki`, `Europe/Kyiv` | +2 / +3 | EMEA pod, from 8:00 GMT |
| Gulf | `Asia/Dubai` | +4, no DST | EMEA pod mornings (GMT); work week varies by country |
| India | `Asia/Kolkata` | +5:30, no DST | EMEA pod mornings, or an APAC pod |
| Singapore / Hong Kong / China | `Asia/Singapore`, `Asia/Hong_Kong`, `Asia/Shanghai` | +8, no DST | APAC pod (China and Hong Kong are `review` in the geo policy) |
| Japan | `Asia/Tokyo` | +9, no DST | APAC pod |
| Australia (east) | `Australia/Sydney`, `Australia/Melbourne` | +10 / +11 | APAC pod, or a US West late shift |
| Australia (Queensland) | `Australia/Brisbane` | +10, no DST | Same as above |
| Australia (west) | `Australia/Perth` | +8, no DST | APAC pod |
| New Zealand | `Pacific/Auckland` | +12 / +13 | APAC pod, or a US West late shift |

**APAC coverage options:** below about one rep's worth of APAC pipeline, a US Pacific late shift (roughly 3:00–7:00 PM PT) reaches Sydney and Auckland mornings on their next calendar day. That shift does **not** reach Singapore, India or Japan business hours well. Above that volume, base an APAC pod in Singapore or Sydney.

---

## 3. DST handling

Southern-hemisphere DST runs opposite to northern, and the US and Europe change on different dates. As a result, the gap between two cities moves several times a year.

| Region | DST starts | DST ends | 2026 dates | 2027 dates |
|---|---|---|---|---|
| US & Canada | 2nd Sunday of March | 1st Sunday of November | Mar 8 → Nov 1 | Mar 14 → Nov 7 |
| UK & EU | Last Sunday of March | Last Sunday of October | Mar 29 → Oct 25 | Mar 28 → Oct 31 |
| Australia (NSW, VIC, ACT, TAS, SA) | 1st Sunday of October | 1st Sunday of April | ends Apr 5, starts Oct 4 | ends Apr 4, starts Oct 3 |
| New Zealand | Last Sunday of September | 1st Sunday of April | ends Apr 5, starts Sep 27 | ends Apr 4, starts Sep 26 |
| No DST | Arizona (except Navajo Nation), Hawaii, Saskatchewan, Queensland, WA, NT, India, China, Japan, Singapore, UAE | | | |

**Mismatch weeks:** between the US and EU change dates (in 2026, Mar 8–28 and Oct 25–31), New York is 4 hours behind London instead of 5. Shared US/EMEA call blocks and handoffs move by an hour in those weeks.

**Implementation rules**
- Calculate every send time and call-block eligibility with a time-zone library (Python `zoneinfo`, or the sequencer's "prospect time zone" setting). Never hand-code offsets.
- Re-check the calendar view of recurring cross-region call blocks the week before each DST change in the table above.
- Sequencer steps scheduled "in prospect's time zone" need the contact's IANA zone populated. Contacts without one go to a "time zone unknown" queue, not the default zone.

The dates above were generated from the IANA time-zone database (Python `zoneinfo`).

---

## 4. Permitted calling hours by country (recipient local time)

The **legal window** is the outer limit set by law. The **team window** is the house rule BDRs actually dial in, and it always sits inside the legal window. Where no statute sets B2B hours, the team window is a policy choice.

| Country | Legal window (source) | Team window | Other call rules (see [outbound-compliance.md](../13-compliance/outbound-compliance.md)) |
|---|---|---|---|
| **United States** | 8 AM–9 PM (TCPA, 47 CFR 64.1200(c)(1); TSR). Some states are narrower, e.g. Florida 8 AM–8 PM. | Weekdays 8:30 AM–5:00 PM | Internal DNC; consent needed for autodialed or prerecorded calls to mobiles |
| **Canada** | Weekdays 9 AM–9:30 PM, weekends 10 AM–6 PM (CRTC Telemarketing Rules; B2B calls are exempt from the National DNCL; whether these hours bind B2B calls: **Unverified, confirm with counsel.**) | Weekdays 9:00 AM–5:00 PM | Register with the DNCL operator; keep an internal DNC list |
| **United Kingdom** | No statutory hours | Weekdays 9:00–17:00 | TPS / CTPS screen |
| **Germany** | No statutory hours; B2B calls need presumed consent (UWG §7) | Weekdays 9:00–17:00 | Document the presumed-consent reason per account |
| **France** | **Consumer telephone prospecting has been opt-in since 11 Aug 2026** (loi n° 2025-594, art. 13; décret n° 2026-662 of 23 July 2026). Consent must be explicit, lasts at most one year, and the caller must be able to prove it (DGCCRF: keep proof for at least 3 years). Bloctel opt-out is replaced. The earlier consumer hours (weekdays 10:00–13:00 and 14:00–20:00, Décret 2022-1313) predate the reform; per the [DGCCRF guide](https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/demarchage-telephonique-professionnels-mettez-vous-en-conformite-avec-la-reglementation) they still apply alongside the consent rule, with at most four calls to the same consumer in 30 days (checked 2026-10-13) The regime is consumer-facing, and B2B treatment is less clear. | Weekdays 10:00–13:00, 14:00–17:30 | **Apply the consent rule whenever a contact's status is doubtful** (sole traders, personal mobiles). Max 4 attempts per 30 days as policy |
| **Other EU** | Check national law; none known for B2B | Weekdays 9:00–17:00 | LIA on file |
| **Australia** | Weekdays 9 AM–8 PM, Saturday 9 AM–5 PM, no Sunday or national public holidays (Telecommunications (Telemarketing and Research Calls) Industry Standard 2017, in force; the [Federal Register entry](https://www.legislation.gov.au/F2017L00323/latest) lists it as scheduled to be repealed on 1 April 2027 and the text has no carve-out for business numbers; checked 2026-10-13) | Weekdays 9:00–17:00 | Do Not Call Register |
| **New Zealand, Singapore, Japan** | No statutory B2B hours known | Weekdays 9:00–17:00 (Japan: avoid 12:00–13:00) | Singapore: DNC provisions exclude B2B calls |
| **India** | DPDP Rules and TRAI commercial-communication rules: **Unverified, confirm with counsel.** | Weekdays 9:30–17:30 | Hold until verified |
| **China, Hong Kong, Macau** | `review` geography | No calling until compliance signs off | PIPL / screening |
| **Blocked geographies** | n/a | **No calling** | See the sanctions policy |

> Calling hours are researched guardrails, not legal advice. Rows marked unverified have not been checked against primary sources: **Unverified, confirm with counsel.** See [Verification status](../13-compliance/outbound-compliance.md#verification-status).

### Dialer configuration
- Orum call blocks pull only contacts whose local time is inside their country's team window at dial time. The [call-block structure](../../02-execution-and-workflows/12-stack-configuration/orum-call-blocks.md) (9:00–10:30 and 2:00–3:30) is defined in prospect-local time.
- Each country's public-holiday calendar is loaded into the dialer and the sequencer.

## Sources
[47 CFR 64.1200](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200) · [CRTC telemarketing rules](https://crtc.gc.ca/eng/phone/telemarketing/reg.htm) · [CRTC business alerts](https://crtc.gc.ca/eng/phone/telemarketing/biz.htm) · [DGCCRF: démarchage téléphonique, professionals' compliance guide](https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/demarchage-telephonique-professionnels-mettez-vous-en-conformite-avec-la-reglementation) · Décret n° 2022-1313 of 13 Oct 2022 (JO 14 Oct 2022; search "2022-1313" on [Légifrance](https://www.legifrance.gouv.fr/)) · [ACMA Telemarketing and Research Calls Industry Standard 2017](https://www.legislation.gov.au/F2017L00323/latest) · [UWG §7](https://www.gesetze-im-internet.de/uwg_2004/__7.html) · [IANA time zone database](https://www.iana.org/time-zones)
