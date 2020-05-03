"""
https://edabit.com/challenge/xmyNqzxAgpE47zXEt
"""


def is_alphabetically_sorted(txt: str) -> bool:
    L = ''.join(i for i in txt if i.isalpha() or i.isspace()).split()
    return any(True for i in L if len(i) >= 3 and i.lower() == ''.join(sorted(i.lower())))


assert is_alphabetically_sorted("Paula has a French accent.") == True
assert is_alphabetically_sorted("The biopsy returned negative results.") == True
assert is_alphabetically_sorted("She sells sea shells by the sea shore.") == False
assert is_alphabetically_sorted("She almost reached the top of Mt. Everest.") == True
assert is_alphabetically_sorted("She was happy with how her earring hoops looked.") == True
assert is_alphabetically_sorted("Beth dislikes eating starfruit but enjoys cherries.") == False
assert is_alphabetically_sorted("Elinor is inside on a rainy day sipping hot chocolate.") == True
assert is_alphabetically_sorted("Mara took a photograph.") == False

print('Success')