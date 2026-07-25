class Car:
    def __init__(self , brand , model , year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        print(self.brand , "\n" , self.model , "\n" , self.year)

x = Car("BMW " , "XC23" , 2022)
y = Car("MERCEDES" , "X232" , 2055)
Z = Car("HONDA " , "CIVIC" , 2022)
y.car_info()
x.car_info()
Z.car_info()