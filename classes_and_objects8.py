import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        ar = math.pi*(self.radius**2)
        return ar

    def circumference(self):
        per = 2*(math.pi)*(self.radius)  
        return per  


circle = Circle(4)

print("Area:", circle.area(), "Circumference:", circle.circumference())