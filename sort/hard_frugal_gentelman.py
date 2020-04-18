"""
https://edabit.com/challenge/RWLWKmGcbp6drWgKB
"""


def chosen_wine(wines: list):
    if len(wines) == 0:
        return None
    elif len(wines) == 1:
        return wines[0]['name']
    else:
        wines.sort(key=lambda x: x['price'])
        return wines[1]['name']


assert chosen_wine([{"name": "Wine A", "price": 8.99}, {"name": "Wine 32", "price": 13.99},
                    {"name": "Wine 9", "price": 10.99}]) == "Wine 9"
assert chosen_wine([{"name": "Wine A", "price": 8.99}, {"name": "Wine B", "price": 9.99}]) == "Wine B"
assert chosen_wine([{"name": "Wine A", "price": 8.99}]) == "Wine A"
assert chosen_wine([]) is None
assert chosen_wine([{"name": "Wine A", "price": 8.99}, {"name": "Wine 389", "price": 109.99},
                    {"name": "Wine 44", "price": 38.44}, {"name": "Wine 72", "price": 22.77}]) == "Wine 72"

print('Success')
