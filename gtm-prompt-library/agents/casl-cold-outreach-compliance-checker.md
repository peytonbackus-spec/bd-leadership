---
id: agent-casl-cold-outreach-compliance-checker
type: prompt-agent
tags: [prompt-library, outbound-sdr]
function: Outbound SDR
purpose: Legal Compliance
priority: P0
last_modified: 2026-10-07
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
Cold B2B outbound to Canadian contacts (Apollo/Clay/sequences) triggers CASL regardless of employer -- violations carry fines up to $1M CAD per violation from the CRTC. Any Canadian-facing outbound role or tool needs this gate; it was a real, unflagged compliance gap when this agent was built. (Scope note 2026-10-01: wording reframed from the consulting-practice rationale to match CLAUDE.md Section 5.)

## Cross-References
[sequence-builder](../agents/sequence-builder.md) . [email-optimizer](../agents/email-optimizer.md)

## See Also
[Prompt Library Index](../README.md) . full-org-agent-taxonomy . [Sub-Agent Layer](../README.md)
