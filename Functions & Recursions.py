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
