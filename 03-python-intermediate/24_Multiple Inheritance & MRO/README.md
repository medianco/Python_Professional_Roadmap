# Multiple Inheritance & Method Resolution Order (MRO)

This module introduces **Multiple Inheritance** in Python and explains how Python determines which method to execute when a class inherits from multiple parent classes.

The module builds on the previous lesson about **Inheritance and Polymorphism** and focuses on the **Method Resolution Order (MRO)** and the behavior of `super()` in complex inheritance hierarchies.

Examples are designed around practical **Network Engineering and Network Automation** scenarios.

---

## 🎯 Learning Objectives

By completing this module, you will learn how to:

* Understand Multiple Inheritance in Python.
* Create classes with more than one parent class.
* Reuse functionality from multiple parent classes.
* Understand Method Resolution Order (MRO).
* Inspect MRO using `__mro__`.
* Inspect MRO using the `mro()` method.
* Understand how Python searches for methods.
* Use `super()` correctly with Multiple Inheritance.
* Understand the Diamond Problem.
* Understand cooperative multiple inheritance.
* Avoid common Multiple Inheritance mistakes.
* Apply Multiple Inheritance to Network Engineering scenarios.
* Design maintainable class hierarchies.

---

# 📚 Topics Covered

## 1. Multiple Inheritance

In Python, a class can inherit from more than one parent class.

Example:

```python
class NetworkDevice:
    pass


class Monitorable:
    pass


class ManagedDevice(NetworkDevice, Monitorable):
    pass
```

The class hierarchy becomes:

```text
NetworkDevice       Monitorable
      │                  │
      └────────┬─────────┘
               │
        ManagedDevice
```

`ManagedDevice` inherits functionality from both parent classes.

---

# 2. Single vs Multiple Inheritance

### Single Inheritance

```text
NetworkDevice
      │
      ▼
CiscoDevice
```

The child has one direct parent.

### Multiple Inheritance

```text
NetworkDevice       Monitorable
      │                  │
      └────────┬─────────┘
               │
        ManagedDevice
```

The child has multiple direct parents.

---

# 3. Reusing Multiple Parent Classes

Each parent class can provide a specialized responsibility.

Example:

```python
class NetworkDevice:
    def show_network_info(self):
        return "Network information"


class Monitorable:
    def show_monitoring_info(self):
        return "Monitoring information"


class ManagedDevice(NetworkDevice, Monitorable):
    pass
```

Now:

```python
device = ManagedDevice()

print(device.show_network_info())
print(device.show_monitoring_info())
```

The child class can use functionality from both parents.

---

# 🔑 Method Resolution Order — MRO

When Python needs to find a method, it follows a specific order.

This order is called:

> **Method Resolution Order (MRO)**

Consider:

```python
class A:
    pass


class B(A):
    pass


class C(B):
    pass
```

The MRO can be inspected with:

```python
print(C.__mro__)
```

or:

```python
print(C.mro())
```

The result represents the order in which Python searches for attributes and methods.

---

# 🧠 Why MRO Matters

MRO becomes especially important when multiple parent classes contain methods with the same name.

Example:

```python
class NetworkDevice:

    def connect(self):
        return "NetworkDevice connection"


class Monitorable:

    def connect(self):
        return "Monitorable connection"


class ManagedDevice(NetworkDevice, Monitorable):
    pass
```

Now:

```python
device = ManagedDevice()

print(device.connect())
```

Which `connect()` method will Python execute?

The answer depends on the class's **MRO**.

---

# 🔍 Inspecting MRO

Python provides two common ways to inspect MRO.

### Using `__mro__`

```python
print(ManagedDevice.__mro__)
```

### Using `mro()`

```python
print(ManagedDevice.mro())
```

Both allow us to understand the method lookup order.

---

# 🧩 The Diamond Problem

A common Multiple Inheritance structure is called the **Diamond Problem**.

Example:

```text
             NetworkDevice
                /      \
               /        \
       CiscoDevice    SecurityDevice
               \        /
                \      /
             EnterpriseDevice
```

The bottom class inherits indirectly from the same top-level parent through multiple paths.

This creates the question:

> Which parent should Python use first?

Python solves this using **MRO**.

---

# 🧠 Python's MRO Algorithm

Python uses the **C3 Linearization algorithm** to calculate MRO.

The goal is to produce a consistent method lookup order while preserving the relationships between classes.

For example:

```python
print(EnterpriseDevice.mro())
```

might produce an order conceptually similar to:

```text
EnterpriseDevice
CiscoDevice
SecurityDevice
NetworkDevice
object
```

The exact order depends on the inheritance hierarchy.

---

# 🔄 `super()` with Multiple Inheritance

`super()` becomes especially powerful in Multiple Inheritance.

Consider:

```python
class A:

    def show(self):
        print("A")


class B(A):

    def show(self):
        print("B")
        super().show()


class C(A):

    def show(self):
        print("C")
        super().show()


class D(B, C):

    def show(self):
        print("D")
        super().show()
```

Calling:

```python
D().show()
```

does not simply mean:

```text
D → B → A
```

Instead, Python follows the MRO:

```text
D → B → C → A → object
```

This is called **cooperative multiple inheritance**.

---

# 🤝 Cooperative Multiple Inheritance

For Multiple Inheritance to work correctly, each class should cooperate by calling:

```python
super()
```

rather than directly calling a specific parent.

