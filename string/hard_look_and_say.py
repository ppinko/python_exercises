"""
https://edabit.com/challenge/6hnrKRh7fZfMC5CKY
"""

def look_and_say(n: int):
    n = str(n)
    l = len(n)
    if len(n) % 2 == 1:
        return 'invalid'
    new_str = ''
    k = 0
    while k < l:
        new_str += n[k+1] * int(n[k])
        k += 2
    return int(new_str)

assert look_and_say(95) == 555555555
assert look_and_say(1213141516171819) == 23456789
assert look_and_say(231) == 'invalid'

print('Success')
