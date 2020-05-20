"""
https://edabit.com/challenge/v2r4rY7qv4ejc4SeQ
"""


def pigLatin(word):
    vowels = {'a','e','i','o','u'}
    if word[0] in vowels:
        return word + 'way'
    else:
        for i, v in enumerate(word):
            if v in vowels:
                return word[i:] + word[:i] + 'ay'
            

assert pigLatin('attack') == 'attackway'
assert pigLatin('defend') == 'efendday'
assert pigLatin('on') == 'onway'

print("Success")
