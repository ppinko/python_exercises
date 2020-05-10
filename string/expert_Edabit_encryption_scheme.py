"""
https://edabit.com/challenge/9cY7ymbp5mtrKdxyR
"""


import math


def encryption(txt: str) -> str:
    txt = ''.join(txt.split())
    rows, cols = math.floor(math.sqrt(len(txt))), math.ceil(math.sqrt(len(txt)))
    if rows * cols < len(txt):
        rows += 1
    L = [txt[cols * i: cols *(i+1)] for i in range(rows)]
    K = [i if len(i) == len(L[0]) else i + ' ' * (len(L[0]) - len(i)) for i in L]
    return ' '.join(''.join(i).rstrip() for i in zip(*K))


assert encryption("haveaniceday") == "hae and via ecy"
assert encryption("feedthedog") == "fto ehg ee dd"
assert encryption("chillout") == "clu hlt io"
assert encryption("A Fool and His Money Are Soon Parted.") == "Anoea FdnSr oHeot oiyoe lsAnd aMrP."
assert encryption("One should not worry over things that have already happened and that cannot be changed.") == "Onvtlphb. noehreae etraentc swttaech hohhddaa oriayann urnvhnng lygeadoe dosapttd"
assert encryption("Back to Square One is a popular saying that means a person has to start over, similar to: back to the drawing board.") == "Brpgatroea aeutpo,:dr cOlhessbrd knaartiaa. tertsamcw oismoriki Ssaentltn qayahoaog upinavrtb aonssetho"

print('Success')