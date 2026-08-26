# Inheritance

This module introduces **Inheritance** in Python and explains how it enables classes to reuse, extend, and specialize behavior from other classes.

The module builds on the previous lesson about **Class Methods and Static Methods**, with a particular focus on understanding how `classmethod` and `cls` behave when inheritance is involved.

The examples are designed around practical **Network Engineering and Network Automation** scenarios.

---

## 🎯 Learning Objectives

By completing this module, you will learn how to:

* Understand the concept of inheritance in Python.
* Create parent and child classes.
* Reuse attributes and methods from a parent class.
* Extend parent classes with additional functionality.
* Override methods in child classes.
* Use the `super()` function correctly.
* Understand inheritance of class attributes.
* Understand how `classmethod` behaves with inheritance.
* Understand why `cls` is preferable to hard-coding a class name.
* Build alternative constructors that work with subclasses.
* Apply inheritance to Network Engineering scenarios.
* Combine inheritance with exception handling and validation.
* Write maintainable and reusable object-oriented Python code.

---

## 📚 Topics Covered

### 1. Parent and Child Classes

A parent class contains common functionality that can be reused by one or more child classes.

Example:

```python
class NetworkDevice:
    """Base class for network devices."""

    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address
```

A child class can inherit from it:

```python
class CiscoDevice(NetworkDevice):
    """Represent a Cisco network device."""

    pass
```

The `CiscoDevice` class automatically inherits the attributes and methods of `NetworkDevice`.

---

## 2. Inheritance Syntax

The general syntax is:

```python
class ChildClass(ParentClass):
    ...
```

Example:

```python
class CiscoDevice(NetworkDevice):
    pass
```

This creates an **is-a relationship**:

```text
CiscoDevice
     │
     └── is a NetworkDevice
```

---

## 3. Reusing Parent Methods

A child class can use methods inherited from its parent.

Example:

```python
router = CiscoDevice(
    "R1",
    "192.168.1.1"
)

print(router.show_info())
```

The `show_info()` method can be inherited from `NetworkDevice`.

---

## 4. Method Overriding

A child class can provide its own implementation of a method inherited from the parent.

Example:

```python
class CiscoDevice(NetworkDevice):

    def show_info(self):
        return (
            f"Cisco Device: "
            f"{self.hostname} - {self.ip_address}"
        )
```

The child class now overrides the parent's `show_info()` method.

---

## 5. Using `super()`

The `super()` function allows a child class to access functionality from its parent class.

Example:

```python
class CiscoDevice(NetworkDevice):

    def __init__(
        self,
        hostname,
        ip_address,
        model,
    ):
        super().__init__(
            hostname,
            ip_address,
        )

        self.model = model
```

This avoids duplicating initialization logic.

---

## 6. `super()` and Method Overriding

A child class can extend the behavior of a parent method instead of completely replacing it.

Example:

```python
class CiscoDevice(NetworkDevice):

    def show_info(self):
        base_info = super().show_info()

        return f"{base_info} - Cisco"
```

This allows the child class to reuse and extend existing functionality.

---

# 🔑 Class Methods and Inheritance

One of the most important concepts in this module is understanding how:

```python
@classmethod
```

works with inheritance.

Consider:

```python
class NetworkDevice:

    @classmethod
    def from_string(cls, data):
        hostname, ip_address = data.split(",")

        return cls(
            hostname,
            ip_address,
        )
```

Notice:

```python
return cls(...)
```

instead of:

```python
return NetworkDevice(...)
```

This allows subclasses to reuse the same alternative constructor.

---

## 🧠 Why `cls` Matters

Consider:

```text
NetworkDevice
      │
      ├── CiscoDevice
      │
      └── JuniperDevice
```

If `from_string()` is called through:

```python
CiscoDevice.from_string(...)
```

then:

```python
cls
```

refers to:

```text
CiscoDevice
```

If it is called through:

```python
JuniperDevice.from_string(...)
```

then:

```python
cls
```

refers to:

```text
JuniperDevice
```

Therefore:

```python
return cls(...)
```

is more flexible than:

```python
return NetworkDevice(...)
```

---

# 🌐 Network Engineering Example

The module will use a network device hierarchy such as:

```text
                    NetworkDevice
                          │
              ┌───────────┴───────────┐
              │                       │
        CiscoDevice             JuniperDevice
              │                       │
          IOS/IOS-XE               Junos
```

The parent class will contain common properties such as:

* Hostname
* IP address
* Device validation
* Common information
* Device creation logic

Child classes can add vendor-specific properties and behavior.

---

# 🧩 Alternative Constructors

The parent class can provide a reusable constructor:

```python
@classmethod
def from_string(cls, data):
    ...
```

Child classes can inherit it without duplicating the implementation.

Example:

```python
cisco_router = CiscoDevice.from_string(
    "R1,192.168.1.1"
)
```

The expected result is a:

```text
CiscoDevice
```

rather than a generic:

```text
NetworkDevice
```

---

# 🧪 Exercises

