# 🐍 Python Intermediate

## Professional Python Development Roadmap

Welcome to the **Python Intermediate** stage of the Python Professional Roadmap.

This stage is designed to move from basic Python programming to **professional, maintainable, and scalable Python development**, with a strong focus on practical applications in:

* Network Engineering
* Network Automation
* Cybersecurity Automation
* AI Engineering
* Infrastructure Automation

---

## 🎯 Stage Objectives

By completing this stage, you will be able to:

* Design applications using Object-Oriented Programming
* Apply professional OOP principles
* Understand Inheritance, Polymorphism, Composition, and Interfaces
* Work with structured data such as JSON, CSV, XML, and YAML
* Parse network configurations and command output
* Handle errors professionally
* Implement logging and timestamps
* Use advanced Python collections and iteration tools
* Build Iterators and Generators
* Use Decorators and Context Managers
* Apply advanced Type Hints
* Work with Dataclasses and Enums
* Understand asynchronous programming
* Use concurrency for automation tasks
* Build scalable Python applications
* Apply Python concepts to Network Automation

---

# 🗺️ Learning Roadmap

## Part 1 — Object-Oriented Programming

### Lesson 21 — Classes & Objects

Topics:

* Classes
* Objects
* Attributes
* Methods
* `__init__`
* Instance Methods
* Network Device Models

---

### Lesson 22 — Class Methods & Static Methods

Topics:

* Class Attributes
* `@classmethod`
* `@staticmethod`
* Instance Methods vs Class Methods
* Instance Methods vs Static Methods
* Practical Network Engineering Examples

---

### Lesson 23 — Inheritance & Polymorphism

Topics:

* Inheritance
* Parent and Child Classes
* Method Overriding
* `super()`
* Polymorphism
* Network Device Hierarchies

**Status:** ✅ Completed

---

### Lesson 24 — Multiple Inheritance & MRO

Topics:

* Multiple Inheritance
* Method Resolution Order
* `mro()`
* `__mro__`
* `super()`
* Diamond Problem
* C3 Linearization
* Cooperative Multiple Inheritance

**Status:** ✅ Completed

---

### Lesson 25 — Composition

Topics:

* Composition
* HAS-A Relationship
* Delegation
* Multiple Components
* Loose Coupling
* Dependency Injection
* `Protocol`
* Composition vs Inheritance

Practical focus:

* Network Connections
* Configuration Management
* Monitoring Components

**Status:** 🔥 Challenge in Progress

---

# Part 2 — Professional OOP Design

## Lesson 26 — Abstract Base Classes & Interfaces

Topics:

* `ABC`
* `abstractmethod`
* Abstract Classes
* Interfaces
* Contracts
* Concrete Classes
* ABC vs Protocol
* Polymorphism with Interfaces

---

## Lesson 27 — Advanced Polymorphism & Design Patterns

Topics:

* Advanced Polymorphism
* Strategy Pattern
* Factory Pattern
* Adapter Pattern
* When to use Design Patterns
* Practical Network Automation Examples

---

## Lesson 28 — Exception Handling

Topics:

* `try`
* `except`
* `else`
* `finally`
* Multiple Exceptions
* Custom Exceptions
* Exception Hierarchy
* Professional Error Handling
* Network Automation Error Handling

---

# Part 3 — Data Processing

## Lesson 29 — Regular Expressions

Topics:

* Regex Fundamentals
* `match()`
* `search()`
* `findall()`
* `split()`
* `sub()`
* Groups
* IP Address Extraction
* CLI Output Parsing
* Log Parsing

Practical applications:

```text
Router Output
      ↓
    Regex
      ↓
Structured Data
```

---

## Lesson 30 — JSON

Topics:

* JSON Structure
* Objects
* Arrays
* Nested JSON
* `json.loads()`
* `json.dumps()`
* Reading JSON
* Writing JSON
* REST API Data

Practical applications:

* Network APIs
* Device Inventory
* Automation Data

---

## Lesson 31 — CSV

Topics:

* CSV Files
* `csv.reader`
* `csv.writer`
* `DictReader`
* `DictWriter`
* Reading CSV
* Writing CSV
* Device Inventory

Example:

```text
hostname,ip,platform,status
R1,192.168.1.1,Cisco,up
R2,192.168.1.2,Cisco,up
```

---

## Lesson 32 — XML

Topics:

