"""
https://edabit.com/challenge/rSpNwuYZSjZS6AsMv
"""

results = {
	'album': { 'id': 'cjh4E', 'type': 'album' },
	'gallery': { 'id': '59npG', 'type': 'gallery' },
	'directImage': { 'id': 'altd8Ld', 'type': 'image' },
	'image': { 'id': 'OzZUNMM', 'type': 'image' }
}


def imgurUrlParser(link: str):
    lst = link.split('/')
    if 'a' in lst:
        if lst[-1] != 'zip':
            return {'id': lst[-1], 'type': 'album'}
        else:
            return {'id': lst[-2], 'type': 'album'}
    elif lst[-2] == 'gallery':
        if '#' not in lst[-1]:
            return {'id': lst[-1], 'type': 'gallery'}
        else:
            return {'id': lst[-1].split('#')[0], 'type': 'gallery'}
    for i in lst:
        if 'i.imgur' in i:
            return {'id': lst[-1].rstrip('.png'), 'type': 'image'}
    return {'id': lst[-1], 'type': 'image'}


# Base tests
assert imgurUrlParser('http://imgur.com/a/cjh4E') == results['album']
assert imgurUrlParser('http://imgur.com/gallery/59npG') == results['gallery']
assert imgurUrlParser('http://imgur.com/OzZUNMM') == results['image']
assert imgurUrlParser('http://i.imgur.com/altd8Ld.png') == results['directImage']

# Additional tests
print(imgurUrlParser('http://imgur.com/a/cjh4E/zip'))
assert imgurUrlParser('http://imgur.com/a/cjh4E/zip') == results['album']

# assert
# 	imgurUrlParser('http://imgur.com/gallery/59npG#g1UvPtF'),
# 	results['gallery'],
# 	'Should work with a #hash at the end'
# )
# assert
# 	imgurUrlParser('www.i.imgur.com/altd8Ld.png'),
# 	results['directImage'],
# 	'Should work with www. instead of http://'
# )
# assert
# 	imgurUrlParser('i.imgur.com/altd8Ld.png'),
# 	results['directImage'],
# 	'Should work without http:// and www.'
# )

print('Success')