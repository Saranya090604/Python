# create a class
# class Person:
#     # class Attributes(variables)
#     bank_name = 'SBI Bank'
#     #Methods(function)
#     def greet(self):
#         print("Welcome to SBI Bank")
#
# # create a object
# c1 = Person()
# c1.greet()
#
# c2 = Person()
# c2.greet()

# class customer:
#     def __init__(self, name, age, year):
#         self.name = name
#         self.age = age
#         self.year = year
#
# c1 = customer("Saran", 21, 2004)
# print(c1.name)
# print(c1.age)
# print(c1.year)
#
# c2 = customer("Anu", 19, 2006)
# print(c2.name)
# print(c2.age)
# print(c2.year)

class customer:
    bank_name = 'SBI BANK'

    def __init__(self, name, age, initial_amount):
        self.name = name
        self.age = age
        self.balance = initial_amount
    def deposit(self, amount):
        self.balance += amount
        print(f'deposit of {amount} is successful. updated balance is {self.balance}')

c1 = customer("Saran", 21, 5000)
c1.deposit(100)

c2 = customer("Anu", 19, 6000)
c2.deposit(100000)
