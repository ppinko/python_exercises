"""
Question:
Write a program that accepts sequence of lines as input and prints the lines after making 
all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""

ls = []
while True:
    n = input("input a sentence: ")
    if n:
        ls.append(n.upper())
    else:
        break

for el in ls:
    print(el)