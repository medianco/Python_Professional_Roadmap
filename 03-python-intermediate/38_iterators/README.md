# Lesson 38 — Iterators

## 1. Overview

In Python, Iterators provide a mechanism for accessing elements one at a time without requiring the entire dataset to be processed or loaded into memory.

Iterators are fundamental to Python's iteration system and are widely used in:

- File processing
- Network monitoring
- Log analysis
- API pagination
- Large dataset processing
- Network device inventory management

This lesson explores how Iterators work internally, how to create custom Iterators, and how to apply them to practical Network Automation scenarios.

---

## 2. Learning Objectives

By the end of this lesson, you will be able to:

- Understand Iterable and Iterator objects.
- Differentiate between Iterable and Iterator.
- Use `iter()` and `next()`.
- Understand `StopIteration`.
- Explain the Iterator Protocol.
- Implement custom Iterator classes.
- Manage iterator state.
- Understand iterator exhaustion.
- Compare Iterators and Generators.
- Apply lazy evaluation.
- Build custom Iterators for Network Automation.

---

# 3. Understanding Iteration

## 3.1 What Is Iteration?

Iteration is the process of accessing elements from a collection one at a time.

For example:

```python
devices = ["R1", "R2", "SW1"]

for device in devices:
    print(device)
```

Output:

```text
R1
R2
SW1
```

The `for` loop retrieves each element automatically.

But what happens internally?

Python uses the Iterator Protocol to retrieve elements from the collection.

Conceptually:

```text
Iterable
    |
    v
  iter()
    |
    v
 Iterator
    |
    v
  next()
    |
    v
  Element
    |
    v
  next()
    |
    v
  Element
    |
    v
StopIteration
```

---

# 4. Iterable vs Iterator

## 4.1 What Is an Iterable?

An Iterable is an object that can return an Iterator.

Common examples include:

- Lists
- Tuples
- Dictionaries
- Sets
- Strings
- Files

Example:

```python
network_devices = ["R1", "R2", "SW1"]

device_iterator = iter(network_devices)
```

The list is an Iterable, and `iter()` creates an Iterator from it.

## 4.2 What Is an Iterator?

An Iterator is an object that produces values one at a time.

It maintains its current position and remembers which element should be returned next.

Example:

```python
devices = ["R1", "R2", "SW1"]

device_iterator = iter(devices)

print(next(device_iterator))
print(next(device_iterator))
print(next(device_iterator))
```

Output:

```text
R1
R2
SW1
```

## 4.3 Important Difference

| Iterable | Iterator |
|---|---|
| Can return an iterator | Produces values |
| Supports `iter()` | Supports `iter()` and `next()` |
| Usually can create multiple iterators | Maintains its own iteration state |
| Example: list | Example: `iter(list)` |

Important:

Every Iterator is an Iterable, but not every Iterable is an Iterator.

---

# 5. The iter() Function

The `iter()` function returns an Iterator from an Iterable.

Syntax:

```python
iterator = iter(iterable)
```

Example:

```python
devices = ("R1", "R2", "R3")

device_iterator = iter(devices)

print(type(devices))
print(type(device_iterator))
```

The first object is a tuple, while the second is an iterator.

### Network Automation Example

```python
network_inventory = [
    "Cisco-R1",
    "Cisco-R2",
    "Juniper-R1"
]

inventory_iterator = iter(network_inventory)

print(next(inventory_iterator))
```

Output:

```text
Cisco-R1
```

---

# 6. The next() Function

The `next()` function retrieves the next available value from an Iterator.

Syntax:

```python
next(iterator)
```

Example:

```python
devices = ["R1", "R2", "SW1"]

device_iterator = iter(devices)

first = next(device_iterator)
second = next(device_iterator)

print(first)
print(second)
```

Output:

```text
R1
R2
```

### Using a Default Value

You can provide a default value to avoid receiving a `StopIteration` exception when the iterator is exhausted.

```python
devices = ["R1", "R2"]

device_iterator = iter(devices)

print(next(device_iterator, "No more devices"))
print(next(device_iterator, "No more devices"))
print(next(device_iterator, "No more devices"))
```

Output:

```text
R1
R2
No more devices
```

---

# 7. StopIteration

`StopIteration` is a built-in exception that indicates that an Iterator has no more values.

Example:

```python
devices = ["R1", "R2"]

device_iterator = iter(devices)

print(next(device_iterator))
print(next(device_iterator))

print(next(device_iterator))
```

The third call raises:

```text
StopIteration
```

### Handling StopIteration

```python
devices = ["R1", "R2"]

device_iterator = iter(devices)

while True:

    try:
        device = next(device_iterator)
        print(device)

    except StopIteration:
        print("Inventory processing completed.")
        break
```

Output:

```text
R1
R2
Inventory processing completed.
```

### Important

A `for` loop handles `StopIteration` automatically.

You normally do not need to catch it manually when using a regular `for` loop.

---

# 8. Iterator Protocol

