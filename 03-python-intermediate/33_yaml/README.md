# Lesson 33 — YAML

# 📌 Introduction to YAML

## What is YAML?

**YAML** is a human-readable data serialization format used to represent
structured data in a simple and easy-to-read syntax.

The name YAML originally stood for:

> YAML Ain't Markup Language

Unlike traditional markup languages, YAML focuses on representing
data rather than formatting documents.

YAML is widely used in:

- Configuration files
- Network Automation
- DevOps
- Infrastructure as Code
- CI/CD pipelines
- Cloud platforms
- Kubernetes
- Ansible
- Application configuration
- Automation workflows

---

## Why is YAML Important?

YAML is especially useful when configuration or inventory data needs
to be maintained separately from application logic.

For example, instead of hard-coding network devices inside Python:

```python
devices = [
    {
        "hostname": "R1",
        "management_ip": "192.168.1.1",
        "vendor": "Cisco"
    }
]
````

we can store the same information in a YAML file:

```yaml
devices:

  - hostname: R1
    management_ip: 192.168.1.1
    vendor: Cisco
```

Python can then read the YAML file and process the data.

This creates a cleaner separation between:

```text
Configuration / Data
        ↓
      YAML
        ↓
      Python
        ↓
  Application Logic
        ↓
   Automation
```

---

## YAML in Network Automation

YAML is particularly useful in Network Automation because network
inventory information can be stored in a human-readable format.

For example:

```yaml
devices:

  - hostname: R1
    management_ip: 192.168.1.1
    device_type: router
    vendor: Cisco
    location: Data Center
    status: active

  - hostname: R2
    management_ip: 192.168.1.2
    device_type: router
    vendor: Cisco
    location: Branch 1
    status: active

  - hostname: SW1
    management_ip: 192.168.1.10
    device_type: switch
    vendor: Cisco
    location: Data Center
    status: active
```

Python can read this inventory and use it to determine:

* Which devices should be automated.
* Which vendor a device belongs to.
* What type of device it is.
* Where the device is located.
* Which management IP should be used.
* Whether the device is active.

This allows us to build a workflow such as:

```text
YAML Inventory
      ↓
     Python
      ↓
   Parse Data
      ↓
    Validate
      ↓
    Filter
      ↓
Automation Targets
      ↓
Netmiko / Nornir / APIs
      ↓
Network Devices
```

---

## YAML is Data, Not Automation

An important concept is that YAML itself does not perform
network automation.

YAML stores structured data.

Python or another automation tool processes that data.

```text
YAML
  │
  │  Stores Data
  ▼
Python
  │
  │  Processes Data
  ▼
Automation Tool
  │
  │  Performs Actions
  ▼
Network Devices
```

For example:

```text
devices.yaml
      ↓
Python
      ↓
Select Cisco Routers
      ↓
Netmiko
      ↓
Connect to R1 / R2
```

---

## YAML and Python

One of the most important concepts in this lesson is the relationship
between YAML structures and Python data structures.

### YAML Mapping → Python Dictionary

YAML:

```yaml
hostname: R1
vendor: Cisco
```

Python:

```python
{
    "hostname": "R1",
    "vendor": "Cisco"
}
```

---

### YAML Sequence → Python List

YAML:

```yaml
vendors:
  - Cisco
  - Juniper
  - Arista
```

Python:

```python
[
    "Cisco",
    "Juniper",
    "Arista"
]
```

---

### Nested YAML → Nested Python Objects

YAML:

```yaml
device:
  hostname: R1
  management:
    ip: 192.168.1.1
    protocol: ssh
