"""
https://edabit.com/challenge/Ddmh9KYg7xA4m9uE7
"""


import re


def convert_binary(txt: str) -> str:
    first_step = re.sub(r'[a-m]', '0', txt, flags=re.IGNORECASE)
    return re.sub(r'[n-z]', '1', first_step, flags=re.IGNORECASE)


assert convert_binary("house") == "01110"
assert convert_binary("excLAIM") == "0100000"
assert convert_binary("moon") == "0111"
assert convert_binary("MOOn") == "0111"
assert convert_binary("topsyTurvy") == "1111111111"

print('Success')