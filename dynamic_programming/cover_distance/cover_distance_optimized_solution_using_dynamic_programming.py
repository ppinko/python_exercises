"""
Given a distance ‘dist, count total number of ways to cover
the distance with 1, 2 and 3 steps.

My first fully solved fully independently dp program using bottom-up
approach :)
"""


def cover_distance(steps: int) -> int:
    # creating tab to store all possibilites size (n+1) x (steps+1)
    dp = [[0 for i in range(steps + 1)] for _ in range(4)]
    for i in range(4):
        for j in range(steps + 1):
            if i == 0 or j == 0 or i ==  1 or j == 1:
                dp[i][j] = 1
            elif j < i:
                dp[i][j] = dp[i-1][j]
            else:
                k = i
                temp = 0
                while k >= 1:
                    temp += dp[i][j-k]
                    k -= 1
                dp[i][j] = temp
    return dp[3][steps]


assert cover_distance(3) == 4
assert cover_distance(4) == 7

print('Success')