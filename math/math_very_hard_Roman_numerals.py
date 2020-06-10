"""
https://edabit.com/challenge/oepiudBYC7PT7TXAM
"""


import itertools


def parse_roman_numeral(roman: str) -> int:
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
         'C': 100, 'D': 500, 'M': 1000}
    num = 0
    L = [d[k] * len(list(group)) for k, group in  itertools.groupby(roman)]
    for i, v in enumerate(L):
        if i == len(L) - 1 or v > L[i+1]:
            num += v
        else:
            num -= v
    return num


assert parse_roman_numeral("I") == 1
assert parse_roman_numeral("VIII") == 8
assert parse_roman_numeral("XXIX") == 29
assert parse_roman_numeral("LIV") == 54
assert parse_roman_numeral("CCV") == 205
assert parse_roman_numeral("CDXLIV") == 444
assert parse_roman_numeral("CMXCIX") == 999
assert parse_roman_numeral("M") == 1000
assert parse_roman_numeral("MMMDCCCLXXXVIII") == 3888
assert parse_roman_numeral("MMMCMX") == 3910

print('Success')