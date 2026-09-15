"""
Lesson 27.12 - SOLID Design Principles

This lesson demonstrates the SOLID principles
using a Network Automation example.

SOLID:

S - Single Responsibility Principle
O - Open/Closed Principle
L - Liskov Substitution Principle
I - Interface Segregation Principle
D - Dependency Inversion Principle
"""

from abc import ABC, abstractmethod
from typing import Protocol


# ============================================================
# S - Single Responsibility Principle
# ============================================================

class Logger:
    """
    Responsible only for logging messages.
    """

    def log(self, message: str) -> None:
        """Write a log message."""

        print(f"[LOG] {message}")


class ConfigurationManager:
    """
    Responsible only for device configuration.
    """

    def configure(self, hostname: str) -> str:
        """Configure a network device."""

        return f"{hostname}: configuration applied"


# ============================================================
# I - Interface Segregation Principle
# ============================================================

class Connection(Protocol):
    """
    Small interface for network connectivity.

    The interface contains only the operations
    required for a connection.
    """

    def connect(self) -> str:
        """Establish a connection."""
        ...

    def disconnect(self) -> str:
        """Close a connection."""
        ...


# ============================================================
# D - Dependency Inversion Principle
# ============================================================

class SSHConnection:
    """
    Concrete implementation of Connection.
    """

    def connect(self) -> str:
        """Establish an SSH connection."""

        return "SSH connection established"

    def disconnect(self) -> str:
        """Close the SSH connection."""

        return "SSH connection closed"


class APIConnection:
    """
    Concrete implementation of Connection.
    """

    def connect(self) -> str:
        """Establish an API connection."""

        return "API connection established"

    def disconnect(self) -> str:
        """Close the API connection."""

        return "API connection closed"


# ============================================================
# L - Liskov Substitution Principle
# ============================================================

class NetworkDevice(ABC):
    """
    Abstract base class for network devices.

    Every concrete device must implement
    show_status().
    """

    def __init__(
        self,
        hostname: str,
        connection: Connection,
    ) -> None:
        """Initialize the network device."""

        self.hostname = hostname

        # Dependency Injection:
        # The connection is provided from outside.
        self.connection = connection

    def connect(self) -> str:
        """Connect to the device."""

        return self.connection.connect()

    def disconnect(self) -> str:
        """Disconnect from the device."""

        return self.connection.disconnect()

    @abstractmethod
    def show_status(self) -> str:
        """Return device status."""
        ...


class CiscoRouter(NetworkDevice):
    """Represent a Cisco router."""

    def show_status(self) -> str:
        """Return Cisco router status."""

        return f"{self.hostname}: Cisco Router is UP"


class JuniperRouter(NetworkDevice):
    """Represent a Juniper router."""

    def show_status(self) -> str:
        """Return Juniper router status."""

        return f"{self.hostname}: Juniper Router is UP"


# ============================================================
# O - Open/Closed Principle
# ============================================================

class AristaRouter(NetworkDevice):
    """
    Represent an Arista router.

    We add a new device type without modifying
    NetworkDevice.
    """

    def show_status(self) -> str:
        """Return Arista router status."""

        return f"{self.hostname}: Arista Router is UP"


# ============================================================
# Network Device Manager
# ============================================================

class NetworkDeviceManager:
    """
    Manage network devices.

    The manager depends on the abstraction
    NetworkDevice rather than concrete classes.
    """

    def __init__(
        self,
        logger: Logger,
        configuration: ConfigurationManager,
    ) -> None:
        """
        Initialize the manager.

        Dependencies are injected from outside.
        """

        self.logger = logger
        self.configuration = configuration

    def check_device(
        self,
        device: NetworkDevice,
    ) -> None:
        """Check a network device."""

        self.logger.log(
            f"Checking device {device.hostname}"
        )

        print(device.connect())
        print(device.show_status())
        print(
            self.configuration.configure(
                device.hostname
            )
        )
        print(device.disconnect())


# ============================================================
# Main
# ============================================================

def main() -> None:
    """Demonstrate the SOLID principles."""

    # --------------------------------------------------------
    # Create dependencies.
    # --------------------------------------------------------

    logger = Logger()
    configuration = ConfigurationManager()

    ssh = SSHConnection()
    api = APIConnection()

    # --------------------------------------------------------
    # Dependency Injection
    # --------------------------------------------------------

    router_1 = CiscoRouter(
        "R1",
        ssh,
    )

    router_2 = JuniperRouter(
        "R2",
        api,
    )

    router_3 = AristaRouter(
        "R3",
        ssh,
    )

    # --------------------------------------------------------
    # Polymorphism
    #
    # All concrete devices can be treated as
    # NetworkDevice objects.
    # --------------------------------------------------------

    devices: list[NetworkDevice] = [
        router_1,
        router_2,
        router_3,
    ]

    # --------------------------------------------------------
    # Create manager with injected dependencies.
    # --------------------------------------------------------

    manager = NetworkDeviceManager(
        logger,
        configuration,
    )

    # --------------------------------------------------------
    # Process devices.
    # --------------------------------------------------------

    for device in devices:
        manager.check_device(device)
        print("=" * 50)


if __name__ == "__main__":
    main()
