"""
https://edabit.com/challenge/jSxo7n5c8J42zrwMB
"""


import math


def circle_area(r):
    return math.pi * pow(r, 2)


def rectangle_area(a, b):
    return a * b


def triangle_area(a, h):
    return 0.5 * a * h


def pentagon_area(s):
    return 2.5 * pow(s, 2) * pow(0.75, 0.5)


def choose_shape(lst):
    if lst[0] == 'Circle':
        return circle_area(int(lst[1]))
    elif lst[0] == 'Rectangle':
        return rectangle_area(int(lst[1]), int(lst[2]))
    elif lst[0] == 'Triangle':
        return triangle_area(int(lst[1]), int(lst[2]))
    else:
        return pentagon_area(int(lst[1]))


def shape_in_shape(bigger: str, smaller: str) -> bool:
    lst = [i.split(', ') for i in [bigger, smaller]]
    return choose_shape(lst[0]) >= choose_shape(lst[1])


assert shape_in_shape("Circle, 3", "Rectangle, 3, 14") == False
assert shape_in_shape("Circle, 5", "Rectangle, 3, 14") == True
assert shape_in_shape("Triangle, 5, 5", "Circle, 2") == False
assert shape_in_shape("Triangle, 10, 5", "Circle, 2") == True
assert shape_in_shape("Circle, 10", "Pentagon, 10") == True
assert shape_in_shape("Pentagon, 10", "Circle, 10") == False

print('Success')