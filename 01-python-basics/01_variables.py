"""
===============================================================================
File        : 01_variables.py
Author      : Mohammed AL-Dubai
Course      : Python Professional Roadmap
Lesson      : Variables

Description:
    This lesson introduces Python variables, assignment techniques,
    naming conventions, dynamic typing, memory references, and
    Python best practices.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Understand what variables are.
✔ Create and assign variables.
✔ Follow Python naming conventions.
✔ Assign multiple variables.
✔ Reassign variables.
✔ Understand dynamic typing.
✔ Display variable data types.
✔ Print variable memory addresses.
✔ Use constants by convention.
✔ Delete variables.
✔ Swap variables without a temporary variable.

===============================================================================
"""

# =============================================================================
# SECTION 1 - What is a Variable?
# =============================================================================

"""
A variable is a named reference to an object stored in memory.

Python variables do not require explicit type declarations.
The data type is automatically determined by the assigned value.

Syntax:

variable_name = value
"""

year = 2026
name = "Alex"

print(year)
print(name)

# =============================================================================
# SECTION 2 - Printing Variable Types
# =============================================================================

"""
The built-in type() function returns the data type of an object.
"""

print(type(year))
print(type(name))

# Expected Output
#
# <class 'int'>
# <class 'str'>


# =============================================================================
# SECTION 3 - Variable Assignment
# =============================================================================

"""
Variables are created automatically when a value is assigned.
"""

city = "Berlin"
temperature = 28.5
is_online = True

print(city)
print(temperature)
print(is_online)

# =============================================================================
# SECTION 4 - Multiple Variable Assignment
# =============================================================================

"""
Python allows assigning multiple variables in one statement.
"""

first_name, age, country = "John", 25, "Germany"

print(first_name)
print(age)
print(country)

# =============================================================================
# SECTION 5 - Assign the Same Value
# =============================================================================

"""
Multiple variables can reference the same object.
"""

x = y = z = 100

print(x)
print(y)
print(z)

# =============================================================================
# SECTION 6 - Variable Naming Rules
# =============================================================================

"""
Rules:

1. Names may contain letters.
2. Names may contain numbers.
3. Names may contain underscores.
4. Names cannot start with numbers.
5. Names are case-sensitive.
6. Reserved keywords cannot be used.
"""

student_name = "Alice"
student_age = 20
course_name = "Python"

print(student_name)
print(student_age)
print(course_name)

# =============================================================================
# Invalid Variable Names
# =============================================================================

"""
The following examples are invalid.

2name = "Alex"
my-name = "Python"
class = "Network"

These examples remain commented because they would generate SyntaxError.
"""

# =============================================================================
# SECTION 7 - Naming Conventions
# =============================================================================

"""
Recommended style: snake_case
"""

employee_name = "David"
employee_salary = 6500

print(employee_name)
print(employee_salary)

"""
Avoid meaningless names.
"""

# Bad examples

# a = "David"
# b = 6500

"""
Good examples are always preferred because they improve readability.
"""

# =============================================================================
# SECTION 8 - Case Sensitivity
# =============================================================================

"""
Python treats uppercase and lowercase names as different variables.
"""

language = "Python"
Language = "Java"

print(language)
print(Language)

# =============================================================================
# SECTION 9 - String Concatenation
# =============================================================================

word1 = "Python"
word2 = "is"
word3 = "awesome"

print(word1 + " " + word2 + " " + word3)

# =============================================================================
# SECTION 10 - Using f-Strings (Recommended)
# =============================================================================

print(f"{word1} {word2} {word3}")

name = "Alex"
age = 24

print(f"My name is {name}.")
print(f"I am {age} years old.")

# =============================================================================
# SECTION 11 - Dynamic Typing
# =============================================================================

"""
Python variables can reference objects of different types during execution.
"""

value = "Python"

print(value)
print(type(value))

value = 2026

print(value)
print(type(value))

value = 3.14159

print(value)
print(type(value))

value = False

print(value)
print(type(value))

# =============================================================================
# SECTION 12 - Common Built-in Data Types
# =============================================================================

