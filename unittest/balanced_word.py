"""
https://edabit.com/challenge/WC2QgAvWYCgk6L36j
"""

def balanced(word):
        if type(word) != str:
                raise TypeError("Function expect a string parameter")
        for letter in word:
                if not letter.islower() or not letter.isalpha():
                        raise ValueError("Function expect a lowercase string without digits, punctuactions and whitespaces")
        import string
        d = {string.ascii_lowercase[i]: i+1 for i in range(len(string.ascii_lowercase))}
        l = len(word)
        if l % 2 == 0:
                left = sum(d[i] for i in word[:l//2])
                right = sum(d[i] for i in word[l//2:])
                return left == right
        else:
                left = sum(d[i] for i in word[:l//2])
                right = sum(d[i] for i in word[1 + l//2:])
                return left == right	

