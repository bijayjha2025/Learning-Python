#Conditional sentences in Python. It means "if a condition is true, then do something". It is used to control the flow of a program based on certain conditions.

a = int(input("Enter your age:"))
if a >= 22:
    print("You are eligible to move abroad without any restrictions")

elif a <=16:
    print("You are not right candidate to move abroad")

else:
    print("You are eligible to move abroad with parental consent")


#Nested if-else statements
marks = int(input("Enter your marks:"))

if marks >= 40:
    if marks >= 90:
        print("A grade")
    elif marks >= 70 and marks < 90:
        print("B grade")
    else:
        print("Average grade")

else:
    print("Fail")