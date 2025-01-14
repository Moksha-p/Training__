import csv
class Employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def __repr__(self):
        return f"Employee(Name: {self.name} , Position: {self.position} , Salary: {self.salary})"
    
def read_frm_csv(file):
    employee_data = []
    with open(file, mode='r', newline='') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            employee = Employee(
                name = row['Name'],
                position = row['Position'],
                salary = row['Salary']

            )
            employee_data.append(employee)
    return employee_data
    


file = "emp_detail.csv"
employees = read_frm_csv(file)
for employee in employees:
    print(employee)

