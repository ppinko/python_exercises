"""
https://edabit.com/challenge/ZvFgCEBqRbBimD7qZ
"""


def bowling(lst: list) -> int:
    tot, turn = 0, 0
    first = True
    for i, v in enumerate(lst):
        if turn == 10:
            break
        if v == 10 and first:
            tot += v + lst[i+1] + lst[i+2]
            turn += 1
        elif v < 10 and first:
            tot += v
            first = False
        elif not first:
            turn += 1
            first = True
            tot += v
            if lst[i-1] + v == 10:
                tot += lst[i+1]
    return tot


assert bowling([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 300
assert bowling([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) == 80
assert bowling([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 150
assert bowling([10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10]) == 200
assert bowling([10, 0, 10, 7, 2, 10, 10, 10, 8, 2, 9, 1, 7, 2, 10, 10, 5]) == 194
assert bowling([8, 0, 8, 2, 10, 10, 7, 3, 9, 1, 7, 2, 10, 10, 9, 0]) == 177
print('Success')