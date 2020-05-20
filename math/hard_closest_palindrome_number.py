"""
https://edabit.com/challenge/s45bQoPtMoZcj7rnR
"""


def ispalindrome(txt: str) -> bool:
    return txt == ''.join(reversed(txt))


def closest_palindrome(num: int) -> int:
    lower, higher = num -1 , num + 1
    if ispalindrome(str(num)):
        return num
    else:
        while True:
            if ispalindrome(str(lower)):
                return lower
            elif ispalindrome(str(higher)):
                return higher
            else:
                lower -= 1
                higher += 1


assert closest_palindrome(887) == 888
assert closest_palindrome(888) == 888
assert closest_palindrome(27) == 22
assert closest_palindrome(519) == 515
assert closest_palindrome(4892) == 4884
assert closest_palindrome(1) == 1
assert closest_palindrome(100) == 99
assert closest_palindrome(33344) == 33333
assert closest_palindrome(123456) == 123321
assert closest_palindrome(978215236) == 978212879

print('Success')