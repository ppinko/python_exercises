"""
https://edabit.com/challenge/kEww9Hjds5Zkgjyfj
"""


def replace_next_largest(lst: list) -> list:
    L = sorted(lst)
    return [- 1 if i == max(lst) else L[L.index(i) + 1] for i in lst]


""" Alternative solution """
def replace_next_largest(lst):
    s = sorted(lst) + [-1]
    return [s[s.index(i)+1] for i in lst]


assert replace_next_largest([5, 7, 3, 2, 8]) == [7, 8, 5, 3, -1]
assert replace_next_largest([4, 1, 6, -7, -8, 2]) == [6, 2, -1, 1, -7, 4]
assert replace_next_largest([2, 3, 4, 5]) == [3, 4, 5, -1]
assert replace_next_largest([1, 0, -1, 8, -72]) == [8, 1, 0, -1, -1]

print('Success')