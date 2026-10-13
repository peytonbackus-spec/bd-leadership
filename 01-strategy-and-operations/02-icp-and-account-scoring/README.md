# 02. ICP & Account Scoring Framework

This module scores and tiers target accounts on firmographic fit plus a time-decayed intent signal, then applies a geography compliance gate.

## Tiers and motion
- **Tier 1 (Score >= 80 *and* an active signal):** Direct custom outreach, AI research brief, high-touch cadence.
- **Tier 2 (Score 50-79, or >= 80 without an active signal):** Semi-automated sequence, high phone volume.
- **Tier 3 (Score < 50):** Nurture sequence or excluded.
- **Excluded (geo block):** Account is in a `block` geography. Score forced to 0; never sequenced.

## How `score_accounts.py` scores (as implemented)

| Component | Rule | Points |
|---|---|---|
| Employees | 250–5,000 / >5,000 | 30 / 20 |
| Revenue ($M) | 50–1,000 / >1,000 | 30 / 20 |
| Salesforce in stack | `has_salesforce` true | 20 |
| Intent signal | `signal_type` + `signal_date`, decayed with the half-lives in [decay_calculator.py](../03-signals-and-research/decay_calculator.py) | up to 20 × decayed strength |
| **Geo gate** | `block` in [geo-policy.csv](../../04-compliance-and-coverage/13-compliance/geo-policy.csv) | score set to 0 |

**Signal rules**
- Signal strength runs from 1.0 for a fresh signal to 0.5 at one half-life (e.g. 14 days for `job_posting`, 60 days for `funding_round`), and 0 when there is no signal or the date can't be parsed.
- A signal is **active** when its strength is at or above `--min-signal-strength` (default 0.5, i.e. within one half-life).
- **Tier 1 requires an active signal.** Fit alone tops out at 80 and is capped at Tier 2, and so is a strong fit with a stale signal.

**Geo rules**
- Each row gets `geo_status` (`allow` / `review` / `block`).
- A region code (ISO 3166-2, e.g. `UA-43`) overrides its country code.
- A missing or unknown geography gets `review`. `review` accounts keep their score, and the script lists them for compliance sign-off before outreach.

**Limitations:** the weights, half-lives and the 0.5 threshold are illustrative. They have not been calibrated against real conversion data. Only one signal per account is scored, the most recent one you supply. [backtest.py](./backtest.py) shows how a calibration check would work on the 10-row sample in `sample-data/historical.csv`.

## Run it
```bash
python3 01-strategy-and-operations/02-icp-and-account-scoring/score_accounts.py --as-of 2026-10-13
python3 01-strategy-and-operations/02-icp-and-account-scoring/backtest.py
```
Scoring reads `sample-data/accounts.csv` and writes `sample-data/scored_accounts.csv` (gitignored). `--as-of` fixes the decay reference date; without it, today's date is used, so sample signals keep aging. Other options are `--min-signal-strength`, a different input path, `--output`, and `--geo-policy`.

With `--as-of 2026-10-13`, the sample data gives:
- 2 Tier 1 accounts, one of them held for geo review
- 2 Tier 2 accounts capped by the signal rule: one stale signal, one fit-only
- 2 Tier 3 accounts
- 2 accounts excluded by geography

Tests: [tests/test_score_accounts.py](../../tests/test_score_accounts.py).
