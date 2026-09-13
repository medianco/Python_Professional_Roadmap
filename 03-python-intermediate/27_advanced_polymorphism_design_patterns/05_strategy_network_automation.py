"""
Lesson 27.6 - Strategy Pattern with Network Automation

This lesson demonstrates how the Strategy Pattern
can be applied to Network Automation.

Topics:
- Strategy Pattern
- Protocol
- Structural Typing
- Polymorphism
- Composition
- Dependency Injection
- Network Automation architecture

Architecture:

                    NetworkDevice
                         |
                         | uses
                         ↓
                  Connection Strategy
                         |
              ┌──────────┼──────────┐
              ↓          ↓          ↓
             SSH        API       NETCONF
"""


from typing import Protocol


# ============================================================
# 1. Strategy Interface
# ============================================================

class ConnectionStrategy(Protocol):
    """
    Define the connection strategy interface.

    Any connection strategy must provide:
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
    """Implement network connectivity using SSH."""

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
    """Implement network connectivity using an API."""

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
    """Implement network connectivity using NETCONF."""

    def connect(self) -> str:
        """Establish a NETCONF connection."""
        return "NETCONF connection established"

    def disconnect(self) -> str:
        """Close the NETCONF connection."""
        return "NETCONF connection closed"


# ============================================================
# 5. Network Device - Context
# ============================================================

class NetworkDevice:
    """
    Represent a network device.

    The device uses a connection strategy instead
    of implementing the connection method itself.
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
            connection: Connection strategy.
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
# 6. Main
# ============================================================

def main() -> None:
    """Demonstrate Strategy Pattern in Network Automation."""

    # Create different connection strategies.
    ssh = SSHConnection()
    api = APIConnection()
    netconf = NETCONFConnection()

    # Inject the SSH strategy into a network device.
    router = NetworkDevice("R1", ssh)

    print(router.show_info())
    print(router.connect())
    print(router.disconnect())

    print("=" * 40)

    # Change the strategy at runtime.
    router.connection = api

    print(router.show_info())
    print(router.connect())
    print(router.disconnect())

    print("=" * 40)

    # Change the strategy again.
    router.connection = netconf

    print(router.show_info())
    print(router.connect())
    print(router.disconnect())


if __name__ == "__main__":
    main()
