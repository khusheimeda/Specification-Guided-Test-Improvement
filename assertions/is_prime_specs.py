"""
Corrected Formal Specifications for is_prime
Generated in Exercise 3 Part 1

Accuracy Rate: 2/5 = 40%
"""

# CORRECTED SPECIFICATIONS (to be used for test generation)

# Specification 1: Numbers <= 1 are not prime
# assert not (n <= 1 and result == True)
# Explanation: If n is less than or equal to 1, the result cannot be True

# Specification 2: The number 2 is prime  
# assert not (n == 2 and result == False)
# Explanation: If n equals 2, the result cannot be False (2 is prime)

# Specification 3: Even numbers greater than 2 are not prime
# assert not (n > 2 and n % 2 == 0 and result == True)
# Explanation: If n is greater than 2 and even, the result cannot be True

# Specification 4: The number 3 is prime
# assert not (n == 3 and result == False)
# Explanation: If n equals 3, the result cannot be False (3 is prime)


# INCORRECT SPECIFICATIONS (from LLM generation - DO NOT USE)

# Original Spec 1: assert is_prime(n) == result
# Issue: Self-reference - calls is_prime() directly

# Original Spec 2: assert (n <= 1 and result == False) or (n > 1 and result == True) or (n > 1 and result == False)
# Issue: Tautology/Incomplete - simplifies to (n <= 1 and result == False) or (n > 1), 
#        only constrains n <= 1 case

# Original Spec 3: assert result == any(n % i != 0 for i in range(2, int(n**0.5) + 1))
# Issue: Re-implements the function - checks all divisors from 2 to √n instead of stating properties
