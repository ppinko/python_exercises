"""
https://edabit.com/challenge/oiHH7qocTyM3JqNf8
"""

"""
First solution using str.translate and ''.maketrans(intab, outtab)
"""

import string

def move(word):
    intab = string.ascii_lowercase
    outtab = intab[1:] + 'a'
    trantab = ''.maketrans(intab, outtab)
    return word.translate(trantab)

"""
Alternative solution - using ord(c) and chr(i)
"""

##def move(word):
##    return ''.join(chr(ord(i) + 1) for i in word) 


print(move("welcome"))
print(move("welcome") == "xfmdpnf")
