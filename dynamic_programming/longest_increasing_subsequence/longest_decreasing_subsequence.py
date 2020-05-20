"""
My personal idea to count the longest decreasing subsequence.

Good exercise to repeat the use the same algorithm in a slightly
different problem.
"""


def LDS(l: list) -> int:
    k = len(l)
    arr = [1] * k
    counter = 0
    for i in range(1, k):
        for j in range(0, i):
            counter += 1
            if l[i] < l[j]:
                arr[i] = max(arr[i], arr[j] + 1)
    print(counter)
    return max(arr)

# print(LDS([50, 3, 10, 7, 40, 80]))  # counter = 15
# print(LDS([3, 10, 2, 1, 20]))       # counter = 10
# print(LDS([10, 22, 9, 33, 21, 50, 41, 60, 80]))     # counter = 36


assert LDS([3, 10, 2, 1, 20]) == 3
assert LDS([50, 3, 10, 7, 40, 80]) == 3
assert LDS([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 2
print('Success')