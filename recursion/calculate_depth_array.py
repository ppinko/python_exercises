"""
https://edabit.com/challenge/cpuah2wBP7t6aStSb
"""

def depth(lst):
    count = 0
    maks = 0
    for i in lst:
        count += 1
        if type(i) == list:
            count += depth(i)
        if count > maks:
            maks = count
        count = 0
    return maks

print(depth([1, 2, 3, 4]) == 1)
print(depth([1, [2, 3, 4]]) == 2)
print(depth([1, [2, [3, 4]]]) == 3)
