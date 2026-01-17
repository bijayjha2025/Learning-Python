#Magic Methods in Python
#Magic methods (also known as dunder methods) are special methods in Python that start and end with double underscores (__). They allow you to define how objects of your class behave with built-in operations, such as arithmetic operations, comparisons, and type conversions. By implementing these methods, you can customize the behavior of your objects in a way that feels natural and intuitive. Eg: __init__, __str__, __add__, __len__, etc.

#Example 1: Using __init__ and __str__ magic methods
class Person:
    def __init__(self, name, age):  #Constructor method to initialize attributes
        self.name = name
        self.age = age

    def __str__(self):  #String representation of the object
        return f"Person(Name: {self.name}, Age: {self.age})"
    
person1 = Person("Max", 30)
print(person1)  #This will call the __str__ method

#Example 2: Using __add__ magic method to add two objects
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  #Defining addition for Vector objects
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

vector1 = Vector(2, 3)
vector2 = Vector(5, 7)
result_vector = vector1 + vector2  #This will call the __add__ method
print(result_vector)

#Example 3: Using __len__ magic method to get the length of an object
class CustomList:
    def __init__(self, elements):
        self.elements = elements

    def __len__(self):  #Defining length for CustomList objects
        return len(self.elements)

my_list = CustomList([1, 2, 3, 4, 5])
print(len(my_list))  #This will call the __len__ method
#In this example, we defined a CustomList class that uses the __len__ method to return the number of elements in the list. When we call len(my_list), it invokes the __len__ method we defined.

#These are just a few examples of magic methods in Python. There are many more magic methods available that you can implement to customize the behavior of your classes and objects. Exploring and using magic methods can greatly enhance the functionality and usability of your custom classes.
