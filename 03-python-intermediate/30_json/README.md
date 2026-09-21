# Lesson 30 — JSON

JSON (JavaScript Object Notation) is one of the most important
data formats used in modern software development, APIs,
Network Automation, and cloud technologies.

In Network Engineering, JSON is especially important because
many modern network platforms and automation tools exchange
structured data using JSON.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand the JSON data format.
- Understand the relationship between JSON and Python data types.
- Convert Python objects to JSON.
- Convert JSON data to Python objects.
- Use `json.dumps()`.
- Use `json.loads()`.
- Write JSON data to files.
- Read JSON data from files.
- Work with nested JSON structures.
- Extract network information from JSON.
- Build structured network device inventories.
- Use JSON in Network Automation workflows.
- Validate and process structured network data.

---

# 📚 Lesson Structure

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

30.1 — JSON Basics

File:

01_json_basics.py

Topics:

What is JSON?
JSON objects.
JSON arrays.
JSON strings.
JSON numbers.
JSON booleans.
JSON null.
JSON structure.
JSON vs Python dictionaries and lists.

Example:

{
    "hostname": "R1",
    "ip_address": "192.168.1.1",
    "device_type": "router",
    "enabled": true
}
Network Engineering Context

Representing a network device using structured data.

30.2 — json.dumps()

File:

02_json_dumps.py

Topics:

Converting Python objects to JSON.
json.dumps().
JSON strings.
Formatting JSON.
indent.
sort_keys.

Example:

import json

device = {
    "hostname": "R1",
    "ip_address": "192.168.1.1",
}

json_data = json.dumps(device, indent=4)

Concept:

Python Object
      ↓
json.dumps()
      ↓
JSON String
30.3 — json.loads()

File:

03_json_loads.py

Topics:

Converting JSON strings to Python objects.
json.loads().
Accessing JSON data.
Working with JSON returned by APIs.

Concept:

JSON String
      ↓
json.loads()
      ↓
Python Object

Example:

json_data = """
{
    "hostname": "R1",
    "ip_address": "192.168.1.1"
}
"""

device = json.loads(json_data)

print(device["hostname"])
30.4 — Writing JSON to a File

File:

04_json_file_write.py

Topics:

Opening files.
Writing JSON.
json.dump().
File modes.
Formatting JSON files.

Concept:

Python Dictionary
       ↓
   json.dump()
       ↓
    JSON File

Example:

with open("devices.json", "w") as file:
    json.dump(devices, file, indent=4)
30.5 — Reading JSON from a File

File:

05_json_file_read.py

Topics:

Reading JSON files.
json.load().
Processing structured data.
Accessing device information.

Concept:

JSON File
    ↓
json.load()
    ↓
Python Object

Example:

with open("devices.json", "r") as file:
    devices = json.load(file)
30.6 — Nested JSON

File:

06_json_nested_data.py

Topics:

Nested dictionaries.
Lists inside dictionaries.
Dictionaries inside lists.
Accessing nested values.
Iterating through nested JSON.

Example:

{
    "hostname": "R1",
    "interfaces": [
        {
            "name": "GigabitEthernet0/0",
            "ip": "192.168.1.1",
            "status": "up"
        },
        {
            "name": "GigabitEthernet0/1",
            "ip": "10.10.10.1",
            "status": "down"
        }
    ]
}
Network Engineering Context

This structure is similar to the type of structured information
returned by network APIs.

30.7 — JSON and Network Devices

File:

07_json_network_devices.py

Topics:

Network device inventory.
Device metadata.
Interfaces.
IP addresses.
Vendors.
Device types.
Structured network information.

Example:

{
    "hostname": "R1",
    "vendor": "Cisco",
    "device_type": "router",
    "management_ip": "192.168.1.1"
}
Network Engineering Context

Creating a structured inventory of network devices.

30.8 — JSON in Network Automation

File:

08_json_network_automation.py

Topics:

JSON + Network Automation.
Device inventory.
Automation input data.
Processing multiple devices.
Extracting configuration information.
Preparing data for APIs.

Architecture:

