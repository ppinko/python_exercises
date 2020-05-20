"""
https://edabit.com/challenge/RJySHrDkBjSAj5gzq
"""


def perm(n):
    tot = 1
    while n > 1:
        tot *= n
        n -= 1
    return tot


def nespers(lst: list) -> int:
    if all(True if type(i) == int else False for i in lst):
        return perm(len(lst))
    else:
        tot = perm(len(lst))
        for i in lst:
            if type(i) == list:
                tot *= nespers(i)
    return tot


assert nespers([1,2,3]) == 6
assert nespers([1,2,3,4,5]) == 120
assert nespers([1,[2,3]]) == 4
assert nespers([[1,7], 3, [2,4,5,6]]) == 288
assert nespers([1,[3,[2,[5,4]]]]) == 16
assert nespers([[],1,[3,[2,[5,4]]]]) == 48
assert nespers([6,[],1,[3,[2,[5,[],4]]]]) == 576
assert nespers([[],[2],[3,6],[4,7,8,9],[5,[11,12,[13,14]]]]) == 138240

print('Success')