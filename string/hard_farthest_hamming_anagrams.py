"""
https://edabit.com/challenge/zE37mNeG4cn6HesaP
"""


def max_ham(s1, s2):
    if len(s1) != len(s2):
        return False
    d1, d2 = {}, {}
    for i in range(len(s1)):
        d1[s1[i]] = d1.get(s1[i], 0) + 1
        d2[s2[i]] = d2.get(s2[i], 0) + 1
    if d1 != d2:
        return False
    x = sum(1 if s1[i] != s2[i] else 0 for i in range(len(s1)))
    if x == len(s1):
        return True
    else:
        return x



assert max_ham('dare','read') == True
assert max_ham('dear','read') == 2
assert max_ham('naive','ravine') == False
assert max_ham('observe','verbose') == 6
print('Success')