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


print(majorityElement([3, 2, 2, 3, 2]))  # 2
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2


def majorityElement_2(nums: list[int]) -> int:
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1
    return max(d, key=d.get)


print(majorityElement_2([3, 2, 2, 3, 2]))  # 2
print(majorityElement_2([2, 2, 1, 1, 1, 2, 2]))  # 2


def majority_element_3(nums):
    """
    Using Boyer-Moore Voting Algorithm
    """
    candidate, count = None, 0

    for num in nums:
        if count == 0:
            candidate = num  # Set new candidate
        count += 1 if num == candidate else -1  # Increase or decrease count

    return candidate


# Example usage
print(majority_element_3([3, 2, 2, 3, 2]))  # 2
print(majority_element_3([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
