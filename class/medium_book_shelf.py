"""
https://edabit.com/challenge/uK4Dw7Pise5uCfKqo
"""


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return 'Title: {}'.format(self.title)

    def get_author(self):
        return 'Author: {}'.format(self.author)


PP = Book('Pride and Prejudice', 'Jane Austen')
H = Book('Hamlet', 'William Shakespeare')
WP = Book('War and Peace', 'Leo Tolstoy')


assert PP.title == 'Pride and Prejudice'
assert PP.author == 'Jane Austen'
assert PP.get_title() == 'Title: Pride and Prejudice'
assert PP.get_author() == 'Author: Jane Austen'

assert H.title == 'Hamlet'
assert H.author == 'William Shakespeare'
assert H.get_title() == 'Title: Hamlet'
assert H.get_author() == 'Author: William Shakespeare'

assert WP.title == 'War and Peace'
assert WP.author == 'Leo Tolstoy'
assert WP.get_title() == 'Title: War and Peace'
assert WP.get_author() == 'Author: Leo Tolstoy'

print('Success')