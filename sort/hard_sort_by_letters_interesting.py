"""
https://edabit.com/challenge/LhMkMu46rG8EweYf7
"""


def sort_by_letter(lst: list) -> list:
    return sorted(lst, key=lambda x: x.strip('1234567890'))


assert sort_by_letter(["932c", "832u32", "2344b"]) == ["2344b", "932c", "832u32"]
assert sort_by_letter(["99a", "78b", "c2345", "11d"]) == ["99a", "78b", "c2345", "11d"]
assert sort_by_letter(["572z", "5y5", "304q2"]) == ["304q2", "5y5", "572z"]
assert sort_by_letter([]) == []

print('Success')