"""
https://edabit.com/challenge/ta8GBizBNbRGo5iC6

Create methods for the Calculator class that can do the following:
    Add two numbers.
    Subtract two numbers.
    Multiply two numbers.
    Divide two numbers.

Examples:
calculator = Calculator()
calculator.add(10, 5) ➞ 15
calculator.subtract(10, 5) ➞ 5
calculator.multiply(10, 5) ➞ 50
calculator.divide(10, 5) ➞ 2
"""

"""
Classic solution
"""

##class Calculator:
##
##    def add(self, x, y):
##        return x + y
##
##    def subtract(self, x, y):
##        return x - y
##
##    def multiply(self, x, y):
##        return x * y
##
##    def divide(self, x, y):
##        return x // y

"""
Using @staticmethod decorator
"""

class Calculator:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract( x, y):
        return x - y

    @staticmethod
    def multiply( x, y):
        return x * y

    @staticmethod
    def divide( x, y):
        return x // y

calculator = Calculator()
print(calculator.add(10, 5)) 
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5)) 
print(calculator.divide(10, 5)) 
