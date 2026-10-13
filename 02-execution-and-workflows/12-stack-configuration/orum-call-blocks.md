# Orum Parallel Dialer Configuration

## Call Block Structure
- **Morning Blitz (9:00 AM - 10:30 AM):** High-priority Tier 1 accounts.
- **Afternoon Blitz (2:00 PM - 3:30 PM):** Follow-ups and Tier 2 accounts.
- **Time basis:** block times are in the *prospect's* local time, inside the permitted calling hours in the [time-zone model](../../04-compliance-and-coverage/14-global-coverage/time-zone-model.md). Accounts with `geo_status` `block`, or an uncleared `review`, are never loaded.
- **Dialing Ratio:** 3-line parallel dialing for unverified numbers; 1-line manual click-to-call for HQ executive direct dials.
