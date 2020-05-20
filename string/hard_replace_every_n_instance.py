"""
https://edabit.com/challenge/Eou5gLqeXZu5mKjeA
"""


def replace_nth(txt: str, n, old, new) -> str:
    if n > txt.count(old) or n <= 0:
        return txt
    positions = [i for i, v in enumerate(txt) if v == old]
    lst = list(txt)
    for i in range(n-1, len(positions), n):
        lst[positions[i]] = new
    return ''.join(lst)


assert replace_nth("Sometimes it is better to just walk away from things and go back to them later when you're in a better frame of mind.", 3, "e", "_") == "Sometimes it is b_tter to just walk away from things and go back to them lat_r when you're in a b_tter frame of mind."
assert replace_nth("The clock within this blog and the clock on my laptop are 1 hour different from each other.", 1, "o", "@") == "The cl@ck within this bl@g and the cl@ck @n my lapt@p are 1 h@ur different fr@m each @ther."
assert replace_nth("Lets all be unique together until we realise we are all the same.", 4, "l", "#") == "Lets all be unique together until we rea#ise we are all the same."
assert replace_nth("Sometimes, all you NEED to do is completely make an ass of yourself and laugh it off to realise that LIFE isn't so bad AFTER all.", 2, "E", "x") == "Sometimes, all you NExD to do is completely make an ass of yourself and laugh it off to realise that LIFE isn't so bad AFTxR all.", "Tests are case sensitive."
assert replace_nth("Is it free?", 100, "e", "Y") == "Is it free?"
assert replace_nth("A glittering gem is not enough.", 0, "o", "-") == "A glittering gem is not enough."
assert replace_nth("Please wait outside of the house.", -3, "s", "s") == "Please wait outside of the house."
assert replace_nth("Joe made the sugar cookies; Susan decorated them.", 5, "e", "*") == "Joe made the sugar cookies; Susan d*corated them."
assert replace_nth("Writing a list of random sentences is harder than I initially thought it would be.", 2, "i", "3") == "Writ3ng a list of random sentences 3s harder than I in3tially thought 3t would be."
assert replace_nth("The book is in front of the table.", 3, "f", "K") == "The book is in front of the table."

print('Success')