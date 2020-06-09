"""
https://edabit.com/challenge/uCKJi6X3KTH9zuSc3
"""


from collections import Counter
from itertools import groupby


def mystery_func(n: int) -> str:
    return ''.join(str(len(list(group))) + k for k, group in groupby(list(str(n))))


mystery_func(11155)
assert mystery_func(15) == "1115"
assert mystery_func(15212) == "1115121112"
assert mystery_func(111111422) == "611422"
assert mystery_func(1) == "11"
assert mystery_func(513515) == "151113151115"
assert mystery_func(666) == "36"
assert mystery_func(69) == "1619"

print("Success")