"""
https://edabit.com/challenge/QyKRBtaMDWofm5D3u
"""


def rgb_to_hex(txt: str):
    ans = '#'
    t = txt[4:-1].split(', ')
    for i in (t):
        temp = str(hex(int(i)))[2:]
        if len(temp) == 2:
            ans += temp
        else:
            ans += '0' + temp
    return ans


assert rgb_to_hex("rgb(0, 128, 192)") == "#0080c0"
assert rgb_to_hex("rgb(45, 255, 192)") == "#2dffc0"
assert rgb_to_hex("rgb(255, 255, 255)") == "#ffffff"
assert rgb_to_hex("rgb(192, 192, 192)") == "#c0c0c0"
assert rgb_to_hex("rgb(255, 0, 0)") == "#ff0000"
assert rgb_to_hex("rgb(0, 0, 255)") == "#0000ff"
assert rgb_to_hex("rgb(0, 0, 0)") == "#000000"

print('Success')