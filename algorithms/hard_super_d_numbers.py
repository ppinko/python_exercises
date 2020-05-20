"""
https://edabit.com/challenge/KSiC4iNjDHFiGS5oh
"""


def is_super_d(n: int) -> str:
    for i in range(2, 10):
        temp = i * pow(n, i)
        if str(i) * i in str(temp):
            return 'Super-{0} Number'.format(i)
    return 'Normal Number'


assert is_super_d(19) == "Super-2 Number"
assert is_super_d(753) == "Super-3 Number"
assert is_super_d(1168) == "Super-4 Number"
assert is_super_d(24) == "Normal Number"
assert is_super_d(20379) == "Super-5 Number"
assert is_super_d(185423) == "Super-8 Number"
assert is_super_d(1170) == "Normal Number"
assert is_super_d(118) == "Normal Number"
assert is_super_d(93568867) == "Super-9 Number"
assert is_super_d(333) == "Super-2 Number"
assert is_super_d(107) == "Super-2 Number"
assert is_super_d(1184321) == "Super-7 Number"
assert is_super_d(10098023246) == "Normal Number"
assert is_super_d(1045361) == "Super-6 Number"
assert is_super_d(0) == "Normal Number"

print('Success')