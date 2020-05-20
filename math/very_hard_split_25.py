"""
https://edabit.com/challenge/XjgoXNmnz59txiQp3
"""


def split(n: int) -> int:
    d_instant = {1:1, 2:1, 3:2, 4:4}
    if n in d_instant:
        return d_instant[n]
    d_sub = {2:2, 3:3, 4:4}
    total = 1
    while n not in d_sub:
        total *= 3
        n -= 3
    return total * d_sub[n]


assert split(25) == 8748
assert split(1) == 1
assert split(10) == 36
assert split(5) == 6
assert split(15) == 243
assert split(20) == 1458

print('Success')