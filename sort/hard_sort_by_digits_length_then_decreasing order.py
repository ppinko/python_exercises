"""
https://edabit.com/challenge/jTBQTDQ568ppnGvq7
"""


def digit_sort(lst):
    lst.sort()
    return sorted(lst, key=lambda x: len(str(x)), reverse=True)


print(digit_sort([77, 23, 5, 7, 101]))
assert digit_sort([77, 23, 5, 7, 101]) == [101, 23, 77, 5, 7]
assert digit_sort([1, 5, 9, 2, 789, 563, 444]) == [444, 563, 789, 1, 2, 5, 9]
assert digit_sort([53219, 3772, 564, 32, 1]) == [53219, 3772, 564, 32, 1]
assert digit_sort([9, 667, 87, 56, 3023, 5555, 111]) == [3023, 5555, 111, 667, 56, 87, 9]

print('Success')

