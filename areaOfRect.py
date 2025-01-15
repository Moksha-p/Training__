class Rect:
    def area(self , len , w):
        return len * w
    def perimeter(self , len , w):
        return (len + w) * 2

r = Rect()
print("area: ",r.area(5,3))
print("perimeter: ",r.perimeter(5,3))