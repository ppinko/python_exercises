"""
https://edabit.com/challenge/ZipMJJocMyozDZ6iP
"""


def group(lst, size):
    # Asses group division
    if len(lst) % size == 0:
        k = len(lst) // size
    elif len(lst) % size < size - 1 and len(lst) % (size - 1) == 0:
        size = size - 1
        k = len(lst) // size
    else:
        k = 1 + len(lst) // size
    print('size =', size, ' k = ', k)
    res = []
    for i in range(k):
        sub_list = []
        for j in range(i, len(lst), k):
            sub_list.append(lst[j])
        res.append(sub_list)
    return res


assert group([1, 2, 3, 4], 2) == [[1, 3], [2, 4]]
assert group([1, 2, 3, 4, 5, 6, 7], 4) == [[1, 3, 5, 7], [2, 4, 6]]
assert group([1, 2, 3, 4, 5], 1) == [[1], [2], [3], [4], [5]]
assert group([1, 2, 3, 4, 5, 6], 4) == [[1, 3, 5], [2, 4, 6]]

print("Success")
