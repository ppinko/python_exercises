"""
https://edabit.com/challenge/pn7QpvW2fW9grvYYE
"""


def find_fulcrum(lst: list) -> int:
    for i in range(1, len(lst) - 1):
        if sum(lst[:i]) == sum(lst[i+1:]):
            return lst[i]
    return -1


assert find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]) == 4
assert find_fulcrum([9, 1, 9]) == 1
assert find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]) == 0
assert find_fulcrum([8, 8, 8, 8]) == -1
print('Success')