"""
https://edabit.com/challenge/Cp3JRpooAqfA4kGkv
"""


def node_type(N, P, n):
    if n not in N:
        return 'Not exist'
    elif P[N.index(n)] == -1:
        return 'Root'
    elif n not in P:
        return 'Leaf'
    else:
        return 'Inner'


assert node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 1) == "Leaf"
assert node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 2) == "Inner"
assert node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 3) == "Leaf"
assert node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 5) == "Root"
assert node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 6) == "Leaf"
assert node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 8) == "Inner"
assert node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 9) == "Leaf"
assert node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 10) == "Not exist"
assert node_type([6, 3, 1, 2, 5, 7, 4, 6, 8], [3, 1, 6, 1, 2, 3, 8, -1, 6], 8) == "Inner"
assert node_type([5, 6, 8, 7, 1, 9, 4, 11, 10, 2], [8, 8, -1, 8, 7, 4, 5, 4, 1, 1], 11) == "Leaf"
assert node_type([3, 2, 4, 9, 11, 10, 8, 5, 6, 7], [-1, 3, 3, 2, 3, 4, 4, 9, 10, 8], 3 ) == "Root"
assert node_type([5, 6, 8, 7, 1, 9, 4, 11, 10, 2], [8, 8, -1, 8, 7, 4, 5, 4, 1, 1], 4) == "Inner"
assert node_type([3, 2, 4, 9, 11, 10, 8, 5, 6, 7], [-1, 3, 3, 2, 3, 4, 4, 9, 10, 8], 6) == "Leaf"
assert node_type([6, 3, 1, 2, 5, 7, 4, 6, 8], [3, 1, 6, 1, 2, 3, 8, -1, 6], 5) == "Leaf"
assert node_type([5, 6, 8, 7, 1, 9, 4, 11, 10, 2], [8, 8, -1, 8, 7, 4, 5, 4, 1, 1], 8) == "Root"
assert node_type([3, 2, 4, 9, 11, 10, 8, 5, 6, 7], [-1, 3, 3, 2, 3, 4, 4, 9, 10, 8], 10) == "Inner"

print('Success')