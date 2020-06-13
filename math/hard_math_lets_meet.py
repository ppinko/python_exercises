"""
https://edabit.com/challenge/9SLvXXz8ED7B6joJg
"""


def lets_meet(dist, v1, v2):
    t = 1000 * dist / ((v1 + v2) * 1000 / 3600)
    return "{0}h {1}min {2}s".format(int(t // 3600), int(t % 3600 // 60), int(t % 3600 % 60))


assert lets_meet(100, 10, 30) == "2h 30min 0s"
assert lets_meet(33, 15, 20) == "0h 56min 34s"
assert lets_meet(250, 60, 80) == "1h 47min 8s"
assert lets_meet(125, 55, 40) == "1h 18min 56s"
assert lets_meet(0.6, 10, 15) == "0h 1min 26s"
assert lets_meet(0.8, 23, 18) == "0h 1min 10s"
assert lets_meet(0.72, 8, 12) == "0h 2min 9s"
assert lets_meet(33, 15, 20) == "0h 56min 34s"
assert lets_meet(360, 80, 64) == "2h 30min 0s"
assert lets_meet(10, 45, 42) == "0h 6min 53s"
assert lets_meet(90, 75, 65) == "0h 38min 34s"
assert lets_meet(280, 70, 80) == "1h 52min 0s"

print("Success")