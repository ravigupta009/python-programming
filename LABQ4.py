class Employee:
    def calculate_salary(self):
        return 50000

class Manager(Employee):
    
    def calculate_salary(self):
        base_salary = super().calculate_salary()
        bonus = 20000
        return base_salary + bonus


emp = Employee()
mgr = Manager()

print(f"Standard Employee Salary: ${emp.calculate_salary()}")
print(f"Manager Salary: ${mgr.calculate_salary()}")