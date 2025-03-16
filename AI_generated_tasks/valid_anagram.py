"""
Valid Anagram

Given two strings, s and t, return True if t is an anagram of s, and False
otherwise. An anagram is a word formed by rearranging the letters of another word.

Example Input 1:
s = "listen"
t = "silent"

Expected Output:
True

Example Input 2:
s = "hello"
t = "world"

Expected Output:
False

Constraints:
-   Solve in O(n) time complexity.
-   Can you solve it without sorting?

Bonus Challenge:
-   Solve it without using extra space.
"""


def validAnagram_1(s: str, t: str) -> bool:
    """
    Using sorting method. The simplest method.
    """
    return sorted(s) == sorted(t)


print(validAnagram_1("listen", "silent"))  # True
print(validAnagram_1("hello", "world"))  # False