```

Python:

```python
{
    "device": {
        "hostname": "R1",
        "management": {
            "ip": "192.168.1.1",
            "protocol": "ssh"
        }
    }
}
```

This relationship will become especially important when we start using
`PyYAML` to load YAML files into Python.

---

## YAML vs JSON

YAML and JSON can represent similar structured data, but their syntax
and typical usage are different.

JSON:

```json
{
    "hostname": "R1",
    "management_ip": "192.168.1.1",
    "vendor": "Cisco"
}
```

YAML:

```yaml
hostname: R1
management_ip: 192.168.1.1
vendor: Cisco
```

YAML is often easier for humans to read and edit, especially for
configuration files.

JSON is extremely common in APIs and application data exchange.

The goal is not to replace JSON with YAML.

The goal is to understand when each format is appropriate.

---

## YAML vs XML

XML represents hierarchical data using tags:

```xml
<device>
    <hostname>R1</hostname>
    <vendor>Cisco</vendor>
</device>
```

YAML can represent the same basic information more concisely:

```yaml
device:
  hostname: R1
  vendor: Cisco
```

Both formats can represent structured and nested data.

However, their syntax, ecosystems, and common use cases differ.

---

## YAML vs CSV

CSV is primarily designed for tabular data:

```text
hostname,management_ip,vendor
R1,192.168.1.1,Cisco
R2,192.168.1.2,Cisco
```

YAML can represent much more complex hierarchical structures:

```yaml
devices:

  - hostname: R1
    management:
      ip: 192.168.1.1
      protocol: ssh

    interfaces:
      - name: GigabitEthernet0/0
        status: up
```

Therefore, YAML is better suited to representing nested configuration
and hierarchical automation data.

---

## YAML and Human Readability

One of YAML's major strengths is readability.

Compare:

```yaml
device:
  hostname: R1
  vendor: Cisco
  device_type: router
  management_ip: 192.168.1.1
```

with equivalent JSON:

```json
{
    "device": {
        "hostname": "R1",
        "vendor": "Cisco",
        "device_type": "router",
        "management_ip": "192.168.1.1"
    }
}
```

Both represent structured data, but YAML is intentionally designed
to be concise and easy for humans to read and maintain.

---

## YAML and Indentation

YAML uses indentation to represent hierarchy.

For example:

```yaml
device:
  hostname: R1
  management:
    ip: 192.168.1.1
```

The indentation represents:

```text
device
├── hostname
└── management
    └── ip
```

Therefore, indentation is not simply formatting in YAML.

It is part of the data structure.

A consistent indentation style should always be used.

In this course, we will use:

```text
2 spaces
```

for each indentation level.

We will also avoid using tabs for YAML indentation.

---

## YAML Comments

Comments begin with `#`.

Example:

```yaml
# Network device information

hostname: R1
management_ip: 192.168.1.1
vendor: Cisco
```

Comments are ignored when the YAML data is parsed.

They are useful for documenting configuration and explaining
the purpose of different sections.

---

## YAML and Configuration-Driven Automation

One of the most important ideas in this lesson is
**configuration-driven automation**.

Instead of modifying Python code whenever the inventory changes,
we can change the YAML data.

For example:

```text
                YAML
                 │
        ┌────────┴────────┐
        │                 │
     R1 / R2            SW1 / FW1
        │                 │
        └────────┬────────┘
                 ▼
              Python
                 │
                 ▼
           Automation
```

Adding a new device can therefore become a data change rather than
a code change.

This supports cleaner and more maintainable automation architectures.

---

## Security Consideration

YAML files may contain sensitive configuration information such as:

* Management IP addresses
* Device names
* Connection parameters
* Environment variables
* Authentication-related configuration

Therefore:

* Do not store passwords directly in YAML files.
* Do not commit secrets to Git repositories.
* Use environment variables or a secrets-management solution
  when sensitive information is required.
* When loading YAML in Python, prefer safe parsing methods such as:

```python
yaml.safe_load()
```

Avoid unsafe deserialization of untrusted YAML data.

---

## What We Will Build in This Lesson

Throughout Lesson 33, we will gradually build a
YAML-based Network Automation workflow.

```text
YAML Basics
     ↓
Load YAML
     ↓
Write YAML
     ↓
Read YAML Files
     ↓
Write YAML Files
     ↓
Nested Data
     ↓
Network Device Inventory
     ↓
Network Automation
     ↓
Validation
     ↓
Final Challenge
```

