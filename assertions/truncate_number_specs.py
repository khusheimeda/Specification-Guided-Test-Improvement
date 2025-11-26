"""
Corrected Formal Specifications for truncate_number
Generated in Exercise 3 Part 1

Accuracy Rate: 3/5 = 60%
"""

# CORRECTED SPECIFICATIONS (to be used for test generation)

# Specification 1: Decimal part equals number minus integer part
# assert result == number - int(number)
# Explanation: The result should equal the input minus its integer part

# Specification 2: Result must be non-negative (lower bound)
# assert result >= 0
# Explanation: Since input is positive, the decimal part must be >= 0

# Specification 3: Result must be less than 1 (upper bound)
# assert result < 1.0
# Explanation: The decimal part is always strictly less than 1

# Specification 4: Alternative formulation using modulo
# assert result == number % 1.0
# Explanation: Modulo 1 gives the fractional part (equivalent to Spec 1)

# Specification 5: For integer-valued floats, result behavior
# assert (number == int(number)) or (result > 0) or (result == 0)
# Explanation: Either number is integer-valued, or result is non-negative


# INCORRECT SPECIFICATIONS (from LLM generation - DO NOT USE)

# Original Spec 2: assert result == abs(number) % 1
# Issue: Out of scope - handles negative numbers using abs(), but problem states
#        "positive floating point number" only

# Original Spec 5: assert int(number) + result == number
# Issue: Floating point precision - direct equality will fail due to FP arithmetic
#        Should use: assert abs((int(number) + result) - number) < 1e-9
