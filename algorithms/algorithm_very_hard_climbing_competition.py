"""
https://edabit.com/challenge/Q7oecYfjkq7tHwPoA
"""


import math


def climb(stamina, obstacles):
    tot = 0
    steps = [obstacles[i+1] - obstacles[i] for i in range(len(obstacles) - 1)]
    cost = [2 * math.ceil(i) if i >= 0 else abs(math.floor(i)) for i in steps]
    for i in cost:
        stamina -= i
        if stamina >= 0:
            tot += 1
        else:
            break
    return tot


assert climb(5,[5, 4.2, 3, 3.5, 6, 4, 6, 8, 1]) == 3
assert climb(10,[5, 4.2, 3, 3.5, 6, 4, 6, 8, 1]) == 3
assert climb(20,[5, 4.2, 3, 3.5, 6, 4, 6, 8, 1]) == 6
assert climb(100,[5, 4.2, 3, 3.5, 6, 4, 6, 8, 1]) == 8
assert climb(5,[0, 1, 2.5, 0.8]) == 1
assert climb(10,[0, 1, 2.5, 0.8]) == 3
assert climb(10,[0.3, 2, 2.8, 3, 3, 0.8, 3.2,2,0]) == 4
assert climb(11,[0.3, 2, 2.8, 3, 3, 0.8, 3.2,2,0]) == 5
assert climb(12,[0.3, 2, 2.8, 3, 3, 0.8, 3.2,2,0]) == 5
assert climb(13,[0.3, 2, 2.8, 3, 3, 0.8, 3.2,2,0]) == 5
assert climb(14,[0.3, 2, 2.8, 3, 3, 0.8, 3.2,2,0]) == 5
assert climb(15,[0.3, 2, 2.8, 3, 3, 0.8, 3.2,2,0]) == 5
assert climb(16,[0.3, 2, 2.8, 3, 3, 0.8, 3.2,2,0]) == 5
assert climb(17,[0.3, 2, 2.8, 3, 3, 0.8, 3.2,2,0]) == 6
assert climb(18,[0.3, 2, 2.8, 3, 3, 0.8, 3.2,2,0]) == 6
assert climb(19,[0.3, 2, 2.8, 3, 3, 0.8, 3.2,2,0]) == 7
assert climb(20,[0.3, 2, 2.8, 3, 3, 0.8, 3.2,2,0]) == 7
assert climb(30,[0.3, 2, 2.8, 3, 3, 0.8, 3.2,2,0]) == 8
assert climb(15,[0.3, 2, 2.8, 3, 3, 0.8, 3.2,2,0]) == 5

print("Success")