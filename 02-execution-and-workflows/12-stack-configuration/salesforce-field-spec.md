# Salesforce Custom Field Specifications

| Object | Field Label | API Name | Data Type | Picklist Values / Formula |
| :--- | :--- | :--- | :--- | :--- |
| Account | Account Tier | `Account_Tier__c` | Picklist | Tier 1, Tier 2, Tier 3, Excluded (geo block) |
| Account | Geo Policy Status | `Geo_Policy_Status__c` | Picklist | allow, review, block (from `geo-policy.csv` via `score_accounts.py`) |
| Account | Last Sanctions Screen | `Sanctions_Screen_Date__c` | Date | Set by the pre-send denied-party screen |
| Account | Fit Score | `Fit_Score__c` | Number(3,0) | Calculated via `score_accounts.py` |
| Contact | Hook Line | `AI_Hook_Line__c` | Text(255) | Populated from `pipeline.py` after human review |
| Contact | Time Zone | `Time_Zone__c` | Text(64) | IANA zone, e.g. `America/Chicago` (see time-zone model) |
| Opportunity| Lead Source Detail | `Lead_Source_Detail__c` | Picklist | Outbound SDR, Inbound Form, Signal Trigger |
