class person:
    def __init__(self , name , age):
        self.name = name
        self.__age = age

p1 = person("wahid ali " , 22)
print(p1.name)
print(p1.get_age())