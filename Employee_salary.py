class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary


p1 = Employee("wahid ali", "IT", 2000)

print("Name:", p1.name)
print("Department:", p1.department)
print("Old Salary:", p1.get_salary())

p1.set_salary(5000)

print("New Salary:", p1.get_salary())