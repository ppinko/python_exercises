"""
https://edabit.com/challenge/9S9k2h4ZnDeyzXEgW
"""


import string


def row(row: str) -> int:
    uppers = '0' + string.ascii_uppercase
    row = row[::-1]
    tot = 0
    for i, v in enumerate(row):
        tot += uppers.index(v) * pow(26, i)
    return tot


assert row("A") == 1
assert row("B") == 2
assert row("Z") == 26
assert row("AA") == 27
assert row("BA") == 53
assert row("BB") == 54
assert row("CW") == 101
assert row("DD") == 108
assert row("PQ") == 433
assert row("ZZ") == 702
assert row("ABC") == 731
assert row("ZZT") == 18272
assert row("STVW") == 348059

print('Success')