"""
https://edabit.com/challenge/7AA54JmzruLMwG6do
"""


def is_icecream_sandwich(txt: str) -> bool:
    if len(txt) < 3 or len(set(txt)) != 2:
        return False
    return txt == ''.join(list(reversed(txt)))


assert is_icecream_sandwich("") == False
assert is_icecream_sandwich("AABBBAA") == True
assert is_icecream_sandwich("3&&3") == True
assert is_icecream_sandwich("yyyyymmmmmmmmyyyyy") == True
assert is_icecream_sandwich("hhhhhhhhmhhhhhhhh") == True
assert is_icecream_sandwich("CDC") == True
assert is_icecream_sandwich("BBBBB") == False
assert is_icecream_sandwich("AAACCCAA") == False
assert is_icecream_sandwich("AACDCAA") == False
assert is_icecream_sandwich("AAABB") == False
assert is_icecream_sandwich("AA") == False
assert is_icecream_sandwich("A") == False

print('Success')