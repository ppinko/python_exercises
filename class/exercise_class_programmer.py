"""
https://edabit.com/challenge/9Q5nsEy2E2apYHwX8

Ccreate a class called programmer. It has a sallary value, work_hours value,
and a __del__ (self) function. __ del __ (self) returns ()
"oof, " + str(sallary) + ", " + str(work_hours)) when the object is destroyed
using del obj. sallary and work_hours will be in the constructor. Varibales
in a class are defined with self.name = value.

Also, define a function that will compare two programmers (their sallary and
work_hours). If their sallary is equal, then work_hours is compared, they will
allways be different. Return the programmer that is worse.

Examples:
prog = programer(25000, 5)

prog.sallary ➞ 25000
prog.work_hours ➞ 5
del prog ➞ "oof, 25000, 5"
# By the __ del __ function.
"""

class programer:

    def __init__ (self, salary, work_hours):
        self.sallary = salary
        self.work_hours = work_hours
            
    def __del__ (self):
        s = "oof, {0}, {1}".format(self.sallary, self.work_hours)
        del self
        return s
            
    def compare (self, other):
        if self.sallary > other.sallary:
            return other
        elif self.sallary < other.sallary:
            return self
        elif self.work_hours > other.work_hours:
            return other
        else:
            return self

prog = programer(25000, 5)
print(prog.sallary) 
print(prog.work_hours)
del prog
