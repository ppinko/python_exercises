"""
https://edabit.com/challenge/KFKziCxeTiCLfzMao
"""


from collections import Counter


# def string_factor(lst: list) -> str:
#     c = Counter(lst)
#     return ' x '.join('{0}^{1}'.format(k, v) if v != 1 else str(k) for k, v in c.items())


def string_factor(lst: list) -> str:
    c = Counter(lst)
    return ' x '.join('{0}^{1}'.format(k, c[k]) if c[k] != 1 else str(k) for k in sorted(c.keys()))


assert string_factor([2, 2, 2, 3, 3]) == "2^3 x 3^2"
assert string_factor([2, 7]) == "2 x 7"
assert string_factor([2, 3, 3]) == "2 x 3^2"
assert string_factor([2, 2, 2, 2, 2]) == "2^5"
assert string_factor([2, 3, 7]) == "2 x 3 x 7"
assert string_factor([2, 2, 7, 11]) == "2^2 x 7 x 11"
assert string_factor([11, 11, 11]) == "11^3"

print('Success')