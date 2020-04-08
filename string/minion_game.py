"""
https://www.hackerrank.com/challenges/the-minion-game/problem
"""

def minion_game(s):
    import string
    s = s.lower()
    vowels = 'aeiou'
    not_vowels = ''
    for i in string.ascii_lowercase:
        if i not in vowels:
            not_vowels += i

    word_vowels, word_nvowels = [], []
    for i in s:
        if i in vowels:
            word_vowels.append(i)
        else:
            word_nvowels.append(i)

    count_nv = 0
    x = 0
    for v in word_nvowels:
        y = s.index(v, x)
        count_nv += len(s) - y
        x = y + 1

    count_v = 0
    x = 0
    for v in word_vowels:
        y = s.index(v, x)
        count_v += len(s) - y
        x = y + 1

    if count_nv > count_v:
        print("Stuart {0}".format(count_nv))
    elif count_nv < count_v:
        print("Kevin {0}".format(count_v)) 
    else:
        print("Draw")      

minion_game("banana")