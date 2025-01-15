import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * (self.radius ** 2), 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

circle = Circle(4)
square = Square(5)

print(f"Circle area: {circle.area()}, Circle perimeter: {circle.perimeter()}")
print(f"Square area: {square.area()}, Square perimeter: {square.perimeter()}")
