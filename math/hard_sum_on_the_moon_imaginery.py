"""
https://edabit.com/challenge/NfhWZbpcyydySzXeq
"""


from itertools import zip_longest


def lunar_sum(a: int, b: int) -> int:
    a_str, b_str = str(a)[::-1], str(b)[::-1]
    temp = ''.join(i if int(i) >= int(j) else j for i, j in zip_longest(a_str, b_str, fillvalue='0'))
    return int(temp[::-1])


assert lunar_sum(246, 317) == 347
assert lunar_sum(134, 54) == 154
assert lunar_sum(20, 140) == 140
assert lunar_sum(1, 1) == 1
assert lunar_sum(198, 44) == 198
assert lunar_sum(36602, 696) == 36696
assert lunar_sum(91, 8823) == 8893
assert lunar_sum(123, 8) == 128
assert lunar_sum(2289, 98211285) == 98212289
assert lunar_sum(9, 11) == 19
assert lunar_sum(11, 22) == 22

print('Success')