"""
https://edabit.com/challenge/jtN8gQ5KDoqEJ8HMx
"""


def nom_nom(lst: list) -> list:
    ans = []
    j = 0
    for i, v in enumerate(lst):
        if i == 0:
            ans.append(v)
        elif lst[i] < ans[j]:
            ans[j] += v
        else:
            ans.append(v)
            j += 1
    return ans


assert nom_nom([1, 2, 3]) == [1, 2, 3]
assert nom_nom([2, 1, 3]) == [3, 3]
assert nom_nom([8, 5, 9]) == [22]
assert nom_nom([5, 3, 7]) == [15]
assert nom_nom([5, 3, 9]) == [8, 9]
assert nom_nom([6, 5, 6, 100]) == [17, 100]

print('Success')