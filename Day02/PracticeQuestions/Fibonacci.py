
a = 0
b = 1
count = 0

n = int(input("Enter number of terms:"))

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence upto", n, ":")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a)
        c = a + b
        a = b
        b = c
        count += 1