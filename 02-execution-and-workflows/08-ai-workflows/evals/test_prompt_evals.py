import pytest

BANNED_FLUFF_WORDS = ["game-changer", "synergy", "cutting-edge", "revolutionary", "delve", "seamlessly"]

def evaluate_brief_quality(brief_text: str) -> dict:
    """Validates LLM-generated account brief outputs against enterprise standards."""
    errors = []
    
    # Check 1: Length check
    if len(brief_text.strip()) < 50:
        errors.append("Brief is too short (< 50 chars).")
    elif len(brief_text.strip()) > 1000:
        errors.append("Brief exceeds maximum length (> 1000 chars).")
        
    # Check 2: Banned generic AI fluff
    found_fluff = [word for word in BANNED_FLUFF_WORDS if word.lower() in brief_text.lower()]
    if found_fluff:
        errors.append(f"Brief contains generic AI buzzwords: {', '.join(found_fluff)}")
        
    return {
        "passed": len(errors) == 0,
        "errors": errors
    }

def test_valid_brief():
    good_brief = "Company expanded EMEA sales team by 30% in Q2. Active hiring for RevOps Lead indicates tooling friction."
    result = evaluate_brief_quality(good_brief)
    assert result["passed"] is True

def test_fluff_brief():
    fluff_brief = "Our cutting-edge platform offers a game-changer solution for your revenue team."
    result = evaluate_brief_quality(fluff_brief)
    assert result["passed"] is False
    assert "cutting-edge" in result["errors"][0]
