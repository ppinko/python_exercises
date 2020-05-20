"""
https://edabit.com/challenge/FeNrBCG9rSdNeJTuX
"""


def max_possible(n1, n2):
    new_str = ''
    j = 0
    back = ''.join(sorted(str(n2), reverse=True))
    for i in str(n1):
        if j < len(back) and back[j] > i:
            new_str += back[j]
            j += 1
        else:
            new_str += i
    return int(new_str)


assert max_possible(9328, 456) == 9658
assert max_possible(523, 76) == 763
assert max_possible(9132, 5564) == 9655
assert max_possible(8732, 91255) == 9755
print('Success')