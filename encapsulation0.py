class person:
    def __init__(self , name , age):
        self.name = name
        self._age = age

p1 = person("wahid ali " , 22)
print(p1.name)
print(p1._age)