"""
https://edabit.com/challenge/qeyinsjZHCPEddbfe
"""

def dice_game(lst):
    total = 0
    for i in lst:
        if i[0] == i[1]:
            return 0
        else:
            total += sum(i)
    return total

"""
Alternative solution
"""

##def dice_game(lst):
##	score = 0
##	for a, b in lst:
##		if a == b:
##			return 0
##		score += a+b
##	return score

print(dice_game([(1, 2), (3, 4), (5, 6)]) == 21)
print(dice_game([(1, 1), (5, 6), (6, 4)]) == 0)
