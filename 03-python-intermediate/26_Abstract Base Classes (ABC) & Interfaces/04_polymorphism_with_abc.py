"""
Lesson 26.4 - Polymorphism with ABC

This lesson demonstrates how Abstract Base Classes can be
combined with Polymorphism.

Different network devices implement the same interface,
but each device can provide its own behavior.
"""

from abc import ABC, abstractmethod


# ============================================================
# Abstract Base Class
# ============================================================

class NetworkDevice(ABC):
    """
    Common interface for all network devices.
    """

    @abstractmethod
    def connect(self):
        """Connect to the device."""
        pass

    @abstractmethod
    def show_status(self):
        """Display device status."""
        pass


# ============================================================
# Cisco Router
# ============================================================

class CiscoRouter(NetworkDevice):
    """Cisco router implementation."""

    def connect(self):
        print("Connecting to Cisco Router using SSH.")

    def show_status(self):
        print("Cisco Router: Routing services are UP.")


# ============================================================
# Cisco Switch
# ============================================================

class CiscoSwitch(NetworkDevice):
    """Cisco switch implementation."""

    def connect(self):
        print("Connecting to Cisco Switch using SSH.")

    def show_status(self):
        print("Cisco Switch: Switching services are UP.")


# ============================================================
# Juniper Router
# ============================================================

class JuniperRouter(NetworkDevice):
    """Juniper router implementation."""

    def connect(self):
        print("Connecting to Juniper Router using NETCONF.")

    def show_status(self):
        print("Juniper Router: Routing services are UP.")


# ============================================================
# Polymorphic Function
# ============================================================

def manage_device(device: NetworkDevice):
    """
    Manage any object that follows the NetworkDevice interface.

    This is Polymorphism:
    The same function can work with different device types.
    """

    device.connect()
    device.show_status()


# ============================================================
# Main Program
# ============================================================

if __name__ == "__main__":

    devices = [
        CiscoRouter(),
        CiscoSwitch(),
        JuniperRouter(),
    ]

    # The same function handles different device types.
    for device in devices:

        print("-" * 50)

        manage_device(device)
