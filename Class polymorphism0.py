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
        print('SAIL')

class plane:
    def __init__(self , model , brand):
        self.model = model
        self.brand = model

    def move(self):
        print('Fly!')

Car1 = Car("honda " , "Civic")
Boat1 = Boat("SAMSUNG" , "I8")
plane1 = plane("PIA" , "samsung")

for x in (Car1 , Boat1 , plane1):
    x.move()