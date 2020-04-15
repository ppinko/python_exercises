"""
https://edabit.com/challenge/ksiA6Q34iXgTcMeZF
"""

def bonus(n: int) -> int:
    if n < 33:
        return 0
    elif n < 41:
        return (n-32) * 325
    elif n < 49:
        return 8* 325 + (n-40) * 550
    else:
        return 8 * 325 + 8 * 550 + (n-48)*600

assert bonus(15) == 0
assert bonus(37) == 1625
assert bonus(50) == 8200

print("Success")
