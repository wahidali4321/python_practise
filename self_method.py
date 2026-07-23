class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi , this is khan " , self.name)

p1 = person("wahid ali " , 22)
p1.greet()