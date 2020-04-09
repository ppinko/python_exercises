"""
https://edabit.com/challenge/bupEio82q8NMnovZx
"""

##def track_robot(instructions):
##    x = 0
##    y = 0
##    for i in instructions:
##        l = i.split()
##        if l[0] == 'right':
##            x += int(l[1])
##        elif l[0] == 'left':
##            x -= int(l[1])
##        elif l[0] == 'up':
##            y += int(l[1])
##        elif l[0] == 'down':
##            y -= int(l[1])
##    return [x, y]

"""
Alternative solution using unpacking
"""

def track_robot(instructions):
    x = 0
    y = 0
    for k in instructions:
        (i, j) = k.split()
        if i == 'right':
            x += int(j)
        elif i == 'left':
            x -= int(j)
        elif i == 'up':
            y += int(j)
        elif i == 'down':
            y -= int(j)
    return [x, y]
        
print(track_robot(["right 10", "up 50", "left 30", "down 10"]) == [-20, 40])
