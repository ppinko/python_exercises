"""
https://edabit.com/challenge/u5JrjKv9BNLLPSKJs
"""


def basis_steps(height, steps):
    if height == 0:
        return 1
    elif height < 0:
        return 0
    total = 0
    for i in steps:
        total += basis_steps(height-i, steps)
    return total


def steps_dict(steps):
    d = {0: 1}
    for i in range(1, max(steps) + 1):
        d[i] = basis_steps(i, steps)
    return d


def num_ways(height, steps) -> int:
    d = steps_dict(steps)
    if height in d:
        return d[height]
    for i in range(max(steps) + 1, height + 1):
        d[i] = 0
        for j in steps:
            d[i] += d[i-j]
    return d[height]


assert num_ways(4, { 1, 2 }) == 5
assert num_ways(3, { 1, 2, 3 }) == 4
assert num_ways(10, { 1, 2, 3, 4 }) == 401
assert num_ways(50, { 1, 2 }) == 20365011074
assert num_ways(100, { 1 }) == 1

print('Success')