"""
https://edabit.com/challenge/JDhs7peiN8nAnnFWz

Create a function that validates a password to conform to the following rules:

    Length between 6 and 24 characters.
    At least one uppercase letter (A-Z).
    At least one lowercase letter (a-z).
    At least one digit (0-9).
    Maximum of 2 repeated characters.
        "aa" is OK 👍
        "aaa" is NOT OK 👎
    Supported special characters:
        ! @ # $ % ^ & * ( ) + = _ - { } [ ] : ; " ' ? < > , .
"""


from collections import Counter


def validate_password(passwd: str) -> bool:
    if len(passwd) < 6 or len(passwd) > 24:
        return False
    c = Counter(passwd)
    if not all(True if i <= 2 else False for i in c.values()):
        return False
    if not any(True if i.islower() else False for i in c.keys()):
        return False
    if not any(True if i.isupper() else False for i in c.keys()):
        return False
    if not any(True if i.isdigit() else False for i in c.keys()):
        return False
    return True


# INVALID PASSWORDS
assert validate_password("P1zz@") == False
assert validate_password("P1zz@P1zz@P1zz@P1zz@P1zz@") == False
assert validate_password("mypassword11") == False
assert validate_password("MYPASSWORD11") == False
assert validate_password("iLoveYou") == False
assert validate_password("Repeeea7!") == False
# VALID PASSWORDS
assert validate_password("H4(k+x0") == True
assert validate_password("Fhg93@") == True
assert validate_password("aA0!@#$%^&*()+=_-{}[]:;\"") == True
assert validate_password("zZ9'?<>,.") == True

print('Success')