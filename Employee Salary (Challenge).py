class Employee:
    def __init__(self , name , department , salary):
        self.name = name
        self.department = department
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(new_salary):
        return new_salary

p1 = Employee("wahid ali" , 2000)
print(p1.name)


    