"""
https://edabit.com/challenge/g6yjSfTpDkX2STnSX
"""


def convert_to_hex(txt: str) -> str:
    return ' '.join(str(hex(ord(c))).lstrip('0x') for c in txt)


assert convert_to_hex("Big Boi") == "42 69 67 20 42 6f 69"
assert convert_to_hex("Marty Poppinson") == "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"
assert convert_to_hex("abcdefghi") == "61 62 63 64 65 66 67 68 69"
assert convert_to_hex("oh dear") == "6f 68 20 64 65 61 72"
assert convert_to_hex("i hate C#") == "69 20 68 61 74 65 20 43 23"
assert convert_to_hex("i love C++ , not really") == "69 20 6c 6f 76 65 20 43 2b 2b 20 2c 20 6e 6f 74 20 72 65 61 6c 6c 79"

print('Success')