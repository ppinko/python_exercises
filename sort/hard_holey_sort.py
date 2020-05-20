"""
https://edabit.com/challenge/fsNMnyjMkErQtvpMW
"""

def holey_sort(lst: list) -> list:
    from operator import itemgetter
    s, l = {4, 6, 9, 0}, []
    for i, v in enumerate(lst):
        temp = 0
        for j in str(v):
            if int(j) in s:
                temp += 1
            elif int(j) == 8:
                temp += 2
        l.append((v, temp, i))
    return [i[0] for i in sorted(l, key=itemgetter(1, 2))]

assert holey_sort([44, 4, 444, 4444]) == [4, 44, 444, 4444]
assert holey_sort([100, 888, 1660, 11]) == [11, 100, 1660, 888]
assert holey_sort([8, 121, 41, 66]) == [121, 41, 8, 66]

print("Success")
