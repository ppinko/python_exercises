"""
https://edabit.com/challenge/ehyZvt6AJF4rKFfXT
"""

def uncensor(txt: str, vow: str) -> str:
    new_str, i = '', 0
    for j in txt:
        if j != '*':
            new_str += j
        else:
            new_str += vow[i]
            i += 1
    return new_str

"""Alternative solution 1"""

def uncensor(txt, vowels):
	txt = txt.replace('*', '{}')
	return txt.format(*vowels)

"""Alternative solution 2"""

def uncensor(txt, vowels):
	vowels = iter(vowels)
	return ''.join(next(vowels) if i == '*' else i for i in txt)

assert uncensor('Wh*r* d*d my v*w*ls g*?', 'eeioeo') == "Where did my vowels go?"
assert uncensor('abcd', '') == 'abcd' 
assert uncensor('*PP*RC*S*', 'UEAE') == 'UPPERCASE'

print("Success")
