# Salesforce Custom Field Specifications

| Object | Field Label | API Name | Data Type | Picklist Values / Formula |
| :--- | :--- | :--- | :--- | :--- |
| Account | ICP Tier | `ICP_Tier__c` | Picklist | Tier 1, Tier 2, Tier 3, Unqualified |
| Account | Fit Score | `Fit_Score__c` | Number(3,0) | Calculated via `score_accounts.py` |
| Contact | Hook Line | `AI_Hook_Line__c` | Text(255) | Populated via AI Pipeline |
| Opportunity| Lead Source Detail | `Lead_Source_Detail__c` | Picklist | Outbound SDR, Inbound Form, Signal Trigger |
