"""
Lesson 27.13 - Network Automation Application

This lesson combines the major concepts learned
through Lesson 27.

Concepts:

- Abstract Base Classes (ABC)
- Protocol
- Composition
- Dependency Injection
- Polymorphism
- Strategy Pattern
- Factory Pattern
- SOLID Principles

Goal:

Build a small but well-structured
Network Automation application.

                    Network Automation System
                              │
                    ┌─────────┴─────────┐
                    │                   │
              DeviceFactory       DeviceManager
                    │                   │
          ┌─────────┼─────────┐         │
          ↓         ↓         ↓         ↓
        Cisco     Juniper    Arista    Operations
          │         │         │
          └─────────┼─────────┘
                    │
               Connection
                    │
             ┌──────┼──────┐
             ↓      ↓      ↓
            SSH    API   NETCONF
"""

from abc import ABC, abstractmethod
from typing import Protocol


# ============================================================
# 1. Connection Protocol
# ============================================================

class Connection(Protocol):
    """
    Define the required behavior for connections.

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
# 2. SSH Connection
# ============================================================

class SSHConnection:
    """Implement network connectivity using SSH."""

    def connect(self) -> str:
        """Establish an SSH connection."""

        return "SSH connection established"

    def disconnect(self) -> str:
        """Close an SSH connection."""

        return "SSH connection closed"


# ============================================================
# 3. API Connection
# ============================================================

class APIConnection:
    """Implement network connectivity using an API."""

    def connect(self) -> str:
        """Establish an API connection."""

        return "API connection established"

    def disconnect(self) -> str:
        """Close an API connection."""

        return "API connection closed"


# ============================================================
# 4. NETCONF Connection
# ============================================================

class NETCONFConnection:
    """Implement network connectivity using NETCONF."""

    def connect(self) -> str:
        """Establish a NETCONF connection."""

        return "NETCONF connection established"

    def disconnect(self) -> str:
        """Close a NETCONF connection."""

        return "NETCONF connection closed"


# ============================================================
# 5. Abstract Network Device
# ============================================================

class NetworkDevice(ABC):
    """
    Abstract base class for network devices.

    The device uses Composition to work with
    an external Connection object.
    """

    def __init__(
        self,
        hostname: str,
        connection: Connection,
    ) -> None:
        """Initialize the network device."""

        self.hostname = hostname
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
# 10. Arista Router
# ============================================================

class AristaRouter(NetworkDevice):
    """Represent an Arista router."""

    def show_status(self) -> str:
        """Return Arista router status."""

        return f"{self.hostname}: Arista Router is UP"


# ============================================================
# 11. Connection Factory
# ============================================================

class ConnectionFactory:
    """
    Create connection strategies.

    The Factory hides connection object creation.
    """

    @staticmethod
    def create_connection(
        connection_type: str,
    ) -> Connection:
        """
        Create a connection strategy.

        Args:
            connection_type: Type of connection.

        Returns:
            A connection implementation.

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
# 12. Device Factory
# ============================================================

class DeviceFactory:
    """
    Create network devices.

    The Factory is responsible for object creation
    and Dependency Injection.
    """

    @staticmethod
    def create_device(
        device_type: str,
        hostname: str,
        connection_type: str,
    ) -> NetworkDevice:
        """
        Create a configured network device.

        Args:
            device_type: Type of network device.
            hostname: Device hostname.
            connection_type: Connection method.

        Returns:
            A configured NetworkDevice.
        """

        # ----------------------------------------------------
        # Create the connection strategy.
        # ----------------------------------------------------

        connection = ConnectionFactory.create_connection(
            connection_type
        )

        # ----------------------------------------------------
        # Create the device.
        # ----------------------------------------------------

        if device_type == "cisco_router":
            return CiscoRouter(
                hostname,
                connection,
            )

        if device_type == "cisco_switch":
            return CiscoSwitch(
                hostname,
                connection,
            )

        if device_type == "juniper_router":
            return JuniperRouter(
                hostname,
                connection,
            )

        if device_type == "juniper_switch":
            return JuniperSwitch(
                hostname,
                connection,
            )

        if device_type == "arista_router":
            return AristaRouter(
                hostname,
                connection,
            )

        raise ValueError(
            f"Unsupported device type: {device_type}"
        )


# ============================================================
# 13. Configuration Service
# ============================================================

class ConfigurationService:
    """
    Handle network device configuration.

    This class follows SRP because its responsibility
    is configuration only.
    """

    def configure_device(
        self,
        device: NetworkDevice,
    ) -> str:
        """Apply configuration to a network device."""

        return (
            f"{device.hostname}: "
            "configuration applied"
        )


# ============================================================
# 14. Logging Service
# ============================================================

class LoggingService:
    """
    Handle application logging.

    This class has one responsibility:
    logging.
    """

    def log(self, message: str) -> None:
        """Write a log message."""

        print(f"[LOG] {message}")


# ============================================================
# 15. Network Device Manager
# ============================================================

class NetworkDeviceManager:
    """
    Manage network devices.

    The manager depends on abstractions and receives
    its services through Dependency Injection.
    """

    def __init__(
        self,
        logger: LoggingService,
        configuration: ConfigurationService,
    ) -> None:
        """Initialize the manager."""

        self.logger = logger
        self.configuration = configuration

    def check_device(
        self,
        device: NetworkDevice,
    ) -> None:
        """
        Connect to a device, check its status,
        configure it, and disconnect.
        """

        self.logger.log(
            f"Checking device {device.hostname}"
        )

        print(device.connect())

        print(device.show_status())

        print(
            self.configuration.configure_device(
                device
            )
        )

        print(device.disconnect())


# ============================================================
# 16. Main Application
# ============================================================
'''
                        MAIN
                          │
                          ↓
                   DeviceFactory
                          │
                  ┌───────┴────────┐
                  ↓                ↓
           Device Creation   ConnectionFactory
                  │                │
                  ↓          ┌─────┼─────┐
           NetworkDevice      SSH   API  NETCONF
               (ABC)
                  │
       ┌──────────┼──────────┐
       ↓          ↓          ↓
     Cisco      Juniper    Arista
       │          │          │
       └──────────┼──────────┘
                  ↓
             Polymorphism
                  │
                  ↓
        NetworkDeviceManager
             /          \
            ↓            ↓
         Logger    Configuration
         
'''
def main() -> None:
    """Run the Network Automation application."""

    # --------------------------------------------------------
    # Create application services.
    # --------------------------------------------------------

    logger = LoggingService()
    configuration = ConfigurationService()

    # --------------------------------------------------------
    # Create devices through the Factory.
    #
    # We do not manually create connection objects.
    # --------------------------------------------------------

    devices: list[NetworkDevice] = [
        DeviceFactory.create_device(
            "cisco_router",
            "R1",
            "ssh",
        ),
        DeviceFactory.create_device(
            "cisco_switch",
            "SW1",
            "api",
        ),
        DeviceFactory.create_device(
            "juniper_router",
            "R2",
            "netconf",
        ),
        DeviceFactory.create_device(
            "juniper_switch",
            "SW2",
            "ssh",
        ),
        DeviceFactory.create_device(
            "arista_router",
            "R3",
            "api",
        ),
    ]

    # --------------------------------------------------------
    # Inject services into the manager.
    # --------------------------------------------------------

    manager = NetworkDeviceManager(
        logger,
        configuration,
    )

    # --------------------------------------------------------
    # Manage every device polymorphically.
    # --------------------------------------------------------

    for device in devices:
        manager.check_device(device)
        print("=" * 50)


# ============================================================
# Program Entry Point
# ============================================================

if __name__ == "__main__":
    main()
