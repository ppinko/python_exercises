"""
https://edabit.com/challenge/Rvxp6owt97Tq7Qr9t
"""

import re
pattern = r"^/users/edabit/"

assert pattern.startswith("^")
assert bool(re.search(pattern, "/users/edabit/python/regex.py")) == True
assert bool(re.search(pattern, "/users/edabit/file.pyw")) == True
assert bool(re.search(pattern, "/users/edabit/python/file.txt")) == True
assert bool(re.search(pattern, "/users/edabitt/python/file.jpg")) == False
assert bool(re.search(pattern, "/uzers/file.ext")) == False
assert bool(re.search(pattern, "/users/python/file.php")) == False
assert bool(re.search(pattern, "/users/pywter/file.txt")) == False

print('Success')