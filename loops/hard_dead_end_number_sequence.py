"""
https://edabit.com/challenge/izhpciCCMsMgKrsKN
"""


def dead_end(n: int) -> tuple:
    s, k = set(), 1
    s.add(n)
    while True:
        sum_digits = sum(int(i) for i in str(n))
        temp = n
        if n % sum_digits == 0:
            n = n // sum_digits
        else:
            n *= sum_digits
        if n in s:
            return (k, temp)
        else:
            k += 1
            s.add(n)


assert dead_end(1), (1, 1)
assert dead_end(9), (2, 1)
assert dead_end(1000), (1, 1000)
assert dead_end(999), (3, 370)
assert dead_end(38), (12, 174813842944)
assert dead_end(93), (9, 217)
assert dead_end(11615819), (74, 1354959139828966431926720346323206635520)
assert dead_end(100000001), (15, 220258825732)

print('Success')