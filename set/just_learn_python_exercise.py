"""
https://www.justlearnpython.com/docs/exercises/sets-exercises/

Find whether a given string has unique characters,
return True, if duplicates return False
"""

def unique_string(word: str) -> bool:
    return len(set(word)) == len(word)

assert unique_string('pawel') == True
assert unique_string('paulina') == False

print("Success")
