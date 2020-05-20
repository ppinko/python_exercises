"""
https://edabit.com/challenge/sMApDJSFkvXqF4u83
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


def interprime(num: int) -> list:
    p1, p2 = num - 1, num + 1
    while p1 > 0:
        if is_prime(p1):
            break
        p1 -= 1
    while True:
        if is_prime(p2):
            break
        p2 += 1
    if num - p1 == p2 - num:
        return [p1, p2]
    return []


assert interprime(6) == [5, 7]
assert interprime(9) == [7, 11]
assert interprime(473) == [467, 479]
print('Success')