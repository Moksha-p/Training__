class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

triangle = Triangle(5, 3)
rectangle = Rectangle(4, 2)

print(f"Triangle area: {triangle.area()}")
print(f"Rectangle area: {rectangle.area()}")
