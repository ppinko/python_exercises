"""
https://edabit.com/challenge/qujNfKFH9JkpwzuLt
"""


def first_index(hex_txt, needle):
    word = ''.join((chr(int(i, 16)) for i in hex_txt.split()))
    return word.find(needle)


assert first_index("68 65 6c 6c 6f 20 77 6f 72 6c 64", "world") == 6
assert first_index("47 6f 6f 64 62 79 65 20 77 6f 72 6c 64", "world") == 8
assert first_index("74 68 65 20 6e 65 65 64 6c 65 20 69 73 20 74 6f 20 62 65 20 66 6f 75 6e 64", "needle") == 4
assert first_index("a3 24 25 2d 2d 2d a3 24 20 77 6f 72 6c 64 2d 2d 2d", "world") == 9
assert first_index("42 6f 72 65 64 20 77 6f 72 6c 64", "Bored") == 0

print('Success')