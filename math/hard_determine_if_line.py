"""
https://edabit.com/challenge/bBExn57vLEsXgHC5m
"""


def same_line(ls: list) -> bool:
    """
    a = y1-y2/x1-x2
    y = ax + b
    b = y- ax
    """
    if ls[0][0] == ls[1][0]:
        if ls[0][0] == ls[2][0]:
            return True
        else:
            return False
    a = (ls[0][1] - ls[1][1]) / (ls[0][0] - ls[1][0])
    b = ls[0][1] - a * ls[0][0]
    return ls[2][1] == a * ls[2][0] + b


assert same_line([[0, 0], [1, 1], [3, 3]]) == True
assert same_line([[-2, -1], [2, 1], [0, 0]]) == True
assert same_line([[-2, 0], [-10, 0], [-8, 0]]) == True

print("Success")

