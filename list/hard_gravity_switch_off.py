"""
https://edabit.com/challenge/jgpfraMtc9nrrPZkL
"""


def switch_gravity_on(lst):
    ls = []
    for i in range(len(lst[0])):
        temp = 0
        for j in range(len(lst)):
            if lst[j][i] == '#':
                temp += 1
        ls.append(temp)
    res = [['#' if len(lst) - 1 - i < ls[j] else '-' for j in range(len(lst[0]))] for i in range(len(lst))]
    return res


print(switch_gravity_on([
['-', '#', '#', '-'],
['-', '-', '-', '-'],
['-', '-', '-', '-'],
['-', '-', '-', '-']
]))

assert switch_gravity_on([
['-', '#', '#', '-'],
['-', '-', '-', '-'],
['-', '-', '-', '-'],
['-', '-', '-', '-']
]
) == [
['-', '-', '-', '-'],
['-', '-', '-', '-'],
['-', '-', '-', '-'],
['-', '#', '#', '-']
]


assert switch_gravity_on([
['-', '#', '#', '-'],
['-', '-', '#', '-'],
['-', '-', '-', '-'],
]
) == [
['-', '-', '-', '-'],
['-', '-', '#', '-'],
['-', '#', '#', '-']
]