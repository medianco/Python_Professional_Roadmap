صحيح 👍 نحن **ما زلنا في مرحلة تجهيز `README.md` للدرس 30**، ولم نبدأ ملفات الدرس بعد.

سنثبت أولًا الـ **README.md** كاملًا، وبعد أن تتأكد أنه مناسب نبدأ `01_json_basics.py`.

### `03-python-intermediate/30_json/README.md`

````markdown
# Lesson 30 — JSON

## 📌 Overview

JSON (JavaScript Object Notation) is one of the most important data formats used in modern software development, APIs, cloud platforms, network automation, and cybersecurity.

For Network Engineers, JSON is especially important because many modern network platforms expose their configuration, inventory, monitoring data, and automation interfaces through REST APIs that use JSON.

Examples:

- Cisco APIs
- Cisco Catalyst Center
- Meraki Dashboard API
- Aruba Central API
- Fortinet APIs
- Cloud APIs
- Network Monitoring Systems
- Automation Platforms

In this lesson, we will learn how to work with JSON professionally using Python.

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand the JSON data format.
- Understand JSON objects and arrays.
- Understand JSON data types.
- Understand the difference between JSON and Python data types.
- Use `json.dumps()`.
- Use `json.loads()`.
- Write JSON data to files.
- Read JSON data from files.
- Work with nested JSON structures.
- Process network device information stored in JSON.
- Use JSON in Network Automation.
- Validate JSON-based network data.
- Build a practical Network Device Inventory application.

---

# 📂 Lesson Structure

```text
30_json/
│
├── README.md
│
├── 01_json_basics.py
├── 02_json_dumps.py
├── 03_json_loads.py
├── 04_json_file_write.py
├── 05_json_file_read.py
├── 06_json_nested_data.py
├── 07_json_network_devices.py
├── 08_json_network_automation.py
├── 09_json_validation.py
│
└── challenge/
    └── network_device_inventory.py
````

---

# 30.1 — JSON Basics

## What is JSON?

JSON stands for:

> JavaScript Object Notation

Despite its name, JSON is not limited to JavaScript.

It is a lightweight format for storing and exchanging structured data.

Example:

```json
{
    "hostname": "R1",
    "ip_address": "192.168.1.1",
    "device_type": "router",
    "enabled": true
}
```

This example represents information about a network device.

---

## JSON Object

A JSON object is enclosed in:

```text
{ }
```

Example:

```json
{
    "hostname": "R1",
    "ip_address": "192.168.1.1"
}
```

A JSON object contains:

```text
key : value
```

Example:

```text
"hostname" : "R1"
```

---

## JSON Array

A JSON array is enclosed in:

```text
[ ]
```

Example:

```json
{
    "hostname": "R1",
    "interfaces": [
        "GigabitEthernet0/0",
        "GigabitEthernet0/1"
    ]
}
```

The `interfaces` value contains an array of interfaces.

---

# JSON Data Types

JSON supports several important data types.

| JSON Type | Example |
| --------- | ------- |
| String    | `"R1"`  |
| Number    | `100`   |
| Boolean   | `true`  |
| Boolean   | `false` |
| Object    | `{ }`   |
| Array     | `[ ]`   |
| Null      | `null`  |

Example:

```json
{
    "hostname": "R1",
    "interfaces": 2,
    "enabled": true,
    "management": null
}
```

---

# JSON vs Python

JSON and Python have very similar data structures.

| JSON    | Python          |
| ------- | --------------- |
| Object  | `dict`          |
| Array   | `list`          |
| String  | `str`           |
| Number  | `int` / `float` |
| `true`  | `True`          |
| `false` | `False`         |
| `null`  | `None`          |

Example JSON:

```json
{
    "hostname": "R1",
    "enabled": true
}
```

Equivalent Python dictionary:

```python
device = {
    "hostname": "R1",
    "enabled": True
}
```

Notice the important difference:

```text
JSON       Python
--------------------
true   →   True
false  →   False
null   →   None
```

---

# 30.2 — json.dumps()

`json.dumps()` converts a Python object into a JSON string.

Concept:

```text
Python
   ↓
json.dumps()
   ↓
JSON String
```

Example:

```python
import json

device = {
    "hostname": "R1",
    "ip_address": "192.168.1.1"
}

json_data = json.dumps(device)

