"""
https://edabit.com/challenge/55f9SDtxuLgSaJdcK
"""

from collections import deque

def balanced_word(word: str) -> bool:
    d = deque(word)
    left, right = 0, 0
    while len(d) > 1:
        left += ord(d.popleft())
        right += ord(d.pop())
    return left == right


assert balanced_word('at') == False
assert balanced_word('forgetful') == False
assert balanced_word('vegetation') == True
assert balanced_word('disillusioned') == False
print('Success')