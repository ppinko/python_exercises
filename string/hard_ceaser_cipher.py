"""
https://edabit.com/challenge/Es985FEDzEQ2tkM75
"""


def caesar_cipher(txt: str, n: int) -> str:
    import string
    alphabet = string.ascii_lowercase
    ans = ''
    for i in txt:
        if not i.isalpha():
            ans += i
        else:
            j = (alphabet.index(i) + n) % 26
            ans += alphabet[j]
    return ans


assert caesar_cipher("hello world", 1) == "ifmmp xpsme"
assert caesar_cipher("hello world", 26) == "hello world"
assert caesar_cipher("iwxh xh p rwxetg", 11) == "this is a chiper"
assert caesar_cipher("z", 2) == "b"
assert caesar_cipher("fruuhfw", 23) == "correct"
assert caesar_cipher("tfexirkj", 9) == "congrats"

print('Success')