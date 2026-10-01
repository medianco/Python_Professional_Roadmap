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

Logging levels are used to classify log messages according to their **severity and importance**.

Python's `logging` module provides five standard logging levels that are commonly used in application development and Network Automation:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

The levels form a severity hierarchy:

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

The higher the level, the more severe the event.

---

## 📊 Standard Logging Levels

| Level      | Numeric Value | Severity | Purpose                                            |
| ---------- | ------------: | -------- | -------------------------------------------------- |
| `DEBUG`    |            10 | Lowest   | Detailed diagnostic information                    |
| `INFO`     |            20 | Normal   | Confirmation of normal application operation       |
| `WARNING`  |            30 | Moderate | Something unexpected or potentially problematic    |
| `ERROR`    |            40 | High     | An operation failed                                |
| `CRITICAL` |            50 | Highest  | A serious failure affecting the application/system |

---

# 1. DEBUG

```python
logger.debug("Preparing SSH connection to R1")
```

### Purpose

`DEBUG` is used for detailed information that is primarily useful during development, troubleshooting, and diagnostics.

It can provide information about the internal state of an application.

### Network Automation Examples

```text
DEBUG | Loading device inventory
DEBUG | Preparing connection to R1
DEBUG | Management IP: 192.168.1.1
DEBUG | Management port: 22
DEBUG | Preparing SSH parameters
DEBUG | Sending command: show version
```

### When to use DEBUG

Use `DEBUG` when you need to answer questions such as:

```text
What exactly is the application doing?
Which parameters were loaded?
Which step is currently executing?
Where did the process stop?
```

### Important Security Note

Do not use DEBUG logs to expose sensitive information.

Avoid:

```text
DEBUG | username=admin password=Cisco123
```

Prefer:

```text
DEBUG | Authentication parameters loaded
```

---

# 2. INFO

```python
logger.info("Successfully connected to R1")
```

### Purpose

`INFO` is used to record normal application events and confirm that expected operations are taking place.

This is usually the primary level for operational logs.

### Network Automation Examples

```text
INFO | Starting Network Automation
INFO | Loading device inventory
INFO | Connecting to R1
INFO | Connection successful
INFO | Executing show version
INFO | Configuration completed
INFO | Disconnecting from R1
```

### When to use INFO

Use `INFO` when an important normal event occurs.

Think of it as:

> "The application is operating normally, and this event is worth recording."

---

# 3. WARNING

```python
logger.warning("R1 response time is higher than expected")
```

### Purpose

`WARNING` indicates an unexpected condition or situation that may require attention, but does not necessarily mean that the current operation has failed.

The application can usually continue.

### Network Automation Examples

```text
WARNING | R1 response time is higher than expected
WARNING | Device configuration is approaching timeout
WARNING | Interface GigabitEthernet0/1 is down
WARNING | Device inventory contains an inactive device
```

### Important Concept

A warning does **not necessarily mean failure**.

For example:

```text
Device response time = 8 seconds
```

The connection may still succeed, but the response time may be unusual.

Therefore:

```text
WARNING
```

is more appropriate than:

```text
ERROR
```

---

# 4. ERROR

```python
logger.error("Failed to connect to R1")
```

### Purpose

`ERROR` indicates that an operation has failed.

The application may still be able to continue processing other operations.

### Network Automation Examples

```text
ERROR | Failed to connect to R1
ERROR | Command execution failed on R2
ERROR | Configuration failed on SW1
ERROR | Invalid device configuration
ERROR | API request failed
```

### Example

Suppose an automation system processes four devices:

```text
R1 → Success
R2 → Connection Failed
SW1 → Success
FW1 → Success
```

The automation process may continue with the other devices.

The event for R2 would be:

```text
ERROR | R2 | Connection failed
```

rather than `CRITICAL`.

---

# 5. CRITICAL

```python
logger.critical("Network Automation system cannot continue")
```

### Purpose

`CRITICAL` represents a very serious failure that may prevent the application from continuing normally.

It is the highest standard logging level.

### Network Automation Examples

```text
CRITICAL | Network Automation system cannot continue
CRITICAL | Configuration database unavailable
CRITICAL | Required automation system unavailable
CRITICAL | Logging system initialization failed
```

### Example

Imagine that the automation application requires its central inventory database.

If the database is unavailable:

```text
CRITICAL | Device inventory service unavailable
```

The application may not be able to safely continue.

---

# 📈 Logging Severity Hierarchy

The five standard levels can be visualized as:

```text
                CRITICAL
                   ▲
                   │
                 ERROR
                   ▲
                   │
                WARNING
                   ▲
                   │
                  INFO
                   ▲
                   │
                 DEBUG
```

Another way to understand them:

```text
DEBUG
│
├── Detailed diagnostics
│
INFO
│
├── Normal application events
│
WARNING
│
├── Unexpected condition
│
ERROR
│
├── Operation failed
│
CRITICAL
│
└── Serious system/application failure
```

---

# 🔢 Numeric Logging Values

Python internally assigns a numeric value to each standard level:

```text
DEBUG      = 10
INFO       = 20
WARNING    = 30
ERROR      = 40
CRITICAL   = 50
```

The numeric values determine the severity ordering.

For example:

```python
logging.DEBUG
```

returns:

```text
10
```

and:

```python
logging.ERROR
```

returns:

```text
40
```

Therefore:

```text
ERROR > WARNING > INFO > DEBUG
```