By the end of the lesson, YAML will no longer be just a
configuration format.

We will use it as a structured data source for
practical Python Network Automation.

---

## Key Concept

The most important idea to remember is:

```text
YAML
  ↓
Human-readable structured data
  ↓
Python
  ↓
Validation / Filtering / Processing
  ↓
Automation
```

The objective is to move from:

```text
Hard-coded Configuration
```

to:

```text
Configuration-Driven Automation
```

This is an important step toward building scalable and maintainable
Network Automation systems.

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand YAML fundamentals.
- Understand YAML syntax and structure.
- Understand mappings and sequences.
- Understand scalar values.
- Understand YAML indentation.
- Read YAML files using Python.
- Write YAML files using Python.
- Convert YAML data into Python objects.
- Convert Python objects into YAML.
- Work with nested YAML data.
- Build Network Device inventories using YAML.
- Search and filter YAML-based inventories.
- Validate YAML network data.
- Use YAML as an input source for Network Automation.

---

# 🗺️ Lesson Roadmap

## 33.1 YAML Basics

Introduction to YAML.

Topics:

- What is YAML?
- Why YAML is used.
- YAML syntax.
- YAML indentation.
- Key-value pairs.
- Comments.
- Strings.
- Numbers.
- Boolean values.
- Lists.
- Dictionaries.

Example:

```yaml
hostname: R1
management_ip: 192.168.1.1
vendor: Cisco
device_type: router
status: active
````

---

# 33.2 YAML Load

Learn how to load YAML data into Python.

We will use:

```python
yaml.safe_load()
```

Concept:

```text
YAML
 ↓
safe_load()
 ↓
Python Object
```

For example:

```yaml
hostname: R1
```

becomes:

```python
{
    "hostname": "R1"
}
```

---

# 33.3 YAML Dump

Learn how to convert Python data into YAML.

We will use:

```python
yaml.safe_dump()
```

Concept:

```text
Python Object
      ↓
safe_dump()
      ↓
YAML
```

---

# 33.4 Reading YAML Files

Learn how to read YAML files from disk.

Example:

```text
data/
└── devices.yaml
```

Python will read the file and convert the YAML data
into Python dictionaries and lists.

---

# 33.5 Writing YAML Files

Learn how to generate YAML files from Python data.

Example:

```text
Python Dictionary
       ↓
PyYAML
       ↓
devices.yaml
```

Generated files will be stored separately from the Python logic.

---

# 33.6 Nested YAML Data

YAML is particularly useful for representing hierarchical data.

Example:

```yaml
device:
  hostname: R1
  management:
    ip: 192.168.1.1
    protocol: ssh

  interfaces:
    - name: GigabitEthernet0/0
      ip: 10.0.0.1
      status: up

    - name: GigabitEthernet0/1
      ip: 192.168.10.1
      status: up
```

Concept:

```text
Device
 ├── Hostname
 ├── Management
 │    ├── IP
 │    └── Protocol
 │
 └── Interfaces
      ├── Interface 1
      └── Interface 2
```

---

# 33.7 YAML & Network Devices

We will build a realistic Network Device Inventory using YAML.

Example:

```yaml
devices:

  - hostname: R1
    management_ip: 192.168.1.1
    device_type: router
    vendor: Cisco
    location: Data Center
    status: active

  - hostname: R2
    management_ip: 192.168.1.2
    device_type: router
    vendor: Cisco
    location: Branch 1
    status: active

  - hostname: SW1
    management_ip: 192.168.1.10
    device_type: switch
    vendor: Cisco
    location: Data Center
    status: active
```

This will become our YAML-based Network Inventory.

---

# 33.8 YAML & Network Automation

We will use YAML as an input source for
Network Automation.

Workflow:

```text
YAML Inventory
      ↓
Python
      ↓
