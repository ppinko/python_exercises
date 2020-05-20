"""
https://edabit.com/challenge/nRAxMKDgcBTDeLzPz
"""

def circular_shift(lst1, lst2, n):
    n = n % len(lst1)
    return lst2 == lst1[n:] + lst1[:n]

print(circular_shift([1, 2, 3, 4], [3, 4, 1, 2], 2))

