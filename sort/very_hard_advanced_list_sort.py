"""
https://edabit.com/challenge/6vSZmN66xhMRDX8YT
"""


# def advanced_sort(ls: list) -> list:
#     d = {}
#     for i in ls:
#         d[i] = d.get(i, 0) + 1
#     return [[k] * v for k, v in d.items()]


def advanced_sort(ls: list) -> list:
    d = {}
    lst = []
    for i in ls:
        d[i] = d.get(i, 0) + 1
        if i not in lst:
            lst.append(i)
    return [[i] * d[i] for i in lst]


assert advanced_sort([1,2,1,2]) == [[1,1],[2,2]]
assert advanced_sort([2,1,2,1]) == [[2,2],[1,1]]
assert advanced_sort([3,2,1,3,2,1]) == [[3,3],[2,2],[1,1]]
print('Success')