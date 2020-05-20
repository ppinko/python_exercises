"""
https://edabit.com/challenge/t56Nk2kJkQ6H4xzgX
"""


def swap_xy(txt: str) -> str:
    txt = txt.replace('(', '').replace(')', '')
    L = txt.split(', ')
    return '({0}, {1}), ({2}, {3})'.format(int(L[1]), int(L[0]), int(L[3]), int(L[2]))


assert swap_xy("(1, 2), (3, 4)") == "(2, 1), (4, 3)"
assert swap_xy("(11, 23), (43, 99)") == "(23, 11), (99, 43)"
assert swap_xy("(-5, -3), (7, 4)") == "(-3, -5), (4, 7)"
assert swap_xy("(-1095, -321), (0, -88)") == "(-321, -1095), (-88, 0)"

print('Success')