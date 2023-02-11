'''
Conditional expressions in Python are used to make decisions based on certain conditions. 
The most commonly used conditional expression in Python is the if statement.
'''
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#Relational operators are used to compare two values and determine the relationship between them
a = 2
b = 8

print(a < b) 
print(a > b) 
print(a <= b) 
print(a >= b) 
print(a == b) 
print(a != b) 

#Logical Operators are used to combine multiple boolean expressions into a single expression and make decisions based on their truth values
x = True
y = False

print(x and y) 
print(x or y) 
print(not x) 

'''
The elif clause in Python is used in conjunction with the if statement to provide additional tests and conditions. 
The elif clause allows you to specify multiple conditions and execute different code blocks for each condition.
'''
x = 2

if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
elif x > 0:
    print("x is positive")


