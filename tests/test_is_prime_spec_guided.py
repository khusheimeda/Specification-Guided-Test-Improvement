"""
SPEC-GUIDED TESTS for is_prime
Generated in Exercise 3 Part 2 using corrected formal specifications

These tests are based on the 4 corrected specifications from Part 1:
1. Numbers <= 1 are not prime
2. The number 2 is prime
3. Even numbers greater than 2 are not prime
4. The number 3 is prime
"""

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from problems.is_prime import is_prime


# ============================================================================
# SPEC-GUIDED TEST: Specification 1
# Numbers <= 1 are not prime
# Formal spec: assert not (n <= 1 and result == True)
# ============================================================================

def test_spec1_numbers_less_than_or_equal_to_1_not_prime():
    """
    SPEC-GUIDED TEST
    Spec 1: Numbers <= 1 are not prime
    Tests boundary cases and negative numbers
    """
    # Test n = 0 (boundary)
    assert is_prime(0) == False, "0 should not be prime"
    
    # Test n = 1 (boundary)
    assert is_prime(1) == False, "1 should not be prime"
    
    # Test negative numbers
    assert is_prime(-1) == False, "-1 should not be prime"
    assert is_prime(-5) == False, "-5 should not be prime"
    assert is_prime(-10) == False, "-10 should not be prime"


# ============================================================================
# SPEC-GUIDED TEST: Specification 2
# The number 2 is prime
# Formal spec: assert not (n == 2 and result == False)
# ============================================================================

def test_spec2_two_is_prime():
    """
    SPEC-GUIDED TEST
    Spec 2: The number 2 is prime
    Tests the smallest prime number
    """
    assert is_prime(2) == True, "2 should be prime"


# ============================================================================
# SPEC-GUIDED TEST: Specification 3
# Even numbers greater than 2 are not prime
# Formal spec: assert not (n > 2 and n % 2 == 0 and result == True)
# ============================================================================

def test_spec3_even_numbers_greater_than_2_not_prime():
    """
    SPEC-GUIDED TEST
    Spec 3: Even numbers greater than 2 are not prime
    Tests various even composite numbers
    """
    # Small even numbers
    assert is_prime(4) == False, "4 should not be prime"
    assert is_prime(6) == False, "6 should not be prime"
    assert is_prime(8) == False, "8 should not be prime"
    assert is_prime(10) == False, "10 should not be prime"
    
    # Larger even numbers
    assert is_prime(100) == False, "100 should not be prime"
    assert is_prime(200) == False, "200 should not be prime"
    assert is_prime(1000) == False, "1000 should not be prime"


# ============================================================================
# SPEC-GUIDED TEST: Specification 4
# The number 3 is prime
# Formal spec: assert not (n == 3 and result == False)
# ============================================================================

def test_spec4_three_is_prime():
    """
    SPEC-GUIDED TEST
    Spec 4: The number 3 is prime
    Tests the smallest odd prime
    """
    assert is_prime(3) == True, "3 should be prime"


# ============================================================================
# ADDITIONAL SPEC-GUIDED TESTS
# These tests explore combinations and edge cases of the specifications
# ============================================================================

def test_spec_combined_small_numbers():
    """
    SPEC-GUIDED TEST (Combined)
    Tests small numbers using multiple specifications
    """
    # Spec 1: n <= 1
    assert is_prime(0) == False
    assert is_prime(1) == False
    
    # Spec 2: n = 2
    assert is_prime(2) == True
    
    # Spec 4: n = 3
    assert is_prime(3) == True
    
    # Spec 3: even n > 2
    assert is_prime(4) == False
    assert is_prime(6) == False


def test_spec_boundary_values():
    """
    SPEC-GUIDED TEST (Boundaries)
    Tests boundary values between specifications
    """
    # Boundary between Spec 1 (n <= 1) and Spec 2 (n == 2)
    assert is_prime(1) == False  # Last value of Spec 1
    assert is_prime(2) == True   # Value of Spec 2
    
    # Boundary between Spec 4 (n == 3) and Spec 3 (even n > 2)
    assert is_prime(3) == True   # Value of Spec 4
    assert is_prime(4) == False  # First even number > 2
