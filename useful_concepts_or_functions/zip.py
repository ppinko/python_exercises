"""
            ZIP()

Main usage - Looping over multiple iterables

Conclusion:
It returns an iterator that can generate tuples
with paired elements from each argument. The
resulting iterator can be quite useful when you
need to process multiple iterables in a single
loop and perform some actions on their items at
the same time.

https://realpython.com/python-zip-function/
"""

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(zipped)  # Holds an iterator object <zip object at 0x7fa4831153c8>
print(type(zipped)) # <class 'zip'>
print(list(zipped)) # [(1, 'a'), (2, 'b'), (3, 'c')]

print("\n----------------\n")

"""
s1 and s2 are set objects, which don’t keep their elements in any
particular order. This means that the tuples returned by zip() will
have elements that are paired up randomly. If you’re going to use
the Python zip() function with unordered iterables like sets, then
this is something to keep in mind.
"""
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
print(list(zip(s1, s2))) # [(1, 'a'), (2, 'c'), (3, 'b')]

print("\n----------------\n")

"""
As you can see, you can call the Python zip() function with as many
input iterables as you need.
"""

integers = [1, 2, 3]
letters = ['a', 'b', 'c']
floats = [4.0, 5.0, 6.0]
zipped = zip(integers, letters, floats)  # Three input iterables
print(list(zipped)) # [(1, 'a', 4.0), (2, 'b', 5.0), (3, 'c', 6.0)]

print("\n----------------\n")

"""
In these cases, the number of elements that zip() puts out will be
equal to the length of the shortest iterable. The remaining elements
in any longer iterables will be totally ignored by zip()
"""

print(list(zip(range(5), range(100)))) # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

print("\n----------------\n")
print("   USAGE ")
print("\n----------------\n")

"""
Traversing list in parallel
"""

letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
     print(f'Letter: {l}')
     print(f'Number: {n}')

print("\n----------------\n")

"""
Traversing dictionaries in parallel
"""

dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
     print(k1, '->', v1)
     print(k2, '->', v2)

print("\n----------------\n")

"""
Unziping a sequence
"""

pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print(numbers) # (1, 2, 3, 4)
print(letters) # ('a', 'b', 'c', 'd')

print("\n----------------\n")

"""
Calculating in paris
"""

total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]
for sales, costs in zip(total_sales, prod_cost):
     profit = sales - costs
     print(f'Total profit: {profit}')

print("\n----------------\n")

"""
Building dictionaries
"""

fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']
a_dict = dict(zip(fields, values))
print(a_dict) # {'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Developer'}
