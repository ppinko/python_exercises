"""
https://edabit.com/challenge/C45TKLcGxh8dnbgqM
"""


import string


def caesar_cipher(txt: str, shift: int) -> str:
    r_shift = shift % 26
    lower = string.ascii_lowercase[r_shift:] + string.ascii_lowercase[:r_shift]
    upper = string.ascii_uppercase[r_shift:] + string.ascii_uppercase[:r_shift]
    ciphered = lower + upper
    cipher = {k: v for k, v in zip(string.ascii_letters, ciphered)}
    return ''.join(cipher[i] if i in cipher else i for i in txt)


assert caesar_cipher("middle-Outz", 2) == "okffng-Qwvb"
assert caesar_cipher("Always-Look-on-the-Bright-Side-of-Life", 5) == "Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj"
assert caesar_cipher("A friend in need is a friend indeed", 20) == "U zlcyhx ch hyyx cm u zlcyhx chxyyx"
assert caesar_cipher("A Fool and His Money Are Soon Parted.", 27) == "B Gppm boe Ijt Npofz Bsf Tppo Qbsufe."
assert caesar_cipher("One should not worry over things that have already happened and that cannot be changed.", 49) == "Lkb pelria klq tloov lsbo qefkdp qexq exsb xiobxav exmmbkba xka qexq zxkklq yb zexkdba."
assert caesar_cipher("Back to Square One is a popular saying that means a person has to start over, similar to: back to the drawing board.", 126) == "Xwyg pk Omqwna Kja eo w lklqhwn owuejc pdwp iawjo w lanokj dwo pk opwnp kran, oeiehwn pk: xwyg pk pda znwsejc xkwnz."

print('Success')