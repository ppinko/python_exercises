"""
https://edabit.com/challenge/Rn3g3hokznLu8ZtDP
"""


def increment_string(s: str) -> str:
    if not s[-1].isdigit():
        return s + '1'
    beg, end = '', ''
    for i, v in enumerate(s):
        if v.isdigit():
            end += v
        else:
            beg += v
    new_end = int(end) + 1
    if len(str(new_end)) != len(end):
        k = len(end) - len(str(new_end))
        return beg + '0' * k + str(new_end)
    return beg + str(new_end)


assert increment_string("foo") == "foo1"
assert increment_string("foobar01002") == "foobar01003"
assert increment_string("foobar00599") == "foobar00600"
assert increment_string("foo099") == "foo100"
assert increment_string("foo09999") == "foo10000"
print('Success')