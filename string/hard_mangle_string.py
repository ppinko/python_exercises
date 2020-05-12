"""
https://edabit.com/challenge/8WcHytN6EEy3mMycG
"""


import string


def mangle(txt: str) -> str:
    alphabet = string.ascii_lowercase + 'a' + string.ascii_uppercase + 'A'
    s = {'a', 'e', 'i', 'o', 'u'}
    ans = ''
    for i in txt:
        try:
            a = alphabet[alphabet.index(i) + 1]
        except ValueError:
            ans += i
        else:
            if a in s:
                ans += a.upper()
            else:
                ans += a
    return ans


assert mangle("Fun times!") == "GvO Ujnft!"
assert mangle("Omega") == "Pnfhb"
assert mangle("I will never be this young again. Ever. Oh damn... I just got older.") == "J xjmm Ofwfs cf UIjt zpvOh bhbjO. Fwfs. PI EbnO... J kvtU hpU pmEfs."
assert mangle("Should we start class now, or should we wait for everyone to get here?") == "TIpvmE xf tUbsU dmbtt Opx, ps tIpvmE xf xbjU gps fwfszpOf Up hfU Ifsf?"
assert mangle("Check back tomorrow; I will see if the book has arrived.") == "DIfdl cbdl Upnpsspx; J xjmm tff jg UIf cppl Ibt bssjwfE."
assert mangle("The lake is a long way from here.") == "UIf mblf jt b mpOh xbz gspn Ifsf."
assert mangle("It was getting dark, and we weren't there yet.") == "JU xbt hfUUjOh Ebsl, bOE xf xfsfO'U UIfsf zfU."
assert mangle("The mysterious diary records the voice.") == "UIf nztUfsjpvt Ejbsz sfdpsEt UIf wpjdf."
assert mangle("Cats are good pets, for they are clean and are not noisy.") == "DbUt bsf hppE qfUt, gps UIfz bsf dmfbO bOE bsf OpU Opjtz."
assert mangle("abcz") == "bcdA"
assert mangle("ABCZ") == "BCDA"

print('Success')