print(json_data)
```

Output:

```text
{"hostname": "R1", "ip_address": "192.168.1.1"}
```

---

## Formatting JSON

We can make JSON easier to read using:

```python
indent=4
```

Example:

```python
json_data = json.dumps(device, indent=4)
```

Output:

```json
{
    "hostname": "R1",
    "ip_address": "192.168.1.1"
}
```

---

## Sorting JSON Keys

We can also use:

```python
sort_keys=True
```

Example:

```python
json.dumps(device, indent=4, sort_keys=True)
```

This sorts the keys alphabetically.

---

# 30.3 — json.loads()

`json.loads()` converts a JSON string into a Python object.

Concept:

```text
JSON String
     ↓
json.loads()
     ↓
Python Object
```

Example:

```python
import json

json_data = '{"hostname": "R1", "ip_address": "192.168.1.1"}'

device = json.loads(json_data)

print(device)
print(type(device))
```

Output:

```text
{'hostname': 'R1', 'ip_address': '192.168.1.1'}
<class 'dict'>
```

Now we can access the values like a normal Python dictionary:

```python
print(device["hostname"])
```

Output:

```text
R1
```

---

# 30.4 — Writing JSON to a File

Python provides:

```python
json.dump()
```

for writing Python data directly to a JSON file.

Concept:

```text
Python Dictionary
       ↓
json.dump()
       ↓
JSON File
```

Example:

```python
import json

device = {
    "hostname": "R1",
    "ip_address": "192.168.1.1",
    "device_type": "router"
}

with open("device.json", "w") as file:
    json.dump(device, file, indent=4)
```

This creates:

```text
device.json
```

with:

```json
{
    "hostname": "R1",
    "ip_address": "192.168.1.1",
    "device_type": "router"
}
```

---

# 30.5 — Reading JSON from a File

Python provides:

```python
json.load()
```

for reading JSON data from a file.

Concept:

```text
JSON File
    ↓
json.load()
    ↓
Python Object
```

Example:

```python
import json

with open("device.json", "r") as file:
    device = json.load(file)

print(device)
```

Now `device` is a Python dictionary.

We can access its values:

```python
print(device["hostname"])
print(device["ip_address"])
```

---

# 30.6 — Nested JSON

Real-world JSON data is often nested.

For example, a network device may contain:

* Device information
* Interfaces
* IP addresses
* VLANs
* Routing protocols
* Monitoring information

Example:

```json
{
    "hostname": "R1",
    "management": {
        "ip_address": "192.168.1.1",
        "protocol": "SSH"
    },
    "interfaces": [
        {
            "name": "GigabitEthernet0/0",
            "ip_address": "10.0.0.1",
            "status": "up"
        },
        {
            "name": "GigabitEthernet0/1",
            "ip_address": "10.0.1.1",
            "status": "down"
        }
    ]
}
```

This structure contains:

```text
Object
│
├── hostname
│
├── management
│   ├── ip_address
│   └── protocol
│
└── interfaces
    ├── Interface 1
    └── Interface 2
```

We will learn how to navigate and process nested JSON using Python.

---

# 30.7 — JSON and Network Devices

JSON is extremely useful for representing network device information.

Example:

```json
{
    "hostname": "R1",
    "management_ip": "192.168.1.1",
    "vendor": "Cisco",
    "device_type": "router",
    "location": "Data Center",
    "enabled": true
}
```

A larger inventory may contain multiple devices:

```json
{
    "devices": [
        {
            "hostname": "R1",
            "management_ip": "192.168.1.1",
            "device_type": "router"
        },
        {
            "hostname": "SW1",
            "management_ip": "192.168.1.10",
            "device_type": "switch"
        }
    ]
}
```

Python can process this information automatically.

---

# 30.8 — JSON in Network Automation

JSON is one of the most important data formats in Network Automation.

A typical automation workflow can look like:

```text
              JSON
                │
                ▼
       Network Inventory
                │
                ▼
             Python
                │
        ┌───────┴───────┐
        ▼               ▼
    Validate         Process
        │               │
        └───────┬───────┘
                ▼
          Automation
                │
                ▼
        Network Devices
