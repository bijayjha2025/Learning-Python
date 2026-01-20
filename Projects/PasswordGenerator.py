import random
import string

length = int(input("Enter password length: "))

useUpper = input("Include uppercase letters? (y/n): ").lower() == "y"
useLower = input("Include lowercase letters? (y/n): ").lower() == "y"
useDigits = input("Include digits? (y/n): ").lower() == "y"
useSymbols = input("Include special characters? (y/n): ").lower() == "y"

characters = ""

if useUpper:
    characters += string.ascii_uppercase
if useLower:
    characters += string.ascii_lowercase
if useDigits:
    characters += string.digits
if useSymbols:
    characters += string.punctuation

if not characters:
    print("Error: No character set selected")
    exit()

password = "".join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:")
print(password)
