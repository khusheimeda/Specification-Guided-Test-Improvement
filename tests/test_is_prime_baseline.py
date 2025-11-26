"""
Baseline tests for is_prime (from Exercise 2 - HumanEval/31)
Configuration: DeepSeek-6.7B + CoT
These are the baseline tests that achieved 71.4% line, 66.7% branch coverage
"""

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from problems.is_prime import is_prime


def test_is_prime_6():
    """HumanEval test case"""
    assert is_prime(6) == False


def test_is_prime_101():
    """HumanEval test case"""
    assert is_prime(101) == True


def test_is_prime_11():
    """HumanEval test case"""
    assert is_prime(11) == True


def test_is_prime_13441():
    """HumanEval test case"""
    assert is_prime(13441) == True


def test_is_prime_61():
    """HumanEval test case"""
    assert is_prime(61) == True


def test_is_prime_4():
    """HumanEval test case"""
    assert is_prime(4) == False


def test_is_prime_1():
    """HumanEval test case"""
    assert is_prime(1) == False


def test_is_prime_5():
    """HumanEval test case"""
    assert is_prime(5) == True


def test_is_prime_17():
    """HumanEval test case"""
    assert is_prime(17) == True


def test_is_prime_5_times_17():
    """HumanEval test case - composite"""
    assert is_prime(5 * 17) == False


def test_is_prime_11_times_7():
    """HumanEval test case - composite"""
    assert is_prime(11 * 7) == False


def test_is_prime_13441_times_19():
    """HumanEval test case - composite"""
    assert is_prime(13441 * 19) == False
