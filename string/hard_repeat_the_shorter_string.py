"""
https://edabit.com/challenge/dRjHygERcDJpiDzze
"""

import math

def lengthen(s1: str, s2: str) -> str:
    if len(s1) < len(s2):
        a, b = s1, s2
    else:
        b, a = s1, s2
    a = a * math.ceil(len(b) / len(a) + 1)
    return a[:len(b)]


""" Alternative solution """


def lengthen2(s1, s2):
    s1, s2 = min(s1,s2,key=len),max(s1,s2,key=len)
    val1 = len(s2)//len(s1)
    val2 = len(s2)%len(s1)
    return s1*val1 + s1[:val2]


assert lengthen("abcdefg", "ab") == "abababa"
assert lengthen("ingenius", "forest") == "forestfo"
assert lengthen("skipping", "clap") == "clapclap"
assert lengthen("k", "champagne") == "kkkkkkkkk"
assert lengthen("DUH", "champagne") == "DUHDUHDUH"

print('Success')