# Sample Data Directory

Fictional sample datasets used to run and test `score_accounts.py`, `backtest.py`, and `pipeline.py`. Company and contact names are invented.

| File | Columns | Used by |
|---|---|---|
| `accounts.csv` | `account_id, account_name, country, region, employees, revenue_m, has_salesforce, signal_type, signal_date` | `score_accounts.py`, `pipeline.py`. `country` is ISO 3166-1 alpha-2; `region` is optional ISO 3166-2 (e.g. `US-CA`, `UA-43`). `signal_type` is one of the types in `decay_calculator.py` (blank means no signal). Rows 106–108 exercise the geo gate (block, block, review); rows 103–104 show the Tier 1 signal cap (stale signal, fit only). |
| `contacts.csv` | `contact_id, account_id, first_name, last_name, title, email` | `pipeline.py`. Emails use the reserved `.example` domain. |
| `historical.csv` | `account_id, tier, converted` | `backtest.py` (10 rows; illustrative only, too small to calibrate anything) |

`scored_accounts.csv`, `approval_queue.csv` and `compliance_hold.csv` are generated outputs and are gitignored.
