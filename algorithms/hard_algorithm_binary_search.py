"""
https://edabit.com/challenge/kfXz49avvohsYSxoe
"""


def binary_search(lst, left, right, n):
    return n in lst[left: right]


assert binary_search([1,2,3,4,5,6,7,8,9,10],0,9,7) == True
assert binary_search([3,6,14,15,17,18,22,43,55,66],0,9,19) == False
assert binary_search([4,8,12,16,20,24,28,32,36,40],0,9,32) == True
assert binary_search([3,6,9,12,15,18,21,24,27,30],0,9,31) == False
assert binary_search([20,1067,5032,10005,20333,36798,45234,55555,64123,99999],0,9,64123) == True

print('Success')

