# Class Methods & Static Methods

This module introduces two important method types in Python: **Class Methods** and **Static Methods**.

Understanding when and why to use `@classmethod` and `@staticmethod` is essential for writing clean, maintainable, reusable, and professional Python code.

The examples in this module also connect these concepts to practical **Network Engineering and Network Automation** scenarios.

---

## 🎯 Learning Objectives

By completing this module, you will learn how to:

* Understand the difference between Instance Methods, Class Methods, and Static Methods.
* Understand the purpose of `self` and `cls`.
* Use the `@classmethod` decorator correctly.
* Use the `@staticmethod` decorator correctly.
* Work with class-level attributes.
* Create alternative constructors using `@classmethod`.
* Understand when a method should belong to the class rather than an instance.
* Build reusable utility methods with `@staticmethod`.
* Understand how Class Methods behave with inheritance.
* Apply these concepts to Network Engineering examples.
* Write cleaner and more maintainable object-oriented Python code.
* Test and validate class behavior.

---

## 📚 Topics Covered

### 1. Instance Methods

Review how instance methods operate on individual objects using:

```python
self
```

Example:

```python
class NetworkDevice:

    def show_info(self):
        return self.hostname
```

---

### 2. Class Methods

Learn how to define methods that operate at the class level using:

```python
@classmethod
```

and:

```python
cls
```

Example:

```python
class NetworkDevice:

    device_count = 0

    @classmethod
    def get_device_count(cls):
        return cls.device_count
```

---

### 3. Alternative Constructors

Use `@classmethod` to provide additional ways to create objects.

Example:

```python
class NetworkDevice:

    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address

    @classmethod
    def from_string(cls, data):
        hostname, ip_address = data.split(",")
        return cls(hostname, ip_address)
```

This pattern is particularly useful when data comes from:

* Configuration files
* CSV files
* APIs
* Databases
* Network inventory systems

---

### 4. Static Methods

Learn how to define methods that do not require access to either the instance or the class.

```python
@staticmethod
```

Example:

```python
class NetworkUtils:

    @staticmethod
    def is_valid_ip(ip_address):
        ...
```

---

### 5. `self` vs `cls`

A key concept in this module:

| Method Type     | First Parameter | Access          |
| --------------- | --------------- | --------------- |
| Instance Method | `self`          | Instance/Object |
| Class Method    | `cls`           | Class           |
| Static Method   | None            | Neither         |

---

## 🌐 Network Engineering Applications

The concepts covered in this module can be applied to real-world Network Automation tasks such as:

* Network device inventory
* IP address validation
* Device configuration parsing
* Device creation from inventory data
* Network device counters
* Configuration utilities
* Input validation
* Network automation helper functions

Example:

```python
class NetworkDevice:

    device_count = 0

    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address
        NetworkDevice.device_count += 1

    @classmethod
    def from_string(cls, data):
        hostname, ip_address = data.split(",")
        return cls(hostname, ip_address)

    @staticmethod
    def is_valid_ip(ip_address):
        parts = ip_address.split(".")

        if len(parts) != 4:
            return False

        return all(
            part.isdigit() and 0 <= int(part) <= 255
            for part in parts
        )
```

---

## 🧪 Exercises

### Exercise 1 — Class Counter

Create a `NetworkDevice` class that keeps track of the number of devices created.

Requirements:

* Use a class attribute.
* Increment the counter when a new device is created.
* Create a `classmethod` that returns the number of devices.

---

### Exercise 2 — Alternative Constructor

Add a class method:

```python
from_string()
```

It should accept:

```text
R1,192.168.1.1
```

and return a properly initialized `NetworkDevice` object.

---

### Exercise 3 — IP Validation

Create a static method:

```python
is_valid_ip()
```

It should return:

```python
True
```

for valid IPv4 addresses and:

```python
False
```

for invalid addresses.

Test at least:

```text
192.168.1.1
10.0.0.1
172.16.0.1
192.168.1.300
192.168.1
abc.def.1.1
```

---

### Exercise 4 — Network Device Factory

Create multiple alternative constructors for a network device.

For example:

```python
from_dict()
from_string()
```

The goal is to allow the same class to create objects from different data formats.

---

## 🧩 Mini Project

### Network Device Inventory Manager

Build a small object-oriented network inventory system.

The system should support:

* Creating network devices.
* Counting devices.
* Creating devices from strings.
* Validating IP addresses.
* Displaying device information.
* Storing multiple network devices.

Example data:

```text
R1,192.168.1.1
R2,192.168.1.2
SW1,192.168.1.10
SW2,192.168.1.11
```

Expected functionality:

```python
NetworkDevice.from_string(...)
NetworkDevice.get_device_count()
NetworkDevice.is_valid_ip(...)
device.show_info()
```

---

## ⚠️ Common Mistakes

### Using `self` in a Class Method

Incorrect:

```python
@classmethod
def get_count(self):
    ...
```

Preferred:

```python
@classmethod
def get_count(cls):
    ...
```

---

### Using `cls` in a Static Method

Incorrect:

```python
@staticmethod
def validate(cls, ip):
    ...
```

A static method normally does not require `self` or `cls`.

---

### Using a Static Method When Class State Is Required

If the method needs to access:

```python
cls.device_count
```

then `@classmethod` is usually the appropriate choice.

---

### Using a Class Method When Object State Is Required

If the method needs:

```python
self.hostname
```

then it should normally be an instance method.

---

## 🏆 Best Practices

* Use instance methods for object-specific behavior.
* Use class methods for class-level behavior.
* Use class methods for alternative constructors.
* Use static methods for logically related utility functions.
* Prefer `cls` instead of hard-coding the class name inside class methods.
* Keep methods focused on a single responsibility.
* Validate input before creating or processing network objects.
* Write tests for important validation logic.
* Keep networking logic separated from generic utility functions.

---

## 🧪 Testing

The module should include tests covering:

* Instance method behavior.
* Class method behavior.
* Alternative constructors.
* Static method behavior.
* IPv4 validation.
* Device counting.
* Invalid input handling.

Example:

```python
assert NetworkDevice.is_valid_ip("192.168.1.1")
assert not NetworkDevice.is_valid_ip("192.168.1.300")
```

---

## 📁 Module Structure

```text
22_class_methods_static_methods/
│
├── README.md
│
├── 01_class_methods_static_methods.py
│
└── tests/
    └── test_class_methods_static_methods.py
```

---

## 🔗 Related Python Concepts

This module builds on the following concepts:

* Classes and Objects
* `__init__`
* Instance Attributes
* Class Attributes
* Methods
* Decorators
* Dataclasses
* Object-Oriented Programming

It prepares the learner for more advanced topics including:

* Inheritance
* Composition
* Abstract Base Classes
* Protocols
* SOLID Principles
* Design Patterns
* Advanced Object-Oriented Design

---

## 🚀 Professional Goal

The goal of this module is not simply to memorize `@classmethod` and `@staticmethod`.

The real objective is to understand **method responsibility and object-oriented design**.

A professional Python developer should be able to answer:

> **Should this behavior belong to the object, the class, or neither?**

That decision is fundamental to writing scalable and maintainable Python applications.

---

## 👨‍💻 Author

**Mohammed AL-Dubai**

**Next Generation Network Engineer**

Focus Areas:

* Network Engineering
* Network Automation
* Cybersecurity
* Python
* AI & Network Engineering
* Infrastructure Automation

---

## 📌 Part of Python Professional Roadmap

This module is part of the:

**Python Professional Roadmap**

A structured learning path designed to progress from Python fundamentals to professional development, network automation, cybersecurity automation, and AI-powered network engineering.
