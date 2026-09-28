# 21 - Dataclasses

## 📌 Overview

Python `dataclasses` provide a convenient way to create classes that are mainly used to store data.

They reduce repetitive code such as:

- `__init__()`
- `__repr__()`
- `__eq__()`

and make data-oriented classes cleaner and easier to maintain.

In network automation, dataclasses are especially useful for representing structured information such as:

- Network devices
- IP addresses
- Interfaces
- VLANs
- Routing information
- Device credentials
- Configuration parameters

---

## 🎯 Learning Objectives

By the end of this lesson, you should be able to:

1. Understand what a dataclass is.
2. Import and use the `@dataclass` decorator.
3. Define fields inside a dataclass.
4. Create dataclass objects.
5. Understand automatically generated `__init__()` and `__repr__()`.
6. Define default values.
7. Use type hints with dataclasses.
8. Use `field()` for advanced field configuration.
9. Understand mutable default values.
10. Compare regular classes with dataclasses.
11. Use dataclasses to model network devices.
12. Apply dataclasses in practical network automation scenarios.

---

## 🧠 What Is a Dataclass?

A dataclass is a Python class designed primarily to store data.

Instead of manually writing an `__init__()` method:

```python
class NetworkDevice:

    def __init__(self, hostname, ip_address, vendor):
        self.hostname = hostname
        self.ip_address = ip_address
        self.vendor = vendor
````

we can use:

```python
from dataclasses import dataclass


@dataclass
class NetworkDevice:
    hostname: str
    ip_address: str
    vendor: str
```

Python automatically generates the constructor and other useful methods.

---

## 🔹 Basic Syntax

```python
from dataclasses import dataclass


@dataclass
class Device:
    hostname: str
    ip_address: str
    vendor: str
```

Creating an object:

```python
device = Device(
    hostname="R1",
    ip_address="192.168.1.1",
    vendor="Cisco"
)
```

Accessing attributes:

```python
print(device.hostname)
print(device.ip_address)
print(device.vendor)
```

---

## 🔹 Type Hints

Dataclasses work naturally with Python type hints.

Example:

```python
@dataclass
class NetworkDevice:
    hostname: str
    ip_address: str
    management_port: int
    enabled: bool
```

Type hints improve:

* Readability
* IDE support
* Code documentation
* Static analysis
* Maintainability

> Note: Type hints do not automatically validate values at runtime.

---

## 🔹 Default Values

Dataclass fields can have default values.

```python
@dataclass
class NetworkDevice:
    hostname: str
    ip_address: str
    vendor: str = "Cisco"
    enabled: bool = True
```

Example:

```python
device = NetworkDevice(
    hostname="R1",
    ip_address="192.168.1.1"
)
```

The default values will be used automatically.

---

## 🔹 Field Order

Fields without default values must appear before fields with default values.

Correct:

```python
@dataclass
class Device:
    hostname: str
    ip_address: str
    vendor: str = "Cisco"
```

Incorrect:

```python
@dataclass
class Device:
    vendor: str = "Cisco"
    hostname: str
```

This results in an error because a non-default field follows a default field.

---

## 🔹 `field()`

The `field()` function provides additional control over dataclass fields.

```python
from dataclasses import dataclass, field


@dataclass
class NetworkDevice:
    hostname: str
    ip_address: str
    interfaces: list = field(default_factory=list)
```

`default_factory` is useful when a new mutable object should be created for every instance.

---

## ⚠️ Mutable Default Values

Avoid using mutable objects directly as defaults.

For example, this pattern should be avoided:

```python
interfaces: list = []
```

Instead, use:

```python
interfaces: list = field(default_factory=list)
```

This ensures that each object receives its own independent list.

---

## 🔹 Automatically Generated Methods

A dataclass automatically provides useful methods.

For example:

```python
@dataclass
class Device:
    hostname: str
    ip_address: str
