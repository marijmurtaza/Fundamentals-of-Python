'''List in python:
a list is an ordered collection of elements, which can be of any type, including other lists. Lists are defined using square brackets [], 
and elements are separated by commas.
'''
bikes = ["YZF-R1", "H2R", "Hayabusa"]
print(bikes)
#list indexing
print(bikes[0])
print(bikes[0:2])  
print(bikes[1:])   
print(bikes[:2])  
print(bikes[-1]) 

#Functions on a List
bikes = ["YZF-R1", "H2R", "Hayabusa"]

# len(list)
print(len(bikes))  

# list.append(element)
bikes.append("S1000RR")
print(bikes) 

# list.insert(index, element)
bikes.insert(1, "MT 420-RR")
print(bikes)  

# list.remove(element)
bikes.remove("MT 420-RR")
print(bikes)  

# list.pop(index)
bikes.pop(2)
print(bikes)  

# list.index(element)
print(bikes.index("S1000RR"))  

# list.count(element)
print(bikes.count("S1000RR"))  

# list.sort()
bikes.sort()
print(bikes)  

# list.reverse()
bikes.reverse()
print(bikes)  

''' Tuples in python :
 A tuple is a collection of ordered, immutable, elements.A tuple is defined using parentheses () and its elements are separated by commas.
'''
student = ("Marij Murtaza", 76, "123 Main St.")
print(student[0])  
print(student[1:3])

#Functions on Tuples

#length
print(len(student))

#Count
print(student.count("Marij Murtaza"))

#index
print(student.index("123 Main St."))

