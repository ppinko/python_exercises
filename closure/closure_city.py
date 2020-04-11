def city(name):

    def population(num):
        return "Population of {0} is {1}.".format(name, num)

    return population # return function with calling it

herborn = city("Herborn")

print(herborn)

for i in range(10000, 110000, 10000):
    print(herborn(i))


