"""
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""

def read_input():
    s = input("Please enter a string: ")
    lower = 0
    upper = 0
    for char in s:
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
    print("LOWER {0}".format(lower))
    print("UPPER {0}".format(upper))

read_input()