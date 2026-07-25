class person:
    def __init__(self , fname , lname):
        self.firstName = fname
        self.lastName = lname

    def greet(self):
        print(self.firstName , self.lastName)

x = person("ANSHA " , "KHANAM")
x.greet()