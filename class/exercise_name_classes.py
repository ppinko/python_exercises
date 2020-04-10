"""
https://edabit.com/challenge/kbtju9wk5pjGYMmHF
"""

"""
Write a class called Name and create the following attributes given a
first name and last name (as fname and lname):

- An attribute called fullname which returns the first and last names.
- A attribute called initials which returns the first letters of the
first and last name. Put a '.' between the two letters.

Remember to allow the attributes fname and lname to be accessed
individually as well.

Examples:
a1 = Name('john', 'SMITH')

a1.fname ➞ 'John'
a1.lname ➞ 'Smith'
a1.fullname ➞ 'John Smith'
a1.initials ➞ 'J.S'
"""

class Name:
    def __init__(self, fname, lname):
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.fullname = "{0} {1}".format(self.fname, self.lname)
        self.initials = "{0}.{1}".format(str(self.fname)[0], str(self.lname)[0])

a1 = Name('john', 'SMITH')

print(a1.fname)
print(a1.lname)
print(a1.fullname)
print(a1.initials)

"""
Alternative solution
"""

class Name:
    def __init__(self, fname, lname):
        self.fname = fname[0].upper() + fname[1:].lower()
        self.lname = lname[0].upper() + lname[1:].lower()
	
    @property
    def fullname(self):
        return "{} {}".format(self.fname, self.lname)
		
    @property
    def initials(self):
        return "{}.{}".format(self.fname[0], self.lname[0])

print(a1.fname)
print(a1.lname)
print(a1.fullname)
print(a1.initials)
