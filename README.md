# GTM & Business Development Leadership Framework

An enterprise-grade blueprint, execution framework, and programmatic toolset for scaling outbound Go-To-Market (GTM) teams, account scoring, AI automation pipelines, and revenue operations.

---

## Repository Architecture & Navigation

```mermaid
flowchart TD
    classDef primary fill:#1f2937,stroke:#4f46e5,stroke-width:2px,color:#fff
    classDef execution fill:#0f172a,stroke:#0ea5e9,stroke-width:1.5px,color:#fff
    classDef strategy fill:#111827,stroke:#10b981,stroke-width:1.5px,color:#fff
    classDef tools fill:#1e1b4b,stroke:#8b5cf6,stroke-width:1.5px,color:#fff

    Root["bd-leadership Repository"]

    subgraph Strat["01. Strategy & Operations"]
        Ops["01-operating-model"]
        ICP["02-icp-and-account-scoring"]
        Signals["03-signals-and-research"]
        Metrics["07-metrics-and-forecasting"]
    end

    subgraph Exec["02. Execution & Workflows"]
        Campaigns["04-outbound-campaigns"]
        AIWorkflows["08-ai-workflows"]
        ToolEval["09-gtm-tool-evaluation"]
        Stack["12-stack-configuration"]
    end

    subgraph Enablement["03. Team & Enablement"]
        Coaching["05-coaching"]
        Hiring["06-hiring-and-onboarding"]
        Alignment["10-cross-functional"]
        Content["15-content-library-for-bdrs"]
    end

    subgraph Compliance["04. Compliance & Coverage"]
        Legal["13-compliance"]
        Coverage["14-global-coverage"]
    end

    subgraph Proof["05. Proof & Tools"]
        CaseStudies["case-studies"]
        Interactive["docs/capacity-calculator.html"]
        Plan90["11-first-90-days"]
    end

    Root --> Strat
    Root --> Exec
    Root --> Enablement
    Root --> Compliance
    Root --> Proof

    ICP --> AIWorkflows
    Signals --> AIWorkflows
    AIWorkflows --> Stack
    Stack --> Ops
    Metrics --> ICP

    class Root primary
    class Ops,ICP,Signals,Metrics strategy
    class Campaigns,AIWorkflows,ToolEval,Stack execution
    class Coaching,Hiring,Alignment,Content,Legal,Coverage tools
    class CaseStudies,Interactive,Plan90 primary
```

---

## Quick Start Commands

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Score target accounts using fit & signal weights
python 01-strategy-and-operations/02-icp-and-account-scoring/score_accounts.py sample-data/accounts.csv

# 3. Validate conversion lift against historical datasets
python 01-strategy-and-operations/02-icp-and-account-scoring/backtest.py sample-data/historical.csv

# 4. Generate AI account brief & personalized hooks (dry-run mode)
python 02-execution-and-workflows/08-ai-workflows/pipeline.py build sample-data/accounts.csv sample-data/contacts.csv

# 5. Process human-approved briefs into sequence execution payloads
python 02-execution-and-workflows/08-ai-workflows/pipeline.py enroll approval_queue.csv
```
