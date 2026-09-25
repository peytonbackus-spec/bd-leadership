---
id: agent-casl-cold-outreach-compliance-checker
type: prompt-agent
tags: [prompt-library, outbound-sdr]
function: Outbound SDR
purpose: Legal Compliance
priority: P0
last_modified: 2026-09-25
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
promoted_to_contract: casl-compliance-gate-contract
---

# /casl-cold-outreach-compliance-checker -- CASL Cold Outreach Compliance Checker

**Function:** Outbound SDR  
**Purpose:** Legal Compliance  
**Priority:** P0

> **Promoted to an autonomous Workflow Contract:** [casl-compliance-gate-contract](../contracts/casl-compliance-gate-contract.md) declares this as a bounded-autonomy automation (boundaries, role_map, stop_rules). This file remains as the human-readable spec; the contract is the enforceable version.

**Status: net-new, identified via second-pass gap research.**

## System Prompt
```
Given a cold outbound email or sequence targeting Canadian contacts, check: sender identification (real name, company, physical address, phone/email present), a functional one-click unsubscribe, non-deceptive subject line, no identity masking, and whether implied consent (existing business relationship) or express consent (opt-in) applies. Flag any message that would require express consent it does not have, and output the compliant version.
```

## Why This Gap Existed
Peyton's consulting firm is Ontario-registered and its core delivery stack (Apollo/Clay/sequences) is cold outbound to B2B contacts -- CASL violations carry fines up to $1M CAD per violation from the CRTC. This was a real, unflagged compliance gap, not a hypothetical one.

## Cross-References
[sequence-builder](sequence-builder.md) . [email-optimizer](email-optimizer.md)

## Sources
[CASL Compliance Research](../../raw-sources/01-casl-compliance.md)

## See Also
[gtm-prompt-library/README](../README.md)
