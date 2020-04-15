"""
https://edabit.com/challenge/q3fWZxXGRxSQo5viw
"""

def cal(depth):
    import math
    if depth <= 150:
        return math.ceil(depth / 5)
    tot = 0
    while depth - 150 > 0:
        depth -= 120
        tot += 40
    tot += depth / 5
    return math.ceil(tot)

assert cal(31) == 7
assert cal(150) == 30
assert cal(200) == 56
assert cal(15) == 3

print("Success")
