"""
https://edabit.com/challenge/AGgQTPNy6G5cxz4KK
"""


def binary_to_text(txt: str) -> str:
    return ''.join(chr(int(txt[8*i: 8*(i+1)], 2)) for i in range(len(txt) // 8))


assert binary_to_text("01110100011110010111000001100101011100110110001101110010011010010111000001110100") == "typescript"
assert binary_to_text("01101110011011110110010001100101") == "node"
assert binary_to_text("0111001001100101011000010110001101110100") == "react"
assert binary_to_text("01101010011000010111011001100001") == "java"
assert binary_to_text("011010110110111101110100011011000110100101101110") == "kotlin"
assert binary_to_text("011100000111100101110100011010000110111101101110") == "python"
assert binary_to_text("01101000011000010111001101101011011001010110110001101100") == "haskell"

print('Success')