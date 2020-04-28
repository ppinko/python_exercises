"""
https://edabit.com/challenge/yuPWwSbCGPm2KzSzx
"""


class Smoothie:

    prices = {'Strawberries': 1.50,
              'Banana': 0.50,
              'Mango': 2.50,
              'Blueberries': 1.00,
              'Raspberries': 1.00,
              'Apple': 1.75,
              'Pineapple': 3.50
              }

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_cost(self):
        return '${:.2f}'.format(sum(Smoothie.prices[i] for i in self.ingredients))

    def get_price(self):
        cost = float(self.get_cost()[1:])
        return '${:.2f}'.format(round(2.5 * cost, 2))

    def get_name(self):
        names = sorted((i.replace('berries', 'berry') if 'berries' in i else i for i in self.ingredients))
        if len(names) == 1:
            return '{} Smoothie'.format(names[0])
        else:
            return ' '.join(names) + ' Fusion'


s1 = Smoothie(["Banana"])
s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
s3 = Smoothie(["Mango", "Apple", "Pineapple"])
s4 = Smoothie(["Pineapple", "Strawberries", "Blueberries", "Mango"])
s5 = Smoothie(["Blueberries"])

assert s1.ingredients, ["Banana"]
assert s1.get_cost() == "$0.50"
assert s1.get_price() == "$1.25"
assert s1.get_name() == "Banana Smoothie"
assert s2.ingredients, ["Raspberries", "Strawberries", "Blueberries"]
assert s2.get_cost() == "$3.50"
assert s2.get_price() == "$8.75"
assert s2.get_name() == "Blueberry Raspberry Strawberry Fusion"
assert s3.ingredients, ["Mango", "Apple", "Pineapple"]
assert s3.get_cost() == "$7.75"
assert s3.get_price() == "$19.38"
assert s3.get_name() == "Apple Mango Pineapple Fusion"
assert s4.ingredients, ["Pineapple", "Strawberries", "Blueberries", "Mango"]
assert s4.get_cost() == "$8.50"
assert s4.get_price() == "$21.25"
assert s4.get_name() == "Blueberry Mango Pineapple Strawberry Fusion"
assert s5.ingredients, ["Blueberries"]
assert s5.get_cost() == "$1.00"
assert s5.get_price() == "$2.50"
assert s5.get_name() == "Blueberry Smoothie"

print('Success')