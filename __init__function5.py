class Student:
    def __init__(self , name , rollNo , department):
        self.name = name
        self.rollNo = rollNo
        self.department = department
        
print("Student 1")
p1 = Student("wahid ali " , "22pwdsc0054" , "Computer science and datascience")
print(p1.name)
print(p1.rollNo)
print(p1.department)

print("Student 2")

p2 = Student("ANSHA KHANAM" , "22pwdsc0054" , "computer science")
print(p2.name)
print(p2.rollNo)
print(p2.department)