integer_number = 100
floating_number = 15.75
text = "Cyber Security"
boolean_value = True
empty_value = None

print(type(integer_number))
print(type(floating_number))
print(type(text))
print(type(boolean_value))
print(type(empty_value))

# =============================================================================
# END OF PART 1
# =============================================================================

# =============================================================================
# SECTION 13 - The id() Function
# =============================================================================

"""
The built-in id() function returns the unique identity (memory address)
of an object during its lifetime.

Syntax:
    id(object)
"""

number = 100

print("Value :", number)
print("Memory Address :", id(number))

number = 200

print("Value :", number)
print("Memory Address :", id(number))

"""
Notice that assigning a new value may result in a different object
with a different memory address.
"""

# =============================================================================
# SECTION 14 - Object Identity
# =============================================================================

"""
Variables in Python do not store values directly.

Instead, variables reference objects stored in memory.
"""

a = 50
b = 50

print(a)
print(b)

print(id(a))
print(id(b))

print(a is b)

"""
Small integers are usually cached by Python, so both variables often
reference the same object.
"""

# =============================================================================
# SECTION 15 - Variable Reassignment
# =============================================================================

"""
Variables can be reassigned at any time.
"""

username = "Alex"

print(username)

username = "Mohammed"

print(username)

username = "Python"

print(username)

# =============================================================================
# SECTION 16 - The None Object
# =============================================================================

"""
None represents the absence of a value.

It is commonly used as a placeholder.
"""

result = None

print(result)
print(type(result))

connection = None

print(connection)

# =============================================================================
# SECTION 17 - Constants (Naming Convention)
# =============================================================================

"""
Python does not support true constants.

By convention, uppercase names indicate values
that should not be modified.
"""

PI = 3.1415926535
MAX_USERS = 100
DEFAULT_PORT = 443

print(PI)
print(MAX_USERS)
print(DEFAULT_PORT)

"""
Although constants can still be modified, it is considered bad practice.
"""

# Avoid doing this.

# PI = 5

# =============================================================================
# SECTION 18 - Deleting Variables
# =============================================================================

"""
The del keyword removes a variable.

Syntax:

del variable_name
"""

temporary_value = 123

print(temporary_value)

del temporary_value

"""
The following statement raises NameError.

print(temporary_value)
"""

# =============================================================================
# SECTION 19 - Swapping Variables
# =============================================================================

"""
Python provides an elegant way to swap variables.
"""

first_number = 5
second_number = 10

print("Before Swapping")
print(first_number)
print(second_number)

first_number, second_number = second_number, first_number

print("After Swapping")
print(first_number)
print(second_number)

# =============================================================================
# SECTION 20 - Reserved Keywords
# =============================================================================

"""
Reserved keywords cannot be used as variable names.
"""

import keyword

print(keyword.kwlist)

print(f"Total Keywords : {len(keyword.kwlist)}")

# =============================================================================
# SECTION 21 - Variable Scope (Introduction)
# =============================================================================

"""
Variables created outside functions are called global variables.

Variables created inside functions are called local variables.
"""

language = "Python"


def show_language():
    print(language)


show_language()

# =============================================================================
# Local Variable Example
# =============================================================================


def display_name():

    student_name = "Alice"

    print(student_name)


display_name()

"""
The variable student_name only exists inside the function.
"""

# =============================================================================
# SECTION 22 - Variable References
# =============================================================================

"""
Two variables may reference the same object.
"""

list_one = [10, 20, 30]

list_two = list_one

print(list_one)
print(list_two)

print(id(list_one))
print(id(list_two))

print(list_one is list_two)

# =============================================================================
# SECTION 23 - Copy vs Reference
# =============================================================================

"""
Assignment creates a reference, not a copy.
"""

numbers = [1, 2, 3]

another_numbers = numbers

another_numbers.append(4)

print(numbers)
print(another_numbers)

"""
Both variables changed because they reference the same list.
"""

# =============================================================================
# SECTION 24 - Creating a Real Copy
# =============================================================================

numbers = [10, 20, 30]

copied_numbers = numbers.copy()

copied_numbers.append(40)

print(numbers)

print(copied_numbers)

