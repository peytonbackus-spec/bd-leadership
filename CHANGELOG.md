# Changelog

## Unreleased
- Tool profiles: added HubSpot and Salesforce (vendor figures as of Oct 2026, vault links and frontmatter stripped); Clay refreshed with the Sculpt 2026 and Workflow cost controls updates. README test counts corrected to 70 (sanitizer tests: 9).
- Maintenance: added a README "Maintainer notes" section (local pre-push check, local-only deny-list, sanitizing synced content); `sanitize_synced.py` folder arguments, including a folder outside the repo, are now covered by a test.
- Compliance: restored checked wording, with primary-source citations already recorded in the repo, for France (calling hours and four-call cap alongside the consent rule), Quebec (Act s.1 work-contact exclusion), the Australian telemarketing standard (in force, scheduled sunset 1 Apr 2027) and Syria's terrorism-sponsor status. Japan, India, Austria and CRTC calling hours for B2B calls remain "Unverified, confirm with counsel". Verification-status table updated.
- Docs aligned to code: the operating model's ICP now matches the scorer (250–5,000 employees, $50–1,000M revenue), and the inbound-touch SLA is the tiered 5-minute / 30-minute / next-business-day windows in the speed-to-lead server and contract, in place of a flat 15 minutes.
- Labeling: funnel conversion figures are described as illustrative ranges to replace with the team's own baseline; unit-economics targets and the onboarding ramp (including "10 Meetings Held") are labeled as starting targets or an example ramp.
- Added `scripts/sanitize_synced.py` (idempotent, with `--check`) and 8 tests, to strip vault-only frontmatter, tags, paths and references from synced files. Run it after any vault sync.

### Earlier in this release
- Guardrails: added `scripts/check_repo.py` (and a `check_repo.sh` wrapper) with 22 tests. It checks for heading-only or empty markdown and empty folders, private-vault leftovers and absolute paths, broken links and anchors, and, locally only, terms from a gitignored deny-list. CI runs the generic checks; output is `path:line` only.
- Compliance: seven items are now explicitly marked "Unverified, confirm with counsel" (Austria B2B email consent, Japan published-address exception, India DPDP Rules, Quebec Law 25 business-contact exemption, CRTC calling hours for B2B calls, the Australian 2017 telemarketing standard, France's 2022 calling-hour limits alongside the new consent rule). Added a Verification status table. Corrected the Australian standard's source link.
- README: rewrote the opening screen (who it is for, what is here, where to start, what is real versus not); removed unsupported superlatives; documented the guardrail checks and the 61-test suite.
- Consistency: stage names standardized to Meeting Set → Meeting Held → SQO (the "SAL" and "Meeting Booked" terms are folded into the glossary); BDR and SDR defined as the same role; the metrics, unit-economics, cross-functional SLA and onboarding docs now state that their figures are unsourced starting targets; removed a claimed research-time reduction that had no baseline.

### Earlier in this release
- Case studies anonymized (enterprise procurement SaaS, 2025–2026; FP&A SaaS, 3-year tenure), renamed, linked from the README, and marked as self-reported. They note that the repo scripts are sample-data reconstructions, not production systems.
- Removed personal-business references from the CASL raw source and the CASL gate contract page.
- Prompt library: removed vault-only `bounded_autonomy_note` frontmatter and dead "See Also" entries; contract YAMLs, contract pages and the speed-to-lead schema now use repo-relative paths. Tool profiles: dropped `wiki/competitive` tags.
- Speed-to-lead: the contract YAML now lists the five tools the server registers, and a new test fails if they drift. `pyyaml` added to requirements.
- CASL: annotated the raw source with the C$10M organization / C$1M individual penalty caps and the conspicuous-publication implied-consent rule. Updated the consent-checker sub-agent, the checker agent and the gate contract to match.
- France: documented the consumer telephone-prospecting opt-in regime in force since 11 Aug 2026 (loi n° 2025-594 art. 13; décret n° 2026-662), with a DGCCRF citation.
- Geo policy: Russia and Belarus labeled "policy choice, not a comprehensive embargo"; Syria (review) carries a note to verify current status with OFAC and State.
- Scoring: `score_accounts.py` now uses `signal_type`/`signal_date` with the decay calculator. Tier 1 requires an active signal (configurable `--min-signal-strength`), fit-only and stale-signal accounts cap at Tier 2, and `--as-of` makes runs reproducible.
- Pipeline: `pipeline.py build` applies the geo policy. It skips blocked contacts, holds review contacts in `compliance_hold.csv`, and logs the reason for each.
- Sample data: accounts use signal columns; contacts cover every account and use `.example` email domains.
- README: roadmap section for planned, not-built items (denied-party screening API, live LLM hook generation, Pages-hosted calculator). Tests: 39.

### Earlier in this release
- Compliance: expanded `outbound-compliance.md` (GDPR/ePrivacy + LIA template, UK PECR subscriber types, Germany UWG §7, California/US state privacy, TCPA/TSR and CRTC DNCL, Quebec Law 25, LGPD, PIPL, sanctions and restricted-geography policy, cited sources); added `geo-policy.csv`; wrote the 13-compliance README.
- Scoring: `score_accounts.py` reads the geo policy. Blocked geographies score 0 and are tiered `Excluded (geo block)`; review/unknown geographies are flagged. Paths now resolve from the repo root. Sample accounts gained `country`/`region`.
- Sequencing: added a pre-send compliance gate (geo, denied-party screening, consent, suppression, DNC, content) to `outreach-sequence-design.md`.
- Global coverage: rebuilt `time-zone-model.md` (separate ET/CT/MT/PT windows, Canada zones, EMEA/APAC, 2026–2027 DST dates, calling hours by country); wrote the 14-global-coverage README.
- Tests: added scoring/geo-gate and pipeline tests (27 total). CI now runs the whole suite including `evals/`.
- Accuracy: `pipeline.py` `enroll` is labeled a dry run (it previously printed a fake "200 OK"); README and AI-workflows README state that no script calls an LLM or live API; trimmed unused dependencies from `requirements.txt`.
- Consistency: tier names standardized to Tier 1/2/3 and `Account_Tier__c` across glossary, field spec, sync spec and 90-day plan; CASL penalty corrected to up to C$10M per violation for organizations; removed stale `gtm-os/` and vault-audit paths from the speed-to-lead POC and contract pages.
- Content: filled heading-only READMEs (12-stack-configuration, 15-content-library); added a worked coaching scorecard example.

## Previous
- README: test section now states what is actually covered (2 unit tests on the signal decay calculator); removed the "Prompt Evals" claim.
- CI: actions/checkout v4, actions/setup-python v5.
- CLAUDE.md: generic scope statement.
- Synced agent prompts and tool profiles from the research vault; added hybrid-team ownership and comp doc.
