"""
https://edabit.com/challenge/FDzEFbNE2q3eKL8dm
"""

import string

# First, naive recursive solution

# def abacaba_pattern(n: int) -> str:
#     if n == 1:
#         return string.ascii_uppercase[n-1]
#     return abacaba_pattern(n-1) + string.ascii_uppercase[n-1] + abacaba_pattern(n-1)

# dynamic programming solution


def abacaba_pattern(n: int) -> str:
    d = {1: 'A'}
    if n == 1:
        return d[1]
    k = 2
    while k <= n:
        d[k] = d[k-1] + string.ascii_uppercase[k-1] + d[k-1]
        k += 1
    return d[n]


assert abacaba_pattern(1) == "A"
assert abacaba_pattern(2) == "ABA"
assert abacaba_pattern(3) == "ABACABA"
print('Success')