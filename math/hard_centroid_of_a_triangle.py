"""
https://edabit.com/challenge/YzZdaqcMsCmndxFcC
"""


def centroid(Ax, Ay, Bx, By, Cx, Cy):
    if Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By) == 0:
        return False
    return (round((Ax + Bx + Cx) /3, 2), round((Ay + By + Cy) / 3, 2))


assert centroid(0, 0, 3, 0, 3, 3) == (2.0, 1.0)
assert centroid(5, 3, -3, -2, -1, 4) == (0.33, 1.67)
assert centroid(2, 2, 8, -2, 0, -3) == (3.33, -1.0)
assert centroid(5, 3, 5, -1, -4, 1) == (2.0, 1.0)
assert centroid(-1, -3, 1, 3, 2, 6) == False
assert centroid(3, 0, 0, 3, 6, 3) == (3.0, 2.0)

print('Success')