# Lesson 27 — Advanced Polymorphism & Design Patterns

## 📌 Overview

This lesson builds on the Object-Oriented Programming concepts covered in the previous lessons and moves toward more advanced and scalable software design.

The focus is on using **Advanced Polymorphism** and introducing **Design Patterns** that are highly useful when building maintainable Python applications, especially **Network Automation systems**.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* Understand advanced forms of polymorphism in Python.
* Understand and apply Duck Typing.
* Understand the relationship between Duck Typing and Protocols.
* Understand why design patterns are useful.
* Implement the **Strategy Pattern**.
* Implement the **Factory Pattern**.
* Apply design patterns to Network Automation.
* Combine:

  * ABC
  * Protocol
  * Polymorphism
  * Composition
  * Dependency Injection
  * Design Patterns
* Build flexible and extensible Python architectures.

---

# 🗺️ Lesson Roadmap

## 27.1 Advanced Polymorphism

Review and extend the concept of polymorphism.

Topics:

* Runtime polymorphism
* Method overriding
* Polymorphic functions
* Polymorphism across different device types
* Designing functions that work with multiple implementations

### Network Automation Example

A single function should be able to work with:

```text
CiscoRouter
CiscoSwitch
JuniperRouter
JuniperSwitch
```

without requiring separate functions for every device type.

---

# 27.2 Duck Typing

Understand Python's dynamic approach to polymorphism.

### Core Principle

> If an object provides the required behavior, we can use it.

Example concept:

```text
SSHConnection
      │
      └── connect()

APIConnection
      │
      └── connect()

SNMPConnection
      │
      └── connect()
```

All can be used by code that requires a `connect()` method.

### Key Concept

```text
Duck Typing
     ↓
Focus on behavior
     ↓
"What can this object do?"
```

---

# 27.3 Duck Typing vs Protocol

Compare traditional Duck Typing with `typing.Protocol`.

### Duck Typing

```python
def establish_connection(connection):
    return connection.connect()
```

The function assumes the object provides `connect()`.

### Protocol

```python
from typing import Protocol


class Connection(Protocol):

    def connect(self) -> str:
        ...
```

Then:

```python
def establish_connection(connection: Connection) -> str:
    return connection.connect()
```

### Key Difference

```text
Duck Typing
    ↓
Behavior is assumed

Protocol
    ↓
Behavior is explicitly described
```

Protocol provides better:

* Type checking
* IDE support
* Documentation
* Maintainability

---

# 27.4 Introduction to Design Patterns

A **Design Pattern** is a reusable solution to a common software design problem.

Design patterns are not ready-made libraries or code that must be copied exactly.

They are **design approaches** that help us structure software effectively.

### Why Design Patterns?

Without good design:

```text
Small Project
     ↓
More Features
     ↓
More if/elif
     ↓
More Dependencies
     ↓
Hard to Maintain
```

With good design:

```text
Clear Architecture
       ↓
Loose Coupling
       ↓
Easy Extension
       ↓
Better Maintainability
```

---

# 27.5 Strategy Pattern ⭐

The first major design pattern in this lesson.

The **Strategy Pattern** allows us to define multiple interchangeable algorithms or behaviors and select one at runtime.

### General Structure

```text
                Context
                   │
                   ▼
                Strategy
                   │
        ┌──────────┼──────────┐
        │          │          │
   Strategy A  Strategy B  Strategy C
```

---

## Network Automation Example

Imagine that a network device can be configured using different methods:

```text
Configuration Strategy
        │
   ┌────┼─────┐
   │    │     │
 CLI   API   NETCONF
```

Instead of creating a huge class containing:

```python
if method == "cli":
    ...
elif method == "api":
    ...
elif method == "netconf":
    ...
```

we can separate each behavior into its own strategy.

---

# 27.6 Strategy Pattern with Protocol

A Protocol can define the Strategy interface.

Example:

```python
from typing import Protocol


class ConfigurationStrategy(Protocol):

    def configure(self) -> str:
        ...
```

Different strategies:

```text
CLIConfiguration
APIConfiguration
NETCONFConfiguration
```

Each provides:

```python
configure()
```

The main application can then use any strategy that follows the required behavior.

---

# 27.7 Strategy Pattern + Dependency Injection

The selected strategy can be injected into another class.

Concept:

```text
NetworkDevice
      │
      └── ConfigurationStrategy
                │
        ┌───────┼────────┐
        │       │        │
       CLI     API    NETCONF
```

This demonstrates:

* Composition
* Dependency Injection
* Protocol
* Polymorphism
* Loose Coupling

---

# 27.8 Factory Pattern ⭐

The second major design pattern in this lesson.

The **Factory Pattern** centralizes object creation.

Instead of creating objects directly throughout the application:

```python
CiscoRouter(...)
JuniperRouter(...)
CiscoSwitch(...)
```

we can delegate creation to a Factory.

Concept:

```text
             DeviceFactory
                  │
        ┌─────────┼─────────┐
        │         │         │
     Cisco      Juniper    ...
```

Example concept:

```python
device = DeviceFactory.create("cisco_router")
```

The Factory decides which class should be created.

---

# 27.9 Factory Pattern + Network Automation

The Factory can create different network devices:

```text
                    DeviceFactory
                          │
          ┌───────────────┼───────────────┐
          │               │               │
     CiscoRouter     CiscoSwitch     JuniperRouter
```

This allows the application to separate:

```text
Object Creation
      ↓
Business Logic
```

---

# 27.10 Combining Strategy + Factory

A more advanced architecture:

