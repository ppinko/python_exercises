"""
Given a distance ‘dist, count total number of ways to cover
the distance with 1, 2 and 3 steps.
"""


def cover_distance(steps: int) -> int:
    if steps == 0:
        return 1
    elif steps < 0:
        return 0
    else:
        return cover_distance(steps - 1) + cover_distance(steps - 2) + cover_distance(steps - 3)


assert cover_distance(3) == 4
assert cover_distance(4) == 7

print('Success')