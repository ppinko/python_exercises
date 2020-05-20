"""
https://edabit.com/challenge/fnLXJnqoDFTJNZk5r
"""

def sort_contacts(names, sort):
    from operator import itemgetter
    if names == [] or names == None:
        return []
    split_name = [i.split() for i in names]
    return [' '.join(i) for i in sorted(split_name, key=itemgetter(1), reverse=(sort=='DESC'))]   

"""
Alternative solution
"""
def sort_contacts(names, sort):
	if not names: return []
	func = lambda x: x.split()[1]
	if sort == 'ASC':
		return sorted(names, key=func)
	return sorted(names, key=func, reverse=True)

assert sort_contacts(['John Locke', 'Thomas Aquinas', 'David Hume', 'Rene Descartes'], 'ASC') == ['Thomas Aquinas', 'Rene Descartes', 'David Hume', 'John Locke']
assert sort_contacts(['Paul Erdos', 'Leonhard Euler', 'Carl Gauss'], 'DESC') == ['Carl Gauss', 'Leonhard Euler', 'Paul Erdos']
assert sort_contacts(['Michael Phelps', 'Jesse Owens', 'Michael Jordan', 'Usain Bolt'], 'DESC') == ['Michael Phelps', 'Jesse Owens', 'Michael Jordan', 'Usain Bolt']
assert sort_contacts(['Al Gore', 'Barack Obama'], 'ASC') == ['Al Gore', 'Barack Obama']
assert sort_contacts(['Albert Einstein'], 'ASC') == ['Albert Einstein']
assert sort_contacts([], 'DESC') == []
assert sort_contacts(None, 'DESC') == []

print("Success")
