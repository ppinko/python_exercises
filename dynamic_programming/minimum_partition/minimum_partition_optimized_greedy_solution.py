"""
https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/

Partition a set into two subsets such that the difference of subset sums is minimum

Given a set of integers, the task is to divide it into two sets S1 and S2 such that
the absolute difference between their sums is minimum.

If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2
must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

Input:  arr[] = {1, 6, 11, 5}
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12
Subset2 = {11}, sum of Subset2 = 11

Greedy algorithm - Optimized solution
"""


def partition(L, n):
    L = sorted(L, reverse=True)
    dp = [0 for i in range(n+1)]
    if n == 1:
        return L[n-1]
    for i in range(1, n+1):
        dp[i] = min(abs(dp[i-1] + L[i-1]), abs(dp[i-1] - L[i-1]))
    return dp[n]


L0 = [5, 7, 3, 1, 9]
L1 = [1, 6, 11, 5]
L2 = [14, 25, 78, 96, 32, 10]

print(partition(L0, len(L0)))
assert partition(L0, len(L0)) == 1

print(partition(L1, len(L1)))
assert partition(L1, len(L1)) == 1