"""
https://edabit.com/challenge/7weXDcQiwtQksC9Eu
"""


def rec_flatten(lst: list, res: list):
    for i in lst:
        if type(i) != list:
            res.append(i)
        else:
            rec_flatten(i, res)
    return res


def flatten_list(lst):
    l = []
    return rec_flatten(lst, l)


""" Alternative solution """


def flatten_list(lst):
    newlist = []
    for element in lst:
        if not type(element) == list:
            newlist.append(element)
        else:
            newlist+=flatten_list(element)
    return newlist


assert flatten_list([1, '2', [3, [4]]]) == [1, '2', 3, 4]
assert flatten_list([1]) == [1]
assert flatten_list([]) == []


print("Success")