PyYAML
      ↓
Parse Data
      ↓
Validate Data
      ↓
Filter Devices
      ↓
Automation Targets
      ↓
Netmiko / Nornir / APIs
      ↓
Network Devices
```

Example:

```text
YAML
 │
 ├── R1
 ├── R2
 ├── SW1
 └── FW1
      │
      ▼
Python Automation
      │
      ▼
Select Cisco Routers
      │
      ▼
R1 + R2
```

---

# 33.9 YAML Validation

Before using YAML data for automation,
we need to validate it.

Validation will include:

* Required fields.
* Hostname.
* Management IP.
* Vendor.
* Device type.
* Location.
* Status.
* Valid IP addresses.
* Allowed device types.
* Allowed status values.

Example:

```text
YAML
 ↓
Syntax Validation
 ↓
Data Validation
 ↓
Automation Readiness
```

---

# 🔄 YAML and Python

One of the most important concepts in this lesson
is the relationship between YAML and Python objects.

```text
YAML Mapping
     ↓
Python Dictionary
```

```text
YAML Sequence
     ↓
Python List
```

Example:

```yaml
devices:
  - hostname: R1
  - hostname: R2
```

becomes conceptually:

```python
{
    "devices": [
        {"hostname": "R1"},
        {"hostname": "R2"}
    ]
}
```

---

# 📊 YAML vs JSON vs XML vs CSV

We have now studied several data formats.

| Format | Main Strength                | Typical Use                         |
| ------ | ---------------------------- | ----------------------------------- |
| CSV    | Tabular data                 | Spreadsheets / simple inventories   |
| JSON   | APIs / structured data       | APIs / applications                 |
| XML    | Hierarchical structured data | Enterprise systems / legacy systems |
| YAML   | Human-readable configuration | Automation / DevOps / configuration |

The goal is not to replace one format with another.

The goal is to understand when each format is appropriate.

---

# 🌐 Network Automation Architecture

By the end of this lesson, we will have:

```text
                YAML Inventory
                      │
                      ▼
                   Python
                      │
                 PyYAML
                      │
                      ▼
              Parsed Data
                      │
             ┌────────┴────────┐
             │                 │
        Validation          Filtering
             │                 │
             └────────┬────────┘
                      │
                      ▼
             Automation Targets
                      │
          ┌───────────┼───────────┐
          │           │           │
       Netmiko      Nornir      APIs
          │           │           │
          └───────────┼───────────┘
                      │
                      ▼
               Network Devices
```

---

# 📁 Project Structure

```text
33_yaml/
│
├── README.md
│
├── data/
│   ├── devices.json
│   └── devices.yaml
│
├── output/
│   └── generated_devices.yaml
│
├── 01_yaml_basics.py
├── 02_yaml_load.py
├── 03_yaml_dump.py
├── 04_yaml_file_read.py
├── 05_yaml_file_write.py
├── 06_yaml_nested_data.py
├── 07_yaml_network_devices.py
├── 08_yaml_network_automation.py
├── 09_yaml_validation.py
│
└── challenge/
    └── network_device_inventory.py
```

---

# 📚 File-by-File Learning Plan

## 01_yaml_basics.py

Learn:

* YAML syntax.
* Mappings.
* Sequences.
* Scalars.
* Comments.
* Indentation.

---

## 02_yaml_load.py

Learn:

* `yaml.safe_load()`
* YAML → Python.
* Dictionaries.
* Lists.

---

## 03_yaml_dump.py

Learn:

* `yaml.safe_dump()`
* Python → YAML.
* YAML formatting.

---

## 04_yaml_file_read.py

Learn:

* Opening YAML files.
* Reading YAML from disk.
* Parsing YAML data.

---

## 05_yaml_file_write.py

Learn:

* Creating YAML files.
* Writing structured data.
* Separating data from logic.

---

## 06_yaml_nested_data.py

Learn:

* Nested dictionaries.
* Nested lists.
* Hierarchical network data.
* Accessing deeply nested values.

---

## 07_yaml_network_devices.py

Build a practical:

```text
Network Device Inventory
```

including:

* Routers.
* Switches.
* Firewalls.
* Vendors.
* Management IPs.
* Locations.
* Status.

---

## 08_yaml_network_automation.py

Use YAML as an input source for
Network Automation.

We will:

* Parse the inventory.
* Select devices.
* Filter devices.
* Build automation targets.
* Simulate automation tasks.

No real network connection will be required.

---

## 09_yaml_validation.py

Validate the YAML inventory before
passing it to an automation workflow.

Validation will include:

```text
Required Fields
      ↓
