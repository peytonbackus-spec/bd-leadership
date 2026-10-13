# 08. AI Workflows

Scripts and prompt templates for account research, opening-line generation, and inbound speed-to-lead. Everything here runs on sample or mock data. **None of these scripts calls an LLM or a live CRM/sequencer API today.** The prompts are written for that next step.

| File | What it does | Status |
|---|---|---|
| [pipeline.py](./pipeline.py) | `build`: joins contacts to accounts and applies the [geo policy](../../04-compliance-and-coverage/13-compliance/geo-policy.csv). Blocked contacts are skipped, review contacts are held in `compliance_hold.csv`, and each skip or hold is logged with its reason. Allowed contacts get a templated opening hook in `approval_queue.csv` for human review. `enroll`: dry run only. | Runnable; fixed string template, no LLM call. Tests: [tests/test_pipeline.py](../../tests/test_pipeline.py) |
| [account_brief.py](./account_brief.py) | Prints a JSON brief skeleton for one account | Runnable stub; no research or LLM call |
| [prompts/](./prompts/) | `account_brief.md`, `first_line.md`, `call_review.md`: prompt templates with `{{variables}}` | Templates; not yet wired to a model |
| [evals/test_prompt_evals.py](./evals/test_prompt_evals.py) | Length and banned-buzzword checks for a generated brief | Runs in `pytest`, against fixed example strings, not live model output |
| [speed_to_lead_server.py](./speed_to_lead_server.py) | MCP server for the speed-to-lead SLA contract | Proof of concept: SLA evaluation is real logic, data and side effects are mocked. See [speed-to-lead-README.md](./speed-to-lead-README.md) |
| [mock_data.json](./mock_data.json) | Sample leads and meetings for the MCP server self-test | Mock data |

## Run
```bash
python3 02-execution-and-workflows/08-ai-workflows/pipeline.py build
python3 02-execution-and-workflows/08-ai-workflows/speed_to_lead_server.py --selftest
```

## Path to a live version
1. Swap the hook template in `pipeline.py` for a model call using `prompts/first_line.md`. Score every output with the eval checks before it reaches the queue.
2. Add the rest of the [pre-send compliance gate](../12-stack-configuration/outreach-sequence-design.md#pre-send-compliance-gate) in front of `enroll`. The geo step is already applied in `build`.
3. Keep the human review step. `approval_queue.csv` is the approval point, not a formality.
