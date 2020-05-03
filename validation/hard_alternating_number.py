"""
https://edabit.com/challenge/f4dnSXMewhHeB6Mgw
"""


def is_alternating(n: int) -> bool:
    if n <= 0:
        return False
    elif n < 10:
        return True
    first = [int(i) for i in str(n)[::2]]
    second = [int(i) for i in str(n)[1::2]]
    return all(True if i % 2 != second[0] % 2 else False for i in first) and \
           all(True if i % 2 != first[0] % 2 else False for i in second)


assert is_alternating(123) == True
assert is_alternating(67) == True
assert is_alternating(2380) == False
assert is_alternating(75) == False
assert is_alternating(3) == True
assert is_alternating(903) == True
assert is_alternating(444) == False
assert is_alternating(0) == False
assert is_alternating(14589) == True
assert is_alternating(1234566789) == False
assert is_alternating(-12) == False
assert is_alternating(10) == True

print('Success')