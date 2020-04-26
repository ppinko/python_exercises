"""
https://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/


Find the longest path in a matrix with given constraints

Given a n*n matrix where all numbers are distinct, find the maximum length path
(starting from any cell) such that all cells along the path are in increasing order
with a difference of 1.

We can move in 4 directions from a given cell (i, j), i.e., we can move to (i+1, j)
or (i, j+1) or (i-1, j) or (i, j-1) with the condition that the adjacent cells have
a difference of 1.

"""

mat = [[1, 2, 9],
    [5, 3, 8],
    [4, 6, 7]]

def longest_path_in_matrix(lst: list) -> int:
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return 1
    L_val = [j for i in lst for j in i]
    L_sorted = sorted(L_val)
    max_val = 1
    ans = 1
    temp = min(L_val)
    ind1 = L_val.index(temp)
    i1, j1 = ind1 // len(lst), ind1 % len(lst)
    while True:
        if temp == max(L_val):
            break
        if temp + 1 in L_val:
            ind2 = L_val.index(temp + 1)
        else:
            temp = L_sorted[L_sorted.index(temp) + 1]
            max_val = 1
            if temp == max(L_val):
                break
            ind1 = L_val.index(temp)
            i1, i2 = ind1 // len(lst), ind1 % len(lst)
            continue
        i2, j2 = ind2 // len(lst), ind2 % len(lst)
        if min(abs(i1 - i2), abs(j1 - j2)) == 0 and max(abs(i1 - i2), abs(j1 - j2)) == 1:
            max_val += 1
            temp += 1
            i1, j1 = i2, j2
            if max_val > ans:
                ans = max_val
        else:
            temp = L_sorted[L_sorted.index(temp) + 1]
            max_val = 1
            if temp == max(L_val):
                break
            ind1 = L_val.index(temp)
            i1, j1 = ind1 // len(lst), ind1 % len(lst)
    return ans


print(longest_path_in_matrix(mat))