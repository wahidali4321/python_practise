class BankAccount:
    def __init__(self , account_holder , balance):
        self.account_holder = account_holder
        self.__balance = balance


    def show_balance(self):
        return self.__balance

p1 = BankAccount("wahidali_43210" , 200)

print(p1.account_holder)
print(p1.show_balance())