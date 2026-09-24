# Lesson 31 — CSV

CSV (Comma-Separated Values) is a simple and widely used
format for storing and exchanging tabular data.

In Network Engineering and Network Automation, CSV files
are commonly used for:

- Network device inventories
- IP address lists
- VLAN inventories
- Interface information
- Migration data
- Device onboarding
- Reports
- Automation input files

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand the structure of CSV files
- Understand rows, columns, and headers
- Use Python's built-in `csv` module
- Read CSV files
- Write CSV files
- Use `csv.reader()`
- Use `csv.writer()`
- Use `csv.DictReader()`
- Use `csv.DictWriter()`
- Process network device inventories
- Filter network devices from CSV data
- Validate CSV data
- Prepare CSV data for Network Automation

---

# 1. What is CSV?

CSV stands for:

> Comma-Separated Values

A CSV file stores data in rows and columns.

Example:

```csv
hostname,management_ip,device_type,vendor
R1,192.168.1.1,router,Cisco
R2,192.168.1.2,router,Cisco
SW1,192.168.1.10,switch,Cisco
FW1,192.168.1.254,firewall,Fortinet
````

The first row is normally the header.

The following rows contain the actual data.

---

# 2. CSV Structure

A CSV file can be visualized as:

```text
Header
  ↓
hostname | management_ip | device_type | vendor
  ↓
  R1     | 192.168.1.1   | router      | Cisco
  R2     | 192.168.1.2   | router      | Cisco
  SW1    | 192.168.1.10  | switch      | Cisco
```

Each line represents a row.

Each value represents a column.

---

# 3. CSV and Python

Python provides a built-in module for working with CSV files:

```python
import csv
```

No external package is required.

The most important tools are:

```python
csv.reader()
csv.writer()
csv.DictReader()
csv.DictWriter()
```

---

# 4. csv.reader()

`csv.reader()` reads CSV data row by row.

Example:

```python
import csv

