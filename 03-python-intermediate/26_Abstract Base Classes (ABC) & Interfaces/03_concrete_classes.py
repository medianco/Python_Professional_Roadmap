"""
Lesson 26.3 - Concrete Classes

This lesson explains the relationship between:
- Abstract Base Classes
- Abstract methods
- Concrete classes

A concrete class provides implementations for all required
abstract methods.
"""

from abc import ABC, abstractmethod


# ============================================================
# Abstract Base Class
# ============================================================

class NetworkDevice(ABC):
    """
    Base class for all network devices.

    The class defines the required behavior that every
    network device must implement.
    """

    @abstractmethod
    def connect(self):
        """Connect to the network device."""
        pass

    @abstractmethod
    def show_status(self):
        """Display the device status."""
        pass


# ============================================================
# Cisco Router
# ============================================================

class CiscoRouter(NetworkDevice):
    """
    Concrete class representing a Cisco router.

    It implements all abstract methods defined by
    NetworkDevice.
    """

    def connect(self):
        """Connect to the Cisco router."""
        print("Connected to Cisco Router.")

    def show_status(self):
        """Display Cisco router status."""
        print("Cisco Router status: UP")


# ============================================================
# Cisco Switch
# ============================================================

class CiscoSwitch(NetworkDevice):
    """
    Concrete class representing a Cisco switch.

    It implements all abstract methods defined by
    NetworkDevice.
    """

    def connect(self):
        """Connect to the Cisco switch."""
        print("Connected to Cisco Switch.")

    def show_status(self):
        """Display Cisco switch status."""
        print("Cisco Switch status: UP")


# ============================================================
# Main Program
# ============================================================

if __name__ == "__main__":

    router = CiscoRouter()
    switch = CiscoSwitch()

    router.connect()
    router.show_status()

    print()

    switch.connect()
    switch.show_status()
