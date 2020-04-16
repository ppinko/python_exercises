"""
https://edabit.com/challenge/mFtJNuH6rveGXtiJd
"""

def matryoshka(lst):
    sub_list = [ (min(i), max(i)) for i in lst ]
    min_set, max_set = set(), set()
    for i, j in sub_list:
        min_set.add(i)
        max_set.add(j)
    if len(min_set) != len(lst) or len(max_set) != len(lst):
        return False
    return sorted(sub_list, key = lambda x: x[0]) == sorted(sub_list, key = lambda x: x[1], reverse=True)

"""
Alternative solution
"""

def matryoshka(lst):
    lst.sort(key=min)
    return all(min(a) < min(b) and max(a) > max(b) for a, b in zip(lst, lst[1:]))


assert matryoshka([[4, 5], [2, 6], [1, 9], [-5, 10, 11]]) == True
assert matryoshka([[1, 2, 3, 4, 5, 6, 7, 8], [2, 3, 4, 5, 6, 7], [3, 4, 5, 6], [4, 5]]) == True
assert matryoshka([[3, 3], [4, 4], [5, 5, 5]]) == False

print("Success")
