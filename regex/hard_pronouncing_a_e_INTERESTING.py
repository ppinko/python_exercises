"""
https://edabit.com/challenge/vZDgbWkcevrwzLh8W
"""


import re


def pronounce_the_a_e(txt: str) -> str:
    return ' '.join(re.sub(r'a(.+)e', r'ay\1', i) for i in txt.split())


assert pronounce_the_a_e("i want to bake a cake") == "i want to bayk a cayk"
assert pronounce_the_a_e("cinnamon flakes") == "cinnamon flayks"
assert pronounce_the_a_e("bravely escape and inflate") == "brayvly escayp and inflayt"
assert pronounce_the_a_e("do not waste the flame") == "do not wayst the flaym"
assert pronounce_the_a_e("taste the paste") == "tayst the payst"
assert pronounce_the_a_e("face it and race it") == "fayc it and rayc it"
assert pronounce_the_a_e("chase the plane to the cranes") == "chays the playn to the crayns"
assert pronounce_the_a_e("the famed name and shame") == "the faymd naym and shaym"
assert pronounce_the_a_e("he chases the cases he makes") == "he chayss the cayss he mayks"

print("Success")