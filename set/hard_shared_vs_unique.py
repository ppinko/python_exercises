"""
https://edabit.com/challenge/GaJkMnuHLuPmXZK7h
"""


def letters(s1, s2):
    set1, set2 = set(s1), set(s2)
    ans1 = ''.join(sorted(set1.intersection(set2)))
    ans2 = ''.join(sorted(set1.difference(set2)))
    ans3 = ''.join(sorted(set2.difference(set1)))
    return [ans1, ans2, ans3]


" Alternative solution "
def letters(word1, word2):
	s1, s2 = set(word1), set(word2)
	return [''.join(sorted(i)) for i in [s1&s2, s1-s2, s2-s1]]


assert letters("sharp", "soap") == ["aps", "hr", "o"]
assert letters("board", "bored") == ["bdor", "a", "e"]
assert letters("happiness", "envelope") == ["enp", "ahis", "lov"]
assert letters("match", "ham") == ["ahm", "ct", ""]
assert letters("kerfuffle", "fluffy") == ["flu", "ekr", "y"]
print('Success')