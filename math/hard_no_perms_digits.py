"""
https://edabit.com/challenge/oQ99uE4iPNbEnf9QZ
"""

def no_perms_digits(n):
	tot = 1
	while n > 1:
		tot *= n
		n -= 1
	return len(str(tot))

assert no_perms_digits(0) == 1
assert no_perms_digits(1) == 1
assert no_perms_digits(2) == 1
assert no_perms_digits(3) == 1
assert no_perms_digits(4) == 2

print("Success")
