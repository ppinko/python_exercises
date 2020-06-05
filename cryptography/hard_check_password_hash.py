"""
https://edabit.com/challenge/37BFkDdipm8qCk2WA
"""


user_pass_db = [{"username" : "tony", "pass_hash" : "11725d3f4588325f1c90c50348624dcc55978f39"},
                {"username" : "jason", "pass_hash" : "5a6d719f958b1a610712f8e342ef0a4dd4b80a35"},
                {"username" : "lola", "pass_hash" : "7dda6e1b3988b488b0821e24732ca42d6b72f0ce"},
                {"username" : "dan", "pass_hash" : "ec09d3b165aeabf77f5c9436c2d644b6e2f31ba9"}]


import hashlib


def check_pass(name: str, passwd: str) -> bool:
    global user_pass_db
    hashed = ''
    for i in user_pass_db:
        if i['username'] == name:
            hashed = i['pass_hash']
    m = hashlib.sha1(passwd.encode())
    return hashed == m.hexdigest()


assert check_pass("lola","jimbob") == True
assert check_pass("tony", "hexagon") == True
assert check_pass("jason", "tyrannosaurus") == True
assert check_pass("dan", "FranklinPierce123") == True
assert check_pass("somebot", "admin123") == False
assert check_pass("lola","wrongpass") == False

print("Success")