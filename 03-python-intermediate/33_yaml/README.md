# Lesson 33 — YAML

## 📌 Overview

YAML is a human-readable data serialization format that is
widely used for configuration files, automation, DevOps,
and Network Automation.

In this lesson, we will learn how to work with YAML using Python
and apply it to practical Network Engineering scenarios.

The goal is not only to learn YAML syntax, but also to understand
how YAML can become a structured data source for automation systems.

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
