"""Leap year checks: flow-chart implementation and conditional-expression version.

This module provides:
- `is_leap_year_flow(year)` : step-by-step flow-chart logic using if-statements.
- `is_leap_year_conditional(year)` : single boolean expression using (A and B) or C.
- Tests and a helper to run a small personal check using a birth year.
"""

def is_leap_year_flow(year):
    """Return True if `year` is a leap year following the flow-chart.

    Flow (matching image):
      1) If not divisible by 4 -> Not Leap Year
      2) If divisible by 4 and not by 100 -> Leap Year
      3) If divisible by 100 -> check divisible by 400 -> Leap Year if yes
    """
    # 1) Check divisibility by 4 first (if not, immediately not leap)
    if year % 4 != 0:
        return False

    # 2) If divisible by 4 but not by 100 -> leap year
    if year % 100 != 0:
        return True

    # 3) If divisible by 100, only leap if divisible by 400
    if year % 400 == 0:
        return True

    return False


def is_leap_year_conditional(year):
    """Return True if `year` is a leap year using a single conditional expression.

    Expression structure: (ConditionA AND ConditionB) OR ConditionC

    - ConditionA: year % 4 == 0
    - ConditionB: year % 100 != 0
    - ConditionC: year % 400 == 0

    Parentheses ensure the intended grouping and evaluation order.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def leap_year_string(year):
    """Return "Leap year" or "Not a leap year" for the given year using if-statements.
    
    Takes a year (positive integer) as a parameter and returns a string
    describing whether it is a leap year or not.
    """
    # Check divisibility by 4 first
    if year % 4 != 0:
        return "Not a leap year"
    
    # If divisible by 4 but not by 100 -> leap year
    if year % 100 != 0:
        return "Leap year"
    
    # If divisible by 100, only leap if divisible by 400
    if year % 400 == 0:
        return "Leap year"
    
    return "Not a leap year"


def test_is_leap_year(func):
    """Basic unit tests exercising all branches of the leap-year logic."""
    # Divisible by 400 -> leap year
    assert func(2000) is True
    assert func(2400) is True

    # Divisible by 100 but not 400 -> not leap
    assert func(1900) is False
    assert func(2100) is False

    # Divisible by 4 but not 100 -> leap
    assert func(1996) is True
    assert func(2004) is True

    # Not divisible by 4 -> not leap
    assert func(2001) is False
    assert func(2019) is False


def test_leap_year_string(func):
    """Test the string-returning leap year function."""
    # Divisible by 400 -> "Leap year"
    assert func(2000) == "Leap year"
    assert func(2400) == "Leap year"

    # Divisible by 100 but not 400 -> "Not a leap year"
    assert func(1900) == "Not a leap year"
    assert func(2100) == "Not a leap year"

    # Divisible by 4 but not 100 -> "Leap year"
    assert func(1996) == "Leap year"
    assert func(2004) == "Leap year"

    # Not divisible by 4 -> "Not a leap year"
    assert func(2001) == "Not a leap year"
    assert func(2019) == "Not a leap year"


def find_closest_leap(year, max_search=50):
    """Find the closest leap year to `year` (search outward).

    Returns the first leap year found at the smallest distance. If the year
    itself is leap this will return the year itself.
    """
    if is_leap_year_conditional(year):
        return year

    for d in range(1, max_search + 1):
        before = year - d
        after = year + d
        if is_leap_year_conditional(before):
            return before
        if is_leap_year_conditional(after):
            return after
    raise ValueError("No leap year found within search range")


def run_personal_tests(birth_year):
    """Run checks for `birth_year` and the closest leap year.

    If `birth_year` is itself a leap year, per instructions we will also
    test `birth_year + 1` as a non-leap sample.
    """
    print(f"Running personal tests for birth year: {birth_year}")

    # Determine sample years according to instructions
    if is_leap_year_conditional(birth_year):
        leap_sample = birth_year
        non_leap_sample = birth_year + 1
    else:
        leap_sample = find_closest_leap(birth_year)
        non_leap_sample = birth_year

    # Verify both implementations agree on these samples
    for year in (leap_sample, non_leap_sample):
        flow = is_leap_year_flow(year)
        cond = is_leap_year_conditional(year)
        print(f"Year {year}: flow={flow}, conditional={cond}")
        assert flow == cond, f"Mismatch for year {year}: flow={flow}, cond={cond}"

    print("Personal tests passed: both implementations agree on samples.")


if __name__ == "__main__":
    # Run unit tests for both boolean-returning functions
    test_is_leap_year(is_leap_year_flow)
    test_is_leap_year(is_leap_year_conditional)
    
    # Run unit tests for the string-returning function
    test_leap_year_string(leap_year_string)
    print("All unit tests passed!")

    # Example personal test: change this to your birth year when running locally
    example_birth_year = 2002
    run_personal_tests(example_birth_year)
