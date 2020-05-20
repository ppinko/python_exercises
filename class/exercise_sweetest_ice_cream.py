"""
https://edabit.com/challenge/uerTkWm9K3oMtMZKz

Create a function which takes a list of objects from the class IceCream
and returns the sweetness value of the sweetest icecream.

Sweetness is calculated from the flavor and number of sprinkles. Each
sprinkle has a sweetness value of 1, and the sweetness values for the
flavors are as follows:

Flavours	Sweetness Value
Plain	        0
Vanilla	        5
ChocolateChip	5
Strawberry	10
Chocolate	10

You'll be given instance attributes in the order flavor, num_sprinkles.

Examples:
ice1 = IceCream("Chocolate", 13)         # value of 23
ice2 = IceCream("Vanillla", 0)           # value of 5
ice3 = IceCream("Strawberry", 7)         # value of 17
ice4 = IceCream("Plain", 18)             # value of 18
ice5 = IceCream("ChocolateChip", 3)      # value of 8

Tests:
sweetest_icecream([ice1, ice2, ice3, ice4, ice5]) ➞ 23
sweetest_icecream([ice3, ice1]) ➞ 23
sweetest_icecream([ice3, ice5]) ➞ 17
"""

class IceCream:

    d_sweet = dict(Plain=0, Vanillla=5, ChocolateChip=5, Strawberry=10, Chocolate=10)

    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.num_sprinkles = sprinkles
        self.sweet_num = IceCream.d_sweet[self.flavor] + self.num_sprinkles 

    def __gt__(self, other):
        return self.sweet_num > other.sweet_num

def sweetest_icecream(lst):
    return max(lst).sweet_num

ice1 = IceCream("Chocolate", 13)         # value of 23
ice2 = IceCream("Vanillla", 0)           # value of 5
ice3 = IceCream("Strawberry", 7)         # value of 17
ice4 = IceCream("Plain", 18)             # value of 18
ice5 = IceCream("ChocolateChip", 3)      # value of 8
    
print(sweetest_icecream([ice1, ice2, ice3, ice4, ice5]))
