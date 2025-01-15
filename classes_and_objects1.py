class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

student = Student("Alice", 20, [90, 85, 88])
print("Name:", student.name, "\n","Age:", student.age, "\n","Grades:", student.grades )
