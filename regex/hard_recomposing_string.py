"""
https://edabit.com/challenge/8J5dFWruwZ6bboBTh
"""


import re


def recompose(txt: str) -> str:
    linked = ''.join(i[::-1] for i in re.findall(r"[iaeou]+|[^iaeou]+", txt, flags=re.IGNORECASE))
    return ' '.join(re.findall(r"[A-Z][a-z]+", linked))


assert recompose("KiKdaola") == "Kid Koala"
assert recompose("BaosdrOCfanada") == "Boards Of Canada"
assert recompose("hCemicarBlohtesr") == "Chemical Brothers"
assert recompose("MuosOeMnasr") == "Mouse On Mars"
assert recompose("AhpewTxin") == "Aphex Twin"
assert recompose("MassivAettakc") == "Massive Attack"
assert recompose("DeosItOffeYdnuoYaeh") == "Does It Offend You Yeah"
                   
print('Success')