class Student:
    def __init__(self , name , age , grades):
        self.name = name
        self.age = age
        self.grades = grades
student1 = Student("Sarthak" , 20 , [90 , 85 , 88])

print(f"name: {student1.name} ,age: {student1.age} ,grades: {student1.grades}")