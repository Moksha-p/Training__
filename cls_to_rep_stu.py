class Student():
    def __init__(self,name,age,grades):
        self.name = name
        self.age = age
        self.grades = grades
    def display(self):
        return f"Name: {self.name} , Age: {self.age} , Grades: {self.grades}"
    

t1 = Student(name = "Alice", age = 20, grades = [90, 85, 88])
print(t1.display())
