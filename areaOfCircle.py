class areaCircumference:
  def areaCicle(self,r):
    return (3.14 * r * r)

  def circumferenceCircle(self,r):
    return 2 * 3.14 * r

circle = areaCircumference()
r = int(input("Enter the radius of the circle: "))
print(circle.areaCicle(r))
print(circle.circumferenceCircle(r))