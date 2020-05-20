"""
https://edabit.com/challenge/D6XfxhRobdQvbKX4v
"""

"""
Function to check if first instance of first is before
first instance of second etc.
"""

##def first_before_second(s, first, second):
##    l1 = [i for i in range(len(s)) if s[i] == first]
##    l2 = [i for i in range(len(s)) if s[i] == second]
##    return all( l1[i] < l2[i] for i in range(min(len(l1), len(l2))))

"""
Actual task
"""

def first_before_second(s, first, second):
    return s.rfind(first) < s.find(second)

print(first_before_second("a rabbit jumps joyfully", "a", "j") == True)
print(first_before_second("precarious kangaroos", "k", "a") == False)
