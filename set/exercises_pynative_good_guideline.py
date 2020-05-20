# https://pynative.com/python-set-exercise-with-solutions/


"""
Exercise Question 1:

Add a list of elements to a given set
sampleSet = {"Yellow", "Orange", "Black"}
sampleListtoAdd = ["Blue", "Green", "Red"]
"""

sampleSet = {"Yellow", "Orange", "Black"}
sampleListtoAdd = ["Blue", "Green", "Red"]

sampleSet.update(sampleListtoAdd) # using s.update(iterable)
print(sampleSet) # {'Green', 'Blue', 'Yellow', 'Red', 'Black', 'Orange'}
print('-----------------')

"""
Exercise Question 2: Return a set of identical items from a given two
Python set
set1 = [10, 20, 30, 40, 50]
set2 = [30, 40, 50, 60, 70]
"""

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1 & set2
# set3 = set1.intersection(set2)
print(set3) # {40, 50, 30}
print('-----------------')

"""
Exercise Question 3: Returns a new set with all items from both sets
by removing duplicates
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
"""

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1 | set2
# set1.union(set2)
print(set3) # {70, 40, 10, 50, 20, 60, 30}
print('-----------------')

"""
Exercise Question 6: Return a set of all elements in either A or B,
but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
"""

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1 ^ set2
# set1.symmetric_difference(set2)
print(set3) # {20, 70, 10, 60}
print('-----------------')

"""
Exercise Question 7: Determines whether or not the following two
sets have any elements in common. If yes display the common elements
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
"""

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

set3 = set1 & set2
print("Two set have {0} item(s) in common. {1}".format(len(set3), set3))
print('-----------------')

"""
Exercise Question 8: Remove items from set1 that are not common
to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
"""

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.difference_update(set2)
# set1 -= set2
print(set1) # {10, 20}
print('-----------------')
