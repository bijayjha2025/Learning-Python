
#Modules in Python => In python, we dont have to write code from scratch every time, we can use pre-written code called modules. A module is a file containing Python definitions and statements. It can define functions, classes, and variables that can be reused in other Python programs.

#There are two types of modules in Python:
#1. Built-in Modules: These are the modules that come pre-installed with Python. Examples include math, random, os, sys, datetime, etc.
#2. User-defined Modules: These are the modules created by users to organize their code into separate files for better readability and reusability.

#Importing Built-in Module
import math
print(math.sqrt(16))  #Using sqrt function to calculate square root
print(math.pi)        #Using pi constant
print(math.factorial(5))  #Using factorial function to calculate factorial
print(math.pow(2, 3))  #Using pow function to calculate power
print(math.ceil(4.3))  #Using ceil function to round up
print(math.floor(4.7))  #Using floor function to round down
#The above are some examples of using built-in math module in Python.

#Importing External Module(meaning modules that are not included in standard library or are created by third party developers)
#To use an external module, pip (package installer for Python) is used to install the module from Python Package Index (PyPI). For example, to install 'pyjokes' module, we use the command:
# python -m pip install pyjokes


import pyjokes
print("Printing jokes")
joke = pyjokes.get_joke()  #Getting a random joke using get_joke function from pyjokes module
print(joke)
#The above code demonstrates how to use an external module 'pyjokes' to fetch and print a random joke.

#pip can be understood as a package manager for Python that allows users to install, update, and manage external modules and packages easily.

