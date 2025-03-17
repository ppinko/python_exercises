"""
Subarray Sum Equals K

Given an array of integers nums and an integer k, find the total number of
subarrays whose sum equals k.

Example Input 1:
nums = [1, 1, 1]
k = 2

Expected Output:
3  # [1,1] (three times)

Example Input 2:
nums = [3, 4, 7, 2, -3, 1, 4, 2, 1]
k = 7

Expected Output:
4 # Subarrays that sum to 7: [3,4], [7], [4,2,1], [2,-3,1,4,2,1]

Constraints:
- Solve in O(n²) time using a simple nested loop.
- Optimize to O(n) time complexity using prefix sum + hashmap (Hint: Think about
cumulative sum).
"""


def subarray_sum_equals_k(nums: list[int]) -> int:
    counter = 0
    return counter


assert subarray_sum_equals_k([1, 1, 1]) == 3
assert subarray_sum_equals_k([3, 4, 7, 2, -3, 1, 4, 2, 1]) == 7
