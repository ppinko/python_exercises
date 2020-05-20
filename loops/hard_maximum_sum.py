"""
https://edabit.com/challenge/m7mJib8kvoyDXgk4i
"""


def max_sum(t: list) -> int:
    lst = []
    for i, v in enumerate(t):
        if i == 0:
            lst.append(v)
        else:
            lst.append(v + lst[i-1])
    return max(lst) - min(lst)


assert max_sum((3, -10, 4, -1, 2, 3, 6, -7)) == 14
assert max_sum((1, -9, 0, -8, 76, 5, 43)) == 124

print('Success')