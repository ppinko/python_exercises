"""
https://edabit.com/challenge/LMnRCtjk4RQbX3DXw
"""

def no_intersecting_ones(matrix: list) -> bool:
    if any(True if sum(i) >= 2 else False for i in matrix):
        return False
    elif any(True if sum(i) >= 2 else False for i in zip(*matrix)):
        return False
    return True


assert no_intersecting_ones([[0, 1], [1, 0]]) == True
assert no_intersecting_ones([[1, 1], [0, 0]]) == False
assert no_intersecting_ones([[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]) == True

print('Success')