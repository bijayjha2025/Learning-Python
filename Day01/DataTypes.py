a = 10     
print(type(a))    #gives <class 'int'>

b= "Bijay"
print(type(b))   #gives <class 'str'>

c = 3.567
print(type(c))   #gives <class 'float'>

d = True
print(type(d))   #gives <class 'bool'>

e = None
print(type(e))   #gives <class 'NoneType'>

z = 5 + 3j
print(type(z))   #gives <class 'complex'>

#The above are the basic data types in Python while type() function is used to know the data type of a variable.

print(float(a))   #converts to float
print(int(c))   #converts to integer
print(str(a))  #converts to string
print(complex(a)) #converts to complex number
print(bool(0)) #converts to boolean False
print(bool(3)) #converts to boolean True

#The above are type conversion functions in Python which converts one data type to another data type. Note that bool(0) is False and bool of any non zero number is True, here 3 is non zero number so it gives True. Type conversion can be implicit or explicit, implict is done by Python interpreter itself to prevent data loss while explicit is done by the user to convert one data type to another.

#Example of implicit type conversion:
a = 9       #int
b = 3.5     #float
c = a + b   #implicit conversion of int to float
print(c)    #gives 12.5
print(type(c))  #gives <class 'float'>

#Example of explicit type conversion:
x = 12.7    #float
y = int(x)  #explicit conversion of float to int
print(y)     #gives 12
print(type(y))  #gives <class 'int'>

#In explicit type conversion, users use built-int functions like int(), float(), str(), etc. to convert into data types they want. Explicit type conversion may lead to data loss, for example in the above case converting float 12.7 to int results in loss of decimal part. Also, note that while converting string to int or float, the string must represent a valid number otherwise it will raise an error. Thus, we can say type casting is a type conversion done by the user explicitly.