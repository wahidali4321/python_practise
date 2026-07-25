class Animal:
    def __init__(self , name , species , age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        print("HAANGGGGGGGG")

A = Animal("Dog" , "German sherfar " , 12)
A.make_sound()