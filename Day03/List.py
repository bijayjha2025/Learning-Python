#List- a data structure that holds an ordered collection of items, which can be of different types.
#Lists are mutable, meaning their contents can be changed after creation.

l = [10, 20, 30, 40, 50, "Bijay", True] #List
print(l)
print(type(l))
print(len(l)) #Length of the list

#Accessing elements in a list using indexing
print(l[0])
print(l[5])
print(l[-1]) #Last element

#List methods and functions = append(), insert(), remove(), pop(), sort(), reverse(), len()
print(l.append("Jha")) #Adds an element at the end
print(l)

l.insert(2, 25) #Inserts an element at a specific index, here 25 at index 2
print(l)

l.remove(30) #Removes the first occurrence of a specific element, here 30
print(l)

popped = l.pop() #Removes and returns the last element
print(popped)

l.reverse() #Reverses the order of elements in the list
print(l)

l.sort() #Sorts the list in ascending order (only works if all elements are of the same type)
print(l)

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()