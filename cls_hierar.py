class Shape:
    def __init__(self,radius,side):
        self.radius = radius
        self.side = side


    
class Circle(Shape):
    def calc_area_of_circ(self):
        pi = 3.14
        area = pi * (self.radius ** 2)
        Perimeter = (self.radius *2 ) * 3.14
        return f"Circle Area: {area} , Circle Perimeter: {Perimeter}"
class Square(Shape):
    def clac_area_of_square(self):
        Area = self.side ** 2
        perimeter = self.side * 4
        return f"Square Area: {Area} , Square Perimeter: {perimeter}"
    
    

    
circle = Circle(radius = 4 , side = 5)
square = Square(radius = 4 , side = 5)



print(circle.calc_area_of_circ() ,square.clac_area_of_square())



    



  
        
        