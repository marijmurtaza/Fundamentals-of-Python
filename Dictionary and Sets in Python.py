'''Dictionary in Python : A dictionary is a collection of unordered, mutable, and indexed elements. 
Dictionaries are defined using curly braces {} and each element in the dictionary is a key-value pair
'''
student = {
    "name": "Marij Murtaza",
    "id": 76,
    "address": "123 Main St."
}
print(student["name"]) #accessing dictionary using keys 

#Operations on Dictionaries

#Adding elements in dict
student["phone"] = "555-555-5555"
print(student)

#updating elements in dict
student["id"] = 12
print(student)

#Deleting elements in dict
del student["address"]
print(student)

#Functions on Dictionaries

#len()
print(len(student))

#str()
print(str(student))

#type()
print(type(student))

#items
print(student.items())

#update
student.update({"email": "marijmurtaza@email.com"})
print(student) 

#get
print(student.get("name", "Not Found"))

''' Sets in python :
A set is an unordered collection data type that is iterable, mutable, and has no duplicates. 
Sets are defined using curly braces {} or the set() constructor.
'''
# Define a set using curly braces
mobile_set = {"A53", "12 pro max", "s21"}

# Define a set using the set() constructor
cars_set = set(["Yaris", "city", "alsvin"])

#Operations on Sets

#len()
print(len(mobile_set))

#remove()
print(cars_set.remove("alsvin"))

#pop()
print(cars_set.pop())

#clear()
print(cars_set.clear())

#union
fruit_set = {"apple", "banana", "cherry"}
vegetable_set = {"carrot", "potato", "celery"}
result_set = fruit_set.union(vegetable_set)
print(result_set)

#Intersection
fruit_set = {"apple", "banana", "cherry"}
vegetable_set = {"carrot", "potato", "celery", "banana"}
result_set = fruit_set.intersection(vegetable_set)
print(result_set)


