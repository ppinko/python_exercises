"""
https://edabit.com/challenge/7DjphCrJvFiKRcpdm
"""


def covered_integers(lst: list) -> int:
    return len({j for i in lst for j in range(i[0], i[1] + 1)})


assert covered_integers([[80, 81], [1, 2], [9, 11]]) == 7
assert covered_integers([[3, 6], [4, 6], [5, 6]]) == 4
assert covered_integers([[1, 2], [1, 2]]) == 2
assert covered_integers([[1, 11]]) == 11
assert covered_integers([[8, 9], [102, 104]]) == 5
assert covered_integers([[1, 1], [5, 5], [8, 8]]) == 3
assert covered_integers([[0, 5], [5, 5], [8, 8]]) == 7
assert covered_integers([[1, 5], [3, 5], [4, 6], [5, 7]]) == 7
assert covered_integers([[-3, 10], [-2, 9], [-1, 8], [0, 7], [1, 6], [2, 5], [3, 4]]) == 14

print('Success')