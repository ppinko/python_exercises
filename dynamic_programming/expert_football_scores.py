"""
https://edabit.com/challenge/k7YPvRyJt9NHbrvzu
"""


def football(n: int):
    if n < 0 or n == 1:
        return 0
    elif n == 0:
        return 1
    scores = [[1 if j == 0 else 0 for j in range(n+1)] for _ in range(8+1)]
    valid_scores = {2, 3, 6, 7, 8}
    for i in range(1, 9):
        for j in range(1, n+1):
            if i not in valid_scores or j < i:
                scores[i][j] = scores[i-1][j]
            else:
                scores[i][j] = scores[i-1][j] + scores[i][j-i]
    return scores[8][n]


assert football(0) == 1
assert football(1) == 0
assert football(8) == 4
assert football(19) == 18
assert football(35) == 103
assert football(66) == 804

print('Success')