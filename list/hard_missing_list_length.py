"""
https://edabit.com/challenge/r9y4yrSAGRaqTT7nM
"""


def find_missing(lst):
    if lst is None or lst == []:
        return False
    elif any(True for i in lst if len(i) == 0):
        return False
    l = sorted([len(i) for i in lst])
    for i, v in enumerate(l):
        if l[i+1] - v != 1:
            return v + 1


assert find_missing([[1], [1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]) == 3
assert find_missing([[5, 6, 7, 8, 9], [1, 2], [4, 5, 1, 1], [1] ]) == 3
assert find_missing([[4, 4, 4, 4], [1], [3, 3, 3]]) == 2
assert find_missing([[False], [False, False, False]]) == 2
assert find_missing([["f", "r", "s"], ["d", "e"], ["a", "f", "b", "n"], ["z"], ["fg", "gty", "d", "dfr", "dr", "q"]]) == 5
assert find_missing([[5, 2, 9], [4, 5, 1, 1, 5, 6], [1, 1], [5, 6, 7, 8, 9]]) == 4
assert find_missing([]) == False
assert find_missing(None) == False
assert find_missing([[], [1, 2, 2]]) == False

print('Success')