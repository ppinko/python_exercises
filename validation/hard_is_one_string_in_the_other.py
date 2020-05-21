"""
https://edabit.com/challenge/rShXJNT2WQQiSiRx6
"""


def overlap(first, second) -> bool:
    if len(first) < len(second):
        a, b = first.lower(), second.lower()
    else:
        b, a = first.lower(), second.lower()
    for i in list(zip(a, b[-len(a):])):
        if i[0] == i[1] or i[0] == '*' or i[1] == '*':
            continue
        else:
            return False
    return True


assert overlap("ABC", "Ican'tsingmyABC") == True
assert overlap("abc", "Ican'tsingmyABC") == True
assert overlap("Ican'tsingmyABC", "abc") == True
assert overlap("*bc", "Ican'tsingmyABC") == True
assert overlap("abc", "Ican'tsingmy***") == True
assert overlap("ab", "Ican'tsingmy**c") == False
assert overlap("hello world", "hello") == False
assert overlap("+=", "this should work too +=") == True
assert overlap("don't forget hyphens-", "-") == True
assert overlap("don't forget periods ", ".") == False
assert overlap("this will always be true", "*") == True
assert overlap("this will always be false", "F") == False
assert overlap("hey", "*********") == True
assert overlap("a*c", "*b*") == True
assert overlap("last test", "congrats you passed the last test") == True

print("Success")