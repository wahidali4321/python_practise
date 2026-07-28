class Teacher:
    def __init__(self , name , department):
        self.name = name
        self.department = department

    def work(self):
        print("Teaching Students")

class Doctor:
    def __init__(self , name , department):
        self.name = name
        self.department = department

    def work(self):
        print("Treating patients")

class Engineer:
    def __init__(self , name , department):
        self.name = name
        self.department = department

    def work(self):
        print("Building software")

Teachers = Teacher("wahid ali" , "teaching")
Doctors = Doctor("ansha khanam" , "Doctor")
Engineers = Engineer("HAMMAD KHAN " , "eNGINNER")

for x in (Teachers , Doctors , Engineers):
    x.work()