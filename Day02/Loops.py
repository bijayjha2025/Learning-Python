#Looping is repeating any action multiple times or till a certain condition is met. There are two types of loops in Python:
#1. For Loop
#2. While Loop

a = 10
for i in range(a):
 print(2*i)

l = [1, 2, 3, 4, 7, 8, 9] #List
for i in l:
    print(i*i)

t = (1, 2, 3, 4, 5) #Tuple
for i in t:
    print(i+i)

s = "Bijay" #String
for i in s:
    print(i)

d = {'a': "car", 'b': "bus", 'c': "taxi"} #Dictionary
for i in d:
    print(i, d[i])

#Noticed? In case of list and tuple, we got each element. In case of string, we got each character. In case of dictionary, we got each key-value.

#There is also a unique case of for with else, where else will be executed after the for loop is completed.

l =[1, 4, 6]
for i in l:
    print(i)
else:
    print("Loop is ended")


#While Loop
i = 1
while i<=5:
    print(i*i)
    i += 1


l = ["Bijay", 1, True, 7.7]
i = 0
while i < len(l):
    print(l[i])
    i += 1 #This is while loop for list

#Break, continue and pass statements can also be used in loops.
#Break is used to exit the loop, continue to skip the current iteration and pass is a null statement.

for i in range(1, 11):
    if i == 5:
        break
    print(i) #This will print from 1 to 4 and exit when i is 5

for i in range(1, 11):
    if i == 5:
        continue
    print(i) #This will print from 1 to 10 except 5


for i in range(1, 11):
    if i == 5:
        pass
    print(i) #This will print from 1 to 10 including 5