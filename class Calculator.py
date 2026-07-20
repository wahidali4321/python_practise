class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


p1 = Calculator()
p2 = Calculator()
p3 = Calculator()
p4 = Calculator()

print(p1.add(11, 11))
print(p2.subtract(11, 11))
print(p3.multiply(11, 11))
print(p4.divide(11, 11))