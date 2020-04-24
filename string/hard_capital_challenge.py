"""
https://edabit.com/challenge/eBTCwYHpdaHciieuP
"""


def select_letters(s1, s2):
	ls = []
	end = []
	for i in zip(s1, s2):
		if i[1].isupper():
			ls.append(i[0])
		if i[0].isupper():
			end.append(i[1])
	return ''.join(ls + end)


assert select_letters("heLLO", "GUlp") == "help"
assert select_letters("1234567", "XxXxX") == "135"
assert select_letters("EVERYTHING", "SomeThings") == "EYSomeThings"
print('Success')