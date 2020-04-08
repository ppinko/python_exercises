"""
https://edabit.com/challenge/yGBevdRmXvSyTaBSA
"""

drinks = [
  {"name": "lemonade", "price": 50},
  {"name": "lime", "price": 10}
]

def sort_drinks_by_price(drinks):
    sorted(drinks, key = lambda x: x["price"])

print(sort_drinks_by_price(drinks))
