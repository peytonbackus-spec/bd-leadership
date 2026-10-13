# 15. BDR Content & Enablement Library

What a BDR should be able to find in under a minute during a call block, and where each piece lives in this repo. The rule is one source per asset, owned by a named person and reviewed quarterly. Reps shouldn't keep private copies.

## Library structure

| Asset | Used for | Where it lives |
|---|---|---|
| Product proof points and internal-usage stories | Credibility lines on calls and in emails | [dogfooding.md](./dogfooding.md) (template; fill in per company) |
| Competitive displacement messaging | Accounts on a competing or legacy vendor | [competitive-displacement.md](../../02-execution-and-workflows/04-outbound-campaigns/competitive-displacement.md) |
| Objection handling | Live calls, role-play | [objection-mapper](../../gtm-prompt-library/sub-agents/objection-mapper.md), [competitive-battlecard](../../gtm-prompt-library/agents/competitive-battlecard.md), [Buyer Objections Heatmap](../../02-execution-and-workflows/09-gtm-tool-evaluation/Buyer%20Objections%20Heatmap.md) |
| Call, voicemail and LinkedIn scripts | First-touch execution | [cold-call-script](../../gtm-prompt-library/agents/cold-call-script.md), [voicemail-script](../../gtm-prompt-library/agents/voicemail-script.md), [linkedin-social-selling-script](../../gtm-prompt-library/agents/linkedin-social-selling-script.md) |
| Sequence templates | Multi-touch cadences | [04-outbound-campaigns](../../02-execution-and-workflows/04-outbound-campaigns/README.md), [sequence-builder](../../gtm-prompt-library/agents/sequence-builder.md) |
| Compliance quick reference | What can be sent to whom, and when | [outbound-compliance.md](../../04-compliance-and-coverage/13-compliance/outbound-compliance.md), [time-zone-model.md](../../04-compliance-and-coverage/14-global-coverage/time-zone-model.md) |
| Coaching scorecard | Self-review before 1:1s | [Coaching framework](../05-coaching/README.md), [worked example](../05-coaching/worked-scorecard-example.md) |

## Keeping it current
- Each asset has an owner and a "last reviewed" date. Anything older than a quarter is flagged in the team meeting.
- New proof points need a source (customer approval or a public case study) before reps use them.
- Retire assets that nobody opened last quarter instead of letting them pile up.
