"""
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""

class StringOp():
    def __init__(self):
        self.answer = ""

    def getString(self):
        self.answer = input("Please enter a string: ")

    def printString(self):
        print(self.answer.upper())

string1 = StringOp()
string1.getString()
string1.printString()

