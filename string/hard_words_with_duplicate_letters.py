"""
https://edabit.com/challenge/WS6hR6b9EZzuDTD26
"""


def no_duplicate_letters(phrase):
    l = phrase.split()
    return all(True if len(set(i)) == len(i) else False for i in l) 
            
assert no_duplicate_letters("Easy does it.") == True
assert no_duplicate_letters("So far, so good.") == False
assert no_duplicate_letters("Better late than never.") == False

print("Success")
