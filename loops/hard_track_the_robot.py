"""
https://edabit.com/challenge/bYDPYX9ajWC6PNGCp
"""


def track_robot(*args) -> list:
    lst = list(args)
    pos = [0, 0]
    switch = True
    for i in lst[0::2]:
        if switch:
            pos[1] += i
            switch = False
        else:
            switch = True
            pos[1] -= i
    switch = True
    for i in lst[1::2]:
        if switch:
            pos[0] += i
            switch = False
        else:
            switch = True
            pos[0] -= i
    return pos


assert track_robot(20, 30, 10, 40) == [-10, 10]
assert track_robot(10, -10, -10, 10) == [-20, 20]
assert track_robot() ==[0, 0]
assert track_robot(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == [6, 5]
assert track_robot(1, 0, 2, 0, 3, 0, 4, 0, 5, 0) == [0, 3]
assert track_robot(0, 1, 0, 2, 0, 3, 0, 4, 0, 5) == [3, 0]

print('Success')