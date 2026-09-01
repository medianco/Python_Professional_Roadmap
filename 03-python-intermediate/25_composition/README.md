# Lesson 25: Composition

## Overview

This lesson introduces **Composition**, one of the most important object-oriented design concepts in Python.

Composition allows a class to build complex functionality by combining multiple independent objects instead of relying heavily on inheritance.

The main idea is:

> **HAS-A relationship**

For example:

```text
NetworkDevice HAS-A SSHConnection
NetworkDevice HAS-A ConfigurationManager
NetworkDevice HAS-A MonitoringManager
```

This lesson uses **Network Engineering and Network Automation** examples to demonstrate how Composition can create flexible, maintainable, and loosely coupled Python applications.

---

## Learning Objectives

By completing this lesson, you will be able to:

* Understand the concept of Composition.
* Understand the **HAS-A relationship**.
* Distinguish Composition from Inheritance.
* Create objects inside other objects.
* Implement Delegation.
* Build classes using multiple components.
* Understand Loose Coupling.
* Apply basic Dependency Injection.
* Use `Protocol` to define flexible component interfaces.
* Apply Composition to Network Automation scenarios.
* Understand when Composition is preferable to Inheritance.

---

## 1. Composition

Composition means creating a class that contains and uses instances of other classes.

### Example

```python
class NetworkDevice:

    def __init__(self, hostname: str) -> None:
        self.hostname = hostname
        self.ssh = SSHConnection()
```

The relationship is:

```text
NetworkDevice
      |
      └── SSHConnection
```

This means:

```text
NetworkDevice HAS-A SSHConnection
```

It does **not** mean:

```text
NetworkDevice IS-A SSHConnection
```

---

## 2. HAS-A vs IS-A

### Inheritance

Inheritance represents an **IS-A** relationship.

```python
class CiscoRouter(NetworkDevice):
    pass
```

Meaning:

```text
CiscoRouter IS-A NetworkDevice
```

### Composition

Composition represents a **HAS-A** relationship.

```python
class NetworkDevice:

    def __init__(self, ssh):
        self.ssh = ssh
```

Meaning:

```text
NetworkDevice HAS-A SSHConnection
```

### Rule of Thumb

```text
IS-A  → Inheritance
HAS-A → Composition
```

---

## 3. Delegation

Delegation means allowing another object to perform a specific responsibility.

Example:

```python
class NetworkDevice:

    def connect(self) -> str:
        return self.ssh.connect()
```

The `NetworkDevice` does not implement the SSH connection itself.

Instead, it delegates the responsibility to:

```python
self.ssh.connect()
```

### Flow

```text
NetworkDevice
      |
      | delegates
      v
SSHConnection
      |
      v
connect()
```

---

## 4. Composition with Multiple Components

A network device can contain several independent components:

```text
                 NetworkDevice
                /      |       \
               /       |        \
              v        v         v
            SSH      Config    Monitoring
```

Example:

```python
class NetworkDevice:

    def __init__(
        self,
        hostname: str,
        ssh: SSHConnection,
        config: ConfigurationManager,
        monitoring: MonitoringManager,
    ) -> None:

        self.hostname = hostname
        self.ssh = ssh
        self.config = config
        self.monitoring = monitoring
```

Each component has its own responsibility.

### Components

```text
SSHConnection
    → Handles connectivity

ConfigurationManager
    → Handles configuration operations

MonitoringManager
    → Handles monitoring operations
```

---

## 5. Loose Coupling

A good software design should minimize unnecessary dependencies between classes.

Instead of creating dependencies directly inside `NetworkDevice`:

```python
self.ssh = SSHConnection()
self.config = ConfigurationManager()
self.monitoring = MonitoringManager()
```

we can provide them from outside:

```python
device = NetworkDevice(
    "R1",
    ssh,
    config,
    monitoring,
)
```

This makes the design more flexible.

### Benefits

* Easier testing
* Easier replacement of components
* Reduced coupling
* Better maintainability
* Greater flexibility
* Easier extension

---

## 6. Dependency Injection

Passing dependencies into a class from outside is commonly known as **Dependency Injection**.

Example:

```python
ssh = SSHConnection()
config = ConfigurationManager()
monitoring = MonitoringManager()

device = NetworkDevice(
    "R1",
    ssh,
    config,
    monitoring,
)
```

The `NetworkDevice` receives its dependencies instead of creating them internally.

### Concept

```text
          Dependencies
        /      |       \
       v       v        v
     SSH     Config   Monitoring
        \      |       /
         \     |      /
          v    v     v
         NetworkDevice
```

---

## 7. Flexible Composition with Protocol