Python Iterators follow a protocol based on two special methods:

```python
__iter__()
__next__()
```

## 8.1 __iter__()

Returns the iterator object itself.

## 8.2 __next__()

Returns the next available value.

When no more values are available, it raises `StopIteration`.

Concept:

```text
             Iterator
                 |
        +--------+--------+
        |                 |
    __iter__()        __next__()
        |                 |
  Returns itself     Returns next value
                          |
                    No values left?
                          |
                          v
                    StopIteration
```

---

# 9. Creating Custom Iterators

Python allows developers to create their own Iterator classes.

Example:

```python
class DeviceIterator:

    def __init__(self, devices):
        self.devices = devices
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index >= len(self.devices):
            raise StopIteration

        device = self.devices[self.index]

        self.index += 1

        return device


devices = ["R1", "R2", "SW1"]

device_iterator = DeviceIterator(devices)

for device in device_iterator:
    print(device)
```

Output:

```text
R1
R2
SW1
```

### Understanding the Internal State

The iterator maintains an `index` attribute.

Each call to `next()` advances the index.

| Call | Index Before | Returned Value |
|---|---:|---|
| First | 0 | R1 |
| Second | 1 | R2 |
| Third | 2 | SW1 |
| Fourth | 3 | StopIteration |

This is the foundation of custom Iterator implementation.

---

# 10. Iterator State Management

An Iterator maintains its current position.

Example:

```python
devices = ["R1", "R2", "R3"]

iterator = iter(devices)

print(next(iterator))
print(next(iterator))
```

Output:

```text
R1
R2
```

The iterator remembers that two elements have already been consumed.

Calling `next()` again returns:

```text
R3
```

The iterator does not restart automatically.

### Important Concept

Two different iterators created from the same Iterable maintain independent states.

```python
devices = ["R1", "R2", "R3"]

iterator_a = iter(devices)
iterator_b = iter(devices)

print(next(iterator_a))
print(next(iterator_a))

print(next(iterator_b))
```

Output:

```text
R1
R2
R1
```

---

# 11. Iterator Exhaustion

An Iterator is exhausted when all its values have been consumed.

Example:

```python
devices = ["R1", "R2"]

iterator = iter(devices)

print(list(iterator))
print(list(iterator))
```

Output:

```text
['R1', 'R2']
[]
```

The second conversion returns an empty list because the iterator has already been consumed.

### How to Iterate Again

Create a new iterator from the original Iterable:

```python
devices = ["R1", "R2"]

iterator = iter(devices)

print(list(iterator))

iterator = iter(devices)

print(list(iterator))
```

Output:

```text
['R1', 'R2']
['R1', 'R2']
```

Remember:

An exhausted Iterator does not automatically reset.

---

# 12. Iterator vs Generator

Generators are a convenient way to create Iterators.

A custom Iterator normally uses a class with `__iter__()` and `__next__()`.

A Generator can be created using a function containing `yield`.

Example:

```python
def network_device_generator():

    devices = ["R1", "R2", "SW1"]

    for device in devices:
        yield device


device_generator = network_device_generator()

print(next(device_generator))
print(next(device_generator))
```

Output:

```text
R1
R2
```

Comparison:

| Feature | Custom Iterator | Generator |
|---|---|---|
| Implementation | Class | Function with `yield` |
| State management | Usually explicit | Managed automatically |
| Special methods | `__iter__`, `__next__` | Generated automatically |
| Complexity | More control | Less code |
| Best use | Custom iteration behavior | Sequential value production |

A Generator is a type of Iterator, but not every Iterator is a Generator.

We will study Generators in detail in Lesson 39.

---

# 13. Lazy Evaluation

Lazy Evaluation means producing values only when they are requested.

Instead of generating all values at once, an Iterator produces them one by one.

Example:

```python
def network_device_iterator():

    for number in range(1, 6):
        print(f"Preparing device R{number}")
        yield f"R{number}"


devices = network_device_iterator()

print("Requesting first device:")
print(next(devices))

print("Requesting second device:")
print(next(devices))
```

Output:

```text
Requesting first device:
Preparing device R1
R1
Requesting second device:
Preparing device R2
R2
```

Notice that Python only processes the requested values.

### Why Is Lazy Evaluation Useful?

Consider a network inventory containing 100,000 devices.

Loading and processing every device at once may consume unnecessary memory.

An Iterator can process devices sequentially.

Applications include:

- Large network inventories.
- Monitoring event streams.
- API pagination.
- Large log files.
- Streaming telemetry.

---

# 14. Network Automation Applications

Iterators are particularly useful in Network Automation.

## 14.1 Sequential Device Processing

Process devices one at a time instead of creating unnecessary intermediate collections.

## 14.2 Network Event Processing

Retrieve monitoring events sequentially.

## 14.3 Critical Event Filtering

Create an iterator that returns only critical events.

## 14.4 Device Inventory Iterator

Implement a custom Iterator that returns network devices according to a defined filtering rule.

## 14.5 Large Log Processing

