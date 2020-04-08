"""
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""

def evenNum(start, end):
    ls = list()
    for i in range(start, end + 1):
        if i%2 == 0 and (i//10)%2 == 0 and (i//100)%2 == 0 and (i//1000)%2 == 0:
            ls.append(str(i))
    return ",".join(ls)

print(evenNum(1000, 3000))