"""
https://edabit.com/challenge/dKLJ4uvssAJwRDtCo
"""


def change(n: int) -> list:
    if n == 0:
        return []
    l = [500, 200, 100, 50, 20, 10]
    res = []
    for i in l:
        while True:
            if n >= i:
                res.append(i)
                n -= i
                if n == 0:
                    return res
            else:
                break


def vending_machine(products, money, product_number):
    from operator import attrgetter, itemgetter
    if product_number > 9 or product_number < 1:
        return 'Enter a valid product number'
    l = sorted(products, key=itemgetter('number'))
    if l[product_number-1]['price'] > money:
        return 'Not enough money for this product'
    else:
        change_money = money - l[product_number-1]['price']
    sub_list = change(change_money)
    d = {'product': l[product_number-1]['name'], 'change': sub_list}
    return d


products = [
    {'number': 1, 'price': 100, 'name': 'Orange juice'},
    {'number': 2, 'price': 200, 'name': 'Soda'},
    {'number': 3, 'price': 150, 'name': 'Chocolate snack'},
    {'number': 4, 'price': 250, 'name': 'Cookies'},
    {'number': 5, 'price': 180, 'name': 'Gummy bears'},
    {'number': 6, 'price': 500, 'name': 'Condoms'},
    {'number': 7, 'price': 120, 'name': 'Crackers'},
    {'number': 8, 'price': 220, 'name': 'Potato chips'},
    {'number': 9, 'price': 80, 'name': 'Small snack'}
]


assert vending_machine(products, 500, 8) == {'product': 'Potato chips', 'change': [200, 50, 20, 10]}
assert vending_machine(products, 500, 1) == {'product': 'Orange juice', 'change': [200, 200]}
assert vending_machine(products, 200, 7) == {'product': 'Crackers', 'change': [50, 20, 10]}

print("Success")
