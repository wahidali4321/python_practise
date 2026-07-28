class CreditCard:
    def __init__(self , amount_holder , amount):
        self.amount_holder = amount_holder
        self.amount = amount


    def pay(self):
        print("Payment made using Credit Card")

class PayPal:
    def __init__(self , amount_holder , amount):
        self.amount_hodler = amount_holder
        self.amount = amount

    def pay(self):
        print("Payment made using PayPal")

class Cash:
    def __init__(self , amount_holder , amount):
        self.amount_holder = amount_holder
        self.amount = amount

    def pay(self):
        print("Payment made using Cash")

Credit = CreditCard("wahid ali"  , 200000)
pays = PayPal("hammad" , 1000)
cashs = Cash("ansha khanam" , 23000)

for x in (Credit , pays , cashs):
    x.pay()

    