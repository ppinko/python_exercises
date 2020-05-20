"""
https://edabit.com/challenge/kS8tfJD2ggohQbWx7

Sort Names According to the Length of Their Last Names

Create a function that takes a list of names in the format "First Name Last Name" (e.g. "John Doe"), and returns a list
of these names sorted by the length of their last names. If the length of multiple last names are the same, then proceed
to sort alphabetically.
"""


def last_name_lensort(lst: list) -> list:
    temp = [i.split() for i in lst]
    temp = sorted(temp, key=lambda x: x[1])
    return [' '.join(i) for i in sorted(temp, key=lambda x: len(x[1]))]


""" Alternative solution """


def last_name_lensort(names):
	return sorted(names, key=lambda x: (len(x.split()[1]), x.split()[1]))


assert last_name_lensort(["Jennifer Figueroa","Heather Mcgee","Amanda Schwartz","Nicole Yoder","Melissa Hoffman"]) == \
       ['Heather Mcgee', 'Nicole Yoder', 'Melissa Hoffman', 'Jennifer Figueroa', 'Amanda Schwartz']
assert last_name_lensort(["Hitagi Senjougahara","Edward Elric","Light Yagami","Rintaro Okabe","Kurisu Makise"]) == \
       ["Edward Elric","Rintaro Okabe","Kurisu Makise","Light Yagami","Hitagi Senjougahara"]

print('Success')