"""
https://edabit.com/challenge/JzBLDzrcGCzDjkk5n
"""

def encrypt(word: str) -> str:
    d = {'a':0, 'e':1, 'o':2, 'u':3}
    return ''.join(str(d[i]) if i in d else i for i in word[::-1]) + 'aca'

""" Alternative solution """
def encrypt(word):
    return word[::-1].translate(str.maketrans('aeou', '0123')) + 'aca'

assert encrypt("karaca") == "0c0r0kaca"
assert encrypt("burak") == "k0r3baca"
assert encrypt("banana") == "0n0n0baca"

print("Success")
