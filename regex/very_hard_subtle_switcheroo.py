"""
https://edabit.com/challenge/o7u9hqTW5AY3SoZgT
"""


import re


def switcheroo(txt: str) -> str:
    L = []
    for i in txt.split():
        if 'nts' in i:
            L.append(re.sub('nts(?![a-zA-Z])', 'nce', i))
        elif 'nce' in i:
            L.append(re.sub('nce(?![a-zA-Z])', 'nts', i))
        else:
            L.append(i)
    return ' '.join(L)


assert switcheroo("While he rants, I fall into a trance...") == "While he rance, I fall into a trants..."
assert switcheroo("The elephants in France were chased by ants!") == "The elephance in Frants were chased by ance!"
assert switcheroo("Bounced over the fence!") == "Bounced over the fents!"
assert switcheroo("Face") == "Face"
assert switcheroo("Fats") == "Fats"
assert switcheroo("") == ""

print('Success')