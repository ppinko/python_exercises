"""
https://edabit.com/challenge/vaCKHWRA9tf98EYLm
"""


def ry_seq(*args):
    options = ("all", "red", "yellow")
    if len(args) < 2 or args[1] not in options:
        return False
    n = 2
    tot = 1
    if args[0] == 1:
        tot = 1
    else:
        while n <= args[0]:
            tot += 4 * (n-1)
            n += 1
    if args[1] == options[0]:
        if args[0] == 0:
            return 0
        return tot
    elif args[1] == options[1]:
        return 2 * args[0] - 1
    else:
        return tot - (2 * args[0] - 1)

assert ry_seq(2, "all") == 5
assert ry_seq(1, "yellow") == 0
assert ry_seq(1, "blue") == False
assert ry_seq(28, "red") == 55
assert ry_seq(6, "all") == 61
assert ry_seq(3) == False
assert ry_seq(0, "all") == 0
assert ry_seq(22, "all") == 925
assert ry_seq(28, "yellow") == 1458
assert ry_seq(23, "red") == 45
assert ry_seq(150, "all") == 44701
assert ry_seq(30, "yellow") == 1682
assert ry_seq(1000, "red") == 1999
assert ry_seq(28, "green") == False

print('Success')