```

Python automatically generates behavior similar to:

```python
device = Device("R1", "192.168.1.1")

print(device)
```

Output:

```text
Device(hostname='R1', ip_address='192.168.1.1')
```

Dataclasses also provide equality comparison:

```python
device1 = Device("R1", "192.168.1.1")
device2 = Device("R1", "192.168.1.1")

print(device1 == device2)
```

Output:

```text
True
```

---

## 🔹 Dataclass vs Regular Class

### Regular Class

```python
class NetworkDevice:

    def __init__(self, hostname, ip_address, vendor):
        self.hostname = hostname
        self.ip_address = ip_address
        self.vendor = vendor
```

### Dataclass

```python
@dataclass
class NetworkDevice:
    hostname: str
    ip_address: str
    vendor: str
```

### Main Advantage

Dataclasses reduce boilerplate code when a class is primarily responsible for storing data.

---

## 🌐 Network Engineering Example

Dataclasses are very useful when modeling network devices.

Example:

```python
@dataclass
class NetworkDevice:
    hostname: str
    ip_address: str
    vendor: str
    device_type: str
    enabled: bool = True
```

Example objects:

```python
router = NetworkDevice(
    hostname="R1",
    ip_address="192.168.1.1",
    vendor="Cisco",
    device_type="Router"
)

switch = NetworkDevice(
    hostname="SW1",
    ip_address="192.168.1.10",
    vendor="Cisco",
    device_type="Switch"
)
```

This provides a clean structure for representing network inventory data.

---

## 🧩 Topics Covered in This Lesson

The lesson examples will progressively cover:

1. Dataclass basics
2. Dataclass fields
3. Type hints
4. Default values
5. `field()`
6. `default_factory`
7. Mutable fields
8. Generated methods
9. Dataclass comparison
10. Nested dataclasses
11. Network device modeling
12. Practical network automation examples

---

## 📂 Lesson Structure

```text
21_dataclasses/
│
├── README.md
│
├── 01_dataclass_basics.py
├── 02_dataclass_fields.py
├── 03_default_values.py
├── 04_field_function.py
├── 05_default_factory.py
├── 06_dataclass_methods.py
├── 07_comparison.py
├── 08_nested_dataclasses.py
└── 09_network_device_model.py
```

---

## 🧪 Practice Challenge

Create a dataclass called `NetworkDevice`.

It should contain:

* `hostname`
* `ip_address`
* `vendor`
* `device_type`
* `os_version`
* `enabled`

Then:

1. Create at least three network devices.
2. Store them in a list.
3. Display the devices.
4. Compare two devices.
5. Add a default value for `enabled`.
6. Add a list of interfaces using `default_factory`.

### Challenge Extension

Create a second dataclass called `Interface`.

It should contain:

* `name`
* `ip_address`
* `status`

Then associate multiple interfaces with a `NetworkDevice`.

---

## 💡 Network Automation Connection

Dataclasses become increasingly useful as network automation projects become larger.

For example, instead of passing many independent variables:

```python
hostname
ip_address
username
vendor
device_type
```

we can represent the device as a single structured object:

```python
NetworkDevice(...)
```

This concept will become especially useful later when working with:

* Network automation
* APIs
* JSON
* YAML
* Nornir
* Netmiko
* REST APIs
* Network inventory systems
* Configuration management
* AI-assisted network automation

---

## 📚 Key Takeaways

* `@dataclass` simplifies data-oriented classes.
* Dataclasses automatically generate common methods.
* Type hints make the data structure clearer.
* Default values can be defined directly.
* `field()` provides advanced field configuration.
* `default_factory` is important for mutable values.
* Dataclasses are excellent for structured network inventory data.
* They help reduce boilerplate and improve code readability.

---

## 🚀 Next Step

After completing this lesson, continue with:

**22 - Class Methods & Static Methods**

The next lesson will focus on methods that belong to the class itself rather than individual objects.
