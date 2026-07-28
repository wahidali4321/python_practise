class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    def move(self):
        print("swim")

class plane:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

Car1 = Car("Honda " , "Honda civic")
Boat1 = Boat("Mercedes " , "Mxc")
plane1 = plane("PIA" , "private")

for x in (Car1 , Boat1 , plane1):
    x.move()

