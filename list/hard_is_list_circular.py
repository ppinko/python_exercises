"""
https://edabit.com/challenge/cBMTHwEzq7bJJj3dE
"""


from itertools import permutations


def check_circular(lst: list) -> bool:
    for i in range(len(lst)):
        if i == 0:
            if lst[i][0] != lst[-1][-1]:
                return False
        elif lst[i][0] != lst[i-1][-1]:
            return False
    return True


def is_circular(lst: list) -> bool:
    perm = permutations(lst)
    return any(check_circular(i) for i in perm)


""" Alternative solution """

def is_circular(lst):
  return sorted(i[0] for i in lst)==sorted(i[-1] for i in lst)


assert is_circular([[9, 8], [6, 9, 1], [8, 4, 2], [1, 9], [2, 1, 6]]) == True
assert is_circular([[1, 2, 7], [7, 9, 3], [3], [3, 4], [4, 2, 1]]) == True
assert is_circular([[1, 2], [2, 3], [3, 4], [4, 5]]) == False
assert is_circular([[9, 9], [9, 2], [2, 9], [9, 5], [5, 9], [9, 6], [6, 9]]) == True
assert is_circular([[1, 2], [4, 1], [3, 4], [2, 3]]) == True
assert is_circular([[1, 1], [1, 2]]) == False
assert is_circular([[6, 7, 8, 9], [1, 2, 3, 4, 5, 6], [6, 6, 9], [9, 0, 1]]) == False
assert is_circular([[2, 1], [1, 2]]) == True
assert is_circular([[2, 1], [1, 2], [2, 1], [1, 3, 1], [1, 4, 4]]) == False

print('Success')