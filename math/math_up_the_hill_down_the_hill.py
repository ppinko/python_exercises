"""
https://edabit.com/challenge/NYEaXXCnSj9jteNWA

minutes / 60 * up = x
x = v2 * down


"""


def ave_spd(minutes: int, up: int, down: int) -> int:
    s = minutes * up / 60
    t2 = s / down
    return 2 * s / (t2 + minutes / 60)


assert ave_spd(18, 10, 30) == 15
assert ave_spd(18, 20, 60) == 30
assert ave_spd(30, 10, 30) == 15
assert ave_spd(30, 8, 24) == 12

print('Success')