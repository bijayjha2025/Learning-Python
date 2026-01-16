#Features of OOP in Python
#1. Encapsulation - Bundling data (attributes) and methods (functions) that operate on the data into a single unit known as a class. This helps to restrict direct access to some of the object's components, which can prevent the accidental modification of data. Access modifiers like public, private, and protected are used to control access to class members.

class StudentAccount:
    def __init__(self, name, balance):
        self.name = name  #public attribute
        self.__balance = balance  #private, private is indicated by double underscore before the attribute name

    def deposit(self, amount):  #public method
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def __getBalance(self):  #private method
        return self.__balance
    
    def showBalance(self):  #public method to access private method
        return self.__getBalance()
    
account = StudentAccount("Max", 1000)
account.deposit(500)
print(account.showBalance())  #Accessing private method through public method

