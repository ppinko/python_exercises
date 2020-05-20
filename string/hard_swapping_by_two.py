"""
https://edabit.com/challenge/bdsWZ29zJfJ2Roymv
"""


def swap_two(txt: str) -> str:
    if len(txt) // 4 == 0:
        return txt
    swapped = ''
    for i in range(len(txt) // 4):
        swapped += txt[4*i+2: 4*i+4] + txt[4*i:4*i+2]
    swapped += txt[4*(len(txt) // 4):]
    return swapped


assert swap_two("ABCDEFGH") == "CDABGHEF"
assert swap_two("AABBCCDDEEFF") == "BBAADDCCFFEE"
assert swap_two("oompaloompa") == "mpooooalmpa"
assert swap_two("munchkins") == "ncmuinhks"
assert swap_two("FFGGHHI") == "GGFFHHI"
assert swap_two("FFG") == "FFG"
assert swap_two("") == ""

print('Success')