"""
https://edabit.com/challenge/MvgCxPkSgtQ8hQjwx
"""

import re


def remove_vowels(text: str) -> str:
    return re.sub('[aAeEoOiIuU]', '', text)


assert remove_vowels("If Obama resigns from office NOW, thereby doing a great service to the country - I will give him free lifetime golf at any one of my courses!") == "f bm rsgns frm ffc NW, thrby dng  grt srvc t th cntry -  wll gv hm fr lftm glf t ny n f my crss!"
assert remove_vowels("This election is a total sham and a travesty. We are not a democracy!") == "Ths lctn s  ttl shm nd  trvsty. W r nt  dmcrcy!"
assert remove_vowels("I have never seen a thin person drinking Diet Coke.") == " hv nvr sn  thn prsn drnkng Dt Ck."

print('Success')