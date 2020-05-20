"""
https://edabit.com/challenge/HBuWYyh5YCmDKF4uH
"""


def almost_sorted(lst: list) -> bool:
    tot_increasing, tot_decreasing = 0, 0
    for i in range(1, len(lst)):
        if lst[i] >= lst[i-1]:
            tot_decreasing += 1
        elif lst[i-1] >= lst[i]:
            tot_increasing += 1
    return min(tot_decreasing, tot_increasing) == 1


assert almost_sorted([1, 3, 5, 9, 11, 80, 15, 33, 37, 41]) == True
assert almost_sorted([6, 5, 4, 7, 3]) == True
assert almost_sorted([6, 4, 2, 0]) == False
assert almost_sorted([7, 8, 9, 3, 10, 11, 12, 2]) == False
assert almost_sorted([9, 1, 8, 2]) == True
assert almost_sorted([1, 3, 9, 44, 15, 17, 33]) == True
assert almost_sorted([5, 4, 3, 2, -1, 0]) == True
assert almost_sorted([5, 2, 3, 4]) == True
assert almost_sorted([8, 3, 7, 4, 9]) == False
assert almost_sorted([-3, -4, -5, -7]) == False
assert almost_sorted([5, 6, 7, 8]) == False
assert almost_sorted([9, 1, 8, 2, 7, 3]) == False

print('Success')