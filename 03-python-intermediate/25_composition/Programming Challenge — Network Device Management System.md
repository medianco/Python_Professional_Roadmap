# 🧩 Programming Challenge — Network Device Management System

## Objective

Design and implement a Python-based **Network Device Management System** that can manage different types of network devices and connection methods.

The system should demonstrate a clean, flexible, and maintainable software design.

---

## Requirements

### 1. Connection Management

The system must support at least two connection methods:

* SSH
* Telnet

Each connection method must provide operations for:

* Establishing a connection
* Closing a connection

The `NetworkDevice` class should be able to work with either connection method without being tightly coupled to a specific implementation.

---

### 2. Configuration Management

Create a component responsible for managing device configurations.

It must support:

* Configuration backup
* Configuration restoration

---

### 3. Monitoring

Create a component responsible for monitoring a network device.

It must provide a method to check the current device status.

For this challenge, the expected status is:

```text
Device status: UP
```

---

### 4. Network Device

Create a `NetworkDevice` class with the following information and capabilities:

* Hostname
* Network connection
* Configuration management
* Monitoring

The class must provide methods to:

* Connect to the device
* Disconnect from the device
* Back up the configuration
* Restore the configuration
* Check device status

The `NetworkDevice` class must not be responsible for creating its own supporting components.

---

### 5. Device Types

Create a specialized `CiscoRouter` class based on `NetworkDevice`.

The router must provide an additional method that displays its platform.

Expected result:

```text
Platform: Cisco IOS
```

---

## 6. Testing Requirements

Create and test the following devices:

### Device R1

* Hostname: `R1`
* Connection: SSH

### Device R2

* Hostname: `R2`
* Connection: Telnet

### Device R3

* Hostname: `R3`
* Device type: Cisco Router
* Connection: SSH

Each device should be tested for its supported operations.

---

## Expected Behavior

The program should produce output similar to:

```text
R1
SSH connection established
Device status: UP
Configuration backup completed
Configuration restore completed
SSH connection closed

==============================

R2
Telnet connection established
Device status: UP
Configuration backup completed
Configuration restore completed
Telnet connection closed

==============================

R3
Platform: Cisco IOS
SSH connection established
Device status: UP
Configuration backup completed
Configuration restore completed
SSH connection closed
```

---

## Design Requirements

The implementation should follow good object-oriented design principles.

The system should:

* Avoid unnecessary coupling between components
* Allow different connection implementations to be used interchangeably
* Separate connection, configuration, monitoring, and device responsibilities
* Support future extension with additional connection types
* Use appropriate Python type hints
* Include clear and professional documentation

---

## Challenge Constraints

Do not modify the expected behavior of the system.

The implementation should be written using standard Python features and should not require external libraries.

---

## Skills Evaluated

This challenge evaluates your ability to apply:

* Object-Oriented Programming
* Composition
* HAS-A Relationships
* Dependency Injection
* Delegation
* Interfaces / Protocols
* Loose Coupling
* Inheritance
* Type Hints
* Clean Code

---

## Challenge Status

**Status:** ✅ Completed

**Stage:** Python Intermediate

**Lesson:** 25 — Composition

**Author:** Mohammed AL-Dubai
