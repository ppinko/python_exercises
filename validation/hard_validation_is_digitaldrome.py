"""
https://edabit.com/challenge/P8YXBzJNysQAi8ePr
"""


def digitaldrome(n: int) -> str:
    if len(set(str(n))) == 1:
        return "Repdrome"
    elif ''.join(sorted(list(str(n)))) == str(n):
        if len(set(str(n))) == len(str(n)):
            return "Metadrome"
        else:
            return "Plaindrome"
    elif ''.join(sorted(list(str(n)), reverse=True)) == str(n):
        if len(set(str(n))) == len(str(n)):
            return "Katadrome"
        else:
            return "Nialpdrome"
    else:
        return "Nondrome"


assert digitaldrome(1357) == "Metadrome"
assert digitaldrome(12344) == "Plaindrome"
assert digitaldrome(7531) == "Katadrome"
assert digitaldrome(9874441) == "Nialpdrome"
assert digitaldrome(666) == "Repdrome"
assert digitaldrome(1985) == "Nondrome"
assert digitaldrome(33333) == "Repdrome"
assert digitaldrome(1) == "Repdrome"
assert digitaldrome(4899) == "Plaindrome"
assert digitaldrome(7521) == "Katadrome"
assert digitaldrome(23) == "Metadrome"
assert digitaldrome(2340) == "Nondrome"
assert digitaldrome(1000000) == "Nialpdrome"
assert digitaldrome(269) == "Metadrome"

print('Success')