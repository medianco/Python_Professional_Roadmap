"""
Lesson 26.5 - ABC Network Devices

Final practical example for Lesson 26.

This project combines:
- Abstract Base Classes
- Abstract methods
- Concrete classes
- Inheritance
- Polymorphism

Network devices:
- Cisco Router
- Cisco Switch
- Juniper Router
- Juniper Switch
"""

from abc import ABC, abstractmethod


# ============================================================
# Abstract Base Class
# ============================================================

class NetworkDevice(ABC):
    """
    Abstract Base Class representing a generic network device.

    Every network device must implement:
    - connect()
    - configure()
    - show_status()
    """

    def __init__(self, hostname, management_ip):
        """
        Initialize common device information.

        Args:
            hostname (str): Device hostname.
            management_ip (str): Management IP address.
        """

        self.hostname = hostname
        self.management_ip = management_ip

    @abstractmethod
    def connect(self):
        """Connect to the network device."""
        pass

    @abstractmethod
    def configure(self):
        """Configure the network device."""
        pass

    @abstractmethod
    def show_status(self):
        """Display device status."""
        pass

    def device_info(self):
        """
        Display common information.

        This is a normal concrete method because its behavior
        is the same for all devices.
        """

        print(f"Hostname: {self.hostname}")
        print(f"Management IP: {self.management_ip}")


# ============================================================
# Cisco Router
# ============================================================

class CiscoRouter(NetworkDevice):
    """Concrete implementation of a Cisco Router."""

    def connect(self):
        print(f"{self.hostname}: Connecting using SSH.")

    def configure(self):
        print(f"{self.hostname}: Applying Cisco IOS configuration.")

    def show_status(self):
        print(f"{self.hostname}: Cisco Router status is UP.")


# ============================================================
# Cisco Switch
# ============================================================

class CiscoSwitch(NetworkDevice):
    """Concrete implementation of a Cisco Switch."""

    def connect(self):
        print(f"{self.hostname}: Connecting using SSH.")

    def configure(self):
        print(f"{self.hostname}: Applying Cisco IOS switch configuration.")

    def show_status(self):
        print(f"{self.hostname}: Cisco Switch status is UP.")


# ============================================================
# Juniper Router
# ============================================================

class JuniperRouter(NetworkDevice):
    """Concrete implementation of a Juniper Router."""

    def connect(self):
        print(f"{self.hostname}: Connecting using NETCONF.")

    def configure(self):
        print(f"{self.hostname}: Applying Junos configuration.")

    def show_status(self):
        print(f"{self.hostname}: Juniper Router status is UP.")


# ============================================================
# Juniper Switch
# ============================================================

class JuniperSwitch(NetworkDevice):
    """Concrete implementation of a Juniper Switch."""

    def connect(self):
        print(f"{self.hostname}: Connecting using NETCONF.")

    def configure(self):
        print(f"{self.hostname}: Applying Junos switch configuration.")

    def show_status(self):
        print(f"{self.hostname}: Juniper Switch status is UP.")


# ============================================================
# Device Management Function
# ============================================================

def manage_device(device: NetworkDevice):
    """
    Manage a network device using the common interface.

    The function does not need to know whether the device is:
    - Cisco Router
    - Cisco Switch
    - Juniper Router
    - Juniper Switch

    This is the practical use of Polymorphism.
    """

    print("=" * 60)

    device.device_info()
    device.connect()
    device.configure()
    device.show_status()


# ============================================================
# Main Program
# ============================================================

if __name__ == "__main__":

    # Create concrete network devices.
    devices = [
        CiscoRouter("R1-CISCO", "192.168.1.1"),
        CiscoSwitch("SW1-CISCO", "192.168.1.10"),
        JuniperRouter("R2-JUNIPER", "192.168.1.2"),
        JuniperSwitch("SW2-JUNIPER", "192.168.1.20"),
    ]

    # Manage all devices through the same interface.
    for device in devices:
        manage_device(device)
