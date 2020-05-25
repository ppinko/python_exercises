"""
https://edabit.com/challenge/XKSwuu4ddzBvkXjvf
"""


import math


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def sentence_primeness(txt: str) -> str:
    A = txt.split()
    import string
    lletters, uletters = string.ascii_lowercase, string.ascii_uppercase
    removed_punc = ''.join(i for i in txt if i.isalpha() or i.isdigit() or i.isspace())
    L = removed_punc.split()
    K = []
    for i in L:
        tot = 0
        for j in i:
            if j in lletters:
                tot += 1 + lletters.index(j)
            elif j in uletters:
                tot += 1 + uletters.index(j)
            elif j.isdigit():
                tot += int(j)
        K.append(tot)
    total = sum(K)
    if is_prime(total):
        return "Prime Sentence"
    for i in range(len(K)):
        if is_prime(total - K[i]):
            return "Almost Prime Sentence ({0})".format(L[i])
    return "Composite Sentence"


assert sentence_primeness("Help me!") == "Prime Sentence"
assert sentence_primeness("42 is THE aNsWeR...") == "Almost Prime Sentence (aNsWeR)"
assert sentence_primeness("Did you Smoke?") == "Composite Sentence"
assert sentence_primeness("She SellS SeaShellS by the SeaShore") == "Prime Sentence"
assert sentence_primeness("Lorem. Ipsum. Dolor. Sit. Amet.") == "Almost Prime Sentence (Lorem)"
assert sentence_primeness("three fASt hUNgry aniMALs -aNd- 3 slow faTTy kiDS") == "Almost Prime Sentence (aniMALs)"
assert sentence_primeness("This is a 'Prime' Sentence") == "Composite Sentence"
assert sentence_primeness("this is a composite sentence") == "Almost Prime Sentence (this)"
assert sentence_primeness("Primes, PRIMES EVERYWHERE!") == "Composite Sentence"
assert sentence_primeness("10 test cases are enough, this is the last one!") == "Prime Sentence"

print('Success')