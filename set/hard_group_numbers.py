"""
https://edabit.com/challenge/SYmHGXX2P26xu7JFR
"""

##def number_groups(group1, group2, group3):
##    s1 = set(group1)
##    s2 = set(group2)
##    s3 = set(group3)
##    l = list(s1) + list(s2) + list(s3)
##    l.sort()
##    print(l)
##    l2 = [l[i] for i in range(1, len(l)) if l[i] == l[i-1]]
##    print(l2)
##    return list(set(l2))

"""
Alternative solution using set functions
"""

def number_groups(*g):
    a, b, c = [set(i) for i in g]
    return sorted(set.union(a.intersection(b),a.intersection(c),b.intersection(c)))

print(number_groups([7, 8, 7, 3, 4], [2, 9, 1, 2, 1], [5, 6, 6, 6, 5]) == [])
print(number_groups([3, 8, 8, 1, 1], [9, 1, 1, 9, 9], [10, 7, 6, 6, 3]))
print(number_groups([3, 8, 8, 1, 1], [9, 1, 1, 9, 9], [10, 7, 6, 6, 3]) == [1, 3])
