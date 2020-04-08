"""
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""

def square_root():
    import math
    x = input("Please enter a few comma separeted number: ")
    ls = x.split(",")
    C = 50
    H = 30
    def sr(D, C, H):
        base = 2 * C * D / H
        return math.sqrt(base)
    ls2 = [ str(math.floor(sr(int(D), C, H))) for D in ls ]
    ans = ",".join(ls2)
    print(ans)

square_root()