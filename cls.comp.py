class Company:
    industry = "Technology"

    def __init__(self, name, num_employees):
        self.name = name
        self.num_employees = num_employees

    def update_employees(self, num_employees):
        self.num_employees = num_employees

company = Company("TechCorp", 200)
company.update_employees(220)
print(f"name: {company.name}, num_employees: {company.num_employees}, industry: {Company.industry}")