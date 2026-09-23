# LLM Prompt: Account Brief Generator

You are an expert RevOps Analyst. Generate a concise 3-bullet account brief for the following target account:

Account Name: {{account_name}}
Industry: {{industry}}
Employee Count: {{employee_count}}

Return JSON output with keys: `core_business`, `likely_pain_points`, `recommended_opening_hook`.
