"""
Lesson 34.1 — Introduction to Logging

This script introduces the Python logging module.

The goal is to understand the basic difference between
print() and logging.

In later lessons, we will build a more professional
logging architecture for Network Automation.
"""

import logging


# ---------------------------------------------------------
# 1. Basic logging configuration
# ---------------------------------------------------------

# basicConfig() provides a simple way to configure
# Python's logging system.
#
# level=logging.INFO means that INFO messages and
# more severe messages will be displayed.
logging.basicConfig(
    level=logging.INFO
)


# ---------------------------------------------------------
# 2. Simple console output with print()
# ---------------------------------------------------------

print("=== Using print() ===")

print("Starting Network Automation")
print("Connecting to R1")
print("Connection successful")


# ---------------------------------------------------------
# 3. Console output using Logging
# ---------------------------------------------------------

print("\n=== Using Logging ===")

# INFO represents a normal application event.
logging.info("Starting Network Automation")

# Another normal application event.
logging.info("Connecting to R1")

# Information about a successful operation.
logging.info("Connection successful")