```text
                   DeviceFactory
                        │
                        ▼
                 NetworkDevice
                        │
               ┌────────┴────────┐
               │                 │
          CiscoRouter       JuniperRouter
               │                 │
               └────────┬────────┘
                        │
                 Configuration
                    Strategy
                        │
             ┌──────────┼──────────┐
             │          │          │
            CLI        API      NETCONF
```

This architecture allows us to change:

* Device type
* Vendor
* Connection method
* Configuration method

without rewriting the entire application.

---

# 27.11 ABC + Protocol + Composition

By the end of this lesson, we will combine the concepts from Lessons 23–27.

```text
                    NetworkDevice
                         ABC
                          │
              ┌───────────┴───────────┐
              │                       │
         CiscoRouter             JuniperRouter
              │                       │
              └───────────┬───────────┘
                          │
                     Composition
                          │
                    Connection
                     Protocol
                          │
                 ┌────────┴────────┐
                 │                 │
                SSH               API
```

And:

```text
NetworkDevice
      │
      └── ConfigurationStrategy
                    │
             ┌──────┼──────┐
             │      │      │
            CLI    API   NETCONF
```

This creates a flexible architecture based on **separation of responsibilities**.

---

# 27.12 Design Principles

Throughout this lesson, we will focus on several important software engineering principles.

## Loose Coupling

Classes should depend on abstractions rather than concrete implementations.

## High Cohesion

Each class should have a clear responsibility.

## Separation of Concerns

Different responsibilities should be separated.

Example:

```text
Device
Connection
Configuration
Monitoring
Object Creation
```

should not all be tightly coupled inside one large class.

## Open/Closed Principle

Software should be:

> Open for extension, but closed for modification.

For example, adding:

```text
NETCONFConfiguration
```

should not require rewriting existing CLI and API implementations.

---

# 27.13 Network Automation Application

We will gradually build a small architecture capable of handling:

```text
Devices
   │
   ├── Cisco
   ├── Juniper
   └── Other Vendors

Connections
   │
   ├── SSH
   ├── API
   └── Other Methods

Configuration
   │
   ├── CLI
   ├── API
   └── NETCONF

Monitoring
   │
   └── Device Status
```

The goal is not to build a production automation framework yet.

The goal is to understand how professional Python applications can be structured for future expansion.

---

# 27.14 Practical Exercises

During the lesson, we will implement:

### Exercise 1 — Duck Typing

Create multiple connection classes with the same behavior.

### Exercise 2 — Strategy Pattern

Create multiple configuration strategies.

### Exercise 3 — Dependency Injection

Inject the selected strategy into a network device.

### Exercise 4 — Factory Pattern

Create a factory that creates different device types.

### Exercise 5 — Polymorphic Management

Use one manager to operate on multiple devices.

---

# 🏆 Final Challenge — Network Automation System

Build a small Network Automation System using the concepts learned in Lessons 23–27.

The system should include:

### Devices

```text
CiscoRouter
CiscoSwitch
JuniperRouter
JuniperSwitch
```

### Connection

Use a Protocol defining:

```text
connect()
disconnect()
```

Implement at least:

```text
SSHConnection
APIConnection
```

### Configuration Strategy

Use a Protocol defining:

```text
configure()
```

Implement at least:

```text
CLIConfiguration
APIConfiguration
```

### Device Architecture

Use an ABC for:

```text
NetworkDevice
```

with appropriate abstract methods.

### Factory

Create:

```text
DeviceFactory
```

to create network devices.

### Manager

Create a manager capable of operating on multiple devices polymorphically.

---

# 📁 Suggested File Structure

```text
27_advanced_polymorphism_design_patterns/
│
├── README.md
│
├── 01_advanced_polymorphism.py
├── 02_duck_typing.py
├── 03_protocol_vs_duck_typing.py
├── 04_strategy_pattern.py
├── 05_strategy_network_automation.py
├── 06_factory_pattern.py
├── 07_factory_network_devices.py
├── 08_combined_architecture.py
│
└── challenge/
    └── network_automation_system.py
```

---

# 🧠 Key Takeaways

By the end of Lesson 27, remember:

```text
Polymorphism
     ↓
Multiple implementations
     ↓
Duck Typing
     ↓
Behavior-based design
     ↓
Protocol
     ↓
Explicit structural contract
     ↓
Strategy Pattern
     ↓
Interchangeable behavior
     ↓
Factory Pattern
     ↓
Centralized object creation
```

The ultimate goal is to move from:

```text
"How do I write this class?"
```

to:

```text
"How should I design this system?"
```

---

# 📊 Progress

**Stage:** `03-python-intermediate`

**Lesson:** `27 — Advanced Polymorphism & Design Patterns`

**Status:** 🟡 In Progress

### Previous Lessons

* ✅ 21 — Classes & Objects
* ✅ 22 — Class Methods & Static Methods
* ✅ 23 — Inheritance & Polymorphism
* ✅ 24 — Multiple Inheritance & MRO
* ✅ 25 — Composition
* ✅ 26 — Abstract Base Classes & Interfaces

### Current Lesson

* 🟡 27 — Advanced Polymorphism & Design Patterns

### Next

* ⬜ 28 — Exception Handling

---

# 🚀 Learning Philosophy

```text
Learn
  ↓
Understand
  ↓
Code
  ↓
Test
  ↓
Apply
  ↓
Document
  ↓
Publish
  ↓
Prove Your Skills
```

This lesson is an important step toward designing professional **Python Network Automation systems** rather than simply writing isolated scripts.
