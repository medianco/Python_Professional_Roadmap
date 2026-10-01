# Lesson 34 — Logging

## 📌 Overview

Logging is one of the most important tools for building reliable and maintainable Python applications.

In simple Python scripts, developers often use:

```python
print("Connecting to device...")
```

However, `print()` is not a proper logging system.

Professional applications need to record:

* What happened
* When it happened
* Which operation was executed
* Which device was involved
* Whether the operation succeeded
* Whether a warning or error occurred
* The severity of the event
* Where the log should be stored

Python provides the built-in `logging` module for this purpose.

This lesson introduces Python Logging from the fundamentals and gradually applies it to **Network Automation** scenarios.

---

# 🎯 Learning Objectives

By the end of this lesson, you will be able to:

* Understand why Logging is important.
* Understand the difference between `print()` and Logging.
* Understand Logging levels.
* Use the Python `logging` module.
* Configure a Logger.
* Create log messages.
* Understand Loggers, Handlers, Formatters, and Levels.
* Write logs to the console.
* Write logs to files.
* Create custom log formats.
* Use timestamps in logs.
* Log exceptions and errors.
* Configure multiple handlers.
* Separate application logs from error logs.
* Use Logging in Network Automation.
* Log device connection attempts.
* Log successful and failed operations.
* Build a reusable logging configuration.
* Prepare logging architecture for larger automation systems.

---

# 🗺️ Lesson Roadmap

## 34.1 Introduction to Logging

Understand:

```text
What is Logging?
Why do we need Logging?
Why is print() not enough?
```

Basic example:

```python
print("Connecting to R1...")
```

Compared with:

```python
logger.info("Connecting to R1...")
```

---

# 34.2 Logging Levels

Python provides several standard logging levels:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

Severity hierarchy:

```text
DEBUG
  ↓
INFO
  ↓
WARNING
  ↓
ERROR
  ↓
CRITICAL
```

### DEBUG

Detailed information useful for troubleshooting.

Example:

```text
DEBUG - Connection parameters loaded
```

### INFO

Normal application events.

Example:

```text
INFO - Successfully connected to R1
```

### WARNING

Something unexpected happened, but the application can continue.

Example:

```text
WARNING - Device response time is high
```

### ERROR

An operation failed.

Example:

```text
ERROR - Failed to connect to R1
```

### CRITICAL

A serious failure that may prevent the application from continuing.

Example:

```text
CRITICAL - Automation system cannot continue
```

---

# 34.3 Basic Python Logging

Learn how to use:

```python
import logging
```

and:

```python
logging.info()
logging.warning()
logging.error()
```

Basic workflow:

```text
Python Application
       ↓
    logging
       ↓
    Log Event
```

---

# 34.4 Logger Configuration

Understand:

```text
Logger
Handler
Formatter
Level
```

Architecture:

```text
                Logger
                   │
          ┌────────┴────────┐
          │                 │
       Handler           Handler
          │                 │
       Console             File
          │                 │
          ▼                 ▼
       Terminal       application.log
```

---

# 34.5 Log Formatting

Learn how to customize log messages.

Example:

```text
2026-10-01 11:30:45 | INFO | Connected to R1
```

Important formatting fields include:

```text
%(asctime)s
%(levelname)s
%(message)s
```

Network Automation logs can include additional context such as:

```text
device
operation
status
```

---

# 34.6 Logging to Files

Learn how to write logs to a file.

Example:

```text
output/
└── automation.log
```

Workflow:

```text
Python Application
       ↓
     Logger
       ↓
     FileHandler
       ↓
automation.log
```

This is especially important for automation systems because the output can be reviewed after the automation process finishes.

---

# 34.7 Multiple Handlers

A professional application may need different destinations for logs.

Example:

```text
                  Logger
                    │
          ┌─────────┴─────────┐
          │                   │
       Console             File
          │                   │
          ▼                   ▼
      Terminal          automation.log
```

We will learn how to send logs to multiple handlers.

---

# 34.8 Logging Exceptions

Logging becomes particularly important when exceptions occur.

Example:

```python
try:
    connect_to_device()

except ConnectionError:
    logger.exception("Connection failed")
```

This allows us to preserve useful diagnostic information.

Workflow:

```text
Operation
    ↓
Exception
    ↓
Logging
    ↓
Log File
```

---

# 34.9 Logging and Network Automation

This is the main practical focus of the lesson.

A Network Automation system should record operations such as:

