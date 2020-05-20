"""
https://edabit.com/challenge/Fpymv2HieqEd7ptAq
"""


def split(txt: str) -> list:
    res = []
    if txt == '':
        return res
    temp = 0
    temp_str = ''
    for i in txt:
        if i == '(':
            temp += 1
            temp_str += i
        elif i == ')':
            temp -= 1
            temp_str += i
        if temp == 0:
            res.append(temp_str)
            temp_str = ''
    return res


assert split("()()()") == ["()", "()", "()"]
assert split("") == []
assert split("()()(())") == ["()", "()", "(())"]
assert split("(())(())") == ["(())", "(())"]
print('Success')