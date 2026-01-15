#Set - a data structure that stores unordered, unique items. It is mutable and allows for fast membership testing, insertions, and deletions. Data can be of different types.

s = {16, 25, 45, 35, 50, "Bijay", True}
print(s)
print(type(s))
print(len(s))

#Sets do not support indexing or slicing because they are unordered. However, you can iterate through a set using loops.
for item in s:
    print(item)

#Adding items
s.add(100)  # Adding a single item
s.update([200, 300, 400])  # Adding multiple items
print(s)

#Removing items
s.remove(25)  # Remove specific item, raises KeyError if not found
s.discard(45)  # Remove specific item, does not raise error if not found
print(s)

popped_item = s.pop()  # Remove and return an arbitrary item
print("Popped item:", popped_item)
print(s)

s.clear()  # Remove all items
print(s)


#Set operations
setA = {1, 5, 4, 3, 2}
setB = {4, 5, 6, 7, 8}

print("Union:", setA | setB)               # Union
print("Intersection:", setA & setB)        # Intersection
print("Difference (A-B):", setA - setB)    # Difference
print("Symmetric Difference:", setA ^ setB)  # Symmetric Difference, it means elements in either setA or setB but not in both
print("Is A subset of B?:", setA.issubset(setB))  # Subset check
print("Is A superset of B?:", setA.issuperset(setB))
print("Are A and B disjoint?:", setA.isdisjoint(setB))  # Disjoint check
print("Frozenset:", frozenset([1, 2, 3, 4, 5]))  # Creating a frozenset (immutable set)

#Set comprehension
squaredSet = {x**2 for x in range(1, 11)}
print("Squared Set:", squaredSet)
print("Even Squared Set:", {x**2 for x in range(1, 11) if x % 2 == 0})

#Set methods
setC = {10, 20, 30, 40, 50}
print("Original SetC:", setC)
setC.update([60, 70])  # Adding multiple items
print("After update:", setC)
setC.intersection_update({30, 40, 80})  # Intersection update
print("After intersectionUpdate:", setC)
setC.difference_update({40})  # Difference update
print("After differenceUpdate:", setC)
setC.symmetric_difference_update({20, 90})  # Symmetric difference update
print("After symmetricDifferenceUpdate:", setC)
setC.clear()  # Clear all items
print("After clear:", setC)

#Nested sets are not allowed because sets are mutable and unhashable. However, you can use frozensets as elements of a set.
nested_set = {frozenset({1, 2}), frozenset({3, 4})}
print("Nested Set with frozensets:", nested_set)
print("Accessing element from nested frozenset:", next(iter(nested_set)))  # Accessing an element from nested frozenset