## Exercise 1 — Basic Inheritance

Create:

```python
class NetworkDevice:
    ...
```

Then create:

```python
class CiscoDevice(NetworkDevice):
    ...
```

Verify that the child class can use methods inherited from the parent.

---

## Exercise 2 — Add Vendor Information

Add a Cisco-specific attribute:

```python
vendor = "Cisco"
```

and display it through a method.

---

## Exercise 3 — Method Overriding

Override:

```python
show_info()
```

in `CiscoDevice`.

The child implementation should extend or modify the parent's behavior.

---

## Exercise 4 — Use `super()`

Create a child class with additional initialization parameters.

Use:

```python
super().__init__()
```

to initialize the parent attributes.

---

## Exercise 5 — Alternative Constructor

Use the inherited:

```python
from_string()
```

method to create a `CiscoDevice`.

Verify the returned object's type.

---

## Exercise 6 — Multiple Vendors

Create:

```text
NetworkDevice
      │
      ├── CiscoDevice
      └── JuniperDevice
```

Both subclasses should be able to use:

```python
from_string()
```

without duplicating the implementation.

---

# 🧪 Testing Requirements

The module should test:

* Parent class creation.
* Child class creation.
* Inherited methods.
* Method overriding.
* `super()`.
* Class attributes.
* Alternative constructors.
* `classmethod` behavior with subclasses.
* Invalid input.
* IPv4 validation.
* Correct object types.

Example:

```python
cisco = CiscoDevice.from_string(
    "R1,192.168.1.1"
)

assert isinstance(
    cisco,
    CiscoDevice,
)
```

And:

```python
juniper = JuniperDevice.from_string(
    "R2,192.168.1.2"
)

assert isinstance(
    juniper,
    JuniperDevice,
)
```

---

# ⚠️ Common Mistakes

### 1. Duplicating Parent Initialization

Avoid unnecessarily repeating:

```python
self.hostname = hostname
self.ip_address = ip_address
```

inside every child class.

Prefer:

```python
super().__init__(
    hostname,
    ip_address,
)
```

---

### 2. Hard-Coding the Parent Class

Avoid:

```python
return NetworkDevice(
    hostname,
    ip_address,
)
```

inside a reusable class method.

Prefer:

```python
return cls(
    hostname,
    ip_address,
)
```

---

### 3. Forgetting `super().__init__()`

When a child class defines its own `__init__()`, remember that the parent initialization does not automatically run in the same way as when no child `__init__()` is defined.

Use:

```python
super().__init__(...)
```

when parent initialization is required.

---

### 4. Incorrect Method Overriding

The child method should maintain a compatible interface with the parent method.

---

### 5. Excessive Inheritance

Inheritance should represent a meaningful **is-a relationship**.

Not every class relationship should be implemented using inheritance.

---

# 🏆 Best Practices

* Keep parent classes focused on shared behavior.
* Keep child classes focused on specialized behavior.
* Use `super()` instead of duplicating parent logic.
* Use `cls` in reusable class methods.
* Prefer composition when an `is-a` relationship does not exist.
* Avoid deep inheritance hierarchies.
* Use type hints.
* Validate external input.
* Keep methods small and focused.
* Write tests for inherited and overridden behavior.

---

# 🔬 Professional Design Principle

Inheritance should answer the question:

> **"Is the child class truly a specialized form of the parent class?"**

For example:

```text
CiscoDevice is a NetworkDevice
```

makes sense.

But:

```text
NetworkDevice is a Logger
```

usually does not.

This distinction becomes increasingly important as applications grow.

---

# 📁 Module Structure

```text
23_inheritance/
│
├── README.md
│
├── 01_inheritance.py
│
└── tests/
    └── test_inheritance.py
```

---

# 🔗 Related Python Concepts

This module builds on:

* Classes and Objects
* Instance Methods
* Class Attributes
* `@classmethod`
* `@staticmethod`
* `cls`
* Type Hints
* Exception Handling
* Input Validation

It prepares the learner for:

* Multiple Inheritance
* Method Resolution Order (MRO)
* Abstract Base Classes
* Composition
* Polymorphism
* Protocols
* SOLID Principles
* Design Patterns

---

# 🚀 Professional Goal

The goal of this module is to move beyond simply understanding the syntax of inheritance.

You should be able to design a reusable class hierarchy where:

* Common behavior belongs to the parent.
* Specialized behavior belongs to child classes.
* Shared initialization is handled through `super()`.
* Alternative constructors remain reusable through `cls`.
* Validation and error handling remain consistent.
* The resulting architecture can support real-world Network Automation projects.

By the end of this module, you should be comfortable designing structures such as:

```text
                    NetworkDevice
                          │
             ┌────────────┼────────────┐
             │            │            │
       CiscoDevice   JuniperDevice   AristaDevice
             │            │            │
            IOS          Junos        EOS
```

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

This module is part of the **Python Professional Roadmap**.

The roadmap is designed to progress from Python fundamentals to professional software development, network automation, cybersecurity automation, and AI-powered network engineering.
