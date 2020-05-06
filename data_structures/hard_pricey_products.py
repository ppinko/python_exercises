"""
https://edabit.com/challenge/SxevRSmRcshgwnAKp
"""


def pricey_prod(d):
    temp = sorted((zip(d.values(), d.keys())), key=lambda x: x[0], reverse=True)
    return [i[1] for i in temp if i[0] >= 500]


assert pricey_prod({'Computer' : 600, 'TV' : 800, 'Radio' : 100}) == ['TV','Computer']
assert pricey_prod({'Bike1' : 510, 'Bike2' : 401, 'Bike3' : 501}) == ['Bike1', 'Bike3']
assert pricey_prod({'Calvin Klein' : 500, 'Armani' : 5000, 'Dolce & Gabbana' : 2000}) == ['Armani', 'Dolce & Gabbana', 'Calvin Klein']
assert pricey_prod({'Loafers' : 50, 'Vans' : 10, 'Crocs' : 20}) == []
assert pricey_prod({'Dell' : 400, 'HP' : 300, 'Apple' : 1200}) == ['Apple']

print('Success')