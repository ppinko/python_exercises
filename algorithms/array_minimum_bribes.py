"""
https://www.hackerrank.com/challenges/new-year-chaos/problem
"""

sample_1 = [2, 1, 5, 3, 4]
sample_2 = [2, 5, 1, 3, 4]
sample_3 = [5, 1, 2, 3, 7, 8, 6, 4]
sample_4 = [1, 2, 5, 3, 7, 8, 6, 4]

def minimumBribes(Q):

    moves = 0 
    Q = [P-1 for P in Q]

    for i,P in enumerate(Q):
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1, 0),i):
            if Q[j] > P:
                moves += 1
    print(moves)