"""
https://www.geeksforgeeks.org/edit-distance-dp-5/

Given two strings str1 and str2 and below operations
that can performed on str1. Find minimum number of
edits (operations) required to convert ‘str1’ into ‘str2’.

    Insert
    Remove
    Replace

All of the above operations are of equal cost.

Applications: There are many practical applications of edit
distance algorithm, refer Lucene API for sample. Another
example, display all the words in a dictionary that are near
proximity to a given wordincorrectly spelled word.
"""


def editDistance(s1, s2, l1, l2):
    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if l1 == 0:
        return l2

    # If second string is empty, the only option is to
    # remove all characters of first string
    elif l2 == 0:
        return l1

    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    elif s1[l1 - 1] == s2[l2 - 1]:
        return editDistance(s1, s2, l1 - 1, l2 - 1)

    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    else:
        return 1 + min(editDistance(s1, s2, l1, l2 - 1),        # insert
                       editDistance(s1, s2, l1 - 1, l2),        # remove
                       editDistance(s1, s2, l1 - 1, l2 - 1))    # replace


str1 = "sunday"
str2 = "saturday"
assert editDistance(str1, str2, len(str1), len(str2)) == 3
print('Success')