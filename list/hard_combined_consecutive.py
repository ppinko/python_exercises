"""
https://edabit.com/challenge/mHLAmj4vmRuXrT8Nb
"""

##def consecutive_combo(lst1, lst2):
##    lst1.extend(lst2)
##    sort_ls = sorted(lst1)
##    for i in range(1, len(sort_ls)):
##        if sort_ls[i] - sort_ls[i-1] != 1:
##            return False
##    return True

"""
Alternative solution with inbuilt function all and list comprehension
"""

def consecutive_combo(lst1, lst2):
    sort_ls = sorted(lst1 + lst2)
    return all(sort_ls[i+1] - sort_ls[i] == 1 for i in range(len(lst1) + len(lst2) - 1))

print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]) == True)
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) == False)
