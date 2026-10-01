"""
Lesson 34.2 — Logging Levels

This script demonstrates the standard Python logging levels:

DEBUG
INFO
WARNING
ERROR
CRITICAL

Each level represents a different severity of an event.

The example uses a Network Automation scenario so that
the logging levels can be understood in a practical context.
"""

import logging


# ---------------------------------------------------------
# 1. Configure the logging system
# ---------------------------------------------------------

# DEBUG is the lowest standard logging level.
#
# By setting the logging level to DEBUG, we allow
# all standard logging messages to be displayed.
logging.basicConfig(
    level=logging.DEBUG
)


# ---------------------------------------------------------
# 2. DEBUG
# ---------------------------------------------------------

# DEBUG is used for detailed diagnostic information.
#
# Example:
# We may want to know which IP address the automation
# system is about to use for a connection.
logging.debug(
    "Preparing connection to R1 at 192.168.1.1"
)


# ---------------------------------------------------------
# 3. INFO
# ---------------------------------------------------------

# INFO represents normal application events.
logging.info(
    "Starting connection to R1"
)


# ---------------------------------------------------------
# 4. WARNING
# ---------------------------------------------------------

# WARNING indicates that something unexpected happened,
# but the application can still continue.
logging.warning(
    "R1 response time is higher than expected"
)


# ---------------------------------------------------------
# 5. ERROR
# ---------------------------------------------------------

# ERROR indicates that an operation failed.
logging.error(
    "Failed to execute configuration command on R1"
)


# ---------------------------------------------------------
# 6. CRITICAL
# ---------------------------------------------------------

# CRITICAL represents a very serious failure.
#
# In a real automation platform, this could indicate
# that the application cannot continue safely.
logging.critical(
    "Network Automation system cannot continue"
)
