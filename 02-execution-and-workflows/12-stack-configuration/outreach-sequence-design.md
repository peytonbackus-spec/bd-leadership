# Outreach Sequence Configuration

## Rules & Settings
- **Max Active Sequence Prospects per Rep:** 300
- **Throttle:** Max 50 new prospect enrollments per day per rep.
- **Safety Settings:** Domain caps set to max 3 contacts per domain in active sequence simultaneously.
- **Send windows:** Steps send in the prospect's local time zone, inside the permitted hours in the [time-zone model](../../04-compliance-and-coverage/14-global-coverage/time-zone-model.md).

## Pre-Send Compliance Gate

Every account and contact passes these checks **before enrollment**. Any failure stops enrollment. Nothing is "warn and send." Steps 1–2 run once per account. Steps 3–6 run per contact, and step 6 runs again before every step in the sequence.

| # | Check | Source of truth | Fail action |
|---|---|---|---|
| 1 | **Geography policy.** Look up the account's country and region in [geo-policy.csv](../../04-compliance-and-coverage/13-compliance/geo-policy.csv). | `geo_status` from [score_accounts.py](../../01-strategy-and-operations/02-icp-and-account-scoring/score_accounts.py) | `block`: never enroll. `review`: hold until compliance signs off in the CRM. |
| 2 | **Denied-party screening.** Screen the account legal name, its parent, and the contact name against the US Consolidated Screening List (OFAC SDN, BIS Entity List and others), the UK Sanctions List, the EU consolidated list, and the Canadian consolidated list. | Screening vendor or the trade.gov CSL API; result stored on the account with date and lists checked | Any potential match: hold, and route to compliance to clear or confirm. A confirmed match leads to a `block` disposition. Re-screen every 90 days and on any ownership change. |
| 3 | **Channel basis.** Check the email rule for the contact's country (CASL consent, UWG opt-in, PECR subscriber type, LIA on file). | [outbound-compliance.md](../../04-compliance-and-coverage/13-compliance/outbound-compliance.md); CASL contacts via the [CASL gate](../../gtm-prompt-library/contracts/casl-compliance-gate-contract.md) | Remove the email steps, or don't enroll if there's no allowed channel. |
| 4 | **Suppression.** Check email opt-out, objection to processing, and prior deletion requests. | `HasOptedOutOfEmail`, global suppression list | Remove the email steps. |
| 5 | **Do-not-call.** Check the internal DNC list, plus National DNC, TPS/CTPS or DNCL scrubs where they apply. | `DoNotCall`, scrub result date | Remove the call steps. |
| 6 | **Message content.** Sender identity, physical address, a working unsubscribe, an accurate subject line, and the send time inside permitted local hours. | Sequence template review | Fix the template before any enrollment. |

**What's implemented here:** only step 1 runs as code in this repo. `score_accounts.py` scores blocked accounts to 0, and `pipeline.py build` skips blocked contacts and holds review contacts in `compliance_hold.csv` with the reason. Both are covered by tests. Steps 2–6 are process specs for a sequencer and CRM setup. They are not implemented in this repo.
