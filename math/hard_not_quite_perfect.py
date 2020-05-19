"""
https://edabit.com/challenge/fEwyy78jfqSfj5c2k
"""

def admirable(n: int):
    L = [i for i in range(1, 1 + n // 2) if n % i == 0]
    k = sum(L)
    if k == n:
        return 'Perfect'
    for i in L:
        if k - 2* i == n:
            return i
    return 'Neither'


assert admirable(6) == 'Perfect'
assert admirable(12) == 2
assert admirable(18) == 'Neither'
assert admirable(496) == 'Perfect'
assert admirable(138) == 6
assert admirable(612) == 'Neither'
assert admirable(1876) == 28
assert admirable(5456) == 496

print('Success')