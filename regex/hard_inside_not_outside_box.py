"""
https://edabit.com/challenge/5FTMMxKmkQtuY9KBP
"""


import re


def count(box: list) -> int:
    txt = ''
    for i in box:
        j = re.search(r'#.+#', i)
        if j is not None:
            txt += j.group()
    s, to_discard = set(txt), ['#', ' ']
    for i in to_discard:
        s.discard(i)
    return len(s)


assert count(["??????", "?####?", "?#&!#?", "@#^Z#?", "$####?"]) == 4
assert count(["??????","?####?","?#ZZ#?","@#ZZ#?","$####?", "AAAAAA"]) == 1
assert count(["??????","?####?", "?#  #?", "@#  #?", "$####?", "AAAAAA"]) == 0
assert count(["??????Z", "Z?####?V", "$?#  #?X", "$@#BA#?P", "$T####?T", "ZAAAAAAT"]) == 2
assert count(["??????Z", "Z?####?V", "$?#BB#?X", "$@#BA#?P","$T####?T","ZAAAAAAT"]) == 2
assert count(["!!Z", "###", "#B#", "#B#", "###"]) == 1
assert count(["!!Z", "###", "#B#", "# #", "###"]) == 1
assert count(["AAAAA", "AAA##", "AAA##", "AAAAA", "AAAAA"]) == 0
assert count(["AAAAAAA", "AAA###A", "AAA#!#A", "AAA###A", "AAAAAAA"]) == 1
assert count(["#AAAAAABC", "AAA#####C", "ZAA#!%@#C", "AAA#####C", "#AAAAAABC"]) == 3

print("Success")