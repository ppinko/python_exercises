"""
https://edabit.com/challenge/G2hLjbHqwCo9TaS6T
"""


def reverse(txt: str) -> str:
    temp = list(reversed([i for i in txt if i.isalpha()]))
    j = 0
    ans = ''
    for i in range(len(txt)):
        if txt[i].isalpha():
            ans += temp[j]
            j += 1
        else:
            ans += txt[i]
    return ans


assert reverse("ab89c") == "cb89a"
assert reverse("jkl5mn923o") == "onm5lk923j"
assert reverse("123a45") == "123a45"
assert reverse("a1b1c") == "c1b1a"

print('Success')