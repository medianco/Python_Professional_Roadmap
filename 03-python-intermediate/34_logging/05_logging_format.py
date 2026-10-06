"""
Lesson 34.5 — Logging Format

This script demonstrates how to customize the format
of logging messages.

A professional logging format should make it easy to
answer four important questions:

1. When did the event happen?
2. How serious is the event?
3. Which component generated the event?
4. What happened?

Example:

2026-10-06 11:20:15 | ERROR | network_automation |
Failed to connect to R1
"""

import logging


# ---------------------------------------------------------
# 1. Create a custom Logger
# ---------------------------------------------------------
# Using a meaningful logger name is useful in larger
# applications because multiple modules may generate logs.

logger = logging.getLogger("network_automation")


# ---------------------------------------------------------
# 2. Set Logger Level
# ---------------------------------------------------------
# DEBUG allows all standard logging levels to pass
# through the logger.

logger.setLevel(logging.DEBUG)


# ---------------------------------------------------------
# 3. Create a Console Handler
# ---------------------------------------------------------
# StreamHandler sends log messages to the terminal.

console_handler = logging.StreamHandler()


# ---------------------------------------------------------
# 4. Set Handler Level
# ---------------------------------------------------------
# The handler will display DEBUG and higher messages.

console_handler.setLevel(logging.DEBUG)


# ---------------------------------------------------------
# 5. Define a Custom Log Format
# ---------------------------------------------------------
#
# %(asctime)s
#     Date and time of the event.
#
# %(levelname)s
#     Severity level of the event.
#
# %(name)s
#     Name of the logger that generated the event.
#
# %(message)s
#     Actual log message.

log_format = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(message)s"
)


# ---------------------------------------------------------
# 6. Create the Formatter
# ---------------------------------------------------------

formatter = logging.Formatter(
    log_format
)


# ---------------------------------------------------------
# 7. Attach Formatter to Handler
# ---------------------------------------------------------

console_handler.setFormatter(formatter)


# ---------------------------------------------------------
# 8. Attach Handler to Logger
# ---------------------------------------------------------

logger.addHandler(console_handler)


# ---------------------------------------------------------
# 9. Generate Network Automation Events
# ---------------------------------------------------------

logger.debug(
    "Preparing SSH connection to R1"
)

logger.info(
    "Connecting to R1 at 192.168.1.1"
)

logger.info(
    "SSH connection established successfully"
)

logger.warning(
    "R1 response time is higher than expected"
)

logger.error(
    "Failed to execute configuration command on R1"
)

logger.critical(
    "Network Automation system cannot continue"
)
