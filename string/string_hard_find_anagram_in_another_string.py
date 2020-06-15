"""
https://edabit.com/challenge/LF6LyPmjcuLnSjgiL
"""


def ana_str_str(short: str, long: str) -> bool:
    s_short = set(short)
    if len(short) == len(long):
        s_long = set(long)
        return s_short.issubset(s_long)
    else:
        for i in range(len(long) - len(short) + 1):
            s_long = set(long[i:i+len(short)])
            if s_short == s_long:
                return True
    return False


import random, string
# assert ana_str_str('car', 'race') == True
# assert ana_str_str('nod', 'done') == True
# assert ana_str_str('bag', 'grab') == False
huge = ''.join([random.choice(string.ascii_lowercase) for _ in range(10000)]) + 'orchestra'
# huge = 'orchestra'
assert ana_str_str('carthorse', huge) == True


print("Success")