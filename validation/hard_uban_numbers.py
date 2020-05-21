"""
https://edabit.com/challenge/rRKbaDKxzBhaLAFJZ
"""


def is_uban(n: int) -> bool:
    return not(('4' in str(n) or n % 1000000 > 99) and n % 1000000 != 40)


assert is_uban(0) == True
assert is_uban(24) == False
assert is_uban(223) == False
assert is_uban(2051) == False
assert is_uban(627) == False
assert is_uban(6258) == False
assert is_uban(12) == True
assert is_uban(202) == False
assert is_uban(98) == True
assert is_uban(6592) == False
assert is_uban(393) == False
assert is_uban(1000096) == True
assert is_uban(40) == True

print('Success')