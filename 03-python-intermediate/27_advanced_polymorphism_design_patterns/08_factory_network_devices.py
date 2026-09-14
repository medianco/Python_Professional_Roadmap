"""
Lesson 27.9 - Factory Pattern + Network Automation

This lesson combines several Python concepts:

- Abstract Base Classes (ABC)
- Protocol
- Polymorphism
- Composition
- Dependency Injection
- Factory Pattern

Goal:

Create different network devices through a Factory
while keeping the application loosely coupled.

Architecture:

                    DeviceFactory
                         |
                  create_device()
                         |
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
    CiscoRouter     CiscoSwitch    JuniperRouter
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                  NetworkDevice
                         │
                         │ HAS-A
                         ↓
                ConnectionStrategy
                         │
               ┌─────────┼─────────┐
               ↓         ↓         ↓
              SSH       API      NETCONF
"""


from abc import ABC, abstractmethod
from typing import Protocol


# ============================================================
# 1. Connection Protocol
# ============================================================

class ConnectionStrategy(Protocol):
    """
    Define the required connection behavior.

    Any connection implementation must provide:
    - connect()
    - disconnect()
    """

    def connect(self) -> str:
        """Establish a connection."""
        ...

    def disconnect(self) -> str:
        """Close a connection."""
        ...


# ============================================================
# 2. Connection Implementations
# ============================================================

class SSHConnection:
    """Implement network connectivity using SSH."""

    def connect(self) -> str:
        """Establish an SSH connection."""
        return "SSH connection established"

    def disconnect(self) -> str:
        """Close the SSH connection."""
        return "SSH connection closed"


class APIConnection:
    """Implement network connectivity using an API."""

    def connect(self) -> str:
        """Establish an API connection."""
        return "API connection established"

    def disconnect(self) -> str:
        """Close the API connection."""
        return "API connection closed"


class NETCONFConnection:
    """Implement network connectivity using NETCONF."""

    def connect(self) -> str:
        """Establish a NETCONF connection."""
        return "NETCONF connection established"

    def disconnect(self) -> str:
        """Close the NETCONF connection."""
        return "NETCONF connection closed"


# ============================================================
# 3. Abstract Network Device
# ============================================================

class NetworkDevice(ABC):
    """
    Abstract base class for network devices.

    The device receives its connection strategy
    through Dependency Injection.
    """

    def __init__(
        self,
        hostname: str,
        connection: ConnectionStrategy,
    ) -> None:
        """Initialize the network device."""

        self.hostname = hostname
        self.connection = connection

    def connect(self) -> str:
        """Connect to the network device."""
        return self.connection.connect()

    def disconnect(self) -> str:
        """Disconnect from the network device."""
        return self.connection.disconnect()

    @abstractmethod
    def show_status(self) -> str:
        """Return the device status."""
        ...


# ============================================================
# 4. Cisco Router
# ============================================================

class CiscoRouter(NetworkDevice):
    """Represent a Cisco router."""

    def show_status(self) -> str:
        """Return Cisco router status."""
        return f"{self.hostname}: Cisco Router is UP"


# ============================================================
# 5. Cisco Switch
# ============================================================

class CiscoSwitch(NetworkDevice):
    """Represent a Cisco switch."""

    def show_status(self) -> str:
        """Return Cisco switch status."""
        return f"{self.hostname}: Cisco Switch is UP"


# ============================================================
# 6. Juniper Router
# ============================================================

class JuniperRouter(NetworkDevice):
    """Represent a Juniper router."""

    def show_status(self) -> str:
        """Return Juniper router status."""
        return f"{self.hostname}: Juniper Router is UP"


# ============================================================
# 7. Juniper Switch
# ============================================================

class JuniperSwitch(NetworkDevice):
    """Represent a Juniper switch."""

    def show_status(self) -> str:
        """Return Juniper switch status."""
        return f"{self.hostname}: Juniper Switch is UP"


# ============================================================
# 8. Device Factory
# ============================================================

class DeviceFactory:
    """
    Create network devices.

    The Factory is responsible for object creation.

    The caller does not need to know how each
    device object is constructed.
    """

    @staticmethod
    def create_device(
        device_type: str,
        hostname: str,
        connection: ConnectionStrategy,
    ) -> NetworkDevice:
        """
        Create a network device based on its type.

        Args:
            device_type: Type of network device.
            hostname: Device hostname.
            connection: Connection strategy.

        Returns:
            A NetworkDevice object.

        Raises:
            ValueError: If the device type is unsupported.
        """

        if device_type == "cisco_router":
            return CiscoRouter(hostname, connection)

        if device_type == "cisco_switch":
            return CiscoSwitch(hostname, connection)

        if device_type == "juniper_router":
            return JuniperRouter(hostname, connection)

        if device_type == "juniper_switch":
            return JuniperSwitch(hostname, connection)

        raise ValueError(
            f"Unsupported device type: {device_type}"
        )


# ============================================================
# 9. Network Device Manager
# ============================================================

class NetworkDeviceManager:
    """
    Manage network devices polymorphically.

    The manager does not care about the concrete
    device type or connection type.
    """

    def check_device(self, device: NetworkDevice) -> None:
        """Check the status of a network device."""

        print(f"Device: {device.hostname}")
        print(device.connect())
        print(device.show_status())
        print(device.disconnect())


# ============================================================
# 10. Main
# ============================================================

def main() -> None:
    """Demonstrate Factory Pattern in Network Automation."""

    # --------------------------------------------------------
    # Create connection strategies.
    # --------------------------------------------------------

    ssh = SSHConnection()
    api = APIConnection()
    netconf = NETCONFConnection()

    # --------------------------------------------------------
    # Create devices through the Factory.
    # --------------------------------------------------------

    router_1 = DeviceFactory.create_device(
        "cisco_router",
        "R1",
        ssh,
    )

    switch_1 = DeviceFactory.create_device(
        "cisco_switch",
        "SW1",
        api,
    )

    router_2 = DeviceFactory.create_device(
        "juniper_router",
        "R2",
        netconf,
    )

    switch_2 = DeviceFactory.create_device(
        "juniper_switch",
        "SW2",
        ssh,
    )

    # --------------------------------------------------------
    # Store all devices in one list.
    #
    # This demonstrates polymorphism.
    # --------------------------------------------------------

    devices: list[NetworkDevice] = [
        router_1,
        switch_1,
        router_2,
        switch_2,
    ]

    # --------------------------------------------------------
    # Create the manager.
    # --------------------------------------------------------

    manager = NetworkDeviceManager()

    # --------------------------------------------------------
    # Manage all devices polymorphically.
    # --------------------------------------------------------

    for device in devices:
        manager.check_device(device)
        print("=" * 40)


if __name__ == "__main__":
    main()
