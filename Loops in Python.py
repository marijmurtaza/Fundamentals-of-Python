'''
A loop in Python is a control structure that allows you to repeat a block of code multiple times. 
There are two main types of loops in Python: for loops and while loops.
'''
#While Loop
i = 1
while i <= 50:
    print(i)
    i += 1
#Another program
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

#For Loop
# Print the numbers from 1 to 10
for i in range(1, 11):
    print(i)

# For loop with else
# Find the first positive integer in a list
numbers = [-5, -4, 0, 2, 9, 8]

for num in numbers:
    if num > 0:
        print("The first positive integer is:", num)
        break
else:
    print("No positive integers were found in the list.")

#For loop with break and continue
# Find the first positive integer in a list
numbers = [-5, -4, 0, 2, 9, 8]

for num in numbers:
    if num <= 0:
        continue
    print("The first positive integer is:", num)
    break