Read log records sequentially without loading the entire file into memory.

---

# 15. Common Mistakes

### Mistake 1 — Calling next() on an Iterable Directly

Incorrect:

```python
devices = ["R1", "R2"]

print(next(devices))
```

Correct:

```python
devices = ["R1", "R2"]

device_iterator = iter(devices)

print(next(device_iterator))
```

### Mistake 2 — Reusing an Exhausted Iterator

An exhausted Iterator does not restart automatically.

Create a new iterator from the original Iterable.

### Mistake 3 — Incorrect Custom Iterator Implementation

A custom Iterator must implement the Iterator Protocol correctly.

- `__iter__()` returns the iterator.
- `__next__()` returns the next value.
- `__next__()` raises `StopIteration` when exhausted.

### Mistake 4 — Confusing Iterable and Iterator

A list is iterable, but a regular list is not itself an Iterator.

---

# 16. Best Practices

- Use built-in Iterators whenever possible.
- Use custom Iterator classes when you need explicit iteration behavior.
- Use Generators for simpler sequential value production.
- Avoid loading large datasets into memory unnecessarily.
- Handle file and data errors appropriately.
- Remember that Iterators can be exhausted.
- Keep iteration logic separate from business logic.
- Use meaningful names for custom Iterator classes.

---

# 17. Practical Exercises

### Exercise 1 — Basic Iterator

Create a list of network devices and retrieve each device using `iter()` and `next()`.

### Exercise 2 — StopIteration

Build a loop that processes an inventory until the Iterator is exhausted.

### Exercise 3 — Custom Iterator

Create a custom Iterator class that returns network devices sequentially.

### Exercise 4 — Iterator State

Create two independent Iterators from the same network inventory and demonstrate their independent states.

### Exercise 5 — Critical Event Iterator

Create an Iterator that returns only events with CRITICAL severity.

### Exercise 6 — Large Log Processing

Read a network log file sequentially without loading all records into memory.

---

# 18. Final Challenge — Network Monitoring Iterator

Build a Network Monitoring Iterator application.

Requirements:

- Load network devices from external JSON data.
- Load monitoring events from external JSON data.
- Implement a custom Iterator class.
- Support enabled-device filtering.
- Support critical-event filtering.
- Maintain the current iterator state.
- Handle iterator exhaustion.
- Demonstrate lazy processing.
- Generate a monitoring summary report.

The application should demonstrate a clear separation between:

```text
External Data
     |
     v
Data Loading
     |
     v
Custom Iterators
     |
     v
Filtering and Processing
     |
     v
Monitoring Report
```

---

# 19. Suggested Project Structure

```text
38_iterators/
│
├── README.md
│
├── data/
│   ├── network_devices.json
│   └── network_events.json
│
├── output/
│
├── 01_iterable_vs_iterator.py
├── 02_iter_and_next.py
├── 03_stop_iteration.py
├── 04_iterator_protocol.py
├── 05_custom_iterator_class.py
├── 06_network_device_iterator.py
├── 07_iterator_state_management.py
├── 08_iterator_exhaustion.py
├── 09_iterator_vs_generator.py
├── 10_lazy_evaluation.py
├── 11_network_automation_iterators.py
│
└── challenge/
    └── network_monitoring_iterator.py
```

---

# 20. Key Takeaways

```text
Iterable
   |
   v
iter()
   |
   v
Iterator
   |
   v
next()
   |
   v
Next Element
   |
   v
Iterator Protocol
   |
   v
Custom Iterators
   |
   v
State Management
   |
   v
Lazy Evaluation
   |
   v
Efficient Network Automation
```

The most important idea:

**An Iterator allows Python to process data one element at a time while maintaining its current state.**

Understanding Iterators is essential before moving to Generators, asynchronous iteration, and advanced data-processing pipelines.

---

# 21. Learning Progress

**Stage:** `03-python-intermediate`

**Lesson:** `38 — Iterators`

**Status:** In Progress

### Previous Lessons

- Lesson 21 — Dataclasses
- Lesson 22 — Class Methods & Static Methods
- Lesson 23 — Inheritance & Polymorphism
- Lesson 24 — Multiple Inheritance & MRO
- Lesson 25 — Composition
- Lesson 26 — Abstract Base Classes & Interfaces
- Lesson 27 — Advanced Polymorphism & Design Patterns
- Lesson 28 — Exception Handling
- Lesson 29 — Regular Expressions
- Lesson 30 — JSON
- Lesson 31 — CSV
- Lesson 32 — XML
- Lesson 33 — YAML
- Lesson 34 — Logging
- Lesson 35 — Datetime
- Lesson 36 — Collections
- Lesson 37 — Itertools

### Current Lesson

- Lesson 38 — Iterators

### Next Lesson

- Lesson 39 — Generators

---

# Learning Philosophy

Learn → Understand → Code → Test → Apply → Document → Publish → Prove Your Skills

The objective is to develop practical Python engineering skills that can be applied to professional Network Automation systems.
