"""
https://edabit.com/challenge/gQgFJiNy8ZDCqaZb4
"""


def overlap(s1: str, s2: str) -> str:
    if s1 == s2:
        return s1
    for i in range(len(s1)):
        if s2.find(s1[i:]) == 0:
            return s1 + s2.replace(s1[i:], '')
    return s1 + s2


assert overlap('sweden', 'denmark') == 'swedenmark'
assert overlap('edabit', 'iterate') == 'edabiterate'
assert overlap('honey', 'milk') == 'honeymilk'
assert overlap('dodge', 'dodge') == 'dodge'
assert overlap('leave', 'eavesdrop') == 'leavesdrop'
print('Success')