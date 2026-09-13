"""
Lesson 27.7 - Strategy Pattern + Dependency Injection

This lesson demonstrates how Dependency Injection
can be combined with the Strategy Pattern.

Topics:
- Strategy Pattern
- Dependency Injection
- Protocol
- Composition
- Polymorphism
- Loose Coupling
- Network Automation architecture

Key idea:

The NetworkDevice does not create its own connection.

Instead, the connection strategy is injected from outside.

Architecture:

                NetworkDevice
                      |
                      | receives
                      ↓
             ConnectionStrategy
                      |
             ┌────────┼────────┐
             ↓        ↓        ↓
            SSH      API     NETCONF
"""


from typing import Protocol


# ============================================================
# 1. Strategy Interface
# ============================================================

class ConnectionStrategy(Protocol):
    """
    Define the connection strategy interface.

    Any connection implementation must provide:
    - connect()
    - disconnect()
    """

    def connect(self) -> str:
        """Establish a connection."""
        ...

    def disconnect(self) -> str:
        """Close the connection."""
        ...


# ============================================================
# 2. SSH Strategy
# ============================================================

class SSHConnection:
    """Implement connection using SSH."""

    def connect(self) -> str:
        """Establish an SSH connection."""
        return "SSH connection established"

    def disconnect(self) -> str:
        """Close the SSH connection."""
        return "SSH connection closed"


# ============================================================
# 3. API Strategy
# ============================================================

class APIConnection:
    """Implement connection using an API."""

    def connect(self) -> str:
        """Establish an API connection."""
        return "API connection established"

    def disconnect(self) -> str:
        """Close the API connection."""
        return "API connection closed"


# ============================================================
# 4. NETCONF Strategy
# ============================================================

class NETCONFConnection:
    """Implement connection using NETCONF."""

    def connect(self) -> str:
        """Establish a NETCONF connection."""
        return "NETCONF connection established"

    def disconnect(self) -> str:
        """Close the NETCONF connection."""
        return "NETCONF connection closed"


# ============================================================
# 5. Network Device
# ============================================================

class NetworkDevice:
    """
    Represent a network device.

    The connection strategy is injected into the device
    through the constructor.

    This is Dependency Injection.
    """

    def __init__(
        self,
        hostname: str,
        connection: ConnectionStrategy,
    ) -> None:
        """
        Initialize the network device.

        Args:
            hostname: Device hostname.
            connection: Injected connection strategy.
        """
        self.hostname = hostname
        self.connection = connection

    def connect(self) -> str:
        """Connect to the network device."""
        return self.connection.connect()

    def disconnect(self) -> str:
        """Disconnect from the network device."""
        return self.connection.disconnect()

    def show_info(self) -> str:
        """Return basic device information."""
        return f"Device: {self.hostname}"


# ============================================================
# 6. Network Device Manager
# ============================================================

class NetworkDeviceManager:
    """
    Manage network devices.

    The manager works with the NetworkDevice interface
    without knowing the concrete connection implementation.
    """

    def check_device(self, device: NetworkDevice) -> None:
        """Connect, display information, and disconnect."""

        print(device.show_info())
        print(device.connect())
        print(device.disconnect())


# ============================================================
# 7. Main
# ============================================================

def main() -> None:
    """Demonstrate Strategy Pattern with Dependency Injection."""

    # --------------------------------------------------------
    # Create connection strategies.
    # --------------------------------------------------------

    ssh = SSHConnection()
    api = APIConnection()
    netconf = NETCONFConnection()

    # --------------------------------------------------------
    # Inject the SSH strategy into R1.
    # --------------------------------------------------------

    router_1 = NetworkDevice("R1", ssh)

    # --------------------------------------------------------
    # Inject the API strategy into R2.
    # --------------------------------------------------------

    router_2 = NetworkDevice("R2", api)

    # --------------------------------------------------------
    # Inject the NETCONF strategy into R3.
    # --------------------------------------------------------

    router_3 = NetworkDevice("R3", netconf)

    # --------------------------------------------------------
    # Create the manager.
    # --------------------------------------------------------

    manager = NetworkDeviceManager()

    # --------------------------------------------------------
    # Manage all devices polymorphically.
    # --------------------------------------------------------

    devices = [
        router_1,
        router_2,
        router_3,
    ]

    for device in devices:
        manager.check_device(device)
        print("=" * 40)


if __name__ == "__main__":
    main()
