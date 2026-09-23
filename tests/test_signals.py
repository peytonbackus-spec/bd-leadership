import pytest
from datetime import datetime
from 01-strategy-and-operations.03-signals-and-research.decay_calculator import calculate_decayed_score

def test_signal_decay():
    ref_date = datetime(2026, 9, 23)
    
    # 14-day old job posting (half-life = 14) -> score should be half
    score = calculate_decayed_score(100.0, "job_posting", "2026-09-09", ref_date)
    assert score == 50.0

def test_fresh_signal():
    ref_date = datetime(2026, 9, 23)
    
    # 0-day old signal -> score should remain unchanged
    score = calculate_decayed_score(100.0, "funding_round", "2026-09-23", ref_date)
    assert score == 100.0
