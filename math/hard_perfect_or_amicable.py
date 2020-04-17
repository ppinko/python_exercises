"""
https://edabit.com/challenge/9cNxcMjfEMzKYoBZY
"""


def num_type(n: int) -> str:
    tot = sum(i for i in range(1, n) if n % i == 0)
    if tot == n:
        return "Perfect"
    tot2 = sum(i for i in range(1, tot) if tot % i == 0)
    if tot2 == n:
        return "Amicable"
    return 'Neither'

assert num_type(6) == "Perfect"
assert num_type(2924) == "Amicable"
assert num_type(5010) == "Neither"




print("Success")