with open("devices.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

The result is returned as a list for each row:

```text
['R1', '192.168.1.1', 'router', 'Cisco']
```

---

# 5. csv.writer()

`csv.writer()` is used to write rows to a CSV file.

Example:

```python
import csv

with open("devices.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "hostname",
        "management_ip",
        "device_type",
        "vendor"
    ])
```

---

# 6. csv.DictReader()

`csv.DictReader()` reads each row as a dictionary.

Example:

```python
import csv

with open("devices.csv", "r") as file:
    reader = csv.DictReader(file)

    for device in reader:
        print(device["hostname"])
```

This is particularly useful for Network Automation because
we can access fields by their names.

Example:

```python
device["management_ip"]
device["vendor"]
device["device_type"]
```

---

# 7. csv.DictWriter()

`csv.DictWriter()` allows us to write dictionaries into CSV files.

Example:

```python
import csv

devices = [
    {
        "hostname": "R1",
        "management_ip": "192.168.1.1",
        "device_type": "router",
        "vendor": "Cisco"
    }
]

with open("devices.csv", "w", newline="") as file:

    fieldnames = [
        "hostname",
        "management_ip",
        "device_type",
        "vendor"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(devices)
```

---

# 8. CSV in Network Engineering

CSV is very useful for storing network inventory.

Example:

```csv
hostname,management_ip,device_type,vendor,location,enabled
R1,192.168.1.1,router,Cisco,Data Center,true
R2,192.168.1.2,router,Cisco,Branch 1,true
SW1,192.168.1.10,switch,Cisco,Data Center,false
FW1,192.168.1.254,firewall,Fortinet,Data Center,true
```

This can become the input for a Network Automation script.

---

# 9. CSV Network Automation Workflow

A typical workflow can look like this:

```text
CSV Inventory
      ↓
Python
      ↓
csv.DictReader()
      ↓
Validate Data
      ↓
Filter Devices
      ↓
Automation Targets
      ↓
Netmiko / APIs / Nornir
      ↓
Network Devices
```

The important concept is:

> Separate the network data from the automation code.

The CSV file contains the inventory.

Python contains the automation logic.

---

# 10. CSV vs JSON

Both CSV and JSON are important in Network Automation.

| Feature             | CSV            | JSON             |
| ------------------- | -------------- | ---------------- |
| Data model          | Tabular        | Hierarchical     |
| Structure           | Rows / Columns | Objects / Arrays |
| Nested data         | Limited        | Excellent        |
| Human readability   | High           | High             |
| Excel compatibility | Excellent      | Limited          |
| REST APIs           | Less common    | Very common      |
| Network inventory   | Excellent      | Excellent        |
| Python module       | `csv`          | `json`           |

---

# 11. CSV vs JSON Example

## CSV

```csv
hostname,management_ip,device_type,vendor
R1,192.168.1.1,router,Cisco
R2,192.168.1.2,router,Cisco
```

## JSON

```json
{
    "devices": [
        {
            "hostname": "R1",
            "management_ip": "192.168.1.1",
            "device_type": "router",
            "vendor": "Cisco"
        },
        {
            "hostname": "R2",
            "management_ip": "192.168.1.2",
            "device_type": "router",
            "vendor": "Cisco"
        }
    ]
}
```

CSV is naturally suited to table-like data.

JSON is better suited to structured and nested data.

---

# 12. Important CSV Parameters

## `newline=""`

Recommended when opening CSV files for writing:

```python
open("devices.csv", "w", newline="")
```

This helps avoid unwanted blank lines on some platforms.

---

## `delimiter`

CSV does not always have to use a comma.

Example:

```python
csv.reader(file, delimiter=";")
```

This allows Python to process files such as:

```text
hostname;management_ip;vendor
R1;192.168.1.1;Cisco
```

---

## `encoding`

For files containing different character sets:

```python
open(
    "devices.csv",
    "r",
    encoding="utf-8"
)
```

---

# 13. Network Automation Best Practice

A good automation architecture separates:

```text
DATA
 ↓
CSV / JSON / YAML
```

from:

```text
LOGIC
 ↓
Python
```

For example:

```text
inventory.csv
     │
     ▼
Python Automation
     │
     ├── Validate
     ├── Filter
     ├── Transform
     └── Process
     │
     ▼
Network Devices
```

This makes automation scripts:

* Reusable
* Easier to maintain
* Easier to test
* Easier to scale
* Easier to modify

---

# 14. Lesson Structure

```text
31_csv/
│
├── README.md
│
├── 01_csv_basics.py
├── 02_csv_reader.py
├── 03_csv_writer.py
├── 04_csv_dictreader.py
├── 05_csv_dictwriter.py
├── 06_csv_file_read.py
├── 07_csv_network_devices.py
├── 08_csv_network_automation.py
├── 09_csv_validation.py
│
└── challenge/
    └── network_device_inventory.py
```

---

# 15. Lesson Roadmap

## 31.1 — CSV Basics

Understand:

* CSV format
* Headers
* Rows
* Columns
* Delimiters

---

## 31.2 — `csv.reader()`

Learn how to:

* Read CSV rows
* Access columns
* Loop through CSV data

---

## 31.3 — `csv.writer()`

Learn how to:

* Create CSV files
* Write headers
* Write rows

---

## 31.4 — `csv.DictReader()`

Learn how to:

* Read CSV as dictionaries
* Access columns by name
* Process network inventory

---

## 31.5 — `csv.DictWriter()`

Learn how to:

* Write dictionaries
* Create structured CSV files
* Export network information

---

## 31.6 — CSV File Operations

Learn how to:

* Read existing inventory files
* Write inventory files
* Handle file operations safely

---

## 31.7 — CSV & Network Devices

Build a network device inventory using CSV.

Example:

```text
R1  → Cisco Router
R2  → Cisco Router
SW1 → Cisco Switch
FW1 → Fortinet Firewall
```

---

## 31.8 — CSV in Network Automation

Use CSV as an input source for automation.

```text
CSV
 ↓
Python
 ↓
Inventory
 ↓
Automation Targets
```

---

## 31.9 — CSV Validation

Validate:

* Required fields
* IP addresses
* Device types
* Vendors
* Enabled status
* Missing data

---

# 16. Practical Challenge

At the end of the lesson, you will build:

> **Network Device Inventory Manager**

The application will:

1. Read devices from a CSV file
2. Display the inventory
3. Filter devices
4. Validate device information
5. Identify devices ready for automation
6. Generate an automation target list

The challenge will be completed without step-by-step solutions.

---

# 17. Key Takeaways

By completing this lesson, you should understand:

```text
CSV
 ↓
Rows
 ↓
Columns
 ↓
Python csv module
 ↓
reader / writer
 ↓
DictReader / DictWriter
 ↓
Network Inventory
 ↓
Validation
 ↓
Network Automation
```

The most important functions are:

```python
csv.reader()
csv.writer()
csv.DictReader()
csv.DictWriter()
```

---

# 18. Connection to Previous Lesson

In Lesson 30 we learned:

```text
JSON
 ↓
Structured Data
 ↓
Network Automation
```

In this lesson we will learn:

```text
CSV
 ↓
Tabular Data
 ↓
Network Automation
```

Together:

```text
             Network Data
                  │
          ┌───────┴───────┐
          ▼               ▼
        JSON              CSV
          │               │
          └───────┬───────┘
                  ▼
               Python
                  ↓
          Network Automation
```

---

# 19. Next Lesson

After completing Lesson 31:

```text
Lesson 32 — XML
```

The learning path will continue:

```text
JSON → CSV → XML → YAML
```

These formats are important foundations for working with:

* APIs
* Network Automation
* Configuration Management
* Cloud Automation
* DevOps
* Infrastructure as Code
