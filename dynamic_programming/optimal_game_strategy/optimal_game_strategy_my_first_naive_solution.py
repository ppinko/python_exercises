"""
https://www.geeksforgeeks.org/optimal-strategy-for-a-game-dp-31/

Problem statement: Consider a row of n coins of values v1 . . . vn,
where n is even. We play a game against an opponent by alternating
turns. In each turn, a player selects either the first or last coin
from the row, removes it from the row permanently, and receives the
value of the coin. Determine the maximum possible amount of money we
can definitely win if we move first.

Note: The opponent is as clever as the user.

Let us understand the problem with few examples:

1. 5, 3, 7, 10 : The user collects maximum value as 15(10 + 5)
2. 8, 15, 3, 7 : The user collects maximum value as 22(7 + 15)
"""


def opt_strategy(lst: list) -> int:
    if len(lst) <= 2:
        return max(lst)
    return max(sum(lst) - opt_strategy(lst[1:]), sum(lst) - opt_strategy(lst[:-1]))


assert opt_strategy([5, 3, 7, 10])
assert opt_strategy([8, 15, 3, 7])

print('Success')