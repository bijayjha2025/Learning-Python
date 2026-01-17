#Iterators and Generators in Python
#Iterators and generators are used to iterate over a sequence of data. An iterator is an object that implements the iterator protocol, which consists of the methods __iter__() and __next__(). A generator is a special type of iterator that is defined using a function that uses the yield statement.

# 1. Creating an iterator using a class
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
        
# 2. Creating a generator using a function
def myGenerator(limit):
    current = 0
    while current < limit:
        yield current
        current += 1

# 3. Using the iterator
def useIterator():
    print("Using MyIterator:")
    iterator = MyIterator(5)
    for value in iterator:
        print(value)

useIterator()

# 4. Using the generator
def useGenerator():
    print("Using myGenerator:")
    for value in myGenerator(5):
        print(value)
useGenerator()

# 5. Converting a generator to a list
def generatorToList():
    gen = myGenerator(5)
    gen_list = list(gen)
    print("Generator converted to list:", gen_list)
generatorToList()

# 6. Using generator expressions
def generatorExpression():
    gen_exp = (x * x for x in range(5))
    print("Using generator expression:")
    for value in gen_exp:
        print(value)

generatorExpression()

# 7. Handling StopIteration exception
def handleStopIteration():
    print("Handling StopIteration exception:")
    iterator = MyIterator(3)
    while True:
        try:
            value = next(iterator)
            print(value)
        except StopIteration:
            print("Reached the end of the iterator.")
            break

handleStopIteration()


#Yield - A yield statement is used in a function to make it a generator. When the function is called, it returns a generator object without executing the function. Each time next() is called on the generator, the function runs until it hits a yield statement, which returns the yielded value and pauses the function's state. The next time next() is called, the function resumes execution right after the yield statement.
def yieldExample():
    def countUpTo(max):
        count = 1
        while count <= max:
            yield count
            count += 1

    counter = countUpTo(5)
    print("Using yield in a generator function:")
    for number in counter:
        print(number)

yieldExample()

# List vs Generator => A list stores all its elements in memory, which can be inefficient for large datasets. A generator, on the other hand, generates items on-the-fly and only keeps one item in memory at a time, making it more memory efficient.
def listVsGenerator():
    import sys

    # List comprehension
    myList = [x * x for x in range(1000)]
    print("List size in bytes:", sys.getsizeof(myList))

    # Generator expression
    myGen = (x * x for x in range(1000))
    print("Generator size in bytes:", sys.getsizeof(myGen))

listVsGenerator()

