"""
https://edabit.com/challenge/MGALfBAXhXqqdFyqo
"""


def atbash(txt: str) -> str:
    import string
    intab = string.ascii_letters
    outtab = ''.join(sorted(string.ascii_lowercase, reverse=True)) + ''.join(sorted(string.ascii_uppercase, reverse=True))
    transtab = ''.maketrans(intab, outtab)
    return txt.translate(transtab)


assert atbash("abcdefghijklmnopqrstuvwxyz") == "zyxwvutsrqponmlkjihgfedcba"
assert atbash("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "ZYXWVUTSRQPONMLKJIHGFEDCBA"
assert atbash("The word 'atbash' derives from the the first and last 2 letters of the Hebrew alphabet.") == "Gsv dliw 'zgyzhs' wvirevh uiln gsv gsv urihg zmw ozhg 2 ovggvih lu gsv Svyivd zokszyvg."
assert atbash("Vmxibkgrlm zmw wvxibkgrlm ziv rwvmgrxzo uli gsv Zgyzhs xrksvi.") =="Encryption and decryption are identical for the Atbash cipher."
print('Success')