"""
https://edabit.com/challenge/vQgmyjcjMoMu9YGGW
"""


def simplify(f: str) -> str:
    a, b = list(map(int, f.split('/')))
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            while a % i == 0 and b % i == 0:
                a, b = int(a/i), int(b/i)
    if b == 1:
        return str(a)
    return '{0}/{1}'.format(a, b)


assert simplify("5/7") == "5/7"
assert simplify("4/6") == "2/3"
assert simplify("11/10") == "11/10"
print('Success')