'''
A function in Python is a block of code that performs a specific task and can be re-used throughout your program
To define a function in Python, you use the def keyword followed by the function name and a pair of parentheses (). The inputs to the function, 
called parameters, are placed within the parentheses.
The code within the function is indented and is executed when the function is called
'''
def greet_user():
    name = input("What is your name? ")
    print("Good day, " + name)

greet_user()
# There are two types of Functions in Python 1.Built in functions 2.User defined functions 

#Function with arguments
def add(a, b):
    return a + b

result = add(10, 20)
print(result)  

'''A default parameter value in a function in Python is a value that is assigned to a parameter when no value is provided for that parameter in a function call. 
If a value is provided, the default value is overridden.
'''
def rectangle_area(length, width=10):
    return length * width

area = rectangle_area(20)
print(area)  

area = rectangle_area(20, 30)
print(area) 

#Recursion 
#Recursion is a technique in computer programming where a function calls itself as a subroutine

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