Prefer:

```python
super().show()
```

instead of:

```python
ParentClass.show(self)
```

This allows Python to follow the MRO correctly.

---

# 🌐 Network Engineering Example

This module uses a realistic network-oriented hierarchy.

For example:

```text
                     NetworkDevice
                           │
              ┌────────────┴────────────┐
              │                         │
        NetworkFeatures          SecurityFeatures
              │                         │
              └────────────┬────────────┘
                           │
                    EnterpriseDevice
```

Possible responsibilities:

### `NetworkDevice`

Common network functionality:

* Hostname
* IP address
* Device information
* IPv4 validation

### `NetworkFeatures`

Network-specific functionality:

* VLAN configuration
* Routing
* Interfaces
* Network connectivity

### `SecurityFeatures`

Security-specific functionality:

* Access control
* Security status
* Monitoring
* Security policies

### `EnterpriseDevice`

Combines functionality from both feature classes.

---

# 🧪 Practical Example

A simplified implementation might look like:

```python
class NetworkDevice:

    def show_info(self):
        return "Network device"


class NetworkFeatures:

    def configure_network(self):
        return "Network configuration"


class SecurityFeatures:

    def configure_security(self):
        return "Security configuration"


class EnterpriseDevice(
    NetworkDevice,
    NetworkFeatures,
    SecurityFeatures,
):
    pass
```

Now:

```python
device = EnterpriseDevice()

print(device.show_info())
print(device.configure_network())
print(device.configure_security())
```

The single object can use functionality provided by multiple parent classes.

---

# 🧪 Testing Requirements

The module should test:

* Multiple parent classes.
* Inherited methods.
* Method conflicts.
* MRO.
* `__mro__`.
* `mro()`.
* `super()`.
* Cooperative inheritance.
* Diamond Problem.
* Correct method lookup.
* Network Engineering use cases.

Example:

```python
print(EnterpriseDevice.__mro__)
```

and:

```python
print(EnterpriseDevice.mro())
```

---

# ⚠️ Common Mistakes

## 1. Calling a Parent Directly

Avoid unnecessarily writing:

```python
ParentClass.method(self)
```

because it can bypass the MRO.

Prefer:

```python
super().method()
```

---

## 2. Forgetting `super()`

In cooperative Multiple Inheritance, forgetting:

```python
super()
```

can stop the method chain.

---

## 3. Creating Unnecessary Multiple Inheritance

Multiple Inheritance should be used carefully.

If a simpler design works, consider:

* Single inheritance
* Composition
* Delegation

---

## 4. Ignoring MRO

Never assume which method Python will call.

Inspect it:

```python
ClassName.mro()
```

---

## 5. Confusing `super()` with "My Parent"

A very important concept:

> `super()` does not simply mean "call my parent class."

It means:

> **Continue the method lookup according to the MRO.**

This distinction becomes critical in Multiple Inheritance.

---

# 🏆 Best Practices

* Keep each parent class focused on a clear responsibility.
* Avoid overly complex inheritance trees.
* Understand the MRO before using Multiple Inheritance.
* Use `super()` for cooperative inheritance.
* Avoid hard-coding parent class names unnecessarily.
* Prefer composition when the relationship is not truly an inheritance relationship.
* Use meaningful class names.
* Keep methods small and focused.
* Use type hints.
* Write tests for method resolution behavior.

---

# 🔬 Professional Design Principle

Multiple Inheritance should not be used simply because Python allows it.

A good design should have clearly separated responsibilities.

For example:

```text
NetworkDevice
      │
      ├── Networking responsibility
      │
      ├── Monitoring responsibility
      │
      └── Security responsibility
```

Each parent should represent a meaningful capability or abstraction.

A well-designed Multiple Inheritance hierarchy should be:

* Predictable
* Understandable
* Testable
* Maintainable
* Extendable

---

# 📁 Module Structure

```text
24_multiple_inheritance/
│
├── README.md
│
├── 01_multiple_inheritance.py
│
└── tests/
    └── test_multiple_inheritance.py
```

---

# 🔗 Related Python Concepts

This module builds on:

* Classes and Objects
* Inheritance
* Method Overriding
* `super()`
* `classmethod`
* `staticmethod`
* `cls`
* Polymorphism
* Type Hints
* Exception Handling

It prepares the learner for:

* Abstract Base Classes
* Interfaces and Protocols
* Composition
* SOLID Principles
* Design Patterns
* Advanced Object-Oriented Programming

---

# 🚀 Professional Goal

The goal of this module is to understand not only **how** Multiple Inheritance works, but **why** Python needs MRO and how `super()` enables cooperative class hierarchies.

By the end of this module, you should be able to analyze a hierarchy such as:

```text
                       NetworkDevice
                      /             \
                     /               \
             NetworkFeatures    SecurityFeatures
                     \               /
                      \             /
                       EnterpriseDevice
```

and determine:

1. Which methods are available.
2. Which implementation Python will execute.
3. Why that implementation is selected.
4. How MRO determines the lookup order.
5. How `super()` moves through the MRO.
6. When Multiple Inheritance is appropriate.
7. When composition would be a better design.

---

# 👨‍💻 Author

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

# 📌 Part of Python Professional Roadmap

This module is part of the **Python Professional Roadmap**.

The roadmap progresses from Python fundamentals to professional software development, Network Automation, Cybersecurity Automation, and AI-powered Network Engineering.
