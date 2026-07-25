class student:
    def __init__(self , name , rollNO , department):
        self.name = name 
        self.rollNO = rollNO
        self.department = department

    def display(self):
        print(self.name , "\n" , self.rollNO , "\n" , self.department)

x = student("wahid ali" , "22pwdsc0054" , "Computer science")

x.display()