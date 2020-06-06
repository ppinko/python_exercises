"""
https://edabit.com/challenge/EHzL3v25wYp7E4AFC
"""


from collections import Counter


def can_build(text: str, note: str) -> bool:
    text_fr_dict, note_fr_dict = Counter(text), Counter(note)
    return all(True if k in text_fr_dict and text_fr_dict[k] >= v else False
               for k, v in note_fr_dict.items())


assert can_build("aPPleAL", "PAL") == True
assert can_build("OAT", "OAT") == True
assert can_build("maybelLINE", "maybe") == True
assert can_build("topsh", "shop") == True
assert can_build("topshSHP", "SHoP") == True
assert can_build("DAISIES", "SAID") == True
assert can_build("ToporP", "porT") == True
assert can_build("PoTluCK", "PuCK") == True
assert can_build("pATS", "p") == True
assert can_build("blah", "") == True

assert can_build("aPPleAL", "apple") == False
assert can_build("shortCAKE", "cakey") == False
assert can_build("maybeLINE", "lINE") == False
assert can_build("teaPOT", "lINE") == False
assert can_build("", "a") == False
assert can_build("a", "aA") == False
assert can_build("a", "A") == False
assert can_build("AAAAAA", "AAAAAAa") == False
assert can_build("apple", "appleY") == False
assert can_build("xxYYzZ", "zzZxYxY") == False
assert can_build("abCD", "aBCD") == False

print('Success')