#String Operations
#String are sequences of characters used to store and manipulate text-based data.

string1= "Bijay"
string2= "Jha"

#Length of a string
print(len(string1))

#Concatenation- adding strings together
print(string1 + " " + string2)

#Accessing characters by index
first = string1[0]
last = string1[-1]
print("First character:", first)
print("Last character:", last)

#Capitalize
print(string1.capitalize())

#Uppercase
print(string1.upper())

#Lowercase
print(string1.lower())

#Substring- substring is like a subset of a string
substr = string1[1:4]  # characters from index 1 to 3 (ignores index 4)
print("Substring:", substr)

substr2 = string1[1:3]  # characters from index 1 to 2 (ignores index 3)
print("Substring 2:", substr2)

#Startswith and Endswith response will be in True or False
print(string1.startswith("Bi"))  #true
print(string2.endswith("ay"))  #false

#Find- returns lowest index of substring if found, else -1 , they are case sensitive
print(string1.find("a"))
print(string2.find("b"))

#count- returns number of occurrences of substring
print(string1.count("j"))
print(string2.count("a"))
print(string1.count("z"))

#Replace- replaces all occurrences of one with another
print(string1.replace("B", "b")) #first is to be replaced, second is to replace with(new)
print(string2.replace("J", "j"))

#Split- splits string into list of substrings
print(string1.split("i")) #splits at 'i' doesnot include 'i' in the result
print(string1.split("j"))
print(string2.split("a")) #if no substrings after that, space will be there in the result

#Join- joins list of strings into a single string with specified separator
words = ["Hello", "Python", "from", "Bijay"]
sentence = " ".join(words)
print(sentence)

#slice- extracts a portion of string based on start, end, and step values
print(string1[0:5:2]) #from index 0 to 4, step 2, move by 2 index
print(string2[0:3:1]) #from index 0 to 2, step 1, move by 1 index
print(string1[-1::-1]) #reverses the string

#strip- removes leading and trailing whitespace characters
string3 = "   Hello, World!   "
print(string3.strip())

