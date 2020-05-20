"""
https://edabit.com/challenge/vBwRuR4mF5yQ4cNuc
"""


def count_missing_nums(ls: list) -> int:
    only_digits = [int(i) for i in ls if i.isdigit()]
    return max(only_digits) - min(only_digits) + 1 - len(set(only_digits))


assert count_missing_nums(['1', '3', '5', '7', '9']) == 4
assert count_missing_nums(['7', '3', '1', '9', '5']) == 4
assert count_missing_nums(['10', '20', '30', '40', '50']) == 36
print('Success')