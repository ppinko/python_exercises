"""
https://edabit.com/challenge/8WvpPQto44PqNLSqJ
"""


def pad(txt: str) -> str:
    if len(txt) == 140:
        return txt
    elif len(txt) % 2 == 1:
        txt += (140 - len(txt) // 2) * 'lo'
        return txt[:140]
    else:
        txt += ' ' + (140 - len(txt) // 2) * 'lo'
        return txt[:140]


assert pad('Even') == 'Even lololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololol'
assert pad('Odd') == 'Oddlolololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololol'
assert pad("I love the new challenge") == 'I love the new challenge lololololololololololololololololololololololololololololololololololololololololololololololololololololololololol'
assert pad("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus dolor purus, finibus eget magna vel, suscipit semper nibh. Quisque posuere.") == 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus dolor purus, finibus eget magna vel, suscipit semper nibh. Quisque posuere.'

print('Success')