* XML Structure
* Elements
* Attributes
* XML Parsing
* `ElementTree`
* Reading XML
* Writing XML
* Network/API Data

---

## Lesson 33 — YAML

Topics:

* YAML Structure
* YAML Configuration
* Reading YAML
* Writing YAML
* Configuration Files
* Automation Workflows

Example:

```yaml
device:
  hostname: R1
  platform: cisco_ios
  ip: 192.168.1.1
```

---

# Part 4 — Professional Python Tools

## Lesson 34 — Logging

Topics:

* Python Logging
* Log Levels
* `DEBUG`
* `INFO`
* `WARNING`
* `ERROR`
* `CRITICAL`
* Log Files
* Formatters
* Professional Application Logging

Example:

```text
2026-09-02 10:15:23 INFO Connecting to R1
2026-09-02 10:15:25 INFO Configuration backup completed
```

---

## Lesson 35 — Datetime

Topics:

* `date`
* `time`
* `datetime`
* `timedelta`
* Timestamps
* Time Zones
* Duration Calculations
* Automation Scheduling Concepts

---

## Lesson 36 — Collections

Topics:

* `Counter`
* `defaultdict`
* `deque`
* `namedtuple`
* `ChainMap`
* Advanced Data Structures
* Network Engineering Examples

---

## Lesson 37 — Itertools

Topics:

* `count()`
* `cycle()`
* `repeat()`
* `chain()`
* `combinations()`
* `permutations()`
* `product()`
* `groupby()`

Practical applications:

* Device combinations
* Interface processing
* Data grouping
* Automation workflows

---

# Part 5 — Iteration & Functional Programming

## Lesson 38 — Iterators

Topics:

* Iterator Protocol
* `iter()`
* `next()`
* `__iter__`
* `__next__`
* Custom Iterators

---

## Lesson 39 — Generators

Topics:

* `yield`
* Generator Functions
* Generator Expressions
* Lazy Evaluation
* Memory Efficiency
* Processing Large Network Outputs

---

## Lesson 40 — Decorators

Topics:

* Functions as Objects
* Nested Functions
* Closures
* Function Decorators
* Class Decorators
* Logging Decorators
* Validation Decorators

---

## Lesson 41 — Context Managers

Topics:

* `with`
* `__enter__`
* `__exit__`
* `contextlib`
* Resource Management
* File Management
* Connection Management

---

# Part 6 — Professional Type System

## Lesson 42 — Advanced Type Hints

Topics:

* `Optional`
* `Union`
* `Literal`
* `TypeAlias`
* `TypedDict`
* `Generic`
* `TypeVar`
* Advanced `Protocol`

Goal:

> Make Python applications easier to understand, maintain, validate, and scale.

---

## Lesson 43 — Dataclasses

Topics:

* `@dataclass`
* Default Values
* `field()`
* `frozen=True`
* Immutable Data
* Data Models
* Network Device Models

Example:

```text
NetworkDevice
├── hostname
├── ip_address
├── platform
└── status
```

---

## Lesson 44 — Enums

Topics:

* `Enum`
* `IntEnum`
* Device States
* Protocol Types
* Status Management
* Network Automation Examples

Example:

```text
DeviceStatus
├── UP
├── DOWN
├── UNKNOWN
└── MAINTENANCE
```

---

# Part 7 — Advanced Python Execution

## Lesson 45 — Resource Management

Topics:

* Resource Lifecycle
* Files
* Connections
* Cleanup
* Safe Resource Handling
* Robust Automation Design

---

## Lesson 46 — Async Programming

Topics:

* `async`
* `await`
* Coroutines
* Event Loop
* `asyncio`
* Asynchronous Network Operations

---

## Lesson 47 — Concurrency

Topics:

* Threads
* Processes
* Async Tasks
* Concurrency vs Parallelism
* Choosing the Right Approach
* Network Automation Scenarios

---

## Lesson 48 — Parallel Network Operations

This lesson combines multiple concepts learned throughout the stage.

Example:

```text
                 Network Automation
                         │
             ┌───────────┴───────────┐
             │                       │
          Asyncio                Concurrency
             │                       │
             └───────────┬───────────┘
                         │
                    SSH Sessions
                         │
        ┌────────┬────────┬────────┬────────┐
        R1       R2       R3       R4      ... R20
```

Goal:

Execute network operations across multiple devices efficiently instead of processing every device sequentially.

---

# 🏆 Part 8 — Intermediate Capstone Project

## Lesson 49 — Network Device Management System

