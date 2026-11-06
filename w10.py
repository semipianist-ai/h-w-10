class BankAccount():

    def deposit(self):
        print("Money has been added to your bank account.")

    def withdraw(self):
        print("Money has been taken away from your bank account")

money = BankAccount()
print(money.deposit())
print(money.withdraw())

class Mobile():
    brand = "Iphone"
    modul = "Iphone 18"
    price = 2000

    def brand(self):
        print("Genesis walks into an Iphone store.")

    def modul(self):
        print("Genesis then buys an Iphone 18 with money from her bank account")

    def price(self):
        print("the price of the phone is 2000 euros")

device = Mobile()
print(device.brand())
print(device.modul())
print(device.price())
  