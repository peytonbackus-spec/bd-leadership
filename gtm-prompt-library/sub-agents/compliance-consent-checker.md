---
id: subagent-compliance-consent-checker
type: sub-agent
tags: [sub-agent, shared-primitive]
last_modified: 2026-09-25
---

# Sub-Agent: Compliance/Consent Checker

**Slug:** `compliance-consent-checker`

## Task (single-purpose, reusable)
Given a target contact for outreach, determine the CASL consent basis and block the send if none is documented:
1. **Express consent:** an opt-in record with timestamp and source (form ID or IP).
2. **Implied consent, existing business relationship:** a purchase, contract or inquiry inside the CASL time windows, documented in the CRM.
3. **Implied consent, conspicuous publication:** the address is published (e.g. company website), with **no** statement that the person doesn't want unsolicited commercial messages, **and** the message is relevant to the person's business role or duties. Record where it was published and when it was checked.
4. **None of the above:** block.

CASL penalties reach C$10M per violation for organizations (C$1M for individuals). Guardrail, not legal advice. See [outbound-compliance.md](../../04-compliance-and-coverage/13-compliance/outbound-compliance.md).

## Called By (parent agents that invoke this sub-agent)
[casl-cold-outreach-compliance-checker](../agents/casl-cold-outreach-compliance-checker.md) . [sequence-builder](../agents/sequence-builder.md) . [account-research-brief](../agents/account-research-brief.md)

## Why This Exists As a Sub-Agent, Not Duplicated Logic
3 different top-level agents need this exact primitive. Rather than each parent re-deriving the logic, they invoke this shared sub-agent and consume its output -- one place to fix or improve the logic instead of 3.

## See Also
[gtm-prompt-library/README](../README.md)
