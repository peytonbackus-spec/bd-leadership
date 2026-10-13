# 12. Tech Stack Configuration Specifications

Configuration specs for the reference outbound stack: Salesforce (system of record), Outreach (sequencing), Orum (parallel dialer), and Clay (enrichment). These are design specs, not exported configs from a live instance.

| File | What it specifies |
|---|---|
| [sync-architecture.md](./sync-architecture.md) | Data flow between the four tools, field mappings and sync direction, opt-out uncoupling (email vs phone), and loop prevention |
| [salesforce-field-spec.md](./salesforce-field-spec.md) | Custom fields for tier, fit score, geo-policy status, sanctions-screen date, hook line, and time zone |
| [outreach-sequence-design.md](./outreach-sequence-design.md) | Enrollment caps, throttles, domain caps, and the **pre-send compliance gate** (geo policy, denied-party screening, consent, suppression, DNC, content) |
| [orum-call-blocks.md](./orum-call-blocks.md) | Call-block schedule by tier and dialing ratios |

Field names and tier values match the [glossary](../../01-strategy-and-operations/glossary.md), which is the source of truth when they conflict.
