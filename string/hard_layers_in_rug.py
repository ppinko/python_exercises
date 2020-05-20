"""
https://edabit.com/challenge/LaBMjgbMjf5BajczX
"""


def count_layers(lst: list) -> int:
    if len(lst) == 1:
        row = lst[0]
    else:
        row = lst[len(lst) // 2]
    return sum(1 for i in range(1, len(row)) if row[i] != row[i-1]) // 2 + 1


assert count_layers(["AAA"]) == 1
assert count_layers(["AAAA", "AAAA", "AAAA"]) == 1
assert count_layers(["AAAA", "ABBA", "AAAA"]) == 2
print('Success')