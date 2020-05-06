"""
https://edabit.com/challenge/M8hDPzNZdie8aBMcb
"""

def count_substring(txt: str) -> int:
    return sum(txt[i:].count('X') for i,v in enumerate(txt[:-1]) if v == 'A')


assert count_substring('CAXAAYXZA') == 4
assert count_substring('AAXOXXA') == 6
assert count_substring('AXAXAXAXAX') == 15

print('Success')