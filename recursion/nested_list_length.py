"""
https://edabit.com/challenge/xmwdk2qwyZEt7ph49
"""

def get_length(lst):
    count = len(lst)
    for i in lst:
        if type(i) == list:
            count -= 1
            count += get_length(i)
    return count

print(get_length([1, [2, 3]]) == 3)
print(get_length([1, [2, [3, 4]]]) == 4)
print(get_length([1, [2, [3, [4, [5, 6]]]]]) == 6)
