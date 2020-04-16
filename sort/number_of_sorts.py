"""
https://edabit.com/challenge/WQjynmyMXcR83Dd8K
"""

def number_of_swaps(lst):
	swaps = 0
	while True:
		temp = 0
		for i in range(len(lst) - 1):
			if lst[i] > lst[i+1]:
				a, b = lst[i], lst[i+1]
				lst[i] = b
				lst[i+1] = a
				swaps += 1
				temp += 1
		if temp == 0:
			return swaps
