"""
https://edabit.com/challenge/dZpAwipzG3w4NYwDE
"""

from collections import Counter

def highest_pair(lst: list):
    rank = list(str(i) for i in range(0, 11)) + ['J', 'Q', 'K', 'A']
    c = Counter(lst)
    max_pair = '0'
    for k, v in c.items():
        if v >= 2 and rank.index(k) > rank.index(max_pair):
            max_pair = k
    if max_pair == '0':
        return False
    else:
        return [True, max_pair]


assert highest_pair(['A', 'A', 'K', 'K', '3']) == [True, 'A']
assert highest_pair(['A', 'K', 'Q', 'J', '10']) == False
assert highest_pair(['A', 'K', 'K', 'K', 'Q']) == [True, 'K']
assert highest_pair(['A', '3', '3', '4', '4']) == [True, '4']
assert highest_pair(['A', 'K', 'Q', 'Q', '5']) == [True, 'Q']

print('Success')

