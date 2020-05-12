"""
https://edabit.com/challenge/35JtGyWLFhxGkHNnj
"""


def sel_reverse(lst: list, rev) -> list:
    if len(lst) <= rev:
        return list(reversed(lst))
    elif rev == 0 or rev == 1:
        return lst

    L = []
    for i in range(len(lst) // rev):
        L.extend(list(reversed(lst[rev*i:rev*(i+1)])))

    if len(lst) % rev == 0:
        return L
    else:
        return L + list(reversed(lst[rev*(len(lst) // rev):]))


assert sel_reverse([1, 2, 3, 4, 5, 6], 2) == [2, 1, 4, 3, 6, 5]
assert sel_reverse([2, 4, 6, 8, 10, 12, 14, 16], 3) == [6, 4, 2, 12, 10, 8, 16, 14]
assert sel_reverse([5, 7, 2, 6, 0, 4, 6], 100) == [6, 4, 0, 6, 2, 7, 5]
assert sel_reverse([6, 0, 0, 0, 3, 8, 9, 7, 1], 9) == [1, 7, 9, 8, 3, 0, 0, 0, 6]
assert sel_reverse([12, 54, 67, 34, 65, 34, 33], 0) == [12, 54, 67, 34, 65, 34, 33]
assert sel_reverse([12, 54, 67, 34, 65, 34, 33], 1) == [12, 54, 67, 34, 65, 34, 33]
assert sel_reverse([22, 13, 22, 13, 13, 22, 22, 13], 5) == [13, 13, 22, 13, 22, 13, 22, 22]
assert sel_reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]
assert sel_reverse([1], 2) == [1]
assert sel_reverse([1, 2], 2) == [2, 1]

print('Success')