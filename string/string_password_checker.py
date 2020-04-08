"""
Question:
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check 
them according to the above criteria. Passwords that match the criteria are to be printed, 
each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
"""

def check_passwd():
    x = str(input("Please enter a string of passwds separeted by comma: "))
    ls_passwd = x.split(',')
    correct_passwd = []
    def req_passwd(passwd):
        if len(passwd) < 6 or len(passwd) > 12:
            return
        flags = {"lower":False, "upper":False, "digit":False, "symbol":False}
        for char in passwd:
            if char.islower():
                flags["lower"] = True
            elif char.isupper():
                flags["upper"] = True
            elif char.isdigit():
                flags["digit"] = True
            elif char in "$#@":
                flags["symbol"] = True
        for i in flags.values():
            if i != True:
                return
        return passwd
    
    for passwd in ls_passwd:
        if req_passwd(passwd) == passwd:
            correct_passwd.append(passwd)
    return ",".join(correct_passwd)

print(check_passwd())

"""
# ALTERNATIVE SOLUTION

Solutions:
import re
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print ",".join(value)
"""
