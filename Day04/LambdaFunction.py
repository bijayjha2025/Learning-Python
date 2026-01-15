#Lambda Function - It is a small anonymous function that can take any number of arguments, but can only have one expression.

#syntax: lambda arguments: expression

add = lambda b, j: b + j  #lambda function to add two numbers
result = add(10, 20)
print("Sum using lambda:", result)

multiply = lambda b, j: b * j  #lambda function to multiply two numbers
result1 = multiply(5, 4)
print("Product using lambda:", result1)

#Lambda function to find maximum of two numbers
maximum = lambda b, j: b if b > j else j
result2 = maximum(15, 25)
print("Maximum using lambda:", result2)

#Lambda function to calculate square of a number
square = lambda b: b ** 2
result3 = square(6)
print("Square using lambda:", result3)

#Lambda function to concatenate two strings
concatenate = lambda str1, str2: str1 + " " + str2
result4 = concatenate("Learning", "Python")
print("Concatenated String:", result4)

#Lambda function to calculate factorial of a number using recursion
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
result5 = factorial(5)
print("Factorial:", result5)

#Using lambda function with map to square a list of numbers
numbers = [1, 2, 3, 4, 5]
squaredNumbers = list(map(lambda x: x ** 2, numbers))
print("Squared Numbers:", squaredNumbers)

#Using lambda function with filter to get even numbers from a list
evenNumbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", evenNumbers)

#Lambda function provides a concise way to write small functions, especially when used as arguments to higher-order functions like map(), filter(), and reduce(). Keeping the code clean and readable by avoiding the need to define a full function. Useful in functional programming paradigms. They are often used in data analysis and manipulation tasks.

#Note: Lambda functions are limited to a single expression and cannot contain multiple statements or complex logic. For more complex operations, it's better to define a regular function using the def keyword.