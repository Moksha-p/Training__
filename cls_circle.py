class Circle:
    def __init__(self,radius):
        self.radius = radius

    def calc(self):
        pi = 3.14
        area = pi * (self.radius ** 2)
        circumference = 2 * pi * self.radius
        return f"Area: {area} , Circumference: {circumference}"
    
t1 = Circle(radius = 4)
print(t1.calc())
