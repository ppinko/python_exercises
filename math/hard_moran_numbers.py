"""
https://edabit.com/challenge/YTf8DZbTkzJ3kizNa
"""


def moran(n: int) -> str:
    n_sum = sum(int(i) for i in str(n))
    if n % n_sum != 0:
        return 'Neither'
    k = n // n_sum
    for i in range(2, k // 2):
        if k % i == 0:
            return 'H'
    return 'M'


assert moran(132) == "H"
assert moran(133) == "M"
assert moran(134) == "Neither"
assert moran(3033) == "M"
assert moran(3030) == "H"
assert moran(491423) == "Neither"
assert moran(20937) == "M"
print('Success')