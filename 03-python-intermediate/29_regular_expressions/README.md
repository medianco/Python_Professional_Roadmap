# 29 — Regular Expressions

Regular Expressions (Regex) are powerful patterns used to search, match, validate, and extract text from strings.

In Python, Regular Expressions are provided through the built-in `re` module.

For Network Engineers and Network Automation Engineers, Regex is especially useful when working with:

* CLI output
* Network device configurations
* IP addresses
* MAC addresses
* Interface names
* VLAN information
* Routing information
* Logs
* Monitoring data
* Security events
* API responses containing text data

---

## 📁 Directory Structure

```text
29_regular_expressions/
│
├── README.md
│
├── 01_regex_basics.py
├── 02_character_classes.py
├── 03_quantifiers.py
├── 04_anchors.py
├── 05_groups.py
├── 06_match_search_findall.py
├── 07_network_data_extraction.py
├── 08_regex_network_automation.py
├── 09_regex_validation.py
│
└── challenge/
    └── network_regex_validator.py
```

---

# 🎯 Learning Objectives

By completing this lesson, you will be able to:

* Understand what Regular Expressions are.
* Use Python's `re` module.
* Create basic Regex patterns.
* Work with character classes.
* Use Regex quantifiers.
* Understand anchors.
* Create capturing groups.
* Search for patterns inside text.
* Extract multiple values from text.
* Validate structured network data.
* Extract network information from CLI output.
* Apply Regex in Network Automation.
* Build a practical Network Regex Validator.

---

# 🧠 What Is Regular Expression?

A Regular Expression is a pattern that describes a specific structure of text.

For example:

```text
Cisco Router R1
```

We can search for:

```text
Router
```

Or we can create a pattern capable of identifying:

```text
R1
R2
R10
SW1
SW10
```

Regex allows us to describe these patterns instead of manually checking every string.

---

# 🐍 Python Regex Module

Python provides the built-in:

```python
import re
```

No external package is required.

Some important functions include:

```python
re.search()
re.match()
re.findall()
re.fullmatch()
re.sub()
re.split()
```

We will study these functions during this lesson.

---

# 🔤 Regex Character Classes

Character classes allow us to define what characters can appear in a pattern.

Important examples:

| Pattern | Meaning               |
| ------- | --------------------- |
| `\d`    | Digit                 |
| `\D`    | Non-digit             |
| `\w`    | Word character        |
| `\W`    | Non-word character    |
| `\s`    | Whitespace            |
| `\S`    | Non-whitespace        |
| `[0-9]` | Any digit from 0 to 9 |
| `[A-Z]` | Uppercase letter      |
| `[a-z]` | Lowercase letter      |
| `[abc]` | `a`, `b`, or `c`      |

Example:

```python
pattern = r"\d"
```

This matches a digit.

---

# 🔢 Regex Quantifiers

Quantifiers specify how many times a pattern can occur.

| Quantifier | Meaning         |
| ---------- | --------------- |
| `*`        | Zero or more    |
| `+`        | One or more     |
| `?`        | Zero or one     |
| `{n}`      | Exactly n       |
| `{n,}`     | n or more       |
| `{n,m}`    | Between n and m |

Example:

```python
r"\d+"
```

Matches one or more digits.

For example:

```text
1
10
100
192
192168
```

---

# ⚓ Regex Anchors

Anchors specify the position of a match.

| Anchor | Meaning         |
| ------ | --------------- |
| `^`    | Start of string |
| `$`    | End of string   |
| `\b`   | Word boundary   |

Example:

```python
r"^Cisco"
```

Matches text that starts with:

```text
Cisco
```

Example:

```python
r"router$"
```

Matches text that ends with:

```text
router
```

---

# 👥 Groups

Groups allow us to capture specific parts of a match.

Example:

```python
pattern = r"Device: (\w+)"
```

Given:

```text
Device: R1
```

The group captures:

```text
R1
```

Groups become especially useful when extracting information from network device output.

---

# 🔎 Regex Search Functions

We will compare the most important functions:

### `re.match()`

Checks for a match at the beginning of the string.

```python
re.match(pattern, text)
```

### `re.search()`

Searches anywhere in the string.

```python
re.search(pattern, text)
```

### `re.findall()`

Returns all matching results.

```python
re.findall(pattern, text)
```

### `re.fullmatch()`

Requires the entire string to match the pattern.

```python
re.fullmatch(pattern, text)
```

Understanding the difference between these functions is important for writing reliable automation scripts.

---

# 🌐 Regex in Network Engineering

Regex is extremely useful when processing CLI output.

Example:

```text
R1# show ip interface brief

GigabitEthernet0/0    192.168.1.1    YES    up    up
GigabitEthernet0/1    10.10.10.1     YES    up    up
Loopback0             172.16.1.1     YES    up    up
```

We may want to extract:

```text
Interfaces
IP addresses
Interface status
Protocol status
```

Regex can help transform unstructured CLI output into structured information.

---

# 🔥 Network Automation Example

A script may receive:

```text
R1# show version

Cisco IOS Software
Hostname: R1
Management IP: 192.168.1.1
Serial Number: FOC1234ABC
```

Regex can extract:

