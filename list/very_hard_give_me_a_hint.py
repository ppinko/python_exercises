"""
https://edabit.com/challenge/vudQZFD64nDWkKz8a
"""


def grant_the_hint(txt: str):
    temp_lst = txt.split()
    max_len = max(len(i) for i in temp_lst)
    ans = []
    for j in range(max_len + 1):
        temp = []
        for i in temp_lst:
            if j == 0:
                temp.append('_' * len(i))
            elif j <= len(i):
                temp.append(i[:j] + '_' * (len(i) - j))
            else:
                temp.append(i)
        ans.append(' '.join(temp))
    return ans


assert grant_the_hint('Mary Queen of Scots') == [
'____ _____ __ _____',
'M___ Q____ o_ S____',
'Ma__ Qu___ of Sc___',
'Mar_ Que__ of Sco__',
'Mary Quee_ of Scot_',
'Mary Queen of Scots'
]


assert grant_the_hint('The Life of Pi') == [
'___ ____ __ __',
'T__ L___ o_ P_',
'Th_ Li__ of Pi',
'The Lif_ of Pi',
'The Life of Pi'
]


assert grant_the_hint('The River Nile') == [
'___ _____ ____',
'T__ R____ N___',
'Th_ Ri___ Ni__',
'The Riv__ Nil_',
'The Rive_ Nile',
'The River Nile'
]


print('Success')