```text
Connecting to R1
Connection successful
Sending configuration
Configuration successful
Disconnecting from R1
```

Example:

```text
2026-10-01 11:40:01 | INFO | R1 | Connection started
2026-10-01 11:40:02 | INFO | R1 | Connection successful
2026-10-01 11:40:03 | INFO | R1 | Configuration sent
2026-10-01 11:40:04 | INFO | R1 | Configuration successful
2026-10-01 11:40:05 | INFO | R1 | Connection closed
```

---

# 34.10 Network Device Error Logging

Automation systems must also record failures.

Example:

```text
2026-10-01 11:42:10 | ERROR | R2 | Connection failed
```

Possible failures include:

```text
Authentication failure
Connection timeout
Invalid IP address
Device unreachable
Configuration failure
Command failure
API failure
```

---

# 34.11 Logging Architecture

We will build toward an architecture similar to:

```text
                  Network Automation
                          │
                          ▼
                       Logger
                          │
             ┌────────────┼────────────┐
             │            │            │
           DEBUG         INFO       ERROR
             │            │            │
             └────────────┼────────────┘
                          ▼
                       Handlers
                          │
               ┌──────────┴──────────┐
               │                     │
            Console                File
               │                     │
               ▼                     ▼
            Terminal          automation.log
```

---

# 34.12 Logging Configuration

We will learn how to create a reusable logging configuration instead of configuring logging repeatedly throughout the application.

Concept:

```text
Application
     │
     ▼
Logging Configuration
     │
     ├── Logger
     ├── Level
     ├── Formatter
     └── Handlers
```

This prepares the project for larger applications.

---

# 34.13 Logging + Network Device Inventory

We will combine Logging with the YAML inventory from Lesson 33.

Architecture:

```text
YAML Inventory
      │
      ▼
Python
      │
      ├── Load
      ├── Validate
      └── Filter
      │
      ▼
Network Automation
      │
      ▼
Logging
```

Example:

```text
YAML
 ↓
R1
 ↓
Validate
 ↓
Connect
 ↓
Configure
 ↓
Log Result
```

This demonstrates how multiple Python concepts can work together.

---

# 34.14 Log File Management

We will learn basic log file organization.

Suggested structure:

```text
34_logging/
│
├── data/
│
├── output/
│   └── automation.log
│
└── Python files
```

This follows the project principle:

```text
Data
  ↓
data/

Generated Output
  ↓
output/

Application Logic
  ↓
Python files
```

---

# 34.15 Logging Best Practices

Throughout the lesson, we will follow professional practices.

## Use Appropriate Levels

Do not use:

```python
logger.error("Connected successfully")
```

Use:

```python
logger.info("Connected successfully")
```

---

## Use Meaningful Messages

Avoid:

```text
ERROR - Failed
```

Prefer:

```text
ERROR - Failed to connect to R1: connection timeout
```

---

## Include Context

For Network Automation, useful context includes:

```text
Hostname
IP Address
Operation
Status
Error
```

---

## Avoid Sensitive Information

Logs should not expose secrets such as:

```text
Passwords
API tokens
Private keys
Credentials
```

Example:

```text
BAD:
password=MySecretPassword

GOOD:
authentication failed for R1
```

---

# 34.16 Logging vs print()

A key comparison:

| Feature                 | `print()` | Logging |
| ----------------------- | --------- | ------- |
| Severity levels         | ❌         | ✅       |
| Timestamp               | Manual    | ✅       |
| Log file                | Manual    | ✅       |
| Multiple destinations   | ❌         | ✅       |
| Filtering               | Limited   | ✅       |
| Exception integration   | Limited   | ✅       |
| Production applications | Limited   | ✅       |
| Network Automation      | Limited   | ✅       |

The goal is not that `print()` is forbidden.

`print()` is still useful for simple scripts and direct user output.

However, Logging is the appropriate mechanism for application events that need to be recorded and analyzed.

---

# 34.17 Practical Network Automation Example

The final examples will simulate a workflow such as:

```text
Load Inventory
      ↓
Validate Device
      ↓
Start Connection
      ↓
Connection Result
      ↓
Send Command
      ↓
Command Result
      ↓
Disconnect
      ↓
Log Everything
```

Example:

```text
INFO     | R1 | Connection started
INFO     | R1 | Connection successful
INFO     | R1 | Executing command
INFO     | R1 | Command completed
INFO     | R1 | Disconnecting
INFO     | R1 | Automation completed
```

