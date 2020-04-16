"""
https://edabit.com/challenge/iBqJcagS56wmDpe4x
"""

def vol_shell(r1, r2):
    import math
    return round(4*math.pi*((max(r1, r2))**3 - (min(r1,r2))**3) /3, 3)

assert vol_shell(17, 36) == 174852.67
assert vol_shell(3, 4) == 154.985
assert vol_shell(1, 90) == 3053623.87

print("Success")
