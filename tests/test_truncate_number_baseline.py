"""
Baseline tests for truncate_number (from Exercise 2 - HumanEval/2)
Configuration: CodeLlama-7B + CoT
These are the baseline tests that achieved 77.8% line, 50.0% branch coverage
"""

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from problems.truncate_number import truncate_number


def test_truncate_number_3_5():
    """HumanEval test case"""
    assert truncate_number(3.5) == 0.5


def test_truncate_number_1_33():
    """HumanEval test case"""
    assert abs(truncate_number(1.33) - 0.33) < 1e-6


def test_truncate_number_123_456():
    """HumanEval test case"""
    assert abs(truncate_number(123.456) - 0.456) < 1e-6
