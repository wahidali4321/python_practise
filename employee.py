class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price


# Create two objects
mobile1 = Mobile("Samsung", "Galaxy S24", 250000)
mobile2 = Mobile("Apple", "iPhone 16", 450000)

# Print details of Mobile 1
print("Mobile 1")
print("Brand:", mobile1.brand)
print("Model:", mobile1.model)
print("Price:", mobile1.get_price())

print()

# Print details of Mobile 2
print("Mobile 2")
print("Brand:", mobile2.brand)
print("Model:", mobile2.model)
print("Price:", mobile2.get_price())

print()

# Update the price of Mobile 1
mobile1.set_price(230000)

print("After Price Update")
print("Brand:", mobile1.brand)
print("New Price:", mobile1.get_price())