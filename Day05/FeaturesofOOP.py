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

#2. Inheritance - A mechanism where a new class (derived class) inherits attributes and methods from an existing class (base class). This promotes code reusability and establishes a hierarchical relationship between classes. It can be single, multiple, or multilevel inheritance.

class Books:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class EBook(Books): #Derived class inheriting from base class Books
    def __init__(self, title, author, price, page):
        super().__init__(title, author, price)
        self.page = page

ebook = EBook("Python Programming", "John Doe", 29.99, 350)
print(f"EBook Title: {ebook.title}, Author: {ebook.author}, Price: {ebook.price}, Pages: {ebook.page}")

#This is a single inheritance example where EBook class inherits from Books class. To show inheritance, we create an instance of EBook and access attributes from the Books class. super() is used to call the constructor of the base class within the derived class. It helps to initialize the inherited attributes properly. 

#3. Polymorphism - ability of different classes to be treated as instances of the same class through a common interface. It allows methods to do different things based on the object it is acting upon, even if they share the same name. This can be achieved through method overriding and operator overloading.

class Brands:
    def showBrand(self):
        return "This is a popular brand."
    
class Shoe(Brands):
    def showBrand(self):  #Overriding the method from base class, overriding means providing a new implementation of a method in the derived class that already exists in the base class with the same name, same parameters.
        return "This is a popular shoe brand."
    
class Bag(Brands):
    def showBrand(self):  #Overriding the method from base class
        return "This is a popular bag brand."
    
shoe = Shoe()
bag = Bag()
print(shoe.showBrand())
print(bag.showBrand())


#In this example, both Shoe and Bag classes override the showBrand method from the Brands class. When we call showBrand on instances of Shoe and Bag, it executes the respective overridden methods, demonstrating polymorphism.

