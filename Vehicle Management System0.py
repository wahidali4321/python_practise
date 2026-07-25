class Vehicle:
    def __init__(self, make, model, year, rental_price):
        self.make = make
        self.model = model
        self.year = year
        self.rental_price = rental_price

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Rental Price: ${self.rental_price} per day")

    def calculate_rental(self, days):
        return days * self.rental_price

class Car(Vehicle):
    def __init__(self, make, model, year, rental_price, num_doors):
        # Call parent constructor with ONLY parent attributes
        super().__init__(make, model, year, rental_price)
        # Initialize Car's own attribute
        self.num_doors = num_doors
    
    def display_info(self):
        # Override to include door information
        super().display_info()
        print(f"Number of doors: {self.num_doors}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, rental_price, has_sidecar):
        # Call parent constructor with ONLY parent attributes
        super().__init__(make, model, year, rental_price)
        # Initialize Motorcycle's own attribute
        self.has_sidecar = has_sidecar
    
    def display_info(self):
        # Override to include sidecar information
        super().display_info()
        print(f"Has sidecar: {self.has_sidecar}")

# Testing the code
print("=" * 40)
print("CAR DETAILS:")
car1 = Car("Honda", "Civic", 2024, 5000, 4)
car1.display_info()
print(f"Rental for 5 days: ${car1.calculate_rental(5)}")

print("\n" + "=" * 40)
print("MOTORCYCLE DETAILS:")
bike1 = Motorcycle("Yamaha", "MT-07", 2023, 3000, False)
bike1.display_info()
print(f"Rental for 3 days: ${bike1.calculate_rental(3)}")