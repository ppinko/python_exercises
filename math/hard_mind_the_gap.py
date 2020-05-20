"""
https://edabit.com/challenge/fPX7FGgzGLFLsorgu
"""


def isgapful(n: int) -> bool:
    n_str = str(n)
    return len(n_str) >= 3 and n % int(n_str[0] + n_str[-1]) == 0


def gapful(n: int) -> int:
    if n <= 100:
        return 100
    elif isgapful(n):
        return n
    else:
        i = 1
        while True:
            if isgapful(n - i):
                return n - i
            elif isgapful(n + i):
                return n + i
            i += 1


assert gapful(25) == 100
assert gapful(100) == 100
assert gapful(103) == 105
assert gapful(1442) == 1441
assert gapful(3345) == 3333
assert gapful(4780) == 4773
assert gapful(3078) == 3078

print("Success")