"""
https://edabit.com/challenge/8rEEHcmq8rRaTksd7
"""


def lines_are_parallel(l1, l2):
    if (l1[0] == 0 and l2[0] == 0) or (l1[1] == 0 and l2[1] == 0):
        return True
    elif l1[0]/l1[1] == l2[0]/l2[1]:
        return True
    else:
        return False


assert lines_are_parallel([2,5,0], [20,50,10]) == True
assert lines_are_parallel([2,5,0], [-200,-500,10]) == True
assert lines_are_parallel([400000,1,0], [400000,2,0]) == False
assert lines_are_parallel([800,20,0], [40,20,0]) == False
assert lines_are_parallel([400000,1,0], [800000,2,100000]) == True
assert lines_are_parallel([-5,7,100000], [5,-7,-200000]) == True

print('Success')