"""
https://edabit.com/challenge/4s9kNQFfk4D4Lbm4q
"""

import string

def ABA(s):
    x = string.ascii_uppercase
    if s == 'A':
        return s
    else:
        y = x.find(s)
        return ABA(x[y-1]) + s + ABA(x[y-1])


"""
Alternative solution - not recursive
ord(c) - returns an integer representing the Unicode character.
    input character
chr(i) - returns a character (a string) from an integer
    (represents unicode code point of the character).
    input int
"""

##def ABA(s):
##    letter, res = 'A', 'A'
##    while letter != s:
##        letter = chr(ord(letter) + 1)   # double conversion 
##        res += letter + res[::-1]       # using slicing and reversing backwords
##    return res

print(ABA('C'))

