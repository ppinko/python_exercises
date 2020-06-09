"""
https://edabit.com/challenge/kjJWvK9XtdbEJ2EKe
"""


def sort_array(L: list) -> list:
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j+1] < L[j]:
                temp = L[j+1]
                L[j+1] = L[j]
                L[j] = temp
    return L


assert sort_array([2, -5, 1, 4, 7, 8]) == [-5, 1, 2, 4, 7, 8]
assert sort_array([23, 15, 34, 17, -28]) == [-28, 15, 17, 23, 34]
assert sort_array([38, 57, 45, 18, 47, 39]) == [18, 38, 39, 45, 47, 57]
assert sort_array([26, -1, -45, 74, 20]) == [-45, -1, 20, 26, 74]

print("Success")