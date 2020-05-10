"""
https://edabit.com/challenge/ia95ckhN5ztgfJHe4

Valid JavaScript Comments

In JavaScript, there are two types of comments:

    Single-line comments start with //
    Multi-line or inline comments start with /* and end with */

The input will be a sequence of //, /* and */. Every /* must have a */ that immediately follows it. To add, there can
be no single-line comments in between multi-line comments in between the /* and */.

Create a function that returns True if comments are properly formatted, and False otherwise.
"""


def comments_correct(txt: str) -> bool:
    if len(txt) % 2 == 1:
        return False
    lst = [txt[2*i: 2*i + 2]for i in range(0, len(txt) // 2)]
    n = 0
    while n < len(lst):
        if lst[n] == '*/':
            return False
        elif lst[n] == '/*':
            if lst[n+1] != '*/':
                return False
            n += 2
        else:
            n += 1
    return True


assert comments_correct("//////") == True
assert comments_correct("/**//**////**/") == True
assert comments_correct("/**//**//**//**/") == True
assert comments_correct("///**///") == True
assert comments_correct("/**//////**//**////**/////") == True
assert comments_correct("//") == True
assert comments_correct("/**/") == True
assert comments_correct("///*/**/") == False
assert comments_correct("//*/**/") == False
assert comments_correct("/////") == False
assert comments_correct("///") == False
assert comments_correct("/**///**/") == False
assert comments_correct("/**/////**/") == False

print('Success')