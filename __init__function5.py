class Student:
    def __init__(self , name , rollNo , department):
        self.name = name
        self.rollNo = rollNo
        self.department = department

print("student 2")

p1 = Student()
p1.name = "wahid ali"
p1.rollNo = "22pwdsc0054"
p1.department = "Computer science and datascience"

print("student 2")

p2 = Student()
p2.name = "hammad khan "
p2.rollNo = "006"
p2.department = "prep"

print(p1.name)
print(p1.rollNo)
print(p1.department)
print(p2.name)
print(p2.department)
print(p2.rollNo)