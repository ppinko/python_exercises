"""
https://www.hackerrank.com/challenges/minimum-swaps-2/problem
"""

arr = [7, 1, 3, 2, 4, 5, 6]

def minimumSwaps(arr):
    swap = 0
    n = 0
    while n < len(arr) - 1:
        if arr[n] == n + 1:
            n += 1
        else:
            # it swaps always the first wrong number from the left side to the the right position
            swap += 1
            temp1 = arr[n]
            temp2 = arr[temp1-1]
            arr[n] = temp2
            arr[temp1-1] = temp1
    return swap

print(minimumSwaps(arr))