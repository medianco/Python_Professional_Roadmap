"""
Lesson 26.1 - ABC Basics

This lesson introduces Abstract Base Classes (ABC) in Python.

Key concepts:
- ABC
- Abstract Base Class
- Inheritance
- Common interface
"""

from abc import ABC


# ============================================================
# Abstract Base Class
# ============================================================

class NetworkDevice(ABC):
    """
    NetworkDevice is an Abstract Base Class.

    ABC allows us to define a common base class that can be
    extended by different types of network devices.
    """

    def device_info(self):
        """Display basic information about the network device."""
        print("This is a network device.")


# ============================================================
# Concrete Class - Router
# ============================================================

class Router(NetworkDevice):
    """Represents a network router."""

    def routing(self):
        """Display a routing message."""
        print("Router is performing routing.")


# ============================================================
# Concrete Class - Switch
# ============================================================

class Switch(NetworkDevice):
    """Represents a network switch."""

    def switching(self):
        """Display a switching message."""
        print("Switch is performing switching.")


# ============================================================
# Main Program
# ============================================================

if __name__ == "__main__":

    router = Router()
    switch = Switch()

    # Both classes inherit from NetworkDevice.
    router.device_info()
    router.routing()

    print()

    switch.device_info()
    switch.switching()
