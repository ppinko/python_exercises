"""
https://edabit.com/challenge/nb836onw9bek4FPDt

Same On Both Ends

Given a sentence, return the number of words which have the same first and last letter.

count_same_ends('Pop! goes the balloon') ➞ 1
count_same_ends('And the crowd goes wild!') ➞ 0
count_same_ends('No I am not in a gang.') ➞ 1
"""


def count_same_ends(txt: str) -> int:
    without_punctuation = ''.join(i.lower() for i in txt if i.isalpha() or i.isspace())
    return sum(1 if len(i) > 1 and i[0] == i[-1] else 0 for i in without_punctuation.split())


""" Alternative solution """

import re

def count_same_ends(txt):
	return sum(i[0] == i[-1] for i in re.findall(r'[A-Za-z]{2,}', txt.lower()))


assert count_same_ends('Pop! the balloon!') == 1
assert count_same_ends('My mom is not a nun.') == 2
assert count_same_ends('A fine morning') == 0
assert count_same_ends('And the crowd goes wild!') == 0
assert count_same_ends('No I am not in a gang.') == 1
assert count_same_ends('Taste the difference') == 0

print('Success')