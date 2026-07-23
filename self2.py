class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, this is", self.name)

p1 = Person("Wahid Ali", 22)
p1.greet()