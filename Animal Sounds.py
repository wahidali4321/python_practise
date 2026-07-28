class Dog:
    def __init__(self , name):
        self.name = name

    def sound(self):
        print("Bark")

class Cat:
    def __init__(self , name):
        self.name = name

    def sound(self):
        print("Meow")

class Cow:
    def __init__(self , name):
        self.name = name

    def sound(self):
        print("MOO")

Dog1 = Dog("Dog")
Cat1 = Cat("cat")
Cow1 = Cow("Cow")

for x in (Dog1 , Cat1 ,  Cow1):
    x.sound()