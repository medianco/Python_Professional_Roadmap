# Lesson 26 — Abstract Base Classes (ABC) & Interfaces

## 📚 Python Intermediate

### Abstract Base Classes, Interfaces & Contracts

This lesson introduces **Abstract Base Classes (ABC)** and the concept of **Interfaces / Contracts** in Python.

The goal is to understand how Python can define a common structure that subclasses must follow while still allowing each implementation to provide its own behavior.

These concepts are especially useful when designing scalable applications such as:

* Network Automation systems
* Device management platforms
* Monitoring systems
* Security automation tools
* API integrations

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* Understand Abstract Base Classes
* Use the `ABC` class
* Use `@abstractmethod`
* Create abstract methods
* Understand abstract vs concrete classes
* Understand Interfaces and Contracts
* Implement Polymorphism using ABC
* Design extensible class hierarchies
* Understand the relationship between ABC and Inheritance
* Compare ABC with `Protocol`
* Apply ABC concepts to Network Engineering

---

# 1. What is an Abstract Base Class?

An **Abstract Base Class (ABC)** is a class that defines a common structure or contract for its subclasses.

It can contain:

* Normal methods
* Abstract methods
* Attributes
* Shared functionality

An abstract method defines behavior that subclasses are required to implement.

Example:

```python
from abc import ABC, abstractmethod


class NetworkDevice(ABC):
    """Define the common interface for network devices."""

    @abstractmethod
    def connect(self) -> str:
        """Connect to the network device."""
        ...
```

`NetworkDevice` defines a contract:

> Every concrete network device must provide a `connect()` method.

---

# 2. The `ABC` Class

Python provides the `ABC` class through the `abc` module.

```python
from abc import ABC


class NetworkDevice(ABC):
    """Define an abstract network device."""
```

A class becomes an Abstract Base Class by inheriting from `ABC`.

---

# 3. The `@abstractmethod` Decorator

The `@abstractmethod` decorator is used to define methods that subclasses must implement.

```python
from abc import ABC, abstractmethod


class NetworkDevice(ABC):

    @abstractmethod
    def connect(self) -> str:
        """Connect to the network device."""
        ...
```

The abstract method provides the required interface.

It does not necessarily provide the implementation.

---

# 4. Abstract vs Concrete Classes

## Abstract Class

An abstract class defines a common contract.

Example:

```python
class NetworkDevice(ABC):

    @abstractmethod
    def connect(self) -> str:
        ...
```

It is not intended to be instantiated directly.

---

## Concrete Class

A concrete class implements all required abstract methods.

Example:

```python
class CiscoRouter(NetworkDevice):

    def connect(self) -> str:
        return "Connected to Cisco Router"
```

`CiscoRouter` is now a concrete implementation.

---

# 5. Why Can't We Instantiate an Abstract Class?

Consider:

```python
device = NetworkDevice()
```

Python will raise an error because the abstract method has not been implemented.

Conceptually:

```text
NetworkDevice
       │
       │ abstract
       ↓
   connect()
       │
       │
       ├───────────────┐
       ↓               ↓
CiscoRouter       CiscoSwitch
   connect()         connect()
```

The abstract class defines **what must exist**.

The subclasses define **how it works**.

---

# 6. Interfaces and Contracts

An interface defines what a class should provide without necessarily specifying how the behavior is implemented.

Think of it as a **contract**.

For example:

```text
NetworkDevice Contract
        │
        ├── connect()
        ├── disconnect()
        └── show_status()
```

Any concrete network device must satisfy this contract.

Different devices can implement the operations differently.

---

# 7. Polymorphism with ABC

ABC works naturally with polymorphism.

Example:

```python
class CiscoRouter(NetworkDevice):

    def connect(self) -> str:
        return "Connected to Cisco Router"


class CiscoSwitch(NetworkDevice):

    def connect(self) -> str:
        return "Connected to Cisco Switch"
```

Both classes implement the same interface:

```python
device.connect()
```

But the behavior depends on the actual object.

```text
NetworkDevice
      │
      ├── CiscoRouter
      │      └── connect()
      │
      └── CiscoSwitch
             └── connect()
```

