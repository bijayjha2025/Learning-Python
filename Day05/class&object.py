#OOP - Object Oriented Programming, allows us to create classes and objects, which help to structure code in a more modular and reusable way. It is based on "objects" that can contain both data and functions. Data in the form of fields (often known as attributes), and functions in the form of methods.

#Class - blueprint for creating objects, and defines a set of attributes and methods that the created objects will have.
#Object - instance of a class, and can hold specific data and use the methods defined in the class. They represent real-world entities and can interact with each other.

#Creating a class
class Animal: #must start with a capital letter(here Animal is the class name)

    species = "Dog"  #class attribute
    weight = 20      #class attribute
    color = "Brown"  #class attribute
    age = 5          #class attribute
    breed = "German Shepherd" #class attribute

    #Methods - functions defined within a class that describe the behaviors of the objects created from the class
    def bark(self): #method
        return "Haha!"
    
    def info(self):   #method
        return f"This is a {self.color} {self.breed}, aged {self.age} years."

myDog = Animal() #myDog is an object (instance) of the class Animal
print(myDog.bark()) #Calling the bark method on the myDog object
print(myDog.info())
    
#Noticed? We used the self parameter in the methods. It refers to the current instance of the class and allows us to access its attributes and methods. attributes are accessed using self.attribute_name within class methods. They are defined inside the class but outside any methods. Methods are defined using the def keyword inside the class and can perform actions using the object's data. We dont have to pass self when calling the method, Python does that automatically.

#Creating another object of the same class
secondDog = Animal() #secondDog is another object (instance) of the class Animal
print(secondDog.bark())
print(secondDog.info())

#Both myDog and secondDog are separate objects of the Animal class, each with its own set of attributes and methods.

#Modifying attributes of an object
myDog.color = "White"
print(myDog.info()) #only changed for myDog object, secondDog remains unchanged
secondDog.age= 3
print(secondDog.info()) #only changed for secondDog object, myDog remains unchanged
myDog.breed = "Labrador"
print(myDog.info())

#In this way, classes and objects in Python allow us to create structured and reusable code that models real-world entities and their behaviors and alteration can be done on a per-object basis without affecting other objects of the same class.

#Important function: _init_() - special method in Python classes, known as the constructor. It is automatically called when an object of the class is created. The primary purpose of the __init__() method is to initialize the attributes of the newly created object with specific values.

class Car:
    def __init__(self, make, model, year):  #here make, model, year are parameters while self is the instance, meaning the object being created, other words can be used in place of self but by convention self is used

        self.make = make      #instance attribute
        self.model = model    #instance attribute
        self.year = year      #instance attribute

    def carInfo(self): #method to display car information
        return f"{self.year} {self.make} {self.model}"
    
myFavoriteCar = Car("Toyota", "Camry", 2020) #Creating an object of the Car class and passing values to the __init__ method
print(myFavoriteCar.carInfo()) #Calling the carInfo method to display car information

anotherCar = Car("Honda", "Civic", 2019)
print(anotherCar.carInfo())

#In this example, the __init__() method initializes the make, model, and year attributes of the Car object when it is created. Each object can have different values for these attributes, allowing for more flexibility and customization.




