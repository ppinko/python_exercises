"""
https://edabit.com/challenge/7AQgJookgCdbom2Zd
"""


def pig_latin(txt: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    translated, temp = '', ''
    for i, v in enumerate(txt):
        if v.isalpha():
            temp += v
        else:
            capitalized = False
            if temp[0].isupper():
                capitalized = True
            temp = temp.lower()
            if temp[0] in vowels:
                temp = temp + 'way'
            else:
                temp = temp[1:] + temp[0] + 'ay'
            if capitalized:
                temp = temp.capitalize()
            translated += temp + v
            temp = ''
    return translated


assert pig_latin("Cats are great pets.") == "Atscay areway reatgay etspay."
assert pig_latin("Tom got a small piece of pie.") == "Omtay otgay away mallsay iecepay ofway iepay."
assert pig_latin("He told us a very exciting tale.") == "Ehay oldtay usway away eryvay excitingway aletay."
assert pig_latin("A diamond is not enough.") == "Away iamondday isway otnay enoughway."
assert pig_latin("Hurry!") == "Urryhay!"

print('Success')