Python's `Protocol` can be used to describe the interface expected from a component.

Example:

```python
from typing import Protocol


class Connection(Protocol):

    def connect(self) -> str:
        ...
```

Now different connection implementations can provide the same behavior.

### SSH

```python
class SSHConnection:

    def connect(self) -> str:
        return "SSH connection established"
```

### Telnet

```python
class TelnetConnection:

    def connect(self) -> str:
        return "Telnet connection established"
```

Both provide:

```python
connect()
```

Therefore, they can be used as different implementations of the same expected interface.

---

## 8. Network Automation Example

A practical architecture can look like this:

```text
                         NetworkDevice
                              |
             +----------------+----------------+
             |                |                |
             v                v                v
       Connection       Configuration      Monitoring
             |
       +-----+------+
       |            |
       v            v
      SSH         Telnet
```

This architecture allows the connection mechanism to change without redesigning the entire `NetworkDevice` class.

---

## 9. Composition vs Inheritance

| Feature               | Inheritance                      | Composition                         |
| --------------------- | -------------------------------- | ----------------------------------- |
| Relationship          | IS-A                             | HAS-A                               |
| Main purpose          | Extend/ specialize behavior      | Combine functionality               |
| Coupling              | Usually tighter                  | Usually looser                      |
| Flexibility           | Lower                            | Higher                              |
| Replacing behavior    | More difficult                   | Easier                              |
| Multiple capabilities | Can become complex               | Easy to combine                     |
| Example               | `CiscoRouter IS-A NetworkDevice` | `NetworkDevice HAS-A SSHConnection` |

---

## 10. Professional Design Example

### Inheritance

```python
class CiscoRouter(NetworkDevice):
    """Represent a Cisco router."""

    def show_platform(self) -> str:
        return "Cisco IOS"
```

Relationship:

```text
CiscoRouter
     |
     └── IS-A → NetworkDevice
```

### Composition

```python
class NetworkDevice:

    def __init__(self, ssh, config, monitoring):
        self.ssh = ssh
        self.config = config
        self.monitoring = monitoring
```

Relationships:

```text
NetworkDevice
     |
     ├── HAS-A → SSHConnection
     ├── HAS-A → ConfigurationManager
     └── HAS-A → MonitoringManager
```

These two concepts can also work together.

A professional application may use:

```text
NetworkDevice
      ↑
      |
CiscoRouter
      |
      +── SSHConnection
      +── ConfigurationManager
      +── MonitoringManager
```

---

## Key Concepts

### Composition

```text
Build complex objects from smaller objects.
```

### HAS-A

```text
NetworkDevice HAS-A SSHConnection
```

### Delegation

```text
Let another object perform a responsibility.
```

### Loose Coupling

```text
Reduce unnecessary dependencies between classes.
```

### Dependency Injection

```text
Provide dependencies from outside the class.
```

### Protocol

```text
Define expected behavior without requiring inheritance.
```

---

## Practical Example

The lesson uses a Network Automation scenario:

```text
NetworkDevice
      |
      +── SSHConnection
      |
      +── ConfigurationManager
      |
      +── MonitoringManager
```

The device exposes simple operations:

```python
device.connect()
device.backup_config()
device.check_status()
```

while delegating the actual work to specialized components.

---

## Lesson Structure

```text
25_composition/
│
├── README.md
│
└── 01_composition.py
```

---

## Skills Practiced

* Object-Oriented Programming
* Composition
* HAS-A relationships
* Delegation
* Dependency Injection
* Loose Coupling
* Protocols
* Network Automation Design
* Object collaboration
* Clean code structure

---

## Key Takeaways

1. **Composition represents HAS-A relationships.**
2. **Inheritance represents IS-A relationships.**
3. Composition allows functionality to be divided into independent components.
4. Delegation allows objects to pass responsibilities to specialized components.
5. Dependency Injection improves flexibility and testability.
6. Composition can reduce tight coupling.
7. `Protocol` can be used to define flexible interfaces.
8. Composition and Inheritance are not competitors; they can be used together when appropriate.

---

## Progress

**Lesson 25 — Composition**

Status: 🚧 In Progress

Completed topics:

* [x] Composition
* [x] HAS-A Relationship
* [x] Delegation
* [x] Multiple Components
* [x] Loose Coupling
* [x] Dependency Injection
* [x] Composition vs Inheritance
* [x] Flexible Composition with `Protocol`

Next:

* [ ] Final code review
* [ ] Refactoring
* [ ] Practical challenge
* [ ] Lesson completion

---

## Author

**Mohammed AL-Dubai**

Python Professional Roadmap
Network Engineering • Cybersecurity • Automation • AI
