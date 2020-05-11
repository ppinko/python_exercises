"""
https://edabit.com/challenge/pa65DgwG5HMbtf6iY

Classes For Fetching Information on a Sports Player

Create a class that takes the following four arguements for a particular football player:

    name
    age
    height
    weight

Also, create three functions for the class that returns the following strings:

    get_age() returns "name is age age"
    get_height() returns "name is height cm"
    get_weight() returns "name weighs weight kg"

Notes

name will be passed in as a string and age height weight will be integers.
"""


class player:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return '{0} is age {1}'.format(self.name, self.age)

    def get_height(self):
        return '{0} is {1}cm'.format(self.name, self.height)

    def get_weight(self):
        return '{0} weighs {1}kg'.format(self.name, self.weight)


player1 = player('Patrick Mahomes', 24, 188, 104)
player2 = player('Jimmy Garoppolo', 28, 188, 102)
player3 = player('Julio Jones', 31, 191, 100)

assert player1.get_age() == 'Patrick Mahomes is age 24'
assert player1.get_height() == 'Patrick Mahomes is 188cm'
assert player1.get_weight() == 'Patrick Mahomes weighs 104kg'

assert player2.get_age() == 'Jimmy Garoppolo is age 28'
assert player2.get_height() == 'Jimmy Garoppolo is 188cm'
assert player2.get_weight() == 'Jimmy Garoppolo weighs 102kg'

assert player3.get_age() == 'Julio Jones is age 31'
assert player3.get_height() == 'Julio Jones is 191cm'
assert player3.get_weight() == 'Julio Jones weighs 100kg'

print('Success')


