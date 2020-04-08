"""
Task 3.3

Question:
Write a program which can filter even numbers in a list by using filter function. 
The list is: [1,2,3,4,5,6,7,8,9,10].
"""

ls = [1,2,3,4,5,6,7,8,9,10]
ls_even =filter(lambda x: x%2 == 0, ls)
print(tuple(ls_even))

print([i for i in range(1,11) if i%2 == 0])

"""
3.4

Question:
Write a program which can map() to make a list whose elements are square of 
elements in [1,2,3,4,5,6,7,8,9,10].
"""

ls = [1,2,3,4,5,6,7,8,9,10]
ls_square = map(lambda x: x**2, ls)
print(tuple(ls_square))

print([i**2 for i in range(1,11)])

"""
3.5

Question:
Write a program which can map() and filter() to make a list whose elements 
are square of even number in [1,2,3,4,5,6,7,8,9,10].
"""

ls = [1,2,3,4,5,6,7,8,9,10]
ls_square_even = map(lambda x: x**2, filter(lambda x: x%2 == 0, ls))
print(tuple(ls_square_even))

print([i**2 for i in range (1,11) if i%2 == 0])