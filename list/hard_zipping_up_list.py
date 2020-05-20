"""
https://edabit.com/challenge/7NCfAsF2Y4wamHvHx
"""


def zipper(A, B):
    if A == B:
        return True
    elif A[-1] != B[-1]:
        return False
    i = -1
    while A[i] == B[i]:
        i -= 1
    return [len(A) + i, len(B) + i]


assert zipper([5, 5, 7, 8, 9, 1, 2], [3, 2, 1, 1, 6, 6, 6, 6, 1, 2]) == [4, 7]
assert zipper([5, 4, 3, 2, 6], [6, 4, 3, 2, 6]) == [0, 0]
assert zipper([5, 4, 3, 2, 7], [6, 4, 3, 2, 6]) == False
assert zipper([1, 5, 4, 3], [9, 8, 7, 5, 4, 3]) == [0, 2]
assert zipper([7, 8, 9, 9, 9], [8, 8, 9, 9, 9, 9, 9]) == [1, 3]
assert zipper([7, 8, 5, 1, 5], [6, 6, 5, 1, 5]) == [1, 1]
assert zipper([6, 6, 5, 1, 5], [6, 6, 5, 1, 5]) == True
assert zipper([1, 1, 2, 6, 6, 5, 1, 5], [7, 8, 9, 4, 4, 6, 6, 5, 1, 5]) == [2, 4]

print('Success')