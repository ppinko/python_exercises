"""
https://edabit.com/challenge/tRHaoWNaHBJCYD5Nx
"""


def same_letter_pattern(first, second):
    for i, v in enumerate(first):
        L_first, L_second = [i], [i]
        first_find = first.find(v, i+1)
        while first_find != -1:
            L_first.append(first_find)
            first_find += 1
            first_find = first.find(v, first_find)
        second_find = second.find(second[i], i+1)
        while second_find != -1:
            L_second.append(second_find)
            second_find += 1
            second_find = second.find(second[i], second_find)
        if L_first != L_second:
            return False
    return True


""" Alternative solution """


def same_letter_pattern(txt1, txt2):
	d = {}
	for i in range(len(txt1)):
		if txt1[i] not in d:
			d[txt1[i]] = txt2[i]
	return ''.join(d[k] for k in txt1)==txt2


assert same_letter_pattern('ABCBA', 'BCDCB') == True
assert same_letter_pattern('AAAA', 'BBBB') == True
assert same_letter_pattern('BAAB', 'ABBA') == True
assert same_letter_pattern('BAAB', 'QZZQ') == True
assert same_letter_pattern('TTZZVV', 'PPSSBB') == True
assert same_letter_pattern('ZYX', 'ABC') == True
assert same_letter_pattern('AABAA', 'SSCSS') == True
assert same_letter_pattern('AABAABAA', 'SSCSSCSS') == True
assert same_letter_pattern('UBUBUBUB', 'WEWEWEWE') == True
assert same_letter_pattern('FFGG', 'FFG') == False
assert same_letter_pattern('FFGG', 'CDCD') == False
assert same_letter_pattern('FFFG', 'GGHI') == False
assert same_letter_pattern('FFFF', 'ABCD') == False
assert same_letter_pattern('ABCA', 'ABCD') == False
assert same_letter_pattern('ABCAAA', 'DDABCD') == False

print('Success')