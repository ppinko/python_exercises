"""
https://edabit.com/challenge/eSBCbWrG3PY9YYF7c
"""


def sexagenary(num: int) -> str:
    l1 = ['metal', 'water', 'wood', 'fire', 'earth']
    l2 = ['monkey', 'rooster', 'dog', 'pig', 'rat', 'ox', 'tiger', 'rabbit',\
          'dragon', 'snake', 'horse', 'sheep']
    s1 = l1[(num % 10) // 2]
    s2 = l2[num % 12]
    return s1.title() + ' ' + s2.title()


assert sexagenary(1971) == 'Metal Pig'
assert sexagenary(1927) == 'Fire Rabbit'
assert sexagenary(2017) == 'Fire Rooster'
print('Success')