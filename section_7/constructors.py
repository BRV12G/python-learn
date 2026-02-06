class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_Salary(self):
        return self.salary

    def get_info(self):
        return print(f"the name of the employee is {self.name} and the salary is {self.get_Salary()} and the bond is {self.bond}")


e = Employee(34000,"john", 4)
print(e.get_info())
