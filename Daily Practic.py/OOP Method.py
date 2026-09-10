# class students:
#     def __init__(self,name, age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print("name:", self.name)
#         print("age:" ,self.age)

# student1=students("Ravi", 22)
# student1.display()

# Car naam ki class banao. brand aur model attributes rakho. start() method banao jo "Car is starting" print kare. 2 car objects banao aur unka data print karo.

# class car:
#     def __init__(self, brand, model):
#         self.brand=brand
#         self.model=model

#     def start(self):
#         print("car is starting")

# car1=car("fortuner","toyota")
# car2=car("BMW","X5")

# print("car1:", car1.brand, car1.model)
# print("car2:", car2.brand, car2.model)

# car1.start()
# car2.start()

#       ______ HINt ______
"""
class Car: → Car ki class banayi
__init__() → brand aur model set karta hai
self.brand / self.model → object ke attributes
start() → method
car1 aur car2 → 2 objects of Car class 
"""
# Rectangle Class Rectangle naam ki class banao.
# class Rectangle:
#     def __init__(self, length, width):
#         self.length=length
#         self.width=width

#     def area(self):
#         print(f"area : {self.length * self.width}")

# areas=Rectangle(15,7)
# areas.area()

# class Bank_account:
#     def __init__(self, account_holder, balance):
#         self.account_holder= account_holder
#         self.balance= balance

#     def deposite(self, amount):
#         self.balance=self.balance+amount

#     def show_balance(self):
#         print("current_balance", self.balance)

# account1=Bank_account("Ravi", 5000)

# account1.show_balance()
# account1.deposite(2000)
# account1.show_balance()


# ------ Bank account manage: Deposite, Withdraw ------ Normal Function
"""def deposite(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("insufficent balance")
        return balance
    return balance - amount

balance = 0
balance = deposite(balance, 1000)
print(balance)
balance = withdraw(balance, 400)
print(balance)
"""

#  ------ Bank account manage: Deposite, Withdraw ------ OOP Method
class Account:
    def __init__(self, balance):
        self.balance = balance
    def deposite(self, amount):
        self.balance=self.balance + amount
        print(f"{amount} is deposite! \nNew balance is {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficent balance!")
        else:
            self.balance = self.balance - amount
            print(self.balance)

# Ravi=Account(5000)
# Ravi.deposite(1000)
# Ravi.withdraw(2000)

Priya=Account(2000)
Priya.deposite(500)
Priya.withdraw(900)



