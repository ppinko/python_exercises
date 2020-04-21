"""
https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

Longest Common Subsequence

It is a classic computer science problem, the basis of diff
(a file comparison program that outputs the differences between
two files), and has applications in bioinformatics.

Naive recursive solution
"""


counter = 0


def LCS(first, second):
    global counter
    counter += 1
    if len(first) == 0 or len(second) == 0:
        return 0
    elif first[-1] == second[-1]:
        return 1 + LCS(first[:-1], second[:-1])
    else:
        return max(LCS(first[:-1], second), LCS(first, second[:-1]))


assert LCS('ABCDGH', 'AEDFHR') == 3
print('counter = ', counter)        # out: 763 !!!
assert LCS('GXTXAYB', 'AGGTAB') == 4
print('counter = ', counter)         # out: 345 !!!
print('Success')