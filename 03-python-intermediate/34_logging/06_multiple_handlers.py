"""
Lesson 34.6 — Multiple Handlers

This script demonstrates how a single Logger can use
multiple Handlers.

We will configure:

1. ConsoleHandler -> Terminal
2. FileHandler    -> multiple_handlers.log

The same logging event will therefore be sent to
both destinations.

                    Logger
                 DEBUG Level
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
   ConsoleHandler          FileHandler
       INFO                  DEBUG
          │                     │
          ▼                     ▼
      Terminal             multiple_handlers.log
"""

import logging


# ---------------------------------------------------------
# 1. Create the Logger
# ---------------------------------------------------------
# A named logger makes the application easier to
# understand when multiple modules are involved.

logger = logging.getLogger("network_automation")


# ---------------------------------------------------------
# 2. Configure the Logger Level
# ---------------------------------------------------------
# DEBUG is the lowest standard logging level.
# Therefore, the logger accepts all standard levels.

logger.setLevel(logging.DEBUG)


# =========================================================
# CONSOLE HANDLER
# =========================================================

# ---------------------------------------------------------
# 3. Create Console Handler
# ---------------------------------------------------------
# StreamHandler sends log records to the terminal.

console_handler = logging.StreamHandler()


# ---------------------------------------------------------
# 4. Configure Console Handler Level
# ---------------------------------------------------------
# The terminal will display INFO and higher messages.
#
# This means DEBUG messages will NOT appear on the
# terminal.

console_handler.setLevel(logging.INFO)


# ---------------------------------------------------------
# 5. Create Console Formatter
# ---------------------------------------------------------
console_formatter = logging.Formatter(
    "%(levelname)s | %(name)s | %(message)s"
)


# ---------------------------------------------------------
# 6. Attach Formatter to Console Handler
# ---------------------------------------------------------

console_handler.setFormatter(
    console_formatter
)


# =========================================================
# FILE HANDLER
# =========================================================

# ---------------------------------------------------------
# 7. Create File Handler
# ---------------------------------------------------------
# FileHandler writes log records to a persistent file.

file_handler = logging.FileHandler(
    "output/multiple_handlers.log"
)


# ---------------------------------------------------------
# 8. Configure File Handler Level
# ---------------------------------------------------------
# The file will store DEBUG and higher messages.

file_handler.setLevel(logging.DEBUG)


# ---------------------------------------------------------
# 9. Create File Formatter
# ---------------------------------------------------------
# The file receives a more detailed format including
# the timestamp.

file_formatter = logging.Formatter(
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(message)s"
)


# ---------------------------------------------------------
# 10. Attach Formatter to File Handler
# ---------------------------------------------------------

file_handler.setFormatter(
    file_formatter
)


# =========================================================
# CONNECT HANDLERS TO LOGGER
# =========================================================

# ---------------------------------------------------------
# 11. Add Console Handler
# ---------------------------------------------------------

logger.addHandler(
    console_handler
)


# ---------------------------------------------------------
# 12. Add File Handler
# ---------------------------------------------------------

logger.addHandler(
    file_handler
)


# =========================================================
# GENERATE LOG EVENTS
# =========================================================

logger.debug(
    "Preparing SSH connection to R1"
)

logger.info(
    "Connecting to R1 at 192.168.1.1"
)

logger.info(
    "Connection to R1 established successfully"
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
