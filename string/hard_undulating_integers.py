"""
https://edabit.com/challenge/NJw4mENpSaMz3eqh2
"""


def is_undulating(n: int) -> bool:
    return len(str(n)) >= 3 and len(set(str(n))) == 2 and len(set(str(n)[::2])) == 1 \
           and len(set(str(n)[1::2])) == 1


assert is_undulating(12) == False
assert is_undulating(949494) == True
assert is_undulating(494) == True
assert is_undulating(363738) == False
print('Success')