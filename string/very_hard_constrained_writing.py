"""
https://edabit.com/challenge/JmyD5D4KnhzmMPEKz
"""


def constraint(txt):
    letters = [i.lower() for i in txt if i.lower().isalpha()]
    words = txt.split()
    if len(set(letters)) == 26:
        return 'Pangram'
    if len(set(letters)) == len(letters):
        return 'Heterogram'
    if len({i.lower()[0] for i in words}) == 1:
        return 'Tautogram'
    s = set(words[0].lower())
    for i in range(1, len(words)):
        s.intersection_update(words[i].lower())
    if len(s) > 0 or len(words) == 1:
        return 'Transgram'
    return 'Sentence'


assert constraint("The quick brown fox jumps over the lazy dog.") == "Pangram"
assert constraint("The big dwarf only jumps.") == "Heterogram"
assert constraint("Todd told Tom to take the tiny turtles.") == "Tautogram"
assert constraint("A cannibal alligator has attacked an unaware vegan alligator.") == "Transgram"
assert constraint("The unbearable lightness of coding...") == "Sentence"
assert constraint("Pack my box with five dozen liquor jugs.") == "Pangram"
assert constraint("The dog is crazy.") == "Heterogram"
assert constraint("It is indeed included instantly!") == "Tautogram"
assert constraint("Those loops could work without constants sometimes.") == "Transgram"
assert constraint("Sphinx of black quartz == judge my vow.") == "Pangram"
assert constraint("Mind the gap!") == "Heterogram"
assert constraint("Put some more tobacco inside it next time == it's just too strong!") == "Sentence"
assert constraint("Thursdays: the time to teach them the truth.") == "Tautogram"
assert constraint("Would you mind pass me that axe == Eugene?") == "Sentence"
assert constraint("AbCdEfGhIjKlMnOpQrStUvWxYz") == "Pangram"

print('Success')