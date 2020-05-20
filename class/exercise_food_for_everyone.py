"""
https://edabit.com/challenge/iRvRtg2xxL9BnSEvf

Create a Person class which will have three properties:

    Name
    List of foods they like
    List of foods they hate

In this class, create the method taste():

    It will take in a food name as a string
    Return {person_name} eats the {food_name}
    If the food is in the person's like list, add 'and loves it!' to the end
    If it is in the person's hate list, add 'and hates it!' to the end
    If it is in neither list, simply add an exclamation mark to the end

Examples:
p1 = Person('Sam', ['ice cream'], ['carrots'])

Testing:
p1.taste('ice cream') ➞ 'Sam eats the ice cream and loves it!'
p1.taste('cheese') ➞ 'Sam eats the cheese!'
p1.taste('carrots') ➞ 'Sam eats the carrots and hates it!'
"""

class Person:

    def __init__(self, name, loves, hates):
        self.name = name
        self.love = loves
        self.hate = hates

    def taste(self, food):
        if food in self.love:
            return "{0} eats the {1}{2}".format(self.name, food, " and loves it!")
        elif food in self.hate:
            return "{0} eats the {1}{2}".format(self.name, food, " and hates it!")
        else:
            return "{0} eats the {1}{2}".format(self.name, food, "!")
        
p1 = Person('Sam', ['ice cream'], ['carrots'])
print(p1.taste('ice cream'))
print(p1.taste('cheese'))
print(p1.taste('carrots'))
