"""
https://edabit.com/challenge/QoavwQhmrDpXJhBW9
"""

def flip_list(lst):
    if lst == []:
        return lst
    elif type(lst[0]) == list:
        return [element for row in lst for element in row]
    else:
        return [[element] for element in lst]

"""
Alternative solution
"""

##def flip_list(lst):
##    return [x[0] if isinstance(x, list) else [x] for x in lst]

print(flip_list([1, 2, 3, 4]) == [[1], [2], [3], [4]])
print(flip_list([[5], [6], [9]]) == [5, 6, 9])
