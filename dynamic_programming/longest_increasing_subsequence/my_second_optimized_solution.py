"""
Optimized solution using LIS algorithm:

Good resource to watch - https://www.youtube.com/watch?v=CE2b_-XfVDk
"""


def LIS(lst):
    counter = 0
    k = len(lst)
    arr = [1] * k   # creating an array to store results
    for i in range(1, k):
        for j in range(0, i):
            counter += 1
            if lst[i] > lst[j]:
                arr[i] = max(arr[i], arr[j] + 1)
    # print(counter)
    return max(arr)


# print(LIS([50, 3, 10, 7, 40, 80]))  # counter = 15
# print(LIS([3, 10, 2, 1, 20]))       # counter = 10
# print(LIS([10, 22, 9, 33, 21, 50, 41, 60, 80]))     # counter = 36

assert LIS([3, 10, 2, 1, 20]) == 3
assert LIS([50, 3, 10, 7, 40, 80]) == 4
assert LIS([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6
print('Success')