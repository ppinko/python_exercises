"""
https://edabit.com/challenge/rPnq2ugsM7zsWr3Pf
"""


def find_all_digits(nums):
    all_digits = list(range(10))
    for num in nums:
        for digit in str(num):
            if int(digit) in all_digits:
                all_digits.remove(int(digit))
            if len(all_digits) == 0:
                return num
    return "Missing digits!"


assert find_all_digits([3129, 7689, 7449, 4389, 5855, 9670, 9245, 1291, 7367, 1810]) == 9670
assert find_all_digits([2758, 3737, 3349, 5118, 7004, 6106, 8868, 6687, 2510, 8911]) == 6106
assert find_all_digits([5343, 6743, 2922, 2423, 7050, 5116, 3992, 2707, 2435, 5251]) == "Missing digits!"
c