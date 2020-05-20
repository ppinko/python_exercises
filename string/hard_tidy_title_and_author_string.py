"""
https://edabit.com/challenge/SKS6J8AHck7gq3Jbj
"""


def tidy_books(lst: list) -> list:
    temp = [ j.strip().split(' - ') for i in lst for j in i]
    return temp


assert tidy_books([["     The Catcher in the Rye - J. D. Salinger    "], ["    Brave New World - Aldous Huxley   "],
                   ["    Of Mice and Men - John Steinbeck    "]]) == \
       [["The Catcher in the Rye", "J. D. Salinger"], ["Brave New World", "Aldous Huxley"], ["Of Mice and Men", "John Steinbeck"] ]


assert tidy_books([
	["     The Grapes of Wrath - John Steinbeck    "], 
	["    Great Expectations - Charles Dickens   "], 
	["    The Scarlet Letter - Nathaniel Hawthorne    "]]) == \
       [["The Grapes of Wrath", "John Steinbeck"],
	    ["Great Expectations", "Charles Dickens"],
	    ["The Scarlet Letter", "Nathaniel Hawthorne"]
]


print('Success')