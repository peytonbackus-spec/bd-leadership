import importlib.util
from datetime import datetime
from pathlib import Path

import pandas as pd
import pytest

# Resolve module using explicit file path to support hyphenated and numeric directory names
file_path = Path(__file__).parent.parent / "01-strategy-and-operations" / "02-icp-and-account-scoring" / "score_accounts.py"
spec = importlib.util.spec_from_file_location("score_accounts", file_path)
score_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(score_module)

POLICY = score_module.load_geo_policy()
AS_OF = datetime(2026, 10, 13)


def make_account(**overrides):
    row = {"account_id": 1, "account_name": "Test Co", "country": "US", "region": "",
           "employees": 1200, "revenue_m": 250, "has_salesforce": True,
           "signal_type": "job_posting", "signal_date": "2026-10-13"}
    row.update(overrides)
    return row


def score_one(min_signal_strength=score_module.DEFAULT_MIN_SIGNAL_STRENGTH, **overrides):
    df = pd.DataFrame([make_account(**overrides)])
    return score_module.score_frame(df, POLICY, AS_OF, min_signal_strength).iloc[0]


# --- fit and signal scoring -------------------------------------------------

def test_full_fit_plus_fresh_signal_scores_100():
    row = score_one()
    assert score_module.fit_points(make_account()) == 80
    assert row["signal_points"] == 20
    assert row["fit_score"] == 100
    assert row["tier"] == "Tier 1"


def test_signal_decays_by_half_life():
    # job_posting half-life is 14 days
    assert score_module.signal_strength("job_posting", "2026-09-29", AS_OF) == 0.5
    assert score_one(signal_date="2026-09-29")["signal_points"] == 10


@pytest.mark.parametrize("signal_type,signal_date", [("", ""), ("job_posting", ""), ("job_posting", "not-a-date")])
def test_missing_or_bad_signal_counts_as_none(signal_type, signal_date):
    row = score_one(signal_type=signal_type, signal_date=signal_date)
    assert row["signal_strength"] == 0.0
    assert not row["active_signal"]


def test_fit_only_caps_at_tier_2():
    row = score_one(signal_type="", signal_date="")
    assert row["fit_score"] == 80
    assert row["tier"] == "Tier 2"


def test_stale_signal_caps_at_tier_2():
    # 30 days old at a 14-day half-life -> strength 0.23, below the 0.5 default
    row = score_one(signal_date="2026-09-13")
    assert row["fit_score"] >= 80
    assert not row["active_signal"]
    assert row["tier"] == "Tier 2"


def test_threshold_is_configurable():
    row = score_one(min_signal_strength=0.2, signal_date="2026-09-13")
    assert row["active_signal"]
    assert row["tier"] == "Tier 1"


def test_tier_boundaries():
    assert score_module.assign_tier(80, "allow", True) == "Tier 1"
    assert score_module.assign_tier(80, "allow", False) == "Tier 2"
    assert score_module.assign_tier(79, "allow", True) == "Tier 2"
    assert score_module.assign_tier(50, "allow", True) == "Tier 2"
    assert score_module.assign_tier(49, "allow", True) == "Tier 3"


# --- geo gate ---------------------------------------------------------------

@pytest.mark.parametrize("country,region", [("IR", ""), ("CU", ""), ("KP", ""), ("RU", ""), ("BY", ""),
                                            ("UA", "UA-43"), ("UA", "UA-14"), ("UA", "UA-09")])
def test_blocked_geographies_score_zero(country, region):
    row = score_one(country=country, region=region)
    assert row["geo_status"] == "block"
    assert row["fit_score"] == 0
    assert row["tier"] == score_module.EXCLUDED_TIER


def test_syria_is_review_not_block():
    assert score_module.geo_status("SY", "", POLICY) == "review"


def test_region_overrides_country():
    assert score_module.geo_status("UA", "UA-43", POLICY) == "block"
    assert score_module.geo_status("UA", "", POLICY) == "allow"
    assert score_module.geo_status("CA", "CA-QC", POLICY) == "allow"


def test_review_keeps_score_but_flags():
    row = score_one(country="CN")
    assert row["geo_status"] == "review"
    assert row["fit_score"] == 100


@pytest.mark.parametrize("country", ["", "ZZ"])
def test_unknown_geography_defaults_to_review(country):
    assert score_one(country=country)["geo_status"] == "review"


def test_missing_optional_columns_default():
    df = pd.DataFrame([make_account()]).drop(columns=["country", "region", "signal_type", "signal_date"])
    row = score_module.score_frame(df, POLICY, AS_OF).iloc[0]
    assert row["geo_status"] == "review"
    assert row["tier"] == "Tier 2"


def test_policy_rejects_unknown_status(tmp_path):
    bad = tmp_path / "policy.csv"
    bad.write_text("country_code,region_code,name,status,email_rule,phone_rule,reason\nUS,,United States,maybe,,,\n")
    with pytest.raises(ValueError):
        score_module.load_geo_policy(bad)


# --- CLI --------------------------------------------------------------------

def test_main_writes_expected_sample_tiers(tmp_path):
    out = tmp_path / "scored.csv"
    score_module.main([str(score_module.DEFAULT_INPUT), "--output", str(out), "--as-of", "2026-10-13"])
    tiers = pd.read_csv(out).set_index("account_name")["tier"].to_dict()
    assert tiers["Acme Corp"] == "Tier 1"          # fit + active signal
    assert tiers["Gamma Systems"] == "Tier 2"      # stale signal
    assert tiers["Delta Health"] == "Tier 2"       # fit only
    assert tiers["Zeta Trading"] == score_module.EXCLUDED_TIER
    assert tiers["Eta Freight"] == score_module.EXCLUDED_TIER