This is **Polymorphism**.

---

# 8. Abstract Classes Can Contain Concrete Methods

An ABC does not have to contain only abstract methods.

It can provide shared functionality.

Example:

```python
class NetworkDevice(ABC):

    def show_info(self) -> str:
        return "Network Device"

    @abstractmethod
    def connect(self) -> str:
        ...
```

Here:

* `show_info()` has an implementation
* `connect()` must be implemented by subclasses

This allows common behavior to be centralized.

---

# 9. ABC with Multiple Abstract Methods

An abstract class can define multiple contracts.

Example:

```python
class NetworkDevice(ABC):

    @abstractmethod
    def connect(self) -> str:
        ...

    @abstractmethod
    def disconnect(self) -> str:
        ...

    @abstractmethod
    def show_status(self) -> str:
        ...
```

Every concrete subclass must implement all three methods.

---

# 10. Network Engineering Example

Imagine we are building a Network Automation platform.

Different vendors may use different implementations:

```text
                    NetworkDevice
                    Abstract Class
                          │
          ┌───────────────┼───────────────┐
          ↓               ↓               ↓
       Cisco            Juniper          Arista
          │               │               │
          ↓               ↓               ↓
       IOS/IOS-XE        Junos            EOS
```

The automation system does not need to know every implementation detail.

It only needs to know the common contract:

```text
connect()
disconnect()
get_config()
show_status()
```

This makes the system easier to extend.

---

# 11. ABC vs Protocol

Both `ABC` and `Protocol` can define interfaces, but they work differently.

| Feature                      | ABC         | Protocol  |
| ---------------------------- | ----------- | --------- |
| Inheritance required         | Usually yes | No        |
| Explicit contract            | Yes         | Yes       |
| Runtime abstract enforcement | Yes         | Limited   |
| Structural typing            | No          | Yes       |
| `@abstractmethod`            | Yes         | No        |
| Useful for class hierarchies | Excellent   | Good      |
| Loose coupling               | Good        | Excellent |
| Duck typing                  | No          | Yes       |

### ABC

ABC generally uses **nominal typing**.

A class explicitly inherits from the abstract base class.

```python
class CiscoRouter(NetworkDevice):
    ...
```

### Protocol

Protocol uses **structural typing**.

A class does not necessarily need to inherit from the Protocol.

If it provides the required methods, it can satisfy the interface.

```python
class SSHConnection:
    def connect(self) -> str:
        ...

    def disconnect(self) -> str:
        ...
```

This is one of the most important differences between the two approaches.

---

# 12. ABC vs Composition

ABC and Composition solve different problems.

### ABC

Defines a common contract between related classes.

```text
NetworkDevice
      │
      ├── CiscoRouter
      ├── CiscoSwitch
      └── Firewall
```

### Composition

Builds an object from independent components.

```text
NetworkDevice
      │
      ├── Connection
      ├── ConfigurationManager
      └── MonitoringManager
```

They can also be used together.

For example:

```text
             Abstract NetworkDevice
                       │
             ┌─────────┴─────────┐
             ↓                   ↓
       CiscoRouter          CiscoSwitch
             │                   │
             └─────────┬─────────┘
                       │
                 Composition
                       │
              ┌────────┼────────┐
              ↓        ↓        ↓
          Connection  Config  Monitoring
```

This combination is useful in professional software design.

---

# 13. ABC Design Principle

A useful design principle is:

> **Program against an abstraction, not a concrete implementation.**

Instead of designing the entire system around:

```text
SSHConnection
```

we can design around:

```text
Connection
```

And instead of requiring a specific vendor implementation:

```text
CiscoRouter
```

we can work with:

```text
NetworkDevice
```

This makes the system easier to extend and maintain.

---

# 14. Extensibility

One major advantage of ABC is extensibility.

Suppose the system initially supports:

```text
CiscoRouter
CiscoSwitch
```

Later we can add:

```text
JuniperRouter
AristaSwitch
FortinetFirewall
PaloAltoFirewall
```

without changing the fundamental abstraction.

