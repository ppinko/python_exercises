"""
https://edabit.com/challenge/vLRpikwB9dqaR3HAj
"""


def is_ord_sub(small: list, long: list) -> bool:
    j = 0
    for i in small:
        try:
            j += long[j:].index(i) + 1
        except ValueError:
            return False
    return True


assert is_ord_sub([4, 3], [3, 4]) == False
assert is_ord_sub([4, 3, 2], [5, 4, 3, 2, 1]) == True
assert is_ord_sub([5, 3, 1], [5, 4, 3, 2, 1]) == True
assert is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]) == False
assert is_ord_sub([1, 2, 3], [3, 2, 1, 2, 3]) == True
assert is_ord_sub([0, 1, 0, 1], [1, 0, 1, 0, 1]) == True
assert is_ord_sub([0, 1, 0, 1], [1, 1, 1, 1, 0, 0, 0, 1, 1, 0]) == False
assert is_ord_sub([0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0]) == False
assert is_ord_sub([1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1]) == False
assert is_ord_sub([1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1]) == True

print('Success')