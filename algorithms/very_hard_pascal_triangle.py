"""
https://edabit.com/challenge/YN33GEpLQqa5imcFx
"""


import math


def pascals_triangle(n: int) -> str:
    return ' '.join(str(int(math.factorial(n) / (math.factorial(i) * math.factorial(n-i))))
                    for i in range(n + 1))


assert pascals_triangle(1) == "1 1"
assert pascals_triangle(2) == "1 2 1"
assert pascals_triangle(3) == "1 3 3 1"
assert pascals_triangle(4) == "1 4 6 4 1"
assert pascals_triangle(5) == "1 5 10 10 5 1"

print('Success')