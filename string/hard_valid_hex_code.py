"""
https://edabit.com/challenge/9p5tMqyYENTmD9Nh5
"""


def is_valid_hex_code(txt: str) -> bool:
    return txt[0] == '#' and len(txt) == 7 and \
           all(True if i.isdigit() or i.lower() in {'a', 'b', 'c', 'd', 'e', 'f'}
               else False for i in txt[1:])


" Alternative solution "

import re

def is_valid_hex_code(txt):
	return bool(re.match(r'#[A-Fa-f0-9]{6}$', txt))


assert is_valid_hex_code('#CD5C5C') == True
assert is_valid_hex_code('#EAECEE') == True
assert is_valid_hex_code('#eaecee') == True
assert is_valid_hex_code('#CD5C58C') == False
assert is_valid_hex_code('#CD5C5Z') == False
assert is_valid_hex_code('#CD5C&C') == False
assert is_valid_hex_code('CD5C5C') == False
assert is_valid_hex_code('#123CCCD') == False
assert is_valid_hex_code('#123456') == True
assert is_valid_hex_code('#987654') == True
assert is_valid_hex_code('#9876543') == False
assert is_valid_hex_code('#CCCCCC') == True
assert is_valid_hex_code('#ZCCZCC') == False
assert is_valid_hex_code('#Z88Z99') == False
assert is_valid_hex_code('#Z88!99') == False

print('Success')