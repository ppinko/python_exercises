"""
https://edabit.com/challenge/cx2KeDmEZDyeFsSfT
"""


def periodic(n: str) -> int:
    k, l = 1, len(n)
    s = set()
    s.add(n)
    while True:
        temp = 0
        for i in n:
            temp += int(i)
        n += str(temp)
        n = n[len(n) - l:]
        if n in s:
            return k
        else:
            s.add(n)
            k += 1


assert periodic("2") == 1
assert periodic("22") == 13
assert periodic("157") == 4
assert periodic("1234567") == 943
assert periodic("1818") == 1
assert periodic("0000001") == 778

print('Success')