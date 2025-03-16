"""
Find Median of Two Sorted Arrays

You are given two sorted arrays, nums1 and nums2, of sizes m and n, respectively.
Find the median of the combined sorted array in O(log (m+n)) time.

Example Input 1:
nums1 = [1, 3]
nums2 = [2]

Expected Output:
2.0  # Merged array = [1, 2, 3], median = 2

Example Input 2:
nums1 = [1, 2]
nums2 = [3, 4]

Expected Output:
2.5  # Merged array = [1, 2, 3, 4], median = (2+3)/2 = 2.5

Constraints:
* Solve it in O(log (m+n)) time complexity.
* Do NOT simply merge the arrays and sort them.
"""


def findMedianSortedArrays_1(nums1: list[int], nums2: list[int]) -> float:
    nums1.extend(nums2)
    nums1.sort()
    if len(nums1) % 2 == 0:
        return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2
    else:
        return nums1[len(nums1) // 2]


print(findMedianSortedArrays_1([1, 3], [2]))  # 2.0
print(findMedianSortedArrays_1([1, 2], [3, 4]))  # 2.5


def findMedianSortedArrays_2(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1  # Ensure nums1 is the smaller array

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxLeftX = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float("inf") if partitionX == x else nums1[partitionX]

        maxLeftY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float("inf") if partitionY == y else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1


print(findMedianSortedArrays_2([1, 3], [2]))  # 2.0
print(findMedianSortedArrays_2([1, 2], [3, 4]))  # 2.5
