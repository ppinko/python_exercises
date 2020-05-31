"""
https://edabit.com/challenge/JJHD7FeBxBEaK87hG
"""

import re
pattern = r"\.py$|\.pyw$"

assert pattern.endswith("$")
assert bool(re.search(pattern, "/users/file.py")) == True
assert bool(re.search(pattern, "/users/file.pyw")) == True
assert bool(re.search(pattern, "/users/file.opy")) == False
assert bool(re.search(pattern, "/users/file.jpg")) == False
assert bool(re.search(pattern, "/users/file.ext")) == False
assert bool(re.search(pattern, "/users/python/file.php")) == False
assert bool(re.search(pattern, "/users/pywter/file.txt")) == False

print('Success')