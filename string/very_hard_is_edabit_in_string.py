"""
https://edabit.com/challenge/ZWEnJEy2DoJF9Ejqa
"""


def edabit_in_string(txt: str) -> str:
    j = 0
    for i in 'edabit':
        x = txt.find(i, j)
        if x == -1:
            return 'NO'
        else:
            j = x
    return 'YES'


assert edabit_in_string("eddaaabt") == "NO"
assert edabit_in_string("edwardisabletodoittoo") == "YES"
assert edabit_in_string("abecdfghijklmnopqrstuvwxyz") == "NO"
print('Success')