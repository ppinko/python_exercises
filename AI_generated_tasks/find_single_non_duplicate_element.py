"""
Find Single Non-Duplicate Element

Given a sorted array where every element appears twice except for one, find the
single non-duplicate element in O(log n) time using O(1) extra space.

Example Input 1:
nums = [1, 1, 2, 2, 3, 3, 4]

Expected Output:
4

Example Input 2:
nums = [0, 1, 1, 2, 2, 3, 3]

Expected Output:
0

Constraints:
-   The array is sorted.
-   You must solve it in O(log n) time complexity (Binary Search).
-   Use O(1) extra space (No extra memory).

Bonus Challenge:
-   Can you solve it using bitwise operations instead of binary search?
-   Can you solve it using only one pass?
"""


def singeNonDuplicate_v1(nums: list[int]) -> int:
    """
    Using simple traversal loop. Complexity O(n).
    """

    for i in range(0, len(nums), 2):
        if i == len(nums) - 1:
            return nums[i]
        elif nums[i] != nums[i + 1]:
            return nums[i]


print(singeNonDuplicate_v1([1, 1, 2, 2, 3, 3, 4]))  # 4
print(singeNonDuplicate_v1([0, 1, 1, 2, 2, 3, 3]))  # 0
print(singeNonDuplicate_v1([0, 0, 1, 1, 2, 3, 3]))  # 2


def singeNonDuplicate_v2(nums: list[int]) -> int:
    """
    Using binary search. Complexity O(log n).
    """

    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        # Ensure mid is even (so we compare valid pairs)
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid + 1]:  # Single element is on the right
            left = mid + 2
        else:  # Single element is on the left or is mid
            right = mid
    return nums[left]  # Left and right will meet at the single element


print(singeNonDuplicate_v2([1, 1, 2, 2, 3, 3, 4]))  # 4
print(singeNonDuplicate_v2([0, 1, 1, 2, 2, 3, 3]))  # 0
print(singeNonDuplicate_v2([0, 0, 1, 1, 2, 3, 3]))  # 2
