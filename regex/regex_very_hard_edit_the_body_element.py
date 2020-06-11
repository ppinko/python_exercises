"""
https://edabit.com/challenge/7DrvnMeY2Ebzk2mfH
"""

import re

body_insert = "(?<=<body>\n)"
body_append = "(?=\n</body>)"
body_rewrite = "(?<=<body>\n)[\s\S]+(?=\n</body>)"

index = '''
<html>
<head>
    <title>edabit.com</title>
</head>
<body>
    <p>This is a paragraph and <a href="https://edabit.com">this is a link</a>.</p>
	<p>Second paragraph</p>
	<p>Third paragraph</p>
	<p>Fourth paragraph</p>
</body>
</html>
'''

res1 = '''
<html>
<head>
    <title>edabit.com</title>
</head>
<body>
	<p>Pre-Paragraph</p>
    <p>This is a paragraph and <a href="https://edabit.com">this is a link</a>.</p>
	<p>Second paragraph</p>
	<p>Third paragraph</p>
	<p>Fourth paragraph</p>
</body>
</html>
'''

res2 = '''
<html>
<head>
    <title>edabit.com</title>
</head>
<body>
    <p>This is a paragraph and <a href="https://edabit.com">this is a link</a>.</p>
	<p>Second paragraph</p>
	<p>Third paragraph</p>
	<p>Fourth paragraph</p>
	<p>Post-Paragraph</p>
</body>
</html>
'''

res3 = '''
<html>
<head>
    <title>edabit.com</title>
</head>
<body>
	<p>Anti-Paragraph</p>
</body>
</html>
'''


# print(re.sub(body_insert, '	<p>Pre-Paragraph</p>\n', index))
assert re.sub(body_insert, '	<p>Pre-Paragraph</p>\n', index) == res1
# print(re.sub(body_append, '\n	<p>Post-Paragraph</p>', index))
assert re.sub(body_append, '\n	<p>Post-Paragraph</p>', index) == res2
# print(re.sub(body_rewrite, '	<p>Anti-Paragraph</p>', index))
assert re.sub(body_rewrite, '	<p>Anti-Paragraph</p>', index) == res3

print("Success")