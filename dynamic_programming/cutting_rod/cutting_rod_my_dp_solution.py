"""
https://www.geeksforgeeks.org/cutting-a-rod-dp-13/

Given a rod of length n inches and an array of prices that contains prices
of all pieces of size smaller than n. Determine the maximum value
obtainable by cutting up the rod and selling the pieces. For example, if
length of the rod is 8 and the values of different pieces are given as
following, then the maximum obtainable value is 22 (by cutting in two
pieces of lengths 2 and 6)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

And if the prices are as following, then the maximum obtainable value is 24
(by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
"""


def rod(lengths, prices, n):
    k = len(lengths)
    dp = [[0 for i in range(n+1)] for _ in range(k+1)]
    for i in range(1, k+1):
        for j in range(1, n+1):
            if lengths[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], prices[i-1] + dp[i][j-lengths[i-1]])
    return dp[k][n]


n = 8
lengths = [1, 2, 3, 4, 5, 6, 7, 8]
prices1 = [1, 5, 8, 9, 10, 17, 17, 20]
prices2 = [3, 5, 8, 9, 10, 17, 17, 20]

assert rod(lengths, prices1, n) == 22
assert rod(lengths, prices2, n) == 24

print('Success')