# 14. Global Coverage & Time-Zone Model

How a BDR team covers North America, EMEA, and APAC without calling anyone outside legal or sensible hours, and without losing coverage around DST changes.

## Files

| File | What it is |
|---|---|
| [time-zone-model.md](./time-zone-model.md) | Separate windows for each North American zone (ET, CT, MT, PT, Arizona, Atlantic, Newfoundland, Saskatchewan), EMEA and APAC zones with pod options, 2026–2027 DST dates and mismatch weeks, and permitted calling hours by country |
| [../13-compliance/geo-policy.csv](../13-compliance/geo-policy.csv) | Which geographies are allow, review, or block. Coverage planning only covers `allow` geographies and `review` geographies that have been cleared. |

## Decisions this model drives

- **Pod structure:** East (ET/CT) and West (MT/PT) pods in North America, an EMEA pod on GMT, and an APAC pod only once volume justifies it. A US Pacific late shift covers ANZ until then.
- **Data requirement:** every contact needs an IANA time-zone field. Contacts without one go to a "time zone unknown" queue, not a default zone.
- **Calendar hygiene:** check recurring cross-region call blocks the week before each DST change listed in the model.

## Related
- [Outbound compliance](../13-compliance/outbound-compliance.md): consent, DNC, and sanctions rules that the calling-hours table references
- [Orum call blocks](../../02-execution-and-workflows/12-stack-configuration/orum-call-blocks.md) and [Outreach sequence settings](../../02-execution-and-workflows/12-stack-configuration/outreach-sequence-design.md): where these windows are configured
- [Capacity calculator](../../05-proof-and-tools/docs/capacity-calculator.html): headcount math once pods are defined
