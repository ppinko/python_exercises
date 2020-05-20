"""
https://edabit.com/challenge/7kZhB4FpJfYHnQYBq
"""


def gcd(n, m):
    n_min, n_max = min(n, m), max(n, m)
    k = n_max % n_min
    if n_min == 1:
        return 1
    elif k == 0:
        return n_min
    else:
        return gcd(n_min, k)


def lcm(a, b):
    return a * b / gcd(a, b)


def lcm_three(lst: list) -> int:
    a, b, c = lst
    temp = lcm(a, b)
    return lcm(temp, c)


assert lcm_three([5, 7, 13]) == 455
assert lcm_three([104, 105, 107]) == 1168440
assert lcm_three([19, 47, 43]) == 38399
assert lcm_three([3, 4, 12]) == 12
assert lcm_three([6, 16, 348]) == 1392
assert lcm_three([97, 103, 301]) == 3007291
assert lcm_three([97, 997, 301]) == 29109409

print('Success')