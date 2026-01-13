x = 4
y = 3

# 1. Arithmetic Operators
print(x + y)  # +
print(x - y)  # -
print(x * y)  # *
print(x / y)  # /
print(x % y)  # %
print(x ** y) # **


#The above are arithmetic operators used to perform mathematical operations like addition, subtraction, multiplication, division, modulus, exponentiation.

# 2. Comparison Operators (gives boolean output)
d = x > y #greater than
print(d)   #This will give True as 4 is greater than 3

e = x < y   #less than
print(e)   #This will give False as 4 is not less than 3

f = x == y #equal to
print(f)   #This will give False as 4 is not equal to 3

g = x != y #not equal to
print(g)   #This will give True as 4 is not equal to 3

h = x >= y #greater than or equal to
print(h)   #This will give True as 4 is greater than 3

i = x <= y #less than or equal to
print(i)   #This will give False as 4 is not less than or equal to

#The above are comparison operators used to compare two values and return a boolean result (True or False).

# 3. Logical Operators
p=True
q=False
print(p and q)  #and
print(p or q)   #or
print(not p)    #not

#The above are logical operators used to combine conditional statements. 'and' returns True if both conditions are True, 'or' returns True if at least one condition is True, and 'not' negates the boolean value. (Remember them as logic gates in electronics: AND, OR, NOT).

# 4. Assignment Operators
a = 5   #simple assignment
a += 3  #equivalent to a = a + 3
print(a)  #gives 8
a *= 2  #equivalent to a = a * 2
print(a)  #gives 16
a -= 4  #equivalent to a = a - 4
print(a)  #gives 12
a /= 3  #equivalent to a = a / 3
print(a)  #gives 4.0
a %= 3  #equivalent to a = a % 3
print(a)  #gives 1.0
#The above are assignment operators used to assign values to variables and perform operations on them in a shorthand way.

# 5. Bitwise Operators
m = 5  #binary: 0101
n = 3  #binary: 0011
print(m & n)  #AND: 0001 gives 1
print(m | n)  #OR:  0111 gives 7
print(m ^ n)  #XOR: 0110 gives 6
print(~m)     #NOT: 1010 gives -6 (two's complement)
print(m << 1) #Left Shift: 1010 gives 10
print(m >> 1) #Right Shift: 0010 gives 2
#The above are bitwise operators used to perform operations on binary representations of integers. They operate at the bit level, manipulating individual bits of the numbers.

'''Note: Python also supports other operators like Membership Operators (in, not in) and Identity Operators (is, is not) which are used to check membership in sequences and identity of objects respectively.'''