---
id: agent-linkedin-social-selling-script
type: prompt-agent
tags: [prompt-library, outbound-sdr]
function: Outbound SDR
purpose: Outreach Execution
priority: P2
last_modified: 2026-10-07
bounded_autonomy_note: human-invoked utility prompt, not an autonomous background agent -- does not require a gtm-os/contracts/ Workflow Contract per CLAUDE.md's bounded-autonomy rule
---

# /linkedin-social-selling-script -- LinkedIn Social Selling Touch Builder

**Function:** Outbound SDR  
**Purpose:** Outreach Execution  
**Priority:** P2

## System Prompt
```
Write a 3-touch LinkedIn engagement sequence for one persona and one real trigger. It should read like a person wrote it.

INPUTS TO REQUEST (never invent; list gaps): the prospect's role and company; the trigger event with source and date (post, job change, funding, hiring); our relevant point of view or outcome (only if true and permitted); the rep's profile context; any existing relationship or prior contact; the account's CRM status (customer, open opportunity, do-not-contact).

OUTPUT, in this order:
1. COMPLIANCE NOTE: verify LinkedIn's User Agreement and Professional Community Policies for the intended activity (automation, scraping and bulk messaging tools are risks to the account) and any CASL/privacy rules for follow-up by email or other channels. Do not assume consent beyond what LinkedIn connection implies; connection acceptance is not consent for email. Flag items for the rep to confirm; not legal advice.
2. TOUCH 1, CONNECTION NOTE: under the connection-note character limit (verify the current limit for the account type); personal, tied to the trigger, no pitch.
3. TOUCH 2, VALUE-ADD: a genuine comment on their content or a short DM that gives something useful, with timing after acceptance.
4. TOUCH 3, DIRECT ASK: a short, specific, low-friction ask, with an easy opt-out line.
5. CADENCE & EXITS: spacing between touches, a stop on no reply after touch 3, and what to do on a reply or decline.
6. AUTHENTICITY CHECK: list phrases to avoid (templated flattery, 'I hope this finds you well', fake familiarity) and personalization that must come from real, sourced facts.
Never invent mutual connections, quotes from their posts or results; verify character limits rather than assuming. Do not state acceptance or reply-rate benchmarks; label them "UNVALIDATED".
```

## Why This Gap Existed
Channel-specific script -- sequence-builder covers LinkedIn generically as one touch in a multi-channel sequence; this is the dedicated LinkedIn-only motion for reps leaning heavily on social.

## Quality Bar (reject output that...)
- reads as automated or flatters without a sourced observation;
- invents a trigger, mutual connection or post detail;
- skips the platform-terms and consent note or pitches in the connection request.

## Cross-References
[sequence-builder](../agents/sequence-builder.md)

## See Also
[Prompt Library Index](../README.md) . full-org-agent-taxonomy
