"""
https://edabit.com/challenge/kgMEhkNNjRmBTAAPz
"""

import re


def remove_special_characters(txt):
    return re.sub('[^\s\-\w_]', '', txt)


assert remove_special_characters("The quick brown fox!") == "The quick brown fox"
assert remove_special_characters("%fd76$fd(-)6GvKlO.") == "fd76fd-6GvKlO"
assert remove_special_characters("D0n$c sed 0di0 du1") == "D0nc sed 0di0 du1"
assert remove_special_characters("cat_pic.jpeg") == "cat_picjpeg"
assert remove_special_characters("519-555-8093") == "519-555-8093"
assert remove_special_characters("h-d+=rf[]_{}<>.`~!@#$%^&*(|)") == "h-drf_"

print('Success')
