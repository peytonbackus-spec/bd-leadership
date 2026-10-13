# 01. Operating Model & Governance

## Charter & Role Definitions
- **Business Development Representative (BDR/SDR):** Responsible for outbound pipeline creation, account research, cold outreach, and qualified meeting booking.
- **Account Executive (AE):** Responsible for discovery, solution mapping, validation, closing, and revenue expansion.
- **Revenue Operations (RevOps):** Responsible for data infrastructure, stack integration, routing rules, and performance analytics.

## Rules of Engagement (RoE)
1. **Account Ownership:** Accounts are assigned for 90-day active windows. If no meaningful touchpoint occurs within 90 days, ownership reverts to unassigned pool.
2. **Inbound vs Outbound Routing:** Inbound leads must be touched by designated inbound reps within the tiered SLA: 5 minutes for Tier 1 (Hot), 30 minutes for Tier 2 (Warm), next business day for Tier 3 (Cold). These are starting targets; the windows live in [speed_to_lead_server.py](../../02-execution-and-workflows/08-ai-workflows/speed_to_lead_server.py) and the [speed-to-lead contract](../../gtm-prompt-library/contracts/speed-to-lead-sla-contract.md). Outbound accounts are protected from inbound re-assignment for 30 days post-outreach.
3. **Handoff Criteria (AE accepts a Meeting Held):**
   - Fits ICP (B2B, 250–5,000 employees and $50–1,000M revenue, matching [score_accounts.py](../02-icp-and-account-scoring/score_accounts.py)).
   - Confirmed economic buyer or key stakeholder involvement.
   - Verified pain point aligned with core product capabilities.
   - Confirmed meeting held with AE present.
