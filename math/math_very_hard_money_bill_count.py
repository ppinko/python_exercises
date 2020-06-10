"""
https://edabit.com/challenge/brJHwyof9NWpXFgS8
"""


def bill_count(account: int, bills: list) -> int:
    num = 0
    for bill in sorted(bills, reverse=True):
        num += account // bill
        account %= bill
    return num


assert bill_count(100, [1, 10, 20]) == 5
assert bill_count(1050, [1, 10, 20, 100]) == 13
assert bill_count(3, [1, 10]) == 3
assert bill_count(555, [1, 10, 100]) == 15
assert bill_count(222, [1, 10, 100]) == 6
assert bill_count(60, [1, 10, 20]) == 3
assert bill_count(55, [1, 5, 10, 50]) == 2

print("Success")