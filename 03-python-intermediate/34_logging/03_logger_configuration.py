"""
Lesson 34.3 — Logger Configuration

This script demonstrates how to create and configure
a custom Logger for a Network Automation application.

We will configure:

1. Logger
2. Logging Level
3. Handler
4. Formatter

The goal is to move from the default root logger
to a more professional logging architecture.

    logger.info(...)
           │
           ▼
        Logger
           │
           ▼
        Handler
           │
           ▼
       Formatter
           │
           ▼
        Terminal
"""

import logging


# ---------------------------------------------------------
# 1. Create a custom Logger
# ---------------------------------------------------------
# __name__ gives the logger the name of the current module.
# This is a common and recommended practice in Python
# applications.

logger = logging.getLogger(__name__)


# ---------------------------------------------------------
# 2. Configure the Logger Level
# ---------------------------------------------------------
# DEBUG is the lowest standard logging level.
#
# Therefore, the logger will allow:
#
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

logger.setLevel(logging.DEBUG)


# ---------------------------------------------------------
# 3. Create a Handler
# ---------------------------------------------------------
# StreamHandler sends log messages to the terminal
# (console).

console_handler = logging.StreamHandler()


# ---------------------------------------------------------
# 4. Configure the Handler Level
# ---------------------------------------------------------
# console_handler.setLevel(logging.WARNING)
# Logger
#  │
#  ├── DEBUG ──┐
#  ├── INFO  ──┤
#  ├── WARNING ───────► Handler ──► Terminal
#  ├── ERROR   ───────► Handler ──► Terminal
#  └── CRITICAL ──────► Handler ──► Terminal
#
# The handler will also accept DEBUG and higher messages.

console_handler.setLevel(logging.DEBUG)


# ---------------------------------------------------------
# 5. Create a Formatter
# ---------------------------------------------------------
# The formatter controls how each log message appears.
#
# %(asctime)s  -> Date and time
# %(levelname)s -> Logging level
# %(name)s     -> Logger name
# %(message)s  -> Actual log message

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)


# ---------------------------------------------------------
# 6. Attach the Formatter to the Handler
# ---------------------------------------------------------

console_handler.setFormatter(formatter)


# ---------------------------------------------------------
# 7. Attach the Handler to the Logger
# ---------------------------------------------------------

logger.addHandler(console_handler)


# ---------------------------------------------------------
# 8. Generate Log Messages
# ---------------------------------------------------------
# We now use our custom logger instead of the root logger.

logger.debug(
    "Preparing connection to R1"
)

logger.info(
    "Connecting to R1 at 192.168.1.1"
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
