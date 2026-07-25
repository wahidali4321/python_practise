class Employee:
    def __init__(self , name , job_title , salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def show_employee(self):
        print(self.name , "\n" , self.job_title , "\n" , self.salary)

E1 = Employee("wahid ali" , "computer vision engineer " , 20000)
E2 = Employee("ansha khanm" , "cimputer vision engineer" , 10000)

E1.show_employee()
E2.show_employee()