```

For example, an inventory file could contain:

```json
{
    "devices": [
        {
            "hostname": "R1",
            "ip": "192.168.1.1",
            "vendor": "Cisco"
        },
        {
            "hostname": "R2",
            "ip": "192.168.1.2",
            "vendor": "Cisco"
        }
    ]
}
```

Python can read this inventory and use it to:

* Connect to devices.
* Validate device information.
* Collect configuration.
* Collect operational data.
* Execute commands.
* Generate reports.
* Automate configuration changes.

---

# 30.9 — JSON Validation

When working with JSON in Network Automation, validation is important.

We should verify that required information exists and has the expected format.

Example:

```python
device = {
    "hostname": "R1",
    "ip_address": "192.168.1.1"
}
```

We may need to validate:

```text
✓ hostname exists
✓ ip_address exists
✓ IP address has a valid format
✓ device_type exists
✓ required fields are not empty
```

JSON validation can prevent incorrect data from entering an automation workflow.

Important:

> JSON validation checks the structure and expected data.

For IP address validation, Python's `ipaddress` module is more appropriate than relying only on regular expressions.

Example:

```python
import ipaddress

ip = ipaddress.ip_address("192.168.1.1")

print(ip)
```

---

# 🧪 Practical Challenge

## Network Device Inventory

Create a Python application that manages a network device inventory using JSON.

### Requirements

The application should store multiple network devices.

Each device should contain information such as:

```text
hostname
management_ip
device_type
vendor
location
enabled
```

Example:

```json
{
    "devices": [
        {
            "hostname": "R1",
            "management_ip": "192.168.1.1",
            "device_type": "router",
            "vendor": "Cisco",
            "location": "Data Center",
            "enabled": true
        }
    ]
}
```

The application should be able to:

1. Create device data.
2. Save the inventory to a JSON file.
3. Load the inventory from the JSON file.
4. Display all devices.
5. Search for a device by hostname.
6. Validate required fields.
7. Display the number of devices.
8. Handle invalid or missing JSON data.

### Challenge Goal

Build the application using the concepts learned in:

```text
Python Dictionaries
        ↓
JSON
        ↓
File Handling
        ↓
Validation
        ↓
Network Device Inventory
```

Do not use external libraries.

Use Python's built-in:

```python
json
```

and:

```python
ipaddress
```

modules where appropriate.

---

# 🧠 Important Concepts

## Python → JSON

Use:

```python
json.dumps()
```

for converting a Python object into a JSON string.

Use:

```python
json.dump()
```

for writing Python data directly to a JSON file.

---

## JSON → Python

Use:

```python
json.loads()
```

for converting a JSON string into a Python object.

Use:

```python
json.load()
```

for reading JSON data from a file.

---

# 📊 JSON Functions Summary

| Function       | Purpose              |
| -------------- | -------------------- |
| `json.dumps()` | Python → JSON string |
| `json.loads()` | JSON string → Python |
| `json.dump()`  | Python → JSON file   |
| `json.load()`  | JSON file → Python   |

---

# 🌐 Network Engineering Perspective

JSON is not simply another Python topic.

It is a fundamental data format for modern Network Engineering.

It appears in:

```text
Network Automation
       │
       ├── REST APIs
       ├── Cisco APIs
       ├── Cloud APIs
       ├── Network Inventory
       ├── Monitoring
       ├── Configuration Management
       └── Automation Platforms
```

Understanding JSON will prepare us for:

```text
Python
   ↓
JSON
   ↓
REST APIs
   ↓
Network Automation
   ↓
AI + Network Automation
```

---

# 🔗 Relationship With Previous Lessons

In Lesson 29, we learned:

```text
Regular Expressions
        ↓
Extract / Validate Network Data
```

In Lesson 30:

```text
JSON
        ↓
Structure / Store / Exchange Network Data
```

This combination is very useful in Network Automation.

For example:

```text
Network Device Output
        ↓
Regex
        ↓
Extract Data
        ↓
Python Dictionary
        ↓
JSON
        ↓
Store / Exchange / API
```

---

# 🚀 Next Lesson

After completing Lesson 30, we will move to:

## Lesson 31 — CSV

We will learn how to:

* Read CSV files.
* Write CSV files.
* Process rows and columns.
* Work with network device inventories.
* Combine CSV with Python.
* Build practical Network Engineering automation tasks.

---

# 🎯 Learning Philosophy

The goal of this lesson is not simply to memorize:

```python
json.dumps()
json.loads()
json.dump()
json.load()
```

The goal is to understand how JSON fits into a real Network Automation workflow:

```text
Learn
  ↓
Understand
  ↓
Practice
  ↓
Automate
  ↓
Document
  ↓
Publish
  ↓
Prove Your Skills
```

**Next Generation Network Engineer**

**Mohammed AL-Dubai**

```

```