```text
                 NetworkDevice
                 Abstract Contract
                        │
        ┌───────────────┼────────────────┐
        ↓               ↓                ↓
      Cisco           Juniper          Arista
        │               │                │
      Router          Router           Switch
```

This is an important concept in scalable automation systems.

---

# 15. Practical Network Automation Architecture

A professional automation application could use:

```text
                    Automation Engine
                           │
                           ↓
                   NetworkDevice ABC
                           │
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
       Cisco            Juniper          Arista
          │                │                │
          └────────────────┼────────────────┘
                           ↓
                    Connection Layer
                           │
                  ┌────────┴────────┐
                  ↓                 ↓
                SSH               API
```

The automation engine works with the abstraction rather than depending directly on every vendor implementation.

---

# 🧪 Practical Exercise

Create an abstract `NetworkDevice` class.

The class should define a common contract for network devices.

Create at least:

* `CiscoRouter`
* `CiscoSwitch`
* `Firewall`

Each concrete class should implement the required abstract methods.

The system should demonstrate polymorphism by storing different devices in a collection and executing the same operations on all of them.

---

# 🧩 Challenge

After completing the lesson, implement a small **Network Device Management System** using Abstract Base Classes.

The system should support multiple network device types while maintaining a common interface.

Requirements:

* Define an abstract network device
* Define required device operations
* Implement multiple concrete device classes
* Demonstrate polymorphism
* Prevent direct instantiation of the abstract class
* Use appropriate type hints
* Keep the design extensible
* Apply the concepts to a realistic Network Engineering scenario

The implementation should use only the Python standard library.

---

# 📁 Suggested Structure

```text
26_abstract_base_classes_interfaces/
│
├── README.md
│
├── 01_abc_basics.py
├── 02_abstract_methods.py
├── 03_concrete_classes.py
├── 04_polymorphism_with_abc.py
├── 05_abc_network_devices.py
└── challenge.py
```

---

# 🎓 Skills Practiced

This lesson develops the following skills:

* Abstract Base Classes
* Interfaces
* Contracts
* Abstract Methods
* Inheritance
* Polymorphism
* Encapsulation
* Loose Coupling
* Extensible Architecture
* Type Hints
* Network Automation Design

---

# 🔑 Key Takeaways

### 1. ABC defines a contract

```text
ABC
 ↓
Defines required behavior
```

### 2. `@abstractmethod` defines required methods

```python
@abstractmethod
def connect(self):
    ...
```

### 3. Concrete classes implement the contract

```python
class CiscoRouter(NetworkDevice):
    ...
```

### 4. ABC supports polymorphism

Different implementations can be treated through the same abstraction.

### 5. ABC and Protocol are not identical

```text
ABC
 ↓
Explicit inheritance + abstract contract

Protocol
 ↓
Structural typing + flexible contract
```

### 6. ABC and Composition can work together

They solve different architectural problems and can be combined in professional applications.

---

# 🚀 Connection to Previous Lessons

This lesson builds directly on the previous OOP lessons:

```text
Classes & Objects
       ↓
Class & Static Methods
       ↓
Inheritance
       ↓
Polymorphism
       ↓
Multiple Inheritance & MRO
       ↓
Composition
       ↓
Protocol
       ↓
🔥 Abstract Base Classes & Interfaces
```

---

# 📈 Progress

| Topic                           | Status |
| ------------------------------- | ------ |
| ABC                             | ⏳      |
| `@abstractmethod`               | ⏳      |
| Abstract vs Concrete Classes    | ⏳      |
| Interfaces & Contracts          | ⏳      |
| Polymorphism with ABC           | ⏳      |
| ABC vs Protocol                 | ⏳      |
| Network Engineering Application | ⏳      |
| Challenge                       | ⏳      |

---

# 🎯 Lesson Goal

The ultimate goal is to move from simply creating classes to **designing reliable abstractions and scalable architectures**.

By the end of this lesson, you should understand not only:

> **How to use an Abstract Base Class**

but also:

> **Why and when an abstraction should be introduced into a software design.**

---

**Author:** Mohammed AL-Dubai

**Roadmap:** Python Professional Development

**Focus:** Python • Networking • Cybersecurity • AI