```text
Hostname
Management IP
Serial Number
```

For example:

```text
Hostname:
R1

Management IP:
192.168.1.1

Serial Number:
FOC1234ABC
```

This information can then be used by an automation system.

---

# 🔐 Regex in Cybersecurity

Regex is also useful for analyzing:

* Firewall logs
* Authentication logs
* IDS/IPS alerts
* Security events
* IP addresses
* Ports
* URLs
* Email addresses
* Indicators of compromise
* Suspicious patterns

Example:

```text
Failed login from 192.168.10.55 on port 22
```

We can extract:

```text
Source IP: 192.168.10.55
Port: 22
```

---

# 🏗️ Lesson Architecture

The lesson progresses from basic Regex concepts toward practical Network Automation.

```text
Regex Basics
     │
     ▼
Character Classes
     │
     ▼
Quantifiers
     │
     ▼
Anchors
     │
     ▼
Groups
     │
     ▼
match / search / findall
     │
     ▼
Network Data Extraction
     │
     ▼
Network Automation
     │
     ▼
Validation
     │
     ▼
Practical Challenge
```

---

# 📚 Lesson Roadmap

## 29.1 — Regex Basics

Learn:

* `re` module
* Regex patterns
* `re.search()`
* Match objects
* `group()`

Network example:

```text
Cisco Router R1
```

---

## 29.2 — Character Classes

Learn:

```text
\d
\D
\w
\W
\s
\S
[0-9]
[A-Z]
[a-z]
```

Network examples:

* Device IDs
* Interface names
* VLAN IDs

---

## 29.3 — Quantifiers

Learn:

```text
*
+
?
{n}
{n,}
{n,m}
```

Network examples:

* Multiple digits
* Interface numbers
* VLAN ranges

---

## 29.4 — Anchors

Learn:

```text
^
$
\b
```

Network examples:

* CLI lines
* Configuration validation
* Hostname validation

---

## 29.5 — Groups

Learn:

* Capturing groups
* Multiple groups
* `group()`
* `groups()`

Network examples:

```text
Hostname: R1
IP: 192.168.1.1
```

---

## 29.6 — match() vs search() vs findall()

Understand the difference between:

```python
re.match()
re.search()
re.findall()
re.fullmatch()
```

This is important for reliable text processing.

---

## 29.7 — Network Data Extraction

Extract information from realistic network output:

```text
IP addresses
Interfaces
Hostnames
VLANs
MAC addresses
```

---

## 29.8 — Regex + Network Automation

Combine Regex with Network Automation concepts.

Example workflow:

```text
Device
   │
   ▼
CLI Output
   │
   ▼
Regex
   │
   ▼
Extract Information
   │
   ▼
Structured Data
```

---

## 29.9 — Regex Validation

Use Regex to validate structured input such as:

```text
Hostname
IPv4 format
MAC address
VLAN ID
Interface name
```

Important:

> Regex can validate the **format** of an IP address, but it is not always the best tool for validating whether an IP is semantically valid. Python's `ipaddress` module is preferred for actual IP validation.

---

# 🧪 Practical Challenge

At the end of the lesson, you will build:

```text
network_regex_validator.py
```

The application will process network-related text and extract or validate information such as:

* Hostnames
* IPv4 addresses
* MAC addresses
* Interface names
* VLAN IDs

The challenge will combine:

```text
Regex
   +
Functions
   +
Validation
   +
Exception Handling
   +
Network Engineering
```

You will implement the challenge independently without following a step-by-step solution.

---

# 🏆 Final Goal

By the end of Lesson 29, you should be comfortable looking at unstructured text such as:

```text
R1# show ip interface brief

GigabitEthernet0/0    192.168.1.1    YES    up    up
GigabitEthernet0/1    10.10.10.1     YES    up    up
Loopback0             172.16.1.1     YES    up    up
```

and thinking:

```text
"What information do I need?"
        ↓
"What pattern identifies it?"
        ↓
"How can Regex extract it?"
        ↓
"How can Python process the result?"
```

This mindset is essential for Network Automation.

---

# 🚀 Connection to the Overall Roadmap

Regular Expressions will become useful in later stages:

```text
Python
  │
  ├── Regex
  │
  ├── JSON
  ├── CSV
  ├── XML
  ├── YAML
  └── Logging
        │
        ▼
Network Automation
        │
        ├── Netmiko
        ├── APIs
        ├── Nornir
        └── pyATS
              │
              ▼
        AI + Network Automation
```

---

# 📌 Important Principle

> **Regex is not just about matching text.**
>
> For a Network Engineer, Regex is a tool for turning unstructured network data into information that Python can process.

---

## 🎯 Success Criteria

Lesson 29 will be considered complete when you can:

* [ ] Explain what Regex is.
* [ ] Use the Python `re` module.
* [ ] Build basic Regex patterns.
* [ ] Use character classes.
* [ ] Use quantifiers.
* [ ] Use anchors.
* [ ] Use groups.
* [ ] Understand `match()`, `search()`, and `findall()`.
* [ ] Extract network information from CLI output.
* [ ] Validate structured network data.
* [ ] Build the Network Regex Validator challenge.

---

**Next:** `29.1 — Regex Basics`
