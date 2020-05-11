"""
https://edabit.com/challenge/N7zMhraJLCEMsmeTW
"""


def min_swaps(txt: str) -> int:
    f = ''.join('1' if i % 2 == 0 else '0' for i in range(len(txt)))
    s = ''.join('0' if i % 2 == 0 else '1' for i in range(len(txt)))
    f1, s1 = 0, 0
    for i in range(len(txt)):
        if txt[i] == f[i]:
            f1 += 1
        if txt[i] == s[i]:
            s1 += 1
    return min(f1, s1)


assert min_swaps("010010111") == 4
assert min_swaps("010101010") == 0
assert min_swaps("101010100") == 1
assert min_swaps("101010000") == 2
assert min_swaps("101000000") == 3
assert min_swaps("10001") == 1
assert min_swaps("10010") == 2

print('Success')