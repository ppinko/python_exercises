"""
https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/

The following is a description of the instance of this famous puzzle
involving n=2 eggs and a building with k=36 floors.

Suppose that we wish to know which stories in a 36-story building
are safe to drop eggs from, and which will cause the eggs to break
on landing. We make a few assumptions:

…..An egg that survives a fall can be used again.
…..A broken egg must be discarded.
…..The effect of a fall is the same for all eggs.
…..If an egg breaks when dropped, then it would break if dropped
from a higher floor.
…..If an egg survives a fall then it would survive a shorter fall.
…..It is not ruled out that the first-floor windows break eggs, nor
is it ruled out that the 36th-floor do not cause an egg to break.

If only one egg is available and we wish to be sure of obtaining the
right result, the experiment can be carried out in only one way. Drop
the egg from the first-floor window; if it survives, drop it from the
second floor window. Continue upward until it breaks. In the worst
case, this method may require 36 droppings. Suppose 2 eggs are
available. What is the least number of egg-droppings that is
guaranteed to work in all cases?

The problem is not actually to find the critical floor, but merely to
decide floors from which eggs should be dropped so that total number
of trials are minimized.
"""

import sys


# Function to get minimum number of trials
# needed in worst case with n eggs and k floors

def eggDrop(n, k):
    if (k <= 2):
        return k

    min_sys = sys.maxsize

    scores = [[min_sys if i == 0 or i > j else 0 for i in range(k+1)] for j in range(k+1)]
    for i in range(1, k+1):
        for j in range(1, i+1):
            if i <= 2:
                scores[i][j] = i
            elif j == 1:
                scores[i][j] = 1 + min(scores[i-1])
            elif i == j:
                scores[i][j] = j
            else:
                scores[i][j] = max(j, 1 + min(scores[i-j]))
    return min(scores[k][1:])


assert eggDrop(2, 10) == 4
assert eggDrop(2, 36) == 8

print('Success')