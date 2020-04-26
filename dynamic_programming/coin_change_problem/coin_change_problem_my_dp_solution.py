"""
https://www.geeksforgeeks.org/coin-change-dp-7/

Given a value N, if we want to make change for N cents, and we have infinite
supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we
make the change? The order of coins doesn’t matter.

For example, for N = 4 and S = {1,2,3}, there are four solutions:
{1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and
S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6},
{2,3,5} and {5,5}. So the output should be 5.
"""


def coin_change(n: int, lst: list) -> int:
    max_coin = max(lst)
    dp = [[1 if i == 0 else 0 for i in range(n+1)] for i in range(max_coin+1)]
    for i in range(1, max_coin+1):
        for j in range(1, n+1):
            if i not in lst or j - i < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j-i]
    return dp[max_coin][n]


assert coin_change(4, [1, 2, 3]) == 4
assert coin_change(10, [2, 3, 5, 6]) == 5

print('Success')