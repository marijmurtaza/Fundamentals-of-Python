# The "print" function is used to display the output on the screen
print("I love python")


#Modules are pre-written libraries that provide additional functionality for your Python programs. some modules are datetime,math and random.
import math
import math
result = math.sqrt(25)
print(result)
# There are two types of modules in python 
# 1. Build in modules
# 2. External modules

#pip is the package installer for Python. It is used to install and manage packages, or libraries.

'''Comments in Python are used to add explanations or annotations to your code.
They are ignored by the Python interpreter and are not executed as part of your program.'''
# There are two types of comments 1.Single line 2.Multi line
#This is a single line comment
'''This is a multi line comment'''

'''Variables in python
A variable is simply a named location in memory where a value can be stored, and the variable can be referred to by its name.'''
msg = "Hi there"
print(msg)

'''Data Types in Python:A data type is a classification of the type of data that a value can hold
Python supports several built-in data types.
'''
string=str("hello")
num=int(256)
boolean=bool(0)
decimal=float(10.50)
print(f"{string} {num} {boolean} {decimal}")

#Operators in Python
a = 6
b = 5
c = 10

# Arithmetic operators
print(a + b)      
print(a - b)      
print(a * b)      
print(a / b)      
print(a % b)      

# Comparison operators
print(a == b)     
print(a != b)     
print(a > b)      
print(a < b)     
print(a >= b)     
print(a <= b)     

# Assignment operators
a += b
print(a)          
a -= b
print(a)          

# Logical operators
print(a < c and b < c) 
print(a < c or b > c)   
print(not (a < c))      

# Identity operators
d = [1, 2, 3]
e = [1, 2, 3]
print(d is e)           
print(d is not e)      

# Membership operators
f = "hello"
print("h" in f)        
print("x" not in f)     

#User Input
name = input("What is your name? ")
print("Hello, " + name + "!")
