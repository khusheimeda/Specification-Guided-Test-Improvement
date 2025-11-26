"""
SPEC-GUIDED TESTS for truncate_number
Generated in Exercise 3 Part 2 using corrected formal specifications

These tests are based on the 5 corrected specifications from Part 1:
1. Decimal part equals number minus integer part
2. Result must be non-negative (lower bound)
3. Result must be less than 1 (upper bound)
4. Alternative formulation using modulo
5. For integer-valued floats, result behavior
"""

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from problems.truncate_number import truncate_number


# ============================================================================
# SPEC-GUIDED TEST: Specification 1
# Decimal part equals number minus integer part
# Formal spec: assert result == number - int(number)
# ============================================================================

def test_spec1_decimal_part_formula():
    """
    SPEC-GUIDED TEST
    Spec 1: Decimal part equals number minus integer part
    Tests the fundamental formula
    """
    # Basic cases
    result1 = truncate_number(3.5)
    assert abs(result1 - (3.5 - int(3.5))) < 1e-9, "3.5: result should equal number - int(number)"
    
    result2 = truncate_number(1.33)
    assert abs(result2 - (1.33 - int(1.33))) < 1e-9, "1.33: result should equal number - int(number)"
    
    result3 = truncate_number(100.999)
    assert abs(result3 - (100.999 - int(100.999))) < 1e-9, "100.999: result should equal number - int(number)"
    
    # Large number
    result4 = truncate_number(1234.56789)
    assert abs(result4 - (1234.56789 - int(1234.56789))) < 1e-9, "Large number test"
    
    # Small decimal
    result5 = truncate_number(0.123)
    assert abs(result5 - (0.123 - int(0.123))) < 1e-9, "Small number test"


# ============================================================================
# SPEC-GUIDED TEST: Specification 2
# Result must be non-negative (lower bound)
# Formal spec: assert result >= 0
# ============================================================================

def test_spec2_result_non_negative():
    """
    SPEC-GUIDED TEST
    Spec 2: Result must be non-negative
    Tests that all results are >= 0
    """
    # Various test cases
    assert truncate_number(5.7) >= 0, "5.7: result must be >= 0"
    assert truncate_number(0.1) >= 0, "0.1: result must be >= 0"
    assert truncate_number(1000.001) >= 0, "1000.001: result must be >= 0"
    assert truncate_number(3.14159) >= 0, "3.14159: result must be >= 0"
    
    # Integer-valued (should be 0)
    assert truncate_number(5.0) >= 0, "5.0: result must be >= 0"
    assert truncate_number(10.0) >= 0, "10.0: result must be >= 0"


# ============================================================================
# SPEC-GUIDED TEST: Specification 3
# Result must be less than 1 (upper bound)
# Formal spec: assert result < 1.0
# ============================================================================

def test_spec3_result_less_than_one():
    """
    SPEC-GUIDED TEST
    Spec 3: Result must be less than 1
    Tests that all results are < 1
    """
    # Various test cases
    assert truncate_number(3.5) < 1.0, "3.5: result must be < 1"
    assert truncate_number(7.999) < 1.0, "7.999: result must be < 1"
    assert truncate_number(0.1) < 1.0, "0.1: result must be < 1"
    assert truncate_number(100.9999) < 1.0, "100.9999: result must be < 1"
    
    # Integer-valued (should be 0, which is < 1)
    assert truncate_number(5.0) < 1.0, "5.0: result must be < 1"


# ============================================================================
# SPEC-GUIDED TEST: Specification 4
# Alternative formulation using modulo
# Formal spec: assert result == number % 1.0
# ============================================================================

def test_spec4_modulo_formulation():
    """
    SPEC-GUIDED TEST
    Spec 4: Alternative formulation using modulo
    Tests that result equals number % 1.0
    """
    # Test various numbers
    result1 = truncate_number(4.25)
    assert abs(result1 - (4.25 % 1.0)) < 1e-9, "4.25: result should equal number % 1.0"
    
    result2 = truncate_number(10.75)
    assert abs(result2 - (10.75 % 1.0)) < 1e-9, "10.75: result should equal number % 1.0"
    
    result3 = truncate_number(123.456)
    assert abs(result3 - (123.456 % 1.0)) < 1e-9, "123.456: result should equal number % 1.0"
    
    result4 = truncate_number(0.999)
    assert abs(result4 - (0.999 % 1.0)) < 1e-9, "0.999: result should equal number % 1.0"


# ============================================================================
# SPEC-GUIDED TEST: Specification 5
# For integer-valued floats, result behavior
# Formal spec: assert (number == int(number)) or (result > 0) or (result == 0)
# ============================================================================

def test_spec5_integer_valued_floats_behavior():
    """
    SPEC-GUIDED TEST
    Spec 5: Integer-valued floats or result is non-negative
    Tests the disjunction property
    """
    # Integer-valued floats (first condition true)
    result1 = truncate_number(5.0)
    number1 = 5.0
    assert (number1 == int(number1)) or (result1 > 0) or (result1 == 0), \
        "5.0: should satisfy the spec"
    
    result2 = truncate_number(10.0)
    number2 = 10.0
    assert (number2 == int(number2)) or (result2 > 0) or (result2 == 0), \
        "10.0: should satisfy the spec"
    
    # Non-integer floats with positive result (second condition true)
    result3 = truncate_number(3.5)
    number3 = 3.5
    assert (number3 == int(number3)) or (result3 > 0) or (result3 == 0), \
        "3.5: should satisfy the spec"
    
    result4 = truncate_number(7.25)
    number4 = 7.25
    assert (number4 == int(number4)) or (result4 > 0) or (result4 == 0), \
        "7.25: should satisfy the spec"


# ============================================================================
# ADDITIONAL SPEC-GUIDED TESTS
# These tests explore combinations and edge cases
# ============================================================================

def test_spec_combined_bounds():
    """
    SPEC-GUIDED TEST (Combined)
    Tests that results satisfy both bound specifications (Spec 2 and 3)
    """
    test_values = [0.5, 1.5, 10.999, 50.1, 100.5]
    
    for val in test_values:
        result = truncate_number(val)
        # Should satisfy both Spec 2 (>= 0) and Spec 3 (< 1)
        assert 0 <= result < 1, f"{val}: result should be in range [0, 1)"


def test_spec_edge_cases():
    """
    SPEC-GUIDED TEST (Edge Cases)
    Tests edge cases based on specifications
    """
    # Very small decimal (close to 0)
    result1 = truncate_number(5.0001)
    assert result1 >= 0 and result1 < 1  # Specs 2 and 3
    
    # Very large integer part with small decimal
    result2 = truncate_number(99999.0001)
    assert result2 >= 0 and result2 < 1  # Specs 2 and 3
    
    # Number very close to next integer
    result3 = truncate_number(4.9999)
    assert result3 >= 0 and result3 < 1  # Specs 2 and 3


def test_spec_integer_valued_explicitly():
    """
    SPEC-GUIDED TEST (Integer-valued)
    Explicitly tests integer-valued floats (Spec 5)
    """
    # Integer-valued floats should return 0.0
    assert truncate_number(1.0) == 0.0, "1.0 should return 0.0"
    assert truncate_number(5.0) == 0.0, "5.0 should return 0.0"
    assert truncate_number(10.0) == 0.0, "10.0 should return 0.0"
    assert truncate_number(100.0) == 0.0, "100.0 should return 0.0"
