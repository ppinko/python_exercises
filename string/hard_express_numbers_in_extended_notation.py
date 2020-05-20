"""
https://edabit.com/challenge/W8QKA4YpzmeLeZWMX

Express Number in Expanded Notation

Create a function that takes a number and return a string with the number in expanded notation
(AKA expanded form). See the resources tab for details on expanded notation.


expand(13) ➞ "10 + 3"

expand(86) ➞ "80 + 6"

expand(17000000) ➞ "10000000 + 7000000"

expand(5325) ➞ "5000 + 300 + 20 + 5"
"""


def expand(n: int) -> str:
    n_str = str(n)
    return ' + '.join(str(int(v) * pow(10, len(n_str) - 1 - i))
                      for i, v in enumerate(n_str) if v != '0')


assert expand(13) == "10 + 3"
assert expand(86) == "80 + 6"
assert expand(17000000) == "10000000 + 7000000"
assert expand(420370022) == "400000000 + 20000000 + 300000 + 70000 + 20 + 2"
assert expand(70304) == "70000 + 300 + 4"
assert expand(9000000) == "9000000"
assert expand(5325) == "5000 + 300 + 20 + 5"
assert expand(2096039485293) == "2000000000000 + 90000000000 + 6000000000 + 30000000 + 9000000 + 400000 + 80000 + 5000 + 200 + 90 + 3"
assert expand(92093403034573) == "90000000000000 + 2000000000000 + 90000000000 + 3000000000 + 400000000 + 3000000 + 30000 + 4000 + 500 + 70 + 3"

print('Success')