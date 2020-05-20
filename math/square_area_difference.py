"""
https://edabit.com/challenge/NNhkGocuPMcryW7GP
"""

def square_areas_difference(r):
    import math
    a = math.sqrt(2*r*r)
    return round((2*r) ** 2 - a * a, 0)

assert square_areas_difference(5) == 50
assert square_areas_difference(6) == 72
assert square_areas_difference(7) == 98
assert square_areas_difference(17) == 578
print("Success")
