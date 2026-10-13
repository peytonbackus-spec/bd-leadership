import importlib.util
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent

# Resolve module using explicit file path to support hyphenated and numeric directory names
file_path = ROOT / "02-execution-and-workflows" / "08-ai-workflows" / "speed_to_lead_server.py"
spec = importlib.util.spec_from_file_location("speed_to_lead_server", file_path)
server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server)

CONTRACT = yaml.safe_load((ROOT / "gtm-prompt-library" / "contracts" / "speed-to-lead-sla-contract.yaml").read_text())


def test_contract_tools_match_server_tools():
    declared = CONTRACT["boundaries"]["allowed_mcp_tools"]
    assert sorted(declared) == sorted(server.REGISTERED_TOOLS)
    assert len(declared) == len(set(declared))


def test_contract_paths_exist_in_repo():
    boundaries = CONTRACT["boundaries"]
    for path in boundaries["readable_paths"]:
        assert (ROOT / path).exists(), path
    for path in boundaries["writeable_paths"]:
        assert (ROOT / path).parent.is_dir(), path
