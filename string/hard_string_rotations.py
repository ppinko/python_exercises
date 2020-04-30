"""
https://edabit.com/challenge/9RvRFtg67AkYiy3vN
"""


def left_rotations(txt: str) -> list:
    return [txt[i:] + txt[:i] for i in range(len(txt))]


def right_rotations(txt: str) -> list:
    temp = txt * 2
    return [temp[len(txt) - i: 2* len(txt) - i] for i in range(len(txt))]


assert left_rotations("abc") == ["abc", "bca", "cab"]
assert left_rotations("abcdef") == ["abcdef", "bcdefa", "cdefab", "defabc", "efabcd", "fabcde"]
assert left_rotations("himalaya") == ["himalaya", "imalayah", "malayahi", "alayahim", "layahima", "ayahimal", "yahimala", "ahimalay"]
assert left_rotations("aab") == ["aab", "aba","baa"]
assert right_rotations("abc") == ["abc", "cab", "bca"]
assert right_rotations("abcdef") == ["abcdef", "fabcde", "efabcd", "defabc", "cdefab", "bcdefa"]
assert right_rotations("himalaya") == ["himalaya", "ahimalay", "yahimala", "ayahimal", "layahima", "alayahim", "malayahi", "imalayah"]

print('Success')