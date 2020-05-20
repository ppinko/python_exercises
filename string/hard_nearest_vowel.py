"""
https://edabit.com/challenge/ZJGBGyZRNrbNtXJok
"""


import string


def nearest_vowel(s):
    letters = string.ascii_letters
    vowels = {'a', 'u', 'e', 'i','o'}
    i,j = letters.index(s), letters.index(s)
    i -= 1
    j += 1
    if s in vowels:
        return s
    while True:
        if i >= 0:
            if letters[i] in vowels:
                return letters[i]
            i -= 1
        if j <= len(letters) - 1:
            if letters[j] in vowels:
                return letters[j]
            j += 1


assert nearest_vowel('a') == 'a'
assert nearest_vowel('b') == 'a'
assert nearest_vowel('c') == 'a'
assert nearest_vowel('d') == 'e'
assert nearest_vowel('e') == 'e'
assert nearest_vowel('f') == 'e'
assert nearest_vowel('g') == 'e'
assert nearest_vowel('h') == 'i'
assert nearest_vowel('i') == 'i'
assert nearest_vowel('j') == 'i'
assert nearest_vowel('k') == 'i'
assert nearest_vowel('l') == 'i'
assert nearest_vowel('m') == 'o'
assert nearest_vowel('n') == 'o'
assert nearest_vowel('o') == 'o'
assert nearest_vowel('p') == 'o'
assert nearest_vowel('q') == 'o'
assert nearest_vowel('r') == 'o'
assert nearest_vowel('s') == 'u'
assert nearest_vowel('t') == 'u'
assert nearest_vowel('u') == 'u'
assert nearest_vowel('v') == 'u'
assert nearest_vowel('w') == 'u'
assert nearest_vowel('x') == 'u'
assert nearest_vowel('y') == 'u'
assert nearest_vowel('z') == 'u'

print('Success')