in terms of logging severity.

---

# 🎚️ Logging Level Configuration

The configured logging level determines the minimum severity that will be processed.

For example:

```python
logging.basicConfig(
    level=logging.INFO
)
```

means:

```text
DEBUG       ❌
INFO        ✅
WARNING     ✅
ERROR       ✅
CRITICAL    ✅
```

Because `INFO` is the configured threshold.

---

## Level = DEBUG

```python
logging.basicConfig(
    level=logging.DEBUG
)
```

Result:

```text
DEBUG       ✅
INFO        ✅
WARNING     ✅
ERROR       ✅
CRITICAL    ✅
```

All standard levels are allowed.

---

## Level = INFO

```python
logging.basicConfig(
    level=logging.INFO
)
```

Result:

```text
DEBUG       ❌
INFO        ✅
WARNING     ✅
ERROR       ✅
CRITICAL    ✅
```

---

## Level = WARNING

```python
logging.basicConfig(
    level=logging.WARNING
)
```

Result:

```text
DEBUG       ❌
INFO        ❌
WARNING     ✅
ERROR       ✅
CRITICAL    ✅
```

---

## Level = ERROR

```python
logging.basicConfig(
    level=logging.ERROR
)
```

Result:

```text
DEBUG       ❌
INFO        ❌
WARNING     ❌
ERROR       ✅
CRITICAL    ✅
```

---

## Level = CRITICAL

```python
logging.basicConfig(
    level=logging.CRITICAL
)
```

Result:

```text
DEBUG       ❌
INFO        ❌
WARNING     ❌
ERROR       ❌
CRITICAL    ✅
```

---

# 🧠 Important Rule

The configured logging level should be understood as a **minimum severity threshold**.

For example:

```python
level=logging.WARNING
```

does not mean:

> "Only show WARNING messages."

It means:

> "Show WARNING and all messages with a higher severity."

Therefore:

```text
WARNING
ERROR
CRITICAL
```

will be processed.

---

# 🌐 Network Automation Mapping

A useful way to map the levels to Network Automation is:

```text
DEBUG
   ↓
Internal troubleshooting information

INFO
   ↓
Normal device operations

WARNING
   ↓
Unexpected but recoverable condition

ERROR
   ↓
Specific device/operation failure

CRITICAL
   ↓
Automation system failure
```

### Example Workflow

```text
Start Automation
       │
       ▼
     INFO
       │
       ▼
Connect to R1
       │
       ▼
     DEBUG
       │
       ▼
Connection successful
       │
       ▼
      INFO
       │
       ▼
High response time
       │
       ▼
    WARNING
       │
       ▼
Command execution fails
       │
       ▼
     ERROR
       │
       ▼
Automation engine unavailable
       │
       ▼
   CRITICAL
```

---

# ⚠️ Common Mistakes

## Mistake 1 — Using ERROR for normal events

Incorrect:

```python
logger.error("Connected to R1")
```

Correct:

```python
logger.info("Connected to R1")
```

---

## Mistake 2 — Using CRITICAL for every error

Incorrect:

```python
logger.critical("R2 connection failed")
```

If only R2 failed but the automation can continue with other devices, use:

```python
logger.error("R2 connection failed")
```

Reserve `CRITICAL` for serious failures affecting the overall application or its ability to continue safely.

---

## Mistake 3 — Using WARNING for actual failures

Incorrect:

```python
logger.warning("Configuration command failed")
```

If the command actually failed:

```python
logger.error("Configuration command failed")
```

is more appropriate.

---

## Mistake 4 — Logging everything as INFO

Incorrect:

```python
logger.info("Everything")
```

A professional application should distinguish between:

```text
Normal event
Warning
Failure
Critical failure
```

This makes the logs easier to search, filter, and analyze.

---

# 🎯 Quick Reference

```text
DEBUG
→ Detailed diagnostic information

INFO
→ Normal application events

WARNING
→ Unexpected condition that may require attention

ERROR
→ Operation failed

CRITICAL
→ Serious failure affecting the application/system
```

---

# 🧪 Practical Example

Consider this Network Automation workflow:

```text
1. Load YAML inventory
2. Validate devices
3. Connect to R1
4. Execute command
5. Detect slow response
6. Configuration fails
7. Automation engine crashes
```

Appropriate logging could be:

```text
INFO     | Loading YAML inventory
INFO     | Validating devices
INFO     | Connecting to R1
DEBUG    | Connecting to 192.168.1.1:22
INFO     | Connection successful
WARNING  | R1 response time is high
ERROR    | Configuration command failed
CRITICAL | Automation engine stopped unexpectedly
```

This provides a chronological and severity-aware view of what happened.

---

# 🔑 Key Takeaways

Remember:

```text
DEBUG
↓
Detailed troubleshooting information

INFO
↓
Normal operations

WARNING
↓
Potential problem

ERROR
↓
Operation failure

CRITICAL
↓
Serious application/system failure
```

And remember the numeric hierarchy:

```text
DEBUG      10
INFO       20
WARNING    30
ERROR      40
CRITICAL   50
```

The configured level acts as a **minimum severity threshold**:

```text
level = WARNING

WARNING    ✅
ERROR      ✅
CRITICAL   ✅

DEBUG      ❌
INFO       ❌
```

This concept will become especially important when we start working with **Handlers and Formatters**, because we will be able to control exactly which events are sent to the console, files, or other destinations.

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
