"""
https://edabit.com/challenge/ojNRprg7fKpWJpj47
"""


def shift_sentence(txt: str) -> str:
    if txt.find(' ') == -1:
        return txt
    l1 = txt.split()
    l2 = l1[:] * 2
    l2 = l2[len(l1) - 1:]
    for i in range(len(l1)):
        if len(l1[i]) > 1:
            l1[i] = l2[i][0] + l1[i][1:]
        else:
            l1[i] = l2[i][0]
    return ' '.join(l1)


assert shift_sentence('create a function') == 'freate c aunction'
assert shift_sentence('it should shift the sentence') == 'st ihould shift she tentence'
assert shift_sentence('the output is not very legible') == 'lhe tutput os iot nery vegible'