import math
from datetime import datetime

SIGNAL_HALF_LIVES_DAYS = {
    "job_posting": 14,      # Hiring signals stale fast
    "tech_stack_change": 30, # Moderate persistence
    "funding_round": 60,    # High persistence
    "web_intent": 7,        # Very high decay rate
    "executive_hire": 45
}

def calculate_decayed_score(base_score: float, signal_type: str, signal_date_str: str, reference_date: datetime = None) -> float:
    """Calculates exponential time-decay for intent signals."""
    if reference_date is None:
        reference_date = datetime.now()
    
    signal_date = datetime.strptime(signal_date_str, "%Y-%m-%d")
    days_old = max(0, (reference_date - signal_date).days)
    
    half_life = SIGNAL_HALF_LIVES_DAYS.get(signal_type, 30)
    decay_factor = math.pow(0.5, days_old / half_life)
    
    return round(base_score * decay_factor, 2)

if __name__ == "__main__":
    sample_signal = calculate_decayed_score(base_score=100.0, signal_type="job_posting", signal_date_str="2026-09-01", reference_date=datetime(2026, 9, 23))
    print(f"Decayed Signal Score: {sample_signal}")
