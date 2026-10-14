# Lesson 35 — Date and Time Handling in Python

## 📌 Overview

This lesson introduces Python's `datetime` module and explains how to work with dates, times, durations, timestamps, and time zones.

Accurate date and time handling is essential in professional applications, especially in **Network Automation, Network Monitoring, Log Analysis, Incident Investigation, and Scheduled Tasks**.

Throughout this lesson, we will use practical examples related to network devices, operational logs, monitoring events, and outage analysis.

The primary goal is to learn how to process time-related data reliably and avoid common mistakes involving date formats, time zones, and duration calculations.

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand the purpose of Python's `datetime` module.
- Work with `date`, `time`, `datetime`, and `timedelta`.
- Create and manipulate date and time objects.
- Format dates and times using `strftime()`.
- Parse date strings using `strptime()`.
- Compare dates and calculate time differences.
- Work with Unix timestamps.
- Understand naive and timezone-aware datetime objects.
- Use UTC and timezone information correctly.
- Handle invalid date and time input.
- Apply date and time operations to network automation tasks.
- Build reusable functions for time-related operations.

---

# 🗺️ Lesson Roadmap

## 35.1 Introduction to Datetime

Understand the `datetime` module and its role in Python applications.

Topics:

- Importing `datetime`
- Understanding the module and its classes
- Getting the current date and time
- Creating date and time objects
- Common use cases in automation

Key classes:

```python
date
time
datetime
timedelta
timezone
```

## 35.2 Working with Date and Time Objects

Learn how to create and access date and time components.

Topics:

- Creating a `date` object
- Creating a `time` object
- Creating a `datetime` object
- Accessing year, month, day, hour, minute, and second
- Comparing date and time values
- Understanding object attributes

Network Automation Example:

Representing the date and time at which a network device was checked.

## 35.3 Formatting Dates with `strftime()`

Learn how to convert date and time objects into readable strings.

Topics:

- Formatting dates
- Formatting times
- Combining date and time formats
- Common formatting directives
- Producing consistent timestamps for logs and reports

Important directives:

| Directive | Meaning | Example |
|---|---|---|
| `%Y` | Four-digit year | `2026` |
| `%m` | Month | `10` |
| `%d` | Day | `14` |
| `%H` | Hour, 24-hour format | `16` |
| `%M` | Minute | `30` |
| `%S` | Second | `45` |
| `%A` | Full weekday name | `Wednesday` |
| `%z` | UTC offset | `+0300` |

The actual weekday depends on the date being formatted.

## 35.4 Parsing Date Strings with `strptime()`

Learn how to convert strings into datetime objects.

Topics:

- Parsing a date string
- Parsing a timestamp
- Matching the input format
- Handling invalid formats
- Using `ValueError` for invalid input

Network Automation Example:

Parsing timestamps received from a monitoring system or an exported device log.

## 35.5 Date Arithmetic with `timedelta`

Understand how to calculate and manipulate time intervals.

Topics:

- Adding days to a date
- Subtracting time intervals
- Calculating the difference between two dates
- Working with hours, minutes, and seconds
- Calculating elapsed time

Network Automation Example:

Calculating how long a device has been unavailable.

## 35.6 Comparing Dates and Times

Learn how to compare datetime objects correctly.

Topics:

- Earlier and later timestamps
- Sorting events chronologically
- Calculating elapsed time
- Detecting stale monitoring records
- Understanding comparison limitations between naive and aware datetimes

Network Automation Example:

Identifying the latest event in a collection of network device logs.

## 35.7 Unix Timestamps

Understand Unix timestamps and their use in software systems.

Topics:

- What a Unix timestamp represents
- Using `timestamp()`
- Converting timestamps with `fromtimestamp()`
- Understanding UTC-based conversion with `utcfromtimestamp()` alternatives such as `datetime.fromtimestamp(timestamp, tz=timezone.utc)`
- Processing timestamps received from APIs and monitoring platforms

Network Automation Example:

Converting API event timestamps into readable UTC date and time values.

## 35.8 Time Zones and UTC

Learn how to handle timezone-aware date and time values.

Topics:

- UTC and why it matters
- Naive versus timezone-aware datetime objects
- The `timezone` class
- Using `datetime.now(timezone.utc)`
- Converting between time zones
- Understanding `astimezone()`
- Introduction to `zoneinfo` for named time zones

Network Automation Example:

Correlating events from network devices located in different time zones.

Important principle:

> Store and compare timestamps consistently, preferably in UTC, and convert them to local time when presenting them to users.

## 35.9 Datetime Error Handling

Learn how to handle common date and time errors safely.

Topics:

- Invalid date values
- Incorrect input formats
- `ValueError`
- Missing timestamp fields
- Invalid timestamp data
- Validating input before processing

Network Automation Example:

Processing a monitoring record without allowing one malformed timestamp to stop the entire analysis.

## 35.10 Network Automation Applications

