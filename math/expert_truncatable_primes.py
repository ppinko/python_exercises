"""
https://edabit.com/challenge/BfSj2nBc33aCQrbSg
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


def truncatable(n: int):
    n_str = str(n)
    if '0' in n_str:
        return False
    if len(n_str) == 1 and is_prime(n):
        return 'both'
    if not is_prime(n):
        return False
    lefty, righty = True, True
    left, right = n, n
    while left > 10:
        left %= pow(10, len(str(left)) - 1)
        if not is_prime(left):
            lefty = False
            break

    while right > 10:
        right = right // 10
        if not is_prime(right):
            righty = False
            break

    if lefty and righty:
        return 'both'
    elif lefty:
        return 'left'
    elif righty:
        return 'right'
    else:
        return False


assert truncatable(47) == "left"
assert truncatable(347) == "left"
assert truncatable(62383) == "left"
assert truncatable(79) == "right"
assert truncatable(7331) == "right"
assert truncatable(233993) == "right"
assert truncatable(3797) == "both"
assert truncatable(739397) == "both"
assert truncatable(5) == "both"
assert truncatable(349) == False
assert truncatable(2317) == False
assert truncatable(131) == False
assert truncatable(6043) == False

print('Success')