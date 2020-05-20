"""
https://edabit.com/challenge/2EK5GMSqSEv436Tc8
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
    return min(f1, s1) // 2


assert min_swaps("10") == 0
assert min_swaps("0101") == 0
assert min_swaps("101010") == 0
assert min_swaps("1100") == 1
assert min_swaps("111000") == 1
assert min_swaps("100101") == 1
assert min_swaps("100011") == 1
assert min_swaps("010110") == 1
assert min_swaps("10001110") == 1
assert min_swaps("11001100") == 2
assert min_swaps("11110000") == 2
assert min_swaps("1001001011") == 2
assert min_swaps("100100100111") == 3
assert min_swaps("101100000111") == 3
assert min_swaps("111000000111") == 3
assert min_swaps("111111000000") == 3
assert min_swaps("11000000011111") == 3
assert min_swaps("11111110000000") == 3
assert min_swaps("1111111100000000") == 4

print('Success')