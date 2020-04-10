"""
https://edabit.com/challenge/j2HauiSdDadkjxjsQ

In the class Employee, implement the instance attributes as firstname,
lastname and salary.

Create the method from_string() which parses a string containing these
attributes and assigns them to the correct properties. Properties will
be separated by a dash.

Examples
emp1 = Employee('Mary', 'Sue', 60000)
emp2 = Employee.from_string('John-Smith-55000')

Tests:
emp1.firstname ➞ 'Mary'
emp1.salary ➞ 60000
emp2.firstname ➞ 'John'
emp2.salary ➞ 55000
"""

class Employee:
    def __init__(self, firstname = '', lastname = '', salary = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

##    @classmethod
##    def from_string(cls, s):
##        l = s.split('-')
##        return cls(l[0], l[1], int(l[2]))

    @classmethod
    def from_string(cls, s):
        firstname, lastname, salary = s.split('-')
        return cls(firstname, lastname, salary)

emp1 = Employee('Mary', 'Sue', 60000)
emp2 = Employee.from_string('John-Smith-55000')

print(emp1.firstname) # 'Mary'
print(emp1.salary) # 60000
print(emp2.firstname) # 'John'
print(emp2.salary) # 55000



