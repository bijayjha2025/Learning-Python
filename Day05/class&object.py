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