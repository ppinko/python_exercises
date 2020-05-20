class Rectangular:

    def __init__(self, bottom, height):
        self.b = bottom
        self.h = height

    def area(self):
        return self.b * self.h

class Square (Rectangular):

    def __init__(self, bottom):
        super().__init__(bottom, bottom)

class Cube(Square):
        
    def volume(self):
        face = super().area()
        return face * self.b


"""
Examples
"""

shape_1 = Rectangular(3, 4)
shape_2 = Square(5)
shape_3 = Cube(3)
print(shape_1.b, shape_1.h, shape_1.area())
print(shape_2.b, shape_2.h, shape_2.area())
print(shape_3.b, shape_3.volume())
