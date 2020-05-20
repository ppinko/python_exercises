"""
https://edabit.com/challenge/zJSF5EfPe69e9sJAc
"""

def censor_string(txt, lst, char):
	newTxt = ''
	temp = ''
	lst = [i.lower() for i in lst]
	for i in txt:
		if not i.isspace():
			temp += i
			if temp.lower() in lst:
				newTxt += char * len(temp)
				temp = ''
		else:
				newTxt += temp + i
				temp = ''
	newTxt += temp
	return newTxt

assert censor_string("The cow jumped over the moon.", ["cow", "over"], "*") == "The *** jumped **** the moon."
assert censor_string("Why do my cats keep eating grass?", ["Why", "keep", "eating"], "!") == "!!! do my cats !!!! !!!!!! grass?"
assert censor_string("How do I stop myself from using python!?", ["do", "stop", "using"], "-") == "How -- I ---- myself from ----- python!?"
assert censor_string("If statements are pretty fun to use.", ["statements", "pretty", "to"], "~~") == "If ~~~~~~~~~~~~~~~~~~~~ are ~~~~~~~~~~~~ fun ~~~~ use."

print("Success")
