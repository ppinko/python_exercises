"""
https://edabit.com/challenge/QcswPnY2cAbrfwuWE
"""


def factorial_to_num(n: int) -> list:
    L, i, prev = [], 1, 1
    while n > prev:
        prev *= i
        i += 1
        L.append(prev)
    return L


def filter_factorials(lst: list) -> list:
    L = set(factorial_to_num(max(lst)))
    return sorted(list(L.intersection(lst)))


assert filter_factorials([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 6]
assert filter_factorials([1, 4, 120]) == [1, 120]
assert filter_factorials([8, 9, 10]) == []
assert filter_factorials([1, 8, 9, 10]) == [1]
print('Success')