The final project will combine the major concepts learned throughout the Intermediate stage.

### Architecture

```text
                    Network Device Management System
                                  │
             ┌────────────────────┼────────────────────┐
             │                    │                    │
        Device Models        Connections         Configuration
             │                    │                    │
        Dataclasses          SSH / Telnet         JSON / YAML
             │                    │                    │
             └────────────────────┼────────────────────┘
                                  │
                             Monitoring
                                  │
                              Logging
                                  │
                         Error Handling
                                  │
                        Async / Concurrency
                                  │
                           Reports / CSV
```

The project will simulate a professional Network Automation application capable of managing multiple network devices.

---

# 📋 Complete Lesson Sequence

```text
21  Classes & Objects
 ↓
22  Class Methods & Static Methods
 ↓
23  Inheritance & Polymorphism
 ↓
24  Multiple Inheritance & MRO
 ↓
25  Composition
 ↓
26  Abstract Base Classes & Interfaces
 ↓
27  Advanced Polymorphism & Design Patterns
 ↓
28  Exception Handling
 ↓
29  Regular Expressions
 ↓
30  JSON
 ↓
31  CSV
 ↓
32  XML
 ↓
33  YAML
 ↓
34  Logging
 ↓
35  Datetime
 ↓
36  Collections
 ↓
37  Itertools
 ↓
38  Iterators
 ↓
39  Generators
 ↓
40  Decorators
 ↓
41  Context Managers
 ↓
42  Advanced Type Hints
 ↓
43  Dataclasses
 ↓
44  Enums
 ↓
45  Resource Management
 ↓
46  Async Programming
 ↓
47  Concurrency
 ↓
48  Parallel Network Operations
 ↓
🏆 49  Intermediate Capstone Project
```

---

# 🎓 Skills Developed

After completing this stage, you should be comfortable with:

### Python

* Intermediate OOP
* Advanced OOP concepts
* Exception Handling
* Type Hints
* Data Processing
* Iteration
* Functional Programming
* Async Programming
* Concurrency

### Data

* JSON
* CSV
* XML
* YAML
* Regex
* Collections
* Itertools

### Software Engineering

* Composition
* Dependency Injection
* Interfaces
* Abstract Classes
* Design Patterns
* Loose Coupling
* Resource Management
* Logging
* Maintainable Code

### Network Engineering

* Device Modeling
* Network Configuration
* Device Inventory
* CLI Parsing
* Network APIs
* SSH/Telnet Concepts
* Multi-device Operations
* Automation Workflows

---

# 🚀 Connection to the Next Stages

The purpose of Python Intermediate is not only to learn Python syntax.

It prepares the foundation for the next stages:

```text
Python Intermediate
        │
        ↓
Professional Python
        │
        ↓
Network Automation
        │
        ↓
Cybersecurity Automation
        │
        ↓
AI + Network Automation
        │
        ↓
AI Agents
        │
        ↓
Capstone Projects
```

---

# 🧭 Learning Philosophy

The roadmap follows a practical learning cycle:

```text
Learn
  ↓
Apply
  ↓
Document
  ↓
Publish
  ↓
Prove Your Skills
```

Every major topic should be reinforced through:

* Practical examples
* Network Engineering scenarios
* Coding exercises
* Challenges
* Mini projects
* Real-world applications

---

# 📈 Progress

| Lesson | Topic                        | Status       |
| ------ | ---------------------------- | ------------ |
| 21     | Classes & Objects            | ✅ Completed  |
| 22     | Class & Static Methods       | ✅ Completed  |
| 23     | Inheritance & Polymorphism   | ✅ Completed  |
| 24     | Multiple Inheritance & MRO   | ✅ Completed  |
| 25     | Composition                  | 🔥 Challenge |
| 26     | ABC & Interfaces             | ⏳ Upcoming   |
| 27     | Design Patterns              | ⏳ Upcoming   |
| 28     | Exception Handling           | ⏳ Upcoming   |
| 29–49  | Advanced Intermediate Topics | ⏳ Upcoming   |

---

## 🎯 Final Goal

By the end of **Python Intermediate**, the goal is to move from:

> **"I can write Python code."**

to:

> **"I can design and build professional Python applications for Network Engineering, Automation, Cybersecurity, and AI."**

---

**Author:** Mohammed AL-Dubai
**Focus:** Python • Networking • Cybersecurity • AI
**Roadmap:** Python Professional Development
