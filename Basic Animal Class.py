class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age} years")

class Dog(Animal):
    def __init__(self, name, species, age, breed):
        # 1. Call parent constructor
        # 2. Initialize breed
        
        # YOUR CODE HERE
        pass
    
    def make_sound(self):
        print("Woof! Woof!")

# What will this output?
dog = Dog("Rex", "Canine", 4, "Bulldog")
dog.display()
dog.make_sound()

# Question: Why do we need to call super().__init__()?
# YOUR ANSWER: 