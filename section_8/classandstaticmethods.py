class Employee:
    company = "Hp"
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
    #instance method - default
    def print_info(self):
        info =  f"The name is {self.name} and salary is {self.salary}"
        print(info)

    #static method
    @staticmethod
    def sum(a,b):
        return (a+b)

    # class methods
    @classmethod
    def print_company(cls):
        print(cls.company)
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


e1 = Employee("Jack", 3455)
e2 = Employee("Jill", 3455)
# print(Employee.company) # class atrribut
# print(Employee.name) #instance attribute not accesible therefore error
e1.print_info() #instancce methods
print(e2.sum(3,4)) #static method
e1.print_company() #class method
print(Employee.company)
e1.change_company("Dell")
e1.print_company()
print(Employee.company)