Data Types
      ↓
IP Validation
      ↓
Allowed Values
      ↓
Automation Readiness
```

---

# 🏆 Final Challenge

## Network Device YAML Inventory Manager

Build a small Network Device Inventory Manager
using YAML and Python.

The application should:

### 1. Read YAML Inventory

Load:

```text
data/devices.yaml
```

---

### 2. Display Devices

Display:

```text
Hostname
Management IP
Device Type
Vendor
Location
Status
```

---

### 3. Search Devices

Allow searching by:

```text
Hostname
Vendor
Device Type
Location
Management IP
```

---

### 4. Filter Devices

Examples:

```text
Cisco Devices
Cisco Routers
Data Center Devices
Active Devices
```

---

### 5. Validate Inventory

Validate:

```text
Hostname
Management IP
Vendor
Device Type
Location
Status
```

---

### 6. Automation Targets

Generate a list of devices
that are ready for automation.

Example:

```text
Automation Targets:

R1
R2
SW1
```

---

# 🧠 Key Takeaways

By the end of Lesson 33, remember:

```text
YAML
 ↓
Human-readable structured data
 ↓
Python
 ↓
safe_load()
 ↓
Python Dictionaries / Lists
 ↓
Validation
 ↓
Filtering
 ↓
Automation Targets
 ↓
Network Automation
```

The important concept is:

> YAML is not the automation itself.

YAML provides structured data that Python and
automation tools can consume.

---

# 🔐 Security Note

When working with YAML in real projects,
always be careful when loading untrusted data.

Prefer:

```python
yaml.safe_load()
```

instead of unsafe object deserialization methods.

Never assume that an external configuration file
is trustworthy simply because it is a YAML file.

---

# 🛠️ Practical Environment

Recommended environment:

```text
Python 3.x
PyYAML
VS Code
Linux / Windows
```

Install PyYAML:

```bash
pip install pyyaml
```

Verify installation:

```bash
python -c "import yaml; print(yaml.__version__)"
```

---

# 🌐 Network Engineering Focus

Throughout this lesson, examples will focus on:

* Network Device Inventory.
* Cisco devices.
* Network management IPs.
* Device types.
* Vendors.
* Locations.
* Automation targets.
* Configuration data.
* Network Automation workflows.

The goal is to understand YAML not only as
a data format, but as a practical tool for
professional Network Automation.

---

# 📈 Progress

**Stage:** `03-python-intermediate`

**Lesson:** `33 — YAML`

**Status:** 🟡 In Progress

### Previous Lessons

* ✅ 21 — Dataclasses
* ✅ 22 — Class Methods & Static Methods
* ✅ 23 — Inheritance & Polymorphism
* ✅ 24 — Multiple Inheritance & MRO
* ✅ 25 — Composition
* ✅ 26 — Abstract Base Classes & Interfaces
* ✅ 27 — Advanced Polymorphism & Design Patterns
* ✅ 28 — Exception Handling
* ✅ 29 — Regular Expressions
* ✅ 30 — JSON
* ✅ 31 — CSV
* ✅ 32 — XML

### Current Lesson

* 🟡 33 — YAML

### Next

* ⬜ 34 — Logging

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

The objective of Lesson 33 is to move from
working with structured data formats toward
building practical configuration-driven
Network Automation systems.
