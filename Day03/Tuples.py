#Tuple - a data structure that is immutable (cannot be changed after creation) and holds an ordered collection of items, which can be of different types.

t = (10, 20, 30, 40, 50, "Bijay", True)
print(t)
print(type(t))
print(len(t))

print(t[0])
print(t[5])
print(t[-1])

#Tuples do not have methods like append(), insert(), remove(), pop(), sort(), reverse() because they are immutable. However, you can use functions like len(), min(), max(), sum() (if elements are of the same type).

marks = (85, 90, 78, 92, 88)
print(min(marks))  # Minimum value
print(max(marks))  # Maximum value
print(sum(marks))  # Sum of all values
print(sorted(marks))  # Returns a sorted list of the tuple's elements
print(marks.count(85))