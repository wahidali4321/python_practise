class student:
    def __init__(self , name , age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

p1 = student("wahidd ali " , 22)
print(p1.name)
print(p1.get_age())