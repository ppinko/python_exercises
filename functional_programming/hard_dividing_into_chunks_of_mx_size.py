"""
https://edabit.com/challenge/9CWPv99o4EjZgHnkq
"""
from typing import List, Any


def divide(lst: list, n: int) -> list:
    arr, temp, val = [], [], 0
    
    for v in lst:
        if val + v <= n:
            val += v
            temp.append(v)
        else:
            arr.append(temp[:])
            temp.clear()
            temp.append(v)
            val = v
    arr.append(temp[:])
    return arr


assert divide([1, 2, 3, 4, 1, 0, 2, 2], 5) == [[1, 2], [3], [4, 1, 0], [2, 2]]
assert divide([1, 2, 3, 4, 1, 0, 2, 2], 4) == [[1, 2], [3], [4], [1, 0, 2], [2]]
assert divide([1, 3, 2, -1, 2, 1, 1, 3, 1], 3) == [[1], [3], [2, -1, 2], [1, 1], [3], [1]]
assert divide([1, 2, 2, -1, 2, 0, 1, 0, 1], 2) == [[1], [2], [2, -1], [2, 0], [1, 0, 1]]
assert divide([1, 2, 2, -1, 2, 0, 1, 0, 1], 3) == [[1, 2], [2, -1, 2, 0], [1, 0, 1]]
assert divide([1, 2, 2, -1, 2, 0, 1, 0, 1], 5) == [[1, 2, 2, -1], [2, 0, 1, 0, 1]]
assert divide([2, 1, 0, -1, 0, 0, 2, 1, 3], 3) == [[2, 1, 0, -1, 0, 0], [2, 1], [3]]
assert divide([2, 1, 0, -1, 0, 0, 2, 1, 3], 4) == [[2, 1, 0, -1, 0, 0, 2], [1, 3]]
assert divide([1, 0, 1, 1, -1, 0, 0], 1) == [[1, 0], [1], [1, -1, 0, 0]]
assert divide([1, 0, 1, 1, -1, 0, 0], 2) == [[1, 0, 1], [1, -1, 0, 0]]
assert divide([1, 0, 1, 1, -1, 0, 0], 3) == [[1, 0, 1, 1, -1, 0, 0]]

print('Success')