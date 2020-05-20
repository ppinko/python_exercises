"""
https://edabit.com/challenge/QuxCNBLcGJReCawjz
"""

def palindrome_type(n):
	k = str(n)
	b = str(bin(n))
	b = b[2:]
	la = [ True for i in range(len(k)) if k[i] == k[-i-1]]
	lb = [ True for i in range(len(b)) if b[i] == b[-i-1]]
	flag_normal = (len(la) == len(k))
	flag_binar = (len(lb) == len(b))
	
	if flag_normal and flag_binar:
		return "Decimal and binary."
	elif flag_normal:
		return "Decimal only."
	elif flag_binar:
		return "Binary only."
	else:
		return "Neither!"

assert palindrome_type(1934391) == "Decimal and binary."
assert palindrome_type(9994521) == "Binary only."
assert palindrome_type(5841485) == "Decimal and binary."
assert palindrome_type(8337738) == "Neither!"

print("Success")
