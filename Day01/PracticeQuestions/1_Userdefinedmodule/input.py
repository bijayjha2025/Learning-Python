#input() function to take user input and display it. Note that input() function returns data in string format always so to use type we want, we need to typecast it.

x = input("Enter first number: ")
p = input("Enter second number: ")

print("The sum is: ", x + p) 
#This will concatenate the two even if they are numbers.

x = int(x)
p = int(p)
print("The sum after typecasting to int is: ", x + p)
#This will add two numbers now.

#Program to typecast currency values, time, and temperature values.
y = input("Enter amount in dollars: ")
y = float(y)
print("Amount in dollars after typecasting to float is: ", y)

t = input("Enter time in hours: ")
t = int(t)
print("Time in hours after typecasting to int is: ", t)

temp = input("Enter temperature in Celsius: ")
temp = float(temp)
print("Temperature in Celsius after typecasting to float is: ", temp)