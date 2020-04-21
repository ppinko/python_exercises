"""
https://edabit.com/challenge/AcEnqyHp9q3Dd92Hn
"""


def multiply_nums(nums):
    ls = [int(i) for i in nums.split(',')]
    for j in range(1, len(ls)):
        ls[j] *= ls[j-1]
    return ls[-1]


assert multiply_nums('2, 3') == 6
assert multiply_nums('1, 2, 3, 4') == 24
assert multiply_nums('54, 75, 453, 0') == 0
assert multiply_nums('10, -2') == -20
print('Success')