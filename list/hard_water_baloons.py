"""
https://edabit.com/challenge/3y2FmfjhbiQPPYbcn
"""


def pop(lst):
    temp = [i for i in range(max(lst)+1)]
    return temp + list(reversed(temp[:len(temp)-1]))


assert pop([0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0]) == [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
assert pop([0, 0, 0, 0, 4, 0, 0, 0, 0]) == [0, 1, 2, 3, 4, 3, 2, 1, 0]
assert pop([0, 0, 0, 3, 0, 0, 0]) == [0, 1, 2, 3, 2, 1, 0]
assert pop([0, 0, 2, 0, 0]) == [0, 1, 2, 1, 0]
assert pop([0, 1, 0]) == [0, 1, 0]
assert pop([0]) == [0]

print('Success')