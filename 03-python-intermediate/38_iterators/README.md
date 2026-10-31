# Lesson 38 — Iterators

## Overview

This lesson explores Python Iterators and the Iterator Protocol.

It builds on the concepts introduced in Lesson 37 — Itertools
and focuses on understanding how Python processes sequences
one element at a time.

The lesson emphasizes practical applications in Network Automation,
including device inventory processing, network event monitoring,
and efficient data handling.

## Learning Objectives

By the end of this lesson, you will be able to:

- Understand Iterable and Iterator objects.
- Use iter() and next().
- Understand StopIteration.
- Explain the Iterator Protocol.
- Implement custom iterator classes.
- Manage iterator state.
- Understand iterator exhaustion.
- Compare Iterators and Generators.
- Apply lazy evaluation.
- Build network automation iterators.

## Lesson Roadmap

### 38.1 Iterable vs Iterator
Understand the difference between iterable and iterator objects.

### 38.2 iter() and next()
Create iterators and retrieve values manually.

### 38.3 StopIteration
Understand how Python signals the end of iteration.

### 38.4 Iterator Protocol
Explore __iter__() and __next__().

### 38.5 Custom Iterator Classes
Implement custom iterator objects.

### 38.6 Network Device Iterator
Build an iterator for network device inventory.

### 38.7 Iterator State Management
Understand how iterators maintain their current position.

### 38.8 Iterator Exhaustion
Understand why exhausted iterators cannot be reused directly.

### 38.9 Iterator vs Generator
Compare their implementation, behavior, and use cases.

### 38.10 Lazy Evaluation
Process large datasets efficiently.

### 38.11 Network Automation with Iterators
Combine iterator concepts in a practical application.

## Project Structure

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
