import importlib.util
from pathlib import Path

import pandas as pd
import pytest

# Resolve module using explicit file path to support hyphenated and numeric directory names
file_path = Path(__file__).parent.parent / "02-execution-and-workflows" / "08-ai-workflows" / "pipeline.py"
spec = importlib.util.spec_from_file_location("pipeline", file_path)
pipeline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pipeline)


def run_build(tmp_path):
    out, hold = tmp_path / "approval_queue.csv", tmp_path / "compliance_hold.csv"
    pipeline.run_pipeline("build", output_file=out, hold_file=hold)
    return pd.read_csv(out), pd.read_csv(hold)


def test_build_queues_only_allowed_geographies(tmp_path):
    queue, _ = run_build(tmp_path)
    assert set(queue["geo_status"]) == {"allow"}
    assert queue["generated_hook"].str.startswith("Hi ").all()


def test_build_skips_blocked_and_logs_why(tmp_path, capsys):
    queue, hold = run_build(tmp_path)
    blocked = {"Zeta Trading", "Eta Freight"}
    assert blocked.isdisjoint(queue["account_name"]) and blocked.isdisjoint(hold["account_name"])
    log = capsys.readouterr().out
    assert "SKIP" in log and "Zeta Trading" in log and "OFAC" in log


def test_build_holds_review_with_reason(tmp_path, capsys):
    _, hold = run_build(tmp_path)
    assert list(hold["account_name"]) == ["Theta Analytics"]
    assert hold["geo_reason"].iloc[0].startswith("CN:")
    assert "HOLD" in capsys.readouterr().out


def test_unknown_geography_is_held():
    accounts = pd.DataFrame([{"account_id": 1, "account_name": "Test Co", "country": ""}])
    contacts = pd.DataFrame([{"account_id": 1, "first_name": "Ana", "last_name": "Diaz", "title": "VP Sales"}])
    allowed, held, blocked = pipeline.apply_geo_gate(pipeline.build_hooks(accounts, contacts))
    assert allowed.empty and blocked.empty
    assert held.iloc[0]["geo_reason"] == "geography missing from geo policy"


def test_hook_uses_contact_and_account_fields():
    accounts = pd.DataFrame([{"account_id": 1, "account_name": "Test Co"}])
    contacts = pd.DataFrame([{"account_id": 1, "first_name": "Ana", "title": "VP Sales"}])
    hook = pipeline.build_hooks(accounts, contacts).iloc[0]["generated_hook"]
    assert "Ana" in hook and "VP Sales" in hook and "Test Co" in hook


def test_contacts_without_account_are_dropped():
    accounts = pd.DataFrame([{"account_id": 1, "account_name": "Test Co"}])
    contacts = pd.DataFrame([{"account_id": 2, "first_name": "Ana", "title": "VP Sales"}])
    assert pipeline.build_hooks(accounts, contacts).empty


def test_enroll_is_dry_run(tmp_path, capsys):
    out = tmp_path / "approval_queue.csv"
    pipeline.run_pipeline("enroll", output_file=out, hold_file=tmp_path / "hold.csv")
    assert "DRY RUN" in capsys.readouterr().out
    assert not out.exists()


def test_unknown_mode_raises():
    with pytest.raises(ValueError):
        pipeline.run_pipeline("send")
