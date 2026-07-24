class Car:
    def __init__(self , brand , year , model):
        self.brand = brand
        self.year = year
        self.model = model

print("Car 1")
C1 = Car("Mercedes" , 2022 , 22)


C2 = Car("BMW" , 2025 , 25)

print(C1.model)
print(C1.year)
print(C1.brand)
print("Car 2")
print(C2.model)
print(C2.brand)
print(C2.year)