And when something fails:

```text
ERROR    | R2 | Connection failed
```

---

# 🧪 Practical Exercises

During the lesson, we will implement:

### Exercise 1 — Basic Logging

Create logs using:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

### Exercise 2 — Custom Logger

Create a configured Logger with a custom format.

### Exercise 3 — File Logging

Write logs to:

```text
output/application.log
```

### Exercise 4 — Multiple Handlers

Send logs to:

```text
Console
+
File
```

### Exercise 5 — Exception Logging

Use Logging to record exceptions.

### Exercise 6 — Network Device Logging

Create a simulated device connection workflow and record its events.

### Exercise 7 — YAML + Logging

Read the Lesson 33 YAML inventory and log the processing of each device.

---

# 🏆 Final Challenge — Network Automation Logging System

Build a small Network Automation Logging System.

The system should:

### 1. Load Network Devices

Read devices from:

```text
data/network_devices.yaml
```

### 2. Validate Devices

Validate:

```text
Hostname
Management IP
Protocol
Port
Vendor
Device Type
Status
```

### 3. Configure Logging

Create:

```text
Console Handler
File Handler
```

### 4. Simulate Device Operations

For each valid device, simulate:

```text
Connection
Command Execution
Configuration
Disconnection
```

### 5. Log Events

Record:

```text
INFO
WARNING
ERROR
```

where appropriate.

### 6. Store Logs

Write the results to:

```text
output/network_automation.log
```

### 7. Protect Sensitive Information

Do not log:

```text
Passwords
Secrets
API Tokens
Private Keys
```

---

# 📁 Suggested File Structure

```text
34_logging/
│
├── README.md
│
├── data/
│   └── network_devices.yaml
│
├── output/
│   ├── application.log
│   └── network_automation.log
│
├── 01_logging_basics.py
├── 02_logging_levels.py
├── 03_logger_configuration.py
├── 04_logging_to_file.py
├── 05_logging_format.py
├── 06_multiple_handlers.py
├── 07_logging_exceptions.py
├── 08_network_device_logging.py
├── 09_yaml_network_logging.py
│
└── challenge/
    └── network_automation_logging.py
```

---

# 🔐 Security Considerations

Logging is extremely useful, but logs can become a security risk if sensitive information is recorded.

Never log:

```text
Passwords
API Keys
Authentication Tokens
Private Keys
Session Cookies
Secrets
```

Instead, log the event without exposing the secret.

For example:

```text
INFO | R1 | Authentication attempt started
ERROR | R1 | Authentication failed
```

rather than:

```text
ERROR | R1 | username=admin password=Cisco123
```

---

# 🌐 Network Automation Workflow

By the end of this lesson, we will have:

```text
                 YAML Inventory
                       │
                       ▼
                  Python App
                       │
              ┌────────┴────────┐
              │                 │
          Validation          Logging
              │                 │
              ▼                 ▼
        Valid Devices      Log Events
              │                 │
              ▼                 ▼
       Automation       automation.log
```

This is a significant step toward building professional automation applications.

---

# 🧠 Key Takeaways

Remember:

```text
print()
   ↓
Simple Console Output

Logging
   ↓
Structured Application Events
   ↓
Levels
   ↓
Handlers
   ↓
Formatters
   ↓
Files
   ↓
Diagnostics
   ↓
Network Automation
```

The most important concepts are:

* `Logger`
* `Handler`
* `Formatter`
* `Level`
* `FileHandler`
* `StreamHandler`
* `logger.debug()`
* `logger.info()`
* `logger.warning()`
* `logger.error()`
* `logger.critical()`
* `logger.exception()`

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
Log
  ↓
Debug
  ↓
Apply
  ↓
Document
  ↓
Publish
  ↓
Prove Your Skills
```

Logging introduces an important professional mindset:

> **A reliable automation system should not only perform operations — it should also provide evidence of what happened.**

---

# 📊 Progress

**Stage:** `03-python-intermediate`

**Lesson:** `34 — Logging`

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
* ✅ 33 — YAML

### Current Lesson

* 🟡 34 — Logging

### Next

* ⬜ 35 — Datetime

---

# 🎯 Final Goal

The ultimate goal of this lesson is to move from:

```text
"I know how to print messages."
```

to:

```text
"I can design a structured logging system
for a Python Network Automation application."
```

Logging will become a fundamental component of the larger architecture we will build in future lessons.
