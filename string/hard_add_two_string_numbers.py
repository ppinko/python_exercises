"""
https://edabit.com/challenge/bwCDG9X8cJiAdvfxE
"""


def add_str_nums(s1: str, s2: str) -> str:
    l = [s1, s2]
    tot = 0
    for i in l:
        if i == '':
            continue
        try:
            k = int(i)
            tot += k
        except ValueError:
            return '-1'
    return str(tot)


assert add_str_nums("", "") == "0"
assert add_str_nums("1", "01") == "2"
assert add_str_nums("1","") == "1"

print('Success')