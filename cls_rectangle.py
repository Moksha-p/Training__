class Rectangle:
    def __init__(self,length , width):
        self.length = length
        self.width = width
    def clac(self):
        self.area = self.length * self.width
        self.perimeter = 2 * (self.length + self.width)

    def __repr__(self):
        return f"Area: {self.area} , Perimeter: {self.perimeter}"
    
t1 = Rectangle(length=5 , width=3)
t1.clac()
print(t1)