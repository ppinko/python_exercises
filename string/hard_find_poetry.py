"""
https://edabit.com/challenge/CD2fqbytBuXrbqJkL
"""

from collections import Counter

def can_build(base: str, txt: str) -> bool:
    without_spaces = ''.join(i for i in base if not i.isspace())
    c1, c2 = Counter(without_spaces), Counter(txt)
    return all(True if v <= c2.get(k, 0) else False for k, v in c1.items())


""" Alternative solution """


def can_build2(txt1, txt2):
    return all(txt2.count(i) >= txt1.count(i) for i in set(txt1) if i.isalpha())



assert can_build("got 2 go" , "go go go 2 today") == True
assert can_build("for an angel" , "angel forest nymph awaken") == True
assert can_build("sit on top" , "its a moo point") == True
assert can_build("solar to oven" , "love desolate rose thorn") == True
assert can_build("gate im in" , "magnetizing") == True
assert can_build("moreso" , "mount rushmore") == True
assert can_build("dool" , "ken doll") == False

print('Success')