Network Inventory
       ↓
      JSON
       ↓
     Python
       ↓
 Automation Logic
       ↓
Network Devices

The objective is to understand how JSON can become
the data layer of a Network Automation application.

30.9 — JSON Validation

File:

09_json_validation.py

Topics:

Validate JSON structure.
Check required fields.
Validate device information.
Handle missing keys.
Handle invalid data.
Combine JSON with Exception Handling.

Example:

JSON
 ↓
Required Fields
 ↓
Data Validation
 ↓
Valid Network Device

This lesson connects concepts learned previously:

Exception Handling
        +
JSON
        +
Validation
🧪 Practical Challenge

Directory:

challenge/
└── network_device_inventory.py
Challenge — Network Device Inventory

Build a small Network Device Inventory system using JSON.

The system should manage multiple network devices.

Each device should contain information such as:

hostname
ip_address
vendor
device_type
connection
status

Example structure:

{
    "devices": [
        {
            "hostname": "R1",
            "ip_address": "192.168.1.1",
            "vendor": "Cisco",
            "device_type": "router",
            "connection": "ssh",
            "status": "active"
        }
    ]
}

The challenge should allow the program to:

Store multiple devices.
Convert Python data to JSON.
Save the inventory to a JSON file.
Read the inventory from the JSON file.
Display devices.
Search for a device.
Validate required fields.
Handle invalid or missing data.
🌐 Network Engineering Perspective

JSON is extremely important in modern Network Engineering.

Traditional automation often worked with:

CLI
 ↓
Text Output
 ↓
Regex
 ↓
Parsed Data

Modern automation increasingly works with:

API
 ↓
JSON
 ↓
Python
 ↓
Automation

For example:

Network Device
      ↓
     API
      ↓
     JSON
      ↓
    Python
      ↓
Automation Logic

This is one reason JSON is an essential skill
for Network Automation Engineers.

🔗 JSON and APIs

Many REST APIs use JSON as the primary
data exchange format.

Typical workflow:

Python
   │
   │ HTTP Request
   ↓
REST API
   │
   │ JSON Response
   ↓
Python

Example:

response.json()

Later, this knowledge will be used when we study:

REST APIs
Network Automation
Netmiko
Nornir
pyATS
FastAPI
Cloud APIs
Security APIs
AI Agents
🔄 JSON vs Python
JSON	Python
Object	Dictionary
Array	List
String	str
Number	int / float
true	True
false	False
null	None

Example:

JSON
{
    "hostname": "R1",
    "enabled": true
}
Python
{
    "hostname": "R1",
    "enabled": True
}
🧠 Important JSON Functions
Function	Purpose
json.dumps()	Python → JSON string
json.loads()	JSON string → Python
json.dump()	Python → JSON file
json.load()	JSON file → Python

Remember:

dumps → string
loads → string

dump → file
load → file
🏗️ Network Automation Architecture

By the end of this lesson, we should understand:

                JSON
                 │
                 ↓
        Network Inventory
                 │
                 ↓
              Python
                 │
       ┌─────────┼─────────┐
       ↓         ↓         ↓
    Validate   Process   Automate
       │         │         │
       └─────────┼─────────┘
                 ↓
          Network Devices
📌 Best Practices

When working with JSON:

Keep the structure simple and predictable.
Use meaningful field names.
Validate required data.
Handle missing keys safely.
Use indent when creating human-readable JSON.
Use structured data instead of parsing text when an API provides JSON.
Do not assume that every JSON response has the expected structure.
Combine JSON parsing with proper exception handling.
🎯 Lesson Outcome

After completing Lesson 30, you should be able to:

Understand JSON
      ↓
Convert JSON ↔ Python
      ↓
Read / Write JSON Files
      ↓
Process Nested JSON
      ↓
Build Network Inventory
      ↓
Validate Network Data
      ↓
Use JSON in Network Automation

This lesson prepares us for more advanced topics such as:

JSON
 ↓
REST APIs
 ↓
Network Automation
 ↓
Nornir / pyATS
 ↓
AI + Network Automation
🚀 Next Lesson

After completing Lesson 30:

Lesson 31 — CSV
