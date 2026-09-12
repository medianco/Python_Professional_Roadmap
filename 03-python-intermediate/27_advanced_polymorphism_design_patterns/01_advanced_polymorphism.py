"""
Lesson 27.1 - Advanced Polymorphism

This lesson demonstrates advanced polymorphism in Python
using a common interface and different implementations.

Focus:
- Polymorphism
- Method overriding
- Common interface
- Polymorphic functions
- Network Automation example
"""


from abc import ABC, abstractmethod


class NetworkDevice(ABC):
    """Define the common interface for network devices."""

    def __init__(self, hostname: str) -> None:
        self.hostname = hostname

    @abstractmethod
    def show_status(self) -> str:
        """Return the device status."""
        ...


class CiscoRouter(NetworkDevice):
    """Represent a Cisco router."""

    def show_status(self) -> str:
        return f"{self.hostname}: Cisco Router is UP"


class CiscoSwitch(NetworkDevice):
    """Represent a Cisco switch."""

    def show_status(self) -> str:
        return f"{self.hostname}: Cisco Switch is UP"


class JuniperRouter(NetworkDevice):
    """Represent a Juniper router."""

    def show_status(self) -> str:
        return f"{self.hostname}: Juniper Router is UP"


class JuniperSwitch(NetworkDevice):
    """Represent a Juniper switch."""

    def show_status(self) -> str:
        return f"{self.hostname}: Juniper Switch is UP"


def check_device(device: NetworkDevice) -> None:
    """Check any network device polymorphically."""
    print(device.show_status())


def main() -> None:
    """Create devices and demonstrate polymorphism."""

    devices: list[NetworkDevice] = [
        CiscoRouter("R1"),
        CiscoSwitch("SW1"),
        JuniperRouter("R2"),
        JuniperSwitch("SW2"),
    ]

    for device in devices:
        check_device(device)


if __name__ == "__main__":
    main()
