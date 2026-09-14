"""
Lesson 27.10 - Combining Strategy + Factory

This lesson combines:

- Strategy Pattern
- Factory Pattern
- Protocol
- Abstract Base Class (ABC)
- Composition
- Dependency Injection
- Polymorphism

Goal:

Create network devices and their connection strategies
through a single Factory.

Example:

    DeviceFactory.create_device(
        "cisco_router",
        "R1",
        "ssh",
    )

Architecture:

                    DeviceFactory
                         |
              ┌──────────┴──────────┐
              ↓                     ↓
        Device Creation       Strategy Creation
              │                     │
              ↓                     ↓
       NetworkDevice          ConnectionStrategy
              │                     │
       ┌──────┼──────┐       ┌──────┼──────┐
       ↓      ↓      ↓       ↓      ↓      ↓
     Cisco  Juniper  ...     SSH    API   NETCONF
"""


from abc import ABC, abstractmethod
from typing import Protocol


# ============================================================
# 1. Connection Strategy Protocol
# ============================================================

class ConnectionStrategy(Protocol):
    """
    Define the required connection behavior.

    Any connection strategy must provide:
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
# 2. SSH Connection Strategy
# ============================================================

class SSHConnection:
    """Implement network connectivity using SSH."""

    def connect(self) -> str:
        """Establish an SSH connection."""
        return "SSH connection established"

    def disconnect(self) -> str:
        """Close the SSH connection."""
        return "SSH connection closed"


# ============================================================
# 3. API Connection Strategy
# ============================================================

class APIConnection:
    """Implement network connectivity using an API."""

    def connect(self) -> str:
        """Establish an API connection."""
        return "API connection established"

    def disconnect(self) -> str:
        """Close the API connection."""
        return "API connection closed"


# ============================================================
# 4. NETCONF Connection Strategy
# ============================================================

class NETCONFConnection:
    """Implement network connectivity using NETCONF."""

    def connect(self) -> str:
        """Establish a NETCONF connection."""
        return "NETCONF connection established"

    def disconnect(self) -> str:
        """Close the NETCONF connection."""
        return "NETCONF connection closed"


# ============================================================
# 5. Abstract Network Device
# ============================================================

class NetworkDevice(ABC):
    """
    Abstract base class for network devices.

    The connection strategy is injected into the device.
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
# 6. Cisco Router
# ============================================================

class CiscoRouter(NetworkDevice):
    """Represent a Cisco router."""

    def show_status(self) -> str:
        """Return Cisco router status."""
        return f"{self.hostname}: Cisco Router is UP"


# ============================================================
# 7. Cisco Switch
# ============================================================

class CiscoSwitch(NetworkDevice):
    """Represent a Cisco switch."""

    def show_status(self) -> str:
        """Return Cisco switch status."""
        return f"{self.hostname}: Cisco Switch is UP"


# ============================================================
# 8. Juniper Router
# ============================================================

class JuniperRouter(NetworkDevice):
    """Represent a Juniper router."""

    def show_status(self) -> str:
        """Return Juniper router status."""
        return f"{self.hostname}: Juniper Router is UP"


# ============================================================
# 9. Juniper Switch
# ============================================================

class JuniperSwitch(NetworkDevice):
    """Represent a Juniper switch."""

    def show_status(self) -> str:
        """Return Juniper switch status."""
        return f"{self.hostname}: Juniper Switch is UP"


# ============================================================
# 10. Connection Factory
# ============================================================

class ConnectionFactory:
    """
    Create connection strategies.

    The Factory hides the creation logic for
    different connection methods.
    """

    @staticmethod
    def create_connection(
        connection_type: str,
    ) -> ConnectionStrategy:
        """
        Create a connection strategy.

        Args:
            connection_type: Connection type.

        Returns:
            A connection strategy.

        Raises:
            ValueError: If the connection type is unsupported.
        """

        if connection_type == "ssh":
            return SSHConnection()

        if connection_type == "api":
            return APIConnection()

        if connection_type == "netconf":
            return NETCONFConnection()

        raise ValueError(
            f"Unsupported connection type: {connection_type}"
        )


# ============================================================
# 11. Device Factory
# ============================================================

class DeviceFactory:
    """
    Create network devices and inject their connection strategy.

    This Factory combines:

    Factory Pattern
    +
    Dependency Injection
    +
    Strategy Pattern
    """

    @staticmethod
    def create_device(
        device_type: str,
        hostname: str,
        connection_type: str,
    ) -> NetworkDevice:
        """
        Create a network device.

        The method first creates the appropriate
        connection strategy, then injects it into
        the selected network device.

        Args:
            device_type: Network device type.
            hostname: Device hostname.
            connection_type: Connection method.

        Returns:
            A configured NetworkDevice.

        Raises:
            ValueError: If the device type is unsupported.
        """

        # ----------------------------------------------------
        # Step 1:
        # Create the connection strategy.
        # ----------------------------------------------------

        connection = ConnectionFactory.create_connection(
            connection_type
        )

        # ----------------------------------------------------
        # Step 2:
        # Create the network device and inject
        # the connection strategy.
        # ----------------------------------------------------

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
# 12. Network Device Manager
# ============================================================

class NetworkDeviceManager:
    """
    Manage network devices polymorphically.

    The manager does not know the concrete device
    or connection implementation.
    """

    def check_device(self, device: NetworkDevice) -> None:
        """Check the network device."""

        print(f"Device: {device.hostname}")
        print(device.connect())
        print(device.show_status())
        print(device.disconnect())


# ============================================================
# 13. Main
# ============================================================

def main() -> None:
    """Demonstrate the combined architecture."""

    # --------------------------------------------------------
    # Create devices using ONLY the DeviceFactory.
    #
    # We no longer need to manually create:
    # SSHConnection()
    # APIConnection()
    # NETCONFConnection()
    # --------------------------------------------------------

    router_1 = DeviceFactory.create_device(
        "cisco_router",
        "R1",
        "ssh",
    )

    switch_1 = DeviceFactory.create_device(
        "cisco_switch",
        "SW1",
        "api",
    )

    router_2 = DeviceFactory.create_device(
        "juniper_router",
        "R2",
        "netconf",
    )

    switch_2 = DeviceFactory.create_device(
        "juniper_switch",
        "SW2",
        "ssh",
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
