"""
https://edabit.com/challenge/vLLXeQH5tgyvbzYZS
"""


import math


def is_prim_pyth_triple(lst):
    # test if right triangle
    lst.sort()
    if math.hypot(lst[0], lst[1]) != lst[-1]:
        return False

    # collecting all divisors
    divisors = set()
    for i in lst:
        for j in range(2, i + 1):
            if i % j == 0:
                if j in divisors:
                    return False
                divisors.add(j)
    return True


assert is_prim_pyth_triple([4,5,3]) == True
assert is_prim_pyth_triple([7,12,13]) == False
assert is_prim_pyth_triple([39,15,36]) == False
print('Success')