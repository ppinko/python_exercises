"""
https://edabit.com/challenge/Fm7ap2w3exqunF9aJ
"""


def count_lone_ones(n: int) -> int:
    ans, n_str = 0, str(n)
    if len(n_str) == 1:
        if n == 1:
            return 1
        else:
            return 0
    for i, val in enumerate(n_str):
        if i == 0 and val == '1' and n_str[i+1] != '1':
            ans += 1
        elif i == len(n_str) - 1 and val == '1' and n_str[i-1] != '1':
            ans += 1
        elif i != 0 and i != len(n_str) - 1 and val == '1' and n_str[i+1] != '1' and n_str[i-1] != '1':
            ans += 1
    return ans


assert count_lone_ones(101) == 2
assert count_lone_ones(1191) == 1
assert count_lone_ones(1111) == 0
assert count_lone_ones(11101) == 1
assert count_lone_ones(462) == 0
assert count_lone_ones(12131415161718191) == 9
assert count_lone_ones(11231212111) == 2
assert count_lone_ones(1) == 1
assert count_lone_ones(0) == 0

print('Success')