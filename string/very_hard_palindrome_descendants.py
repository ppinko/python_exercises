"""
https://edabit.com/challenge/MvtxpxtFDrzEtA9k5
"""


def ispalindrome(num: str) -> bool:
    return num == num[::-1]


def palindrome_descendant(num: int) -> bool:
    n = str(num)
    while len(n) >= 2:
        if ispalindrome(n):
            return True
        temp = ''
        for i in range(len(n) // 2):
            temp += str(int(n[2*i]) + int(n[2*i + 1]))
        n = temp
    return False


assert palindrome_descendant(11211230) == True
assert palindrome_descendant(13001120) == True
assert palindrome_descendant(23336014) == True
assert palindrome_descendant(11) == True
assert palindrome_descendant(1122) == False
assert palindrome_descendant(332233) == True
print('Success')