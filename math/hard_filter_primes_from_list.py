"""
https://edabit.com/challenge/yXZhG7zq6dWhWhirt
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


def filter_primes(num):
    return [i for i in num if is_prime(i)]


assert filter_primes([7, 9, 3, 9, 10, 11, 27]) == [7, 3, 11]
assert filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == [2,
                                                                                                                      3,
                                                                                                                      5,
                                                                                                                      7,
                                                                                                                      11,
                                                                                                                      13,
                                                                                                                      17,
                                                                                                                      19,
                                                                                                                      23]
assert filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]) == [1009, 3, 61, 1087,
                                                                                                 1091, 1093, 1097]
assert filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) == [10007, 1009]

print("Success")
