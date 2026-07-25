class Vehical:
    def __init__(self, make , model , year , rental_price):
        self.make = make
        self.model = model
        self.year = year
        self.rental_price = rental_price

    def display_info(self):
        print(self.make , "\n" , self.model , "\n" , self.year , "\n" , self.rental_price)

    def calculate_rental(self, days):
        return days * 5000

class Car(Vehical):
    def __init__(self, make, model, year, rental_price , num_doors):
        super.__init__(make, model, year, rental_price , num_doors)

C1 = Car("Honda " , 18 , 2024 , 5000 , 4)
C1.display_info()

class Motorcycle(Vehical):
    def __init__(self, make, model, year, rental_price , has_sidecar):
        super().__init__(make, model, year, rental_price , has_sidecar)

        


    