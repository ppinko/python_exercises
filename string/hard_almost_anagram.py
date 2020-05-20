"""
https://edabit.com/challenge/APNhiaMCuRSwALN63
"""


def almost_palindrome(txt: str) -> bool:
    counter = 0
    while len(txt) > 1:
        if txt[0] != txt[-1]:
            counter += 1
        txt = txt[1:-1]
    if counter > 1 or counter == 0:
        return False
    return True


# Test.assert_equals(almost_palindrome("ggggg"), False, 'Should return false if already palindrome.')
assert almost_palindrome("abcdcbg") == True
assert almost_palindrome("abccia") == True
assert almost_palindrome("abcdaaa") == False
print('Success')