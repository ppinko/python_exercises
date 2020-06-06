"""
https://edabit.com/challenge/FhmzcAxoydTybNjyA
"""


def carry_digits(a: int, b: int) -> int:
    counter, temp, carry = 0, 0, 0
    n_min, n_max = min(a, b), max(a, b)
    n1, n2 = str(n_min)[::-1], str(n_max)[::-1]
    for i, v in enumerate(n1):
        temp = int(v) + int(n2[i])
        if temp + carry >= 10:
            counter += 1
            carry = 1
        else:
            carry = 0
    return counter


assert carry_digits(36, 135) == 1
assert carry_digits(671, 329) == 3
assert carry_digits(1111, 3333) == 0
assert carry_digits(4, 5268) == 1
assert carry_digits(53214, 16905) == 2
assert carry_digits(53214, 56905) == 3
assert carry_digits(515, 4) == 0
assert carry_digits(515, 90) == 1
assert carry_digits(63223, 70000) == 1

print('Success')