#Dictionary- a data structure that stores data in key-value pairs. It is mutable (can be changed after creation) and allows for fast lookups, insertions, and deletions based on keys. The data can be of different types.

d = {
    "name": "Bijay",
    "address": "Itahari",
    "hobbies": ["Reading", "Coding", "Cricket"],
    "isStudent": True,
    "marks": {"Math": 90, "C": 85, "Physics": 88},
    "faculty": "CSIT",
}

print(d)
print(type(d))
print(len(d))

#accessing values using keys
print(d["name"])
print(d["hobbies"])
print(d["marks"]["Math"])
print(d.get("address"))
print(d.get("phone", "Not Available"))  # Using get() to avoid KeyError

print(d.keys())    # Get all keys
print(d.values())  # Get all values
print(d.items())   # Get all key-value pairs

#Modifying dictionary
d["address"] = "Dharan"  # Update existing key
d["phone"] = "1234567890"   # Add new key-value pair
print(d)
print(len(d))

print(d.update({"faculty": "CS"}))  # Update, curly brackets compulsory
print(d)

#Removing items
del d["isStudent"]  # Remove key-value pair
print(d)
d.pop("phone", None)  # Remove key-value pair safely
print(d)
d.popitem()  # Remove and return an arbitrary key-value pair
print(d)
d.clear()  # Remove all items
print(d)

#Nested dictionary
student = {
    "name": "Bijay",
    "roll": 21,
    "courses": {
        "Math": {"marks": 90, "credits": 4},
        "C": {"marks": 85, "credits": 3},
        "Physics": {"marks": 88, "credits": 4},
    },
}

print(student["courses"]["C"]["marks"])  # Accessing nested dictionary value
print(student["courses"]["Math"]["credits"])  # Accessing nested dictionary value
student["courses"]["Digital Logic"] = {"marks": 80, "credits": 3}  # Adding new nested dictionary
print(student)