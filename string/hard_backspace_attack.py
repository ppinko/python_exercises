"""
https://edabit.com/challenge/c5aZLMAvq3ctPkBcD
"""


def erase(txt: str) -> str:
    L = []
    for i in txt:
        if i != '#':
            L.append(i)
        elif len(L) > 0:
            L.pop()
    return ''.join(L)


assert erase("he##l#hel#llo") == "hello"
assert erase("major# spar##ks") == "majo spks" 
assert erase("si###t boy") == "t boy"
assert erase("motion #sick") == "motionsick"
assert erase("m#oti#o#n sick##ne#ss##") == "otn sin"
assert erase("courz#i#age") == "courage"
assert erase("aris##### c#r#ti#c") == " tc"
assert erase("beauty##") == "beau"
assert erase("beauty#") == "beaut"
assert erase("b#") == ""
assert erase("####") == ""

print('Success')