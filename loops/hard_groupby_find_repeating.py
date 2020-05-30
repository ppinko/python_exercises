"""
https://edabit.com/challenge/b9sTvowiouGsiaZE3
"""


import itertools


def find_repeating(txt: str) -> list:
    L, start = [], 0
    if len(txt) == 0:
        return L
    for i, group in itertools.groupby(txt):
        temp = []
        temp.append(i)
        temp.append(start)
        a = len(list(group))
        end = start + a - 1
        temp.append(end)
        temp.append(a)
        start = end + 1
        L.append(temp)
    return L


assert find_repeating('') == []
assert find_repeating('a') == [['a', 0, 0, 1]]
assert find_repeating('1337') == [['1', 0, 0, 1], ['3', 1, 2, 2], ['7', 3, 3, 1]]
assert find_repeating('aabbb') == [['a', 0, 1, 2], ['b', 2, 4, 3]]
assert find_repeating('addressee') == [['a', 0, 0, 1], ['d', 1, 2, 2], ['r', 3, 3, 1], ['e', 4, 4, 1], ['s', 5, 6, 2], ['e', 7, 8, 2]]
assert find_repeating('aabbbaabbb') == [['a', 0, 1, 2], ['b', 2, 4, 3], ['a', 5, 6, 2], ['b', 7, 9, 3]]
assert find_repeating('1111222233334444') == [['1', 0, 3, 4], ['2', 4, 7, 4], ['3', 8, 11, 4], ['4', 12, 15, 4]]
assert find_repeating('1000000000000066600000000000001') == [['1', 0, 0, 1], ['0', 1, 13, 13], ['6', 14, 16, 3], ['0', 17, 29, 13], ['1', 30, 30, 1]]

print('Success')