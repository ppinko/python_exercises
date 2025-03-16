from collections import Counter

"""
Majority Element

Given an array nums of size n, find the majority element. The majority element
is the number that appears more than n / 2 times.

Example Input 1:
nums = [3, 2, 3]

Expected Output:
3

Example Input 2:
nums = [2, 2, 1, 1, 1, 2, 2]

Expected Output:
2

Constraints:
* Solve in O(n) time complexity.
* Solve in O(1) extra space.

Bonus Challenge:
* Can you solve it without sorting or using a dictionary?
* Can you solve it using only one loop?
"""


def majorityElement(nums: list[int]) -> int:
    counter = Counter(nums)
    return max(counter, key=counter.get)


print(majorityElement([3, 2, 3]))  # 3
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
