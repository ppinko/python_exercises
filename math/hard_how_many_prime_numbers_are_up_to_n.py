"""
https://edabit.com/challenge/oTzuXDWL26gnY5a5P
"""


import math


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_numbers(n):
    return sum(1 for i in range(2, n+1) if is_prime(i))



assert prime_numbers(20) == 8
assert prime_numbers(30) == 10
assert prime_numbers(100) == 25
assert prime_numbers(200) == 46
assert prime_numbers(1000) == 168
assert prime_numbers(-5) == 0
assert prime_numbers(66) == 18
assert prime_numbers(133) == 32
assert prime_numbers(99) == 25


print('Success')