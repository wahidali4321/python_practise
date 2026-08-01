class person:
    def __init__(self , name ,age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.get_age

p1 = person("wahid ali " , 22)
print(p1.name)
print(p1.get_age())