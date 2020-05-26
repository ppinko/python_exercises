"""
https://edabit.com/challenge/u9nd9D3HYcLxNZr7x
"""


def group_monotonic(lst: list) -> list:
    if len(lst) < 3:
        return []
    ans = []
    minus, plus = False, False
    for i in range(len(lst) - 1):
        if i == 0:
            if lst[i+1] - lst[i] > 0:
                plus = True
            else:
                minus = True
        elif lst[i+1] - lst[i] >= 0 and plus:
            continue
        elif lst[i+1] - lst[i] <= 0 and minus:
            continue
        elif plus:
            ans.append(i)
            plus = False
            minus = True
        else:
            ans.append(i)
            plus = True
            minus = False
    return ans


lst = [
    [[], []],
    [[0], []],
    [[1], []],
    [[0, 1], []],
    [[1, 0], []],
    [[1, 1], []],
    [[0, 1, 2], []],
    [[2, 1, 0], []],
    [[0, 2, 1], [1]],
    [[1, 0, 2], [1]],
    [[0, 1, 1, 0], [2]],
    [[1, 2, 3, 4, 4, 4, 3, 2, 1], [5]],
    [[0, 6, 10, 9, 3, -3, -9, -10, -6, 0], [2, 7]]]

for input, output in lst:
    assert group_monotonic(input) == output

print('Success')