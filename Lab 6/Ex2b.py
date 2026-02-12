def determine_progress1(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins

    if hits_spins_ratio > 0:
        progress = "On your way!"
        if hits_spins_ratio >= 0.25:
            progress = "Almost there!"
            if hits_spins_ratio >= 0.5:
                if hits < spins:
                    progress = "You win!"
    else:
        progress = "Get going!"

    return progress

def determine_progress2(hits, spins):
    if spins == 0:
        return "Get going!"

    hits_spins_ratio = hits / spins

    if hits_spins_ratio == 0:
        return "Get going!"

    progress = "On your way!"
    if hits_spins_ratio >= 0.25:
        progress = "Almost there!"
    if hits_spins_ratio >= 0.5 and hits < spins:
        progress = "You win!"

    return progress

# All possible return values and short explanations
POSSIBLE_RETURNS = {
    "Get going!": "Returned when spins == 0 (no activity) or when hits/spins == 0 (no hits).",
    "On your way!": "Returned when 0 < hits/spins < 0.25 (some progress but under 25%).",
    "Almost there!": "Returned when 0.25 <= hits/spins < 0.5, or when hits == spins.",
    "You win!": "Returned when hits/spins >= 0.5 and hits < spins (>=50% success but not all spins).",
}

def list_possible_returns():
    """Return the list of possible progress strings (for docs/tests)."""
    return list(POSSIBLE_RETURNS.keys())

def test_determine_progress(progress_function):
    """
    Test function that checks all possible return values of a determine_progress function.
    Uses assert statements to validate each return case.
    """
    # Test case 1: spins = 0 returns "Get going!"
    assert progress_function(10, 0) == "Get going!", "Test case 1 failed: spins = 0"
    
    # Test case 2: hits = 0 (ratio = 0, no hits) returns "Get going!"
    assert progress_function(0, 10) == "Get going!", "Test case 2 failed: no hits"
    
    # Test case 3: ratio > 0 but < 0.25 (e.g., 1/10 = 0.1) returns "On your way!"
    assert progress_function(1, 10) == "On your way!", "Test case 3 failed: ratio 0-0.25"
    
    # Test case 4: ratio >= 0.25 but < 0.5 (e.g., 3/10 = 0.3) returns "Almost there!"
    assert progress_function(3, 10) == "Almost there!", "Test case 4 failed: ratio 0.25-0.5"
    
    # Test case 5: ratio >= 0.5 and hits < spins (e.g., 5/10 = 0.5) returns "You win!"
    assert progress_function(5, 10) == "You win!", "Test case 5 failed: ratio >= 0.5, hits < spins"
    
    # Test case 6: ratio = 1.0 (hits = spins) - edge case
    # Based on the condition "hits < spins", this should NOT return "You win!"
    assert progress_function(10, 10) == "Almost there!", "Test case 6 failed: hits = spins (ratio 1.0)"
        
    print("All tests passed!")

if __name__ == "__main__":
    test_determine_progress(determine_progress1)
    test_determine_progress(determine_progress2)