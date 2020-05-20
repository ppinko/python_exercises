"""
https://edabit.com/challenge/pTtzfmR2z7jqYXJDf
"""


from collections import Counter


def possible_palindrome(txt: str) -> bool:
    return sum(1 for i in Counter(txt).values() if i % 2 == 1) <= 1


assert possible_palindrome("acabbaa") == True
assert possible_palindrome("aacbdbc") == True
assert possible_palindrome("aacbdb") == False
assert possible_palindrome("abacbb") == False
assert possible_palindrome("abb") == True
assert possible_palindrome("bbb") == True
print('Success')