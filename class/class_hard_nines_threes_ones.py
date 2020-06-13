"""
https://edabit.com/challenge/8Fwv2f8My4kcNjMZh
"""

class ones_threes_nines:

    def __init__(self, num):
        self.nines = num // 9
        self.threes = (num - self.nines * 9) // 3
        self.ones = num - 9 * self.nines - 3 * self.threes
        self.answer = 'nines:{0}, threes:{1}, ones:{2}'.format(self.nines, self.threes, self.ones)

# Alternative solution

class ones_threes_nines:
	def __init__(self, n):
		self.answer = 'nines:{}, threes:{}, ones:{}'.format(n//9, n%9//3, n%9%3)


n1 = ones_threes_nines(1)
assert n1.answer == 'nines:0, threes:0, ones:1'
n2 = ones_threes_nines(5)
print(n2.answer)
assert n2.answer == 'nines:0, threes:1, ones:2'
n3 = ones_threes_nines(7)
assert n3.answer == 'nines:0, threes:2, ones:1'
n4 = ones_threes_nines(10)
assert n4.answer == 'nines:1, threes:0, ones:1'
n5 = ones_threes_nines(12)
assert n5.answer == 'nines:1, threes:1, ones:0'
n6 = ones_threes_nines(15)
assert n6.answer == 'nines:1, threes:2, ones:0'
n7 = ones_threes_nines(22)
assert n7.answer == 'nines:2, threes:1, ones:1'
n8 = ones_threes_nines(25)
assert n8.answer == 'nines:2, threes:2, ones:1'

print("Success")