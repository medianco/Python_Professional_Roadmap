"""
 Variables are used to store data that can be referenced and manipulated during program execution. 
 A variable is essentially a name that is assigned to a value.

    Unlike Java and many other languages, Python variables do not require explicit declaration of type.
    Type of the variable is inferred based on the value assigned.
"""  

nbr = 2026    # Basic Assignment: Variables are assigned values using the = operator.
name = "Alex"  

print(nbr)
print(name)

# Python allows you to assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry" 

print(x, y, z)

###  Rules for Naming Variables ### 

# To use variables correctly, the following naming rules should be followed:

#     Names can contain letters, digits and underscores (_).
#     The first character cannot be a digit.
#     Names are case-sensitive, so myVar and myvar are treated differently.
#     Keywords such as if, else and for cannot be used as variable names.

X = "Python "
Y = "is "
Z = "awesome"

print(X + Y + Z)  # You can also use the + operator to output multiple variables

# Dynamic Typing: Python is dynamically typed, so the same variable can store different data types during execution.

X = 1234
print(X)

# Assigning Same Value: same value can be assigned to multiple variables in a single line.
a = b = c = 100
print(a, b, c)

 # Assigning Different Values: Multiple variables can also be assigned different values in a single line.
x, y, z = 1, 2.5, "Python"
print(x, y, z)

### Deleting a Variable ###
# del keyword is used to delete a variable from memory.
# After deletion, the variable can no longer be accessed.

x = 10
del x
# print(x)

# Explanation: del x deletes the variable x. 
# Accessing x after deletion raises a NameError because the variable no longer exists.

### Swapping Two Variables ###
# Using multiple assignments, we can swap the values of two variables without needing a temporary variable.

a, b = 5, 10
a, b = b, a
print(a, b)