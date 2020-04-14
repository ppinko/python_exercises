"""
https://edabit.com/challenge/dy3WWJr34gSGRPLee
"""

def makeBox(n):
    l = []
    t = n
    while n > 0:
        if n == t or n == 1:
            l.append('#' * t)
        else:
            l.append('#' + ' '*(t-2) + '#')
        n -= 1
    return l

assert makeBox(5) == [
		"#####", 
		"#   #", 
		"#   #", 
		"#   #", 
		"#####"]

assert makeBox(6) == [
		"######", 
		"#    #", 
		"#    #", 
		"#    #", 
		"#    #", 
		"######"]

assert makeBox(2) == [
		"##", 
		"##"]

print("Success")
