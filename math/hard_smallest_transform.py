"""
https://edabit.com/challenge/gSXYqtEFxLgQxoHvt
"""

def smallest_transform(num):
    s_min, s_max = 10, -1
    k = str(num)
    l = len(k)
    for i in str(num):
        if int(i) > s_max:
            s_max = int(i)
        if int(i) < s_min:
            s_min = int(i)
    trans_min = 1000000
    for i in range(s_min, s_max + 1):
        temp = str(i) * l
        changes = 0
        for a, b in zip(k, temp):
            changes += abs(int(a)-int(b))
        if changes < trans_min:
            trans_min = changes
    return trans_min

assert smallest_transform(399) == 6
assert smallest_transform(1234) == 4
assert smallest_transform(153) == 4

print("Success")
