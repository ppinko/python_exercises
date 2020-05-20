"""
https://edabit.com/challenge/sDvjdcBrbHoXKvDsZ
"""

def anagram(name: str, ls: list) -> bool:
    l1 = [i.lower() for i in name if i != ' ']
    l1.sort()
    l2 = [i.lower() for j in ls for i in j]
    l2.sort()
    return l1 == l2

assert anagram("Justin Bieber", ["injures", "ebb", "it"]) == True
assert anagram("Natalie Portman", ["ornamental", "pita"]) == True
assert anagram("Emma Watson", ["mows", "meant", "a"]) == True

print("success")
