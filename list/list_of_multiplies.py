## https://edabit.com/challenge/BuwHwPvt92yw574zB
## list_of_multiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

def list_of_multiples (num, length):
	ls = [ num * i for i in range(1, length + 1) ]
	return ls

print(list_of_multiples(12, 10))
