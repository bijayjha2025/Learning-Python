#Exception Handling - It demonstrates basic exception handling using try, except, else, and finally blocks. try block contains code that may raise an exception. except block handles the exception if it occurs. else block executes if no exception occurs. finally block executes regardless of whether an exception occurred or not.

def divideNumbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Invalid input type. Please use numbers only.")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution completed.")

divideNumbers(10, 2)  # Valid
divideNumbers(10, 0)  # Division by zero
divideNumbers(10, 'a')  # Invalid input type
divideNumbers(15, 3)  # valid


# Custom Exception - It defines a custom exception class InvalidAgeError that inherits from the built-in Exception class. The checkAge function raises this exception if the provided age is less than 0 or greater than 120. In place of using built-in exceptions, this custom exception provides a more specific error message related to age validation. It is then demonstrated in a try-except block. In place of InvalidAgeError, we can define and use other custom exceptions as needed, which needs to be desecriptive of the specific error condition being handled. It enhances code readability and maintainability by providing clear context about the error.

class InvalidAgeError(Exception):
    pass

def checkAge(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")
    else:
        print(f"Age {age} is valid.")

try:
    checkAge(25)  # Valid age
    checkAge(-5)  # Invalid age
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")


#Another custom exception example

class NegativeNumberError(Exception):
    pass

def squareRoot(num):
    if num < 0:
        raise NegativeNumberError("Square root of a negative number is not possible.")
    else:
        print(f"Square root of {num} is {num ** 0.5}")

try:
    squareRoot(16)  # Valid input
    squareRoot(-4)  # Invalid input

except NegativeNumberError as e:
    print(f"NegativeNumberError: {e}")

#Another example with multiple custom exceptions
class InsufficientMarksError(Exception):
    pass

def checkMarks(marks):
    if marks < 0 or marks > 100:
        raise InsufficientMarksError("Marks must be between 0 and 100.")
    else:
        print(f"Marks {marks} are valid.")

try:
    checkMarks(85)  # Valid marks
    checkMarks(150)  # Invalid marks

except InsufficientMarksError as e:
    print(f"InsufficientMarksError: {e}")


#Another example with custom exception for email validation
class InvalidEmailError(Exception):
    pass

def validateEmail(email):
    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email format.")
    else:
        print(f"Email {email} is valid.")

try:
    validateEmail("example@example.com")
    validateEmail("invalidemail")  # Invalid email

except InvalidEmailError as e:
    print(f"InvalidEmailError: {e}")


#Exception handling and custom handling plays crucial role in building robust applications by managing errors gracefully and providing meaningful feedback to users and developers alike.They arer used extensively in real-world applications across various domains such as web development, data processing, and user input validation.

