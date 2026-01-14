#some famous problems

#1. Armstrong Number - an integer of three digits such that the sum of the cubes of its digits is equal to the number itself. Example: 153 = 1^3 + 5^3 + 3^3

n = int(input("Enter a number: "))
sum = 0
temp = n

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if n == sum:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")

#Palindrome Number- a number that remains the same when its digits are reversed. Example: 121

n = int(input("Enter a number: "))
rev = 0
temp = n
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if n == rev:
    print(f"{n} is a Palindrome number.")
else:
    print(f"{n} is not a Palindrome number.")

#Sum of digits
n = int(input("Enter a number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10

print(f"Sum of digits: {sum}")