
def greet(name):  #function definition with parameter 'name'
    print("I am " + name)

greet("Bijay")  #function call with argument "Bijay"

#parameter vs argument, parameter is what is defined in function, argument is what passed during function call, parameter is variable while argument is value
def add(a, b):  # 'a' and 'b' are parameters
    return a + b #returning the sum of a and b

result = add(5, 10)  # 5 and 10 are arguments, same function can be called with different arguments and as much as needed
result1 = add(20, 30)
print("Sum:", result)
print("Sum1:", result1)

#default parameter value
def multiply(x, y=2):  # 'y' has a default value of 2
    return x * y

print("Multiply 5 and default y:", multiply(5))

#function without arguments
def avg():
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    c= int(input("Enter third number: "))
    d= int(input("Enter fourth number: "))

    average = (a+b+c+d) / 4
    print(average)

avg() #we must define a constant if we will accept any return value

#same program with return
def avgReturn():
    a1= int(input("Enter first number: "))
    b1= int(input("Enter second number: "))
    c1= int(input("Enter third number: "))
    return (a1+b1+c1) / 3

average1 = avgReturn()  #capturing the return value
print("Average from return function:", average1)

#default parameters can also be set
def greet1(name, msg="Learning Python is fun!"):  #msg iss default value
    print("Hello " + name)
    print(msg)

greet1("Bijay")  #using default msg
greet1("Max")
greet1("Tiger", "Welcome to Python World!")  #overriding default msg

#function with variable number of arguments
def fruits(*names):  #'*names' allows variable number of arguments, represented by *varname, it collects all arguments into a tuple
    print("Fruits List:")
    for name in names:
        print(name)
    
fruits("Coconut", "DragonFruit", "Grapes")  #calling with 3 arguments
fruits("Pear", "Banana")  #calling with 2 arguments
fruits("Carrot")  #calling with 1 argument

#function with keyword arguments, it means we can pass arguments with parameter names
def personInfo(name, roll, city):
    print("Name:", name)
    print("Roll:", roll)
    print("City:", city)

personInfo(roll=25, name="Bijay", city="Itahari")  #arguments passed with parameter names, order doesn't matter
personInfo(name="Max", city="Dharan", roll=30)
personInfo(city="Biratnagar", roll=22, name="Tiger")

#function with both variable and keyword arguments
def mixedArgs(*args, **kwargs):  #'*args' for variable positional arguments, '**kwargs' for variable keyword arguments
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

#Recursion function- function calling itself
def factorial(n):
    if n == 0 or n == 1:  #base case
        return 1
    else:
        return n * factorial(n - 1)  #recursive case
    
num = int(input("Enter a number to find its factorial: "))
print(f"Factorial of {num} is {factorial(num)}")

#Base case is essential in recursion to prevent infinite loops and eventual stack overflow errors while recursive case is where the function calls itself with modified arguments to approach the base case. Their difference is that base case stops recursion while recursive case continues it.


