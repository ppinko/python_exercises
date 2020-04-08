"""
Question
A robot moves in a plane starting from the original point (0,0). The robot can move 
toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is 
shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance 
from current position after a sequence of movement and original point. If the distance 
is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""

inp = "UP 5 DOWN 3 LEFT 3 RIGHT 2"

import math

def plane_dist(p):
    ls = p.split()
    x, y = 0, 0
    for i in range(int(len(ls) / 2)):
        if ls[2*i] == "UP":
            y += int(ls[2*i + 1])
        elif ls[2*i] == "DOWN":
            y -= int(ls[2*i + 1])
        elif ls[2*i] == "LEFT":
            x -= int(ls[2*i + 1])
        elif ls[2*i] == "RIGHT":
            x += int(ls[2*i + 1])
    return round(math.sqrt(x**2 + y**2))

print(plane_dist(inp))