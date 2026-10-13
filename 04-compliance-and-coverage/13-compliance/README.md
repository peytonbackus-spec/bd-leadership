# 13. Outbound Compliance

Guardrails that decide **who** a BDR team may contact, **on which channel**, and **what has to happen first**. This is an operating checklist, not legal advice. Confirm with counsel before relying on it.

## Files

| File | What it is |
|---|---|
| [outbound-compliance.md](./outbound-compliance.md) | Channel rules by jurisdiction (CAN-SPAM, CASL, GDPR/ePrivacy, UK PECR, Germany UWG §7, California and other US state laws, TCPA and Canada's DNCL, Quebec Law 25, LGPD, PIPL), an LIA template, the sanctions and restricted-geography policy, and cited sources |
| [geo-policy.csv](./geo-policy.csv) | Machine-readable allow / review / block list by ISO country code and ISO 3166-2 region code, with the email and phone rule for each |

## How it connects to the rest of the repo

- **Scoring:** [score_accounts.py](../../01-strategy-and-operations/02-icp-and-account-scoring/score_accounts.py) reads `geo-policy.csv`. `block` accounts score 0 and are tiered `Excluded (geo block)`. `review` accounts keep their score but are flagged for sign-off. Geographies that aren't in the file default to `review`. [pipeline.py](../../02-execution-and-workflows/08-ai-workflows/pipeline.py) applies the same policy before building the hook review queue: blocked contacts are skipped, and review contacts are held with the reason. Tests: [tests/test_score_accounts.py](../../tests/test_score_accounts.py), [tests/test_pipeline.py](../../tests/test_pipeline.py).
- **Sequencing:** the [pre-send compliance gate](../../02-execution-and-workflows/12-stack-configuration/outreach-sequence-design.md#pre-send-compliance-gate) runs geography, denied-party screening, consent, suppression, DNC, and content checks before enrollment.
- **Calling hours:** permitted local calling windows live in the [time-zone model](../14-global-coverage/time-zone-model.md).
- **Prompt library:** the [CASL compliance gate contract](../../gtm-prompt-library/contracts/casl-compliance-gate-contract.md) and the [compliance/consent checker sub-agent](../../gtm-prompt-library/sub-agents/compliance-consent-checker.md) apply the CASL rules to drafts.

## Editing the policy

1. Change the row in `geo-policy.csv`. `status` must be `allow`, `review`, or `block`, otherwise the scorer raises an error.
2. Give the reason in the `reason` column and update the matching section of `outbound-compliance.md` with a source.
3. Run `pytest`. The tests check that the comprehensive-sanctions geographies still score 0.
