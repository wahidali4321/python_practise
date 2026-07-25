class person:
    def __init__(self , fname , lname):
        self.firstName = fname
        self.lastName = lname

    def printName(self):
        print(self.firstName , self.lastName)

class Student(person):
    def __init__(self, fname, lname):
        person.__init__(self ,fname, lname)

x = Student("wahid " , "ali")
x.printName()