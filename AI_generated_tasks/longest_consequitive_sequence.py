"""
Longest Consecutive Sequence

Given an unsorted list of integers, find the length of the longest consecutive
sequence of numbers.

Example Input 1:
nums = [100, 4, 200, 1, 3, 2]

Expected Output:
4  # The longest consecutive sequence is [1, 2, 3, 4]

Example Input 2:
nums = [9, 1, 4, 7, 3, -2, 0, 5, 8, -1, 6]

Expected Output:
7  # The longest consecutive sequence is [3, 4, 5, 6, 7, 8, 9]

Constraints:
- Solve it in O(n) time complexity (Hint: Use a set for fast lookups).
- You cannot sort the array first (that would be O(n log n), which is too slow).
"""


def longest_consequitive_sequence_v1(nums: list[int]) -> int:
    """
    Simple solution with sorting first. Complexity O(n log n)
    """
    nums.sort()
    counter, highest = 0, 0
    for i, v in enumerate(nums):
        if counter == 0:
            counter += 1
        elif v == nums[i - 1]:
            pass  # skip duplications
        elif v - nums[i - 1] == 1:
            counter += 1
        else:
            counter = 1

        if counter > highest:
            highest = counter

    return highest


assert longest_consequitive_sequence_v1([100, 4, 200, 1, 3, 2]) == 4
assert longest_consequitive_sequence_v1([9, 1, 4, 7, 3, -2, 0, 5, 8, -1, 6]) == 7


def longest_consequitive_sequence_v2(nums: list[int]) -> int:
    """
    Use set for efficient look-up and elements removal.
    """
    s = set(nums)
    counter, highest = 0, 0
    while len(s) != 0:
        v = s.pop()
        counter += 1
        # check left side
        temp = v - 1
        while temp in s:
            counter += 1
            s.remove(temp)
            temp -= 1

        # check left side
        temp = v + 1
        while temp in s:
            counter += 1
            s.remove(temp)
            temp += 1

        if counter > highest:
            highest = counter
        counter = 0  # reset counter
    return highest


assert longest_consequitive_sequence_v2([100, 4, 200, 1, 3, 2]) == 4
assert longest_consequitive_sequence_v2([9, 1, 4, 7, 3, -2, 0, 5, 8, -1, 6]) == 7
