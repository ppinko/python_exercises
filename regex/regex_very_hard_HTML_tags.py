"""
https://edabit.com/challenge/AHgupTs2ELjAehzHv
"""

index = '''
<html>
<head>
	Hi! I'm a text in the head. 
	I probably shouldn't be here.
    <title>edabit.com</title>
</head>
<body>
	Hi! I'm a text in the body.
	<p>This is a parragraph and <a href="https://edabit.com">this is a link</a>.</p>
	Here comes a fake tag: <>.
</body>
</html>
'''

import re

opening_tags = "<[^/].*?>"
closing_tags = "</.*?>"
all_tags = "<.+>"

print(re.findall(opening_tags, index))
assert re.findall(opening_tags, index) == ['<html>', '<head>', '<title>', '<body>', '<p>', '<a href="https://edabit.com">']
print(re.findall(closing_tags, index))
assert re.findall(closing_tags, index) == ['</title>', '</head>',  '</a>', '</p>', '</body>', '</html>']
print(re.findall(all_tags, index))
assert re.findall(all_tags, index) == ['<html>', '<head>', '<title>edabit.com</title>', '</head>', '<body>', '<p>This is a parragraph and <a href="https://edabit.com">this is a link</a>.</p>', '</body>', '</html>']

print("Success")