print(numbers is copied_numbers)

# =============================================================================
# SECTION 25 - Mutable vs Immutable (Introduction)
# =============================================================================

"""
Immutable Objects

int
float
bool
str
tuple

Mutable Objects

list
set
dictionary
"""

text = "Python"

print(id(text))

text = "Cyber Security"

print(id(text))

"""
Strings are immutable.

A new object is created after reassignment.
"""

# =============================================================================
# Mutable Example
# =============================================================================

items = ["Router", "Switch"]

print(id(items))

items.append("Firewall")

print(id(items))

"""
Lists are mutable.

The same object is modified instead of creating a new one.
"""

# =============================================================================
# SECTION 26 - Multiple Assignment with Different Types
# =============================================================================

username, score, active = "Alex", 99.5, True

print(username)
print(score)
print(active)

print(type(username))
print(type(score))
print(type(active))

# =============================================================================
# SECTION 27 - Unpacking Values
# =============================================================================

"""
Sequence unpacking assigns values from a sequence to variables.
"""

colors = ["Red", "Green", "Blue"]

first, second, third = colors

print(first)
print(second)
print(third)

# =============================================================================
# SECTION 28 - Best Practices
# =============================================================================

"""
✔ Use meaningful variable names.

✔ Follow snake_case.

✔ Keep names readable.

✔ Use uppercase for constants.

✔ Avoid abbreviations unless they are common.

✔ Avoid single-letter variable names.

✔ Choose descriptive names.
"""

# Good Examples

network_name = "Office LAN"

device_count = 25

is_connected = True

# Poor Examples

# n = "Office"
# x = 25
# y = True

# =============================================================================
# SECTION 29 - Common Mistakes
# =============================================================================

"""
Common Mistakes

❌ Starting a variable with a digit.

❌ Using reserved keywords.

❌ Using unclear names.

❌ Forgetting that Python is case-sensitive.

❌ Assuming assignment creates a copy.

❌ Using uppercase variables for normal values.

❌ Modifying values intended to be constants.
"""

# =============================================================================
# END OF PART 2
# =============================================================================

# =============================================================================
# SECTION 30 - Real-World Example
# =============================================================================

"""
Variables are used everywhere in real-world applications.

The following example represents a simple employee profile.
"""

employee_name = "John Smith"
employee_id = 1052
department = "Network Engineering"
salary = 6500.00
is_full_time = True

print("=" * 60)
print("Employee Information")
print("=" * 60)

print(f"Employee Name : {employee_name}")
print(f"Employee ID   : {employee_id}")
print(f"Department    : {department}")
print(f"Salary        : ${salary}")
print(f"Full Time     : {is_full_time}")

# =============================================================================
# SECTION 31 - Real-World Example (Network Engineer)
# =============================================================================

"""
A practical example for Network Engineers.
"""

hostname = "R1"
management_ip = "192.168.10.1"
vendor = "Cisco"
os_version = "IOS-XE"
uptime_days = 150
ssh_enabled = True

print("\nNetwork Device Information")
print("-" * 60)

print(f"Hostname      : {hostname}")
print(f"Management IP : {management_ip}")
print(f"Vendor        : {vendor}")
print(f"OS Version    : {os_version}")
print(f"Uptime        : {uptime_days} days")
print(f"SSH Enabled   : {ssh_enabled}")

# =============================================================================
# SECTION 32 - Real-World Example (Cybersecurity)
# =============================================================================

"""
Variables are widely used in cybersecurity scripts.
"""

target_ip = "192.168.1.100"
open_port = 443
service = "HTTPS"
status = "Open"

print("\nSecurity Scan Result")
print("-" * 60)

print(f"Target IP : {target_ip}")
print(f"Port      : {open_port}")
print(f"Service   : {service}")
print(f"Status    : {status}")

# =============================================================================
# SECTION 33 - Quick Review
# =============================================================================

"""
You have learned:

✔ Creating variables
✔ Naming conventions
✔ Dynamic typing
✔ type()
✔ id()
✔ None
✔ Constants
✔ Multiple assignment
✔ Variable references
✔ Copy vs Reference
✔ Mutable vs Immutable
✔ Variable scope
✔ Best practices
"""

