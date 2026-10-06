"""
Lesson 34.4 — Logging to File

This script demonstrates how to write logging messages
to a file using logging.FileHandler.

Network Automation applications should normally keep
persistent logs so that engineers can investigate:

- Connection failures
- Configuration errors
- Device events
- Automation activity
- Troubleshooting information

The log file will be created inside:

output/application.log
"""

import logging


# ---------------------------------------------------------
# 1. Create a custom Logger
# ---------------------------------------------------------
# __name__ identifies the current module.
# Using a module-specific logger is a common practice
# in professional Python applications.

logger = logging.getLogger(__name__)


# ---------------------------------------------------------
# 2. Set the Logger Level
# ---------------------------------------------------------
# DEBUG is the lowest standard logging level.
# Therefore, the logger accepts all standard levels.

logger.setLevel(logging.DEBUG)


# ---------------------------------------------------------
# 3. Create a File Handler
# ---------------------------------------------------------
# FileHandler sends logging messages to a file instead
# of displaying them only on the terminal.
#
# The file will be created automatically if it does
# not already exist.

file_handler = logging.FileHandler(
    "output/application.log"
)


# ---------------------------------------------------------
# 4. Set the Handler Level
# ---------------------------------------------------------
# The FileHandler will store DEBUG and higher messages.

file_handler.setLevel(logging.DEBUG)


# ---------------------------------------------------------
# 5. Create a Formatter
# ---------------------------------------------------------
# The formatter defines the structure of every log entry.
#
# %(asctime)s  -> Date and time
# %(levelname)s -> Logging level
# %(name)s     -> Logger name
# %(message)s  -> Actual message

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)


# ---------------------------------------------------------
# 6. Attach the Formatter to the File Handler
# ---------------------------------------------------------

file_handler.setFormatter(formatter)


# ---------------------------------------------------------
# 7. Attach the File Handler to the Logger
# ---------------------------------------------------------

logger.addHandler(file_handler)


# ---------------------------------------------------------
# 8. Generate Network Automation Log Messages
# ---------------------------------------------------------

logger.debug(
    "Preparing connection to R1"
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
