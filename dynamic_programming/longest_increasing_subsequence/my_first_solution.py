"""
https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/
"""

"""
First naive solution
"""

counter = 0


def LIS(lst, n, last) -> int:
    global counter
    counter += 1
    if n == 0:
        return 0
    elif lst[0] <= last:
        return LIS(lst[1:], n-1, last)
    return max(1 + LIS(lst[1:], n-1, lst[0]), LIS(lst[1:], n-1, last))


# print(LIS([50, 3, 10, 7, 40, 80], 6, -100000))
# print(counter) # out = 57
#
# print(LIS([3, 10, 2, 1, 20], 5, -100000))
# print(counter) # out = 30
#
# print(LIS([10, 22, 9, 33, 21, 50, 41, 60, 80], 9, -100000))
# print(counter) # out = 334


assert LIS([3, 10, 2, 1, 20], 5, -100000) == 3
assert LIS([50, 3, 10, 7, 40, 80], 6, -100000) == 4
assert LIS([10, 22, 9, 33, 21, 50, 41, 60, 80], 9, -100000) == 6
print('Success')