# =============================================================================
# SECTION 34 - Interview Questions
# =============================================================================

"""
Question 1
----------
What is a variable?

Question 2
----------
Does Python require declaring variable types?

Question 3
----------
What is Dynamic Typing?

Question 4
----------
What does type() return?

Question 5
----------
What does id() return?

Question 6
----------
What is None?

Question 7
----------
Does Python support constants?

Question 8
----------
What is the difference between == and is?

Question 9
----------
What is the difference between copying a list and assigning a list?

Question 10
-----------
Why should variable names be meaningful?
"""

# =============================================================================
# SECTION 35 - Coding Exercises
# =============================================================================

"""
Exercise 1
----------
Create variables for:

First Name
Last Name
Age
Country

Print them using f-strings.
"""

"""
Exercise 2
----------
Create variables of these types:

int
float
str
bool
None

Print the type of each variable.
"""

"""
Exercise 3
----------
Assign three values in one statement.

Print all variables.
"""

"""
Exercise 4
----------
Assign one value to three variables.

Print each variable.
"""

"""
Exercise 5
----------
Swap two numbers without using
a temporary variable.
"""

"""
Exercise 6
----------
Create a constant called PI.

Print its value.
"""

"""
Exercise 7
----------
Create a list.

Assign it to another variable.

Append a new value.

Observe both variables.
"""

"""
Exercise 8
----------
Create a copy of a list.

Modify the copy.

Verify that the original list
has not changed.
"""

"""
Exercise 9
----------
Display all Python reserved keywords.
"""

"""
Exercise 10
-----------
Create five descriptive variables
for a university student.
"""

# =============================================================================
# SECTION 36 - Mini Challenge
# =============================================================================

"""
Build a simple student profile.

Requirements

Full Name

Student ID

University

Major

Current GPA

Graduation Year

Scholarship Status

Print all information using f-strings.
"""

# =============================================================================
# SECTION 37 - Mini Project
# =============================================================================

"""
Mini Project

Network Device Information System

Create variables for:

Hostname

Management IP

Subnet Mask

Default Gateway

MAC Address

Vendor

Model

Operating System

Software Version

Serial Number

Location

Administrator

SSH Status

Uptime

Save all information in variables.

Print a formatted report.
"""

# =============================================================================
# Expected Output Example
# =============================================================================

"""
============================================================

Device Information

============================================================

Hostname        : R1
Vendor          : Cisco
Model           : Catalyst 9300
IP Address      : 192.168.10.1
Subnet Mask     : 255.255.255.0
Gateway         : 192.168.10.254
Operating System: IOS-XE
SSH Enabled     : True
Location        : Data Center

============================================================
"""

# =============================================================================
# SECTION 38 - Best Practices Summary
# =============================================================================

"""
✔ Follow PEP 8.

✔ Use snake_case.

✔ Keep names descriptive.

✔ Avoid meaningless variables.

✔ Avoid unnecessary global variables.

✔ Use constants by convention.

✔ Keep your code readable.

✔ Write comments only when necessary.

✔ Group related variables.

✔ Follow consistent naming throughout the project.
"""

# =============================================================================
# SECTION 39 - Common Mistakes Summary
# =============================================================================

"""
❌ Using reserved keywords.

❌ Starting names with numbers.

❌ Using confusing abbreviations.

❌ Creating unnecessary variables.

❌ Ignoring naming conventions.

❌ Using uppercase for normal variables.

❌ Assuming assignment copies objects.

❌ Forgetting Python is case-sensitive.
"""

# =============================================================================
# SECTION 40 - What's Next?
# =============================================================================

"""
Congratulations!

You have completed the Variables lesson.

Next Lesson

02_data_types.py

Topics include

✔ Numeric Types

✔ Strings

✔ Boolean

✔ NoneType

✔ Lists

✔ Tuples

✔ Sets

✔ Dictionaries

✔ Bytes

✔ Memory Concepts

✔ Mutable vs Immutable (Detailed)

Keep practicing every day.
"""

# =============================================================================
# END OF FILE
# =============================================================================
