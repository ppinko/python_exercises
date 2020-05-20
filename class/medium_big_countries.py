"""
https://edabit.com/challenge/smLmHK89zNoeaDSZp
"""


class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.population > 250000000 or self.area > 3000000


    def compare_pd(self, other):
        if self.population / self.area < other.population / other.area:
            return '{0} has a smaller population density than {1}'.format(self.name, other.name)
        else:
            return '{0} has a larger population density than {1}'.format(self.name, other.name)


australia = Country('Australia', 23545500, 7692024)
andorra = Country('Andorra', 76098, 468)
brazil = Country('Brazil', 202794000, 8515767)
china = Country('China', 1393000000, 9597000)
madagascar = Country('Madagascar', 26260000, 587000)


assert australia.is_big == True
assert australia.compare_pd(andorra) == 'Australia has a smaller population density than Andorra'

assert andorra.is_big == False
assert andorra.compare_pd(australia) == 'Andorra has a larger population density than Australia'

assert brazil.is_big == True
assert brazil.compare_pd(china) == 'Brazil has a smaller population density than China'

assert china.is_big == True
assert china.compare_pd(madagascar) == 'China has a larger population density than Madagascar'

assert madagascar.is_big == False
assert madagascar.compare_pd(australia) == 'Madagascar has a larger population density than Australia'


print('Success')