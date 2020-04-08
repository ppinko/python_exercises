"""
https://edabit.com/challenge/jwzgYjymYK7Gmro93

get_indices(["a", "a", "b", "a", "b", "a"], "a") ➞ [0, 1, 3, 5]
get_indices([1, 5, 5, 2, 7], 7) ➞ [4]
get_indices([1, 5, 5, 2, 7], 5) ➞ [1, 2]
get_indices([1, 5, 5, 2, 7], 8) ➞ []
"""

def get_indices(lst, el):
    return [ x for x, y in enumerate(lst) if y == el ]

print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
