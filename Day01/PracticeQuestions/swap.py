a = 10
b = 6

#First method by direct swapping
a,b = b, a
print(f"a:{a}, b:{b}")


# Another method using temporary variable
p = 8
q= 4

temp = p
p = q
q = temp

print(f"p:{p}, q:{q}")


# Third method using arithmetic operations
x = 15
y = 25

x = x + y
y = x - y
x = x - y

print(f"x:{x}, y:{y}")