Combine the concepts from this lesson in practical scenarios.

Potential applications:

- Recording device check timestamps
- Measuring response and processing durations
- Calculating device downtime
- Detecting stale inventory or monitoring records
- Sorting network events
- Correlating logs from multiple devices
- Generating timestamped reports
- Processing timestamps received from REST APIs

---

# 🧪 Practical Exercises

### Exercise 1 — Current Timestamp

Display the current date and time in a consistent format.

### Exercise 2 — Date Formatting

Convert a datetime object into a readable timestamp.

### Exercise 3 — String Parsing

Parse a date string and handle invalid input.

### Exercise 4 — Time Difference

Calculate the duration between two timestamps.

### Exercise 5 — Device Downtime

Calculate how long a network device has been unavailable.

### Exercise 6 — Event Sorting

Sort network monitoring events by timestamp.

### Exercise 7 — UTC Conversion

Convert timezone-aware timestamps to UTC.

### Exercise 8 — Stale Monitoring Records

Identify records older than a specified time threshold.

The exercises should be solved independently before reviewing any reference implementation.

---

# 🏆 Final Challenge — Network Event Time Analyzer

Build a small Python application that analyzes timestamped network events.

## Requirements

### 1. Input Data

Create a separate data file containing multiple network events.

Each event should include:

- `hostname`
- `event_type`
- `timestamp`
- `status`

Example event types:

```text
device_up
device_down
interface_error
configuration_change
```

### 2. Data Processing

The application must:

- Load the event data.
- Validate required fields.
- Parse timestamps correctly.
- Handle invalid timestamps without stopping the processing of all remaining events.
- Sort valid events chronologically.
- Identify the oldest and newest valid events.

### 3. Time Analysis

Calculate the time difference between selected events.

Where sufficient information exists, estimate device downtime using matching down and up events for the same device.

Do not assume that every down event has a corresponding up event.

### 4. Time Zone Handling

Use timezone-aware timestamps and a consistent comparison standard.

UTC is recommended for internal event processing.

### 5. Output

Generate a readable report containing:

- Total events processed
- Valid and invalid event counts
- Events sorted by time
- Oldest and newest event timestamps
- Relevant time differences
- Any unmatched device-down events

### 6. Code Quality

The solution must use:

- Clear function names
- Type hints where appropriate
- Docstrings and educational comments
- Exception handling
- A separate data file
- A separate output location for generated reports

### 7. Security and Reliability

Do not invent missing timestamps or silently discard malformed records.

Document any assumptions used when calculating downtime.

---

# 📁 Suggested File Structure

```text
35_datetime/
│
├── README.md
│
├── data/
│   └── network_events.json
│
├── output/
│   └── event_analysis_report.txt
│
├── 01_datetime_basics.py
├── 02_date_time_objects.py
├── 03_strftime_formatting.py
├── 04_strptime_parsing.py
├── 05_timedelta_arithmetic.py
├── 06_datetime_comparison.py
├── 07_unix_timestamps.py
├── 08_timezone_utc.py
├── 09_datetime_error_handling.py
├── 10_network_automation_datetime.py
│
└── challenge/
    └── network_event_time_analyzer.py
```

Generated output files should be created by the relevant scripts. Keep source data inside `data/` and generated reports inside `output/`.

---

# 🧠 Key Takeaways

```text
datetime
    ↓
Represent Dates and Times
    ↓
strftime()
    ↓
Format Date and Time Values
    ↓
strptime()
    ↓
Parse Date Strings
    ↓
timedelta
    ↓
Calculate Time Differences
    ↓
Unix Timestamps
    ↓
Process System and API Time Values
    ↓
UTC and Time Zones
    ↓
Correlate Events Reliably
```

The objective is not simply to display the current time. It is to process time-related data accurately and use it to make reliable operational decisions.

---

# 📊 Progress

**Stage:** `03-python-intermediate`

**Lesson:** `35 — Datetime`

**Status:** 🟡 Planned

### Previous Lessons

- ✅ 21 — Dataclasses
- ✅ 22 — Class Methods & Static Methods
- ✅ 23 — Inheritance & Polymorphism
- ✅ 24 — Multiple Inheritance & MRO
- ✅ 25 — Composition
- ✅ 26 — Abstract Base Classes & Interfaces
- ✅ 27 — Advanced Polymorphism & Design Patterns
- ✅ 28 — Exception Handling
- ✅ 29 — Regular Expressions
- ✅ 30 — JSON
- ✅ 31 — CSV
- ✅ 32 — XML
- ✅ 33 — YAML
- 🟡 34 — Logging (final challenge pending)

### Current Lesson

- 🟡 35 — Datetime (README prepared)

### Next Lessons

- ⬜ 36 — Collections
- ⬜ 37 — Itertools

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

Our focus remains on practical Python skills that support professional Network Engineering, Network Automation, monitoring, and troubleshooting.

