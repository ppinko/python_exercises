"""
https://edabit.com/challenge/arobBz954ZDxkDC9M
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


def next_prime(n: int) -> int:
    while True:
        if is_prime(n):
            return n
        else:
            n += 1


assert next_prime(12) == 13
assert next_prime(24) == 29
assert next_prime(11) == 11
print('Success')