'''In Python, a string is a sequence of characters used to represent text. Strings can contain letters, numbers, and symbols, 
and are typically used to store and manipulate text data.Strings are defined using either single quotes or double quotes, 
and can span multiple lines using triple quotes'''
# Single quotes
string1 = 'Hello, World!'

# Double quotes
string2 = "Hello, World!"

# Triple quotes
string3 = """Hello,
World!"""

#operations on strings in Python
# Concatenation
string1 = "Hello, "
string2 = "World!"
print(string1 + string2)  # Output: Hello, World!

# Slicing
string = "Hello, World!"
print(string[0:5])        # Output: Hello
print(string[7:12])       # Output: World

# Repeating
print(string1 * 3)        # Output: Hello, Hello, Hello,

# Length
print(len(string))        # Output: 13

# Converting to a string
num = 42
print(str(num))           # Output: 42

# Formatting
template = "The answer is {}."
print(template.format(num))  # Output: The answer is 42.

string = "Hello, World!"

# str.endswith()
print(string.endswith("World!"))  # Output: True

# str.count()
print(string.count("o"))  # Output: 2

# str.capitalize()
print(string.capitalize())  # Output: Hello, world!

# str.find()
print(string.find("World"))  # Output: 7

# str.replace()
print(string.replace("World", "Python"))  # Output: Hello, Python!

'''Escape Sequence in Python
An escape character is a backslash \ followed by the character you want to insert'''
# Newline
string = "Hello,\nWorld!"
print(string)


# Tab
string = "Hello,\tWorld!"
print(string)


# Backslash
string = "Hello, \\World!"
print(string)


# Single quote
string = 'Hello,\'World!\''
print(string)


# Double quote
string = "Hello,\"World!\""
print(string)

