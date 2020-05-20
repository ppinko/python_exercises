"""
https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

Longest Common Subsequence

a) find the length of longest common subsequence
b) find the subsequence
"""


def LCS(first, second):
    m, n = len(first), len(second)
    L = [[i for i in range(m+1)] for _ in range(n+1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif first[j - 1] == second[i - 1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])
    # Length of the longest subsequence = L[n][m]

    # Finding longest subsequence
    a, b = n, m
    val = L[n][m]
    V = []
    while a > 0 and b > 0:
        if L[a][b] > L[a][b-1] and L[a][b] > L[a-1][b]:
            V.append(first[b - 1])
            a -= 1
            b -= 1
        elif L[a][b-1] == L[a-1][b] or L[a][b-1] < L[a-1][b]:
            a -= 1
        else:
            b -= 1
    V.reverse()
    print(V)
    return L[n][m]


assert LCS('ABCDGH', 'AEDFHR') == 3
assert LCS('GXTXAYB', 'AGGTAB') == 4
print('Success')