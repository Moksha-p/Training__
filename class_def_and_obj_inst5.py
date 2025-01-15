class School:
    total_students = 0

    def __init__(self, name, students):
        self.name = name
        self.students = students
        School.total_students += students

    def enroll_students(self, num_students):
        self.students += num_students
        School.total_students += num_students

school = School("Greenwood High", 300)
school.enroll_students(50)
print(f"name: {school.name}, students: {school.students}, total_students: {School.total_students}")
