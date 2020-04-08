"""
https://www.hackerrank.com/challenges/count-triplets-1/problem
"""

def countTriplets(arr, r):
    dictA = {}
    for i in arr:
        if i == 1:
            dictA[0] = dictA.get(0, 0) + 1
        elif i % r == 0:
            dictA[int(i/r)] = dictA.get(int(i/r), 0) + 1
    count = 0
    for j in dictA:
        if j == 0:
            count += dictA[j] * dictA.get(1, 0) * dictA.get(r, 0)
        else:
            count += dictA[j] * dictA.get(j * r, 0) * dictA.get( j * r **2, 0)
    return count   

# arr = [1, 3, 9, 9, 27, 81]
# r = 3
# print(countTriplets(arr, r))

arr = [1, 2, 2, 4]
r = 2

print(countTriplets(arr, r))