"""
https://edabit.com/challenge/zeHgBRuYyxp9TFry4
"""


from collections import Counter


def can_form(lst: list) -> bool:
    L = sorted(lst, key=len, reverse=True)
    c = Counter(L[0])
    for word in L[1:]:
        d = Counter(word)
        for key, value in d.items():
            if value > c.get(key, 0):
                return False
    return True


assert can_form(["mast", "manifest", "met", "fan"]) == True
assert can_form(["may", "master", "same", "reams"]) == False
assert can_form(["may", "same", "reams", "mastery"]) == True
assert can_form(["kerfuffle", "fluke", "fluff", "ruffle", ]) == True
assert can_form(["monument", "momento", "moment", "tome"]) == False
assert can_form(["shape", "shapers", "raps", "saps"]) == True

print("Success")