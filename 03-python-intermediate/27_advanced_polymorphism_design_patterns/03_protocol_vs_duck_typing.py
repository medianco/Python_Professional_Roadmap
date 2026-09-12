"""
Lesson 27.3 - Protocol vs Duck Typing

This lesson compares Duck Typing and Protocol
using a Network Automation example.

Topics:
- Duck Typing
- Protocol
- Structural Typing
- Type Hints
- Runtime behavior
- Network Automation example

Key idea:

Duck Typing:
    If an object provides the required behavior, use it.

Protocol:
    Define the expected behavior explicitly so that
    type checkers and IDEs can understand the interface.
"""


from typing import Protocol


# ============================================================
# 1. Duck Typing
# ============================================================

class SSHConnection:
    """Represent an SSH connection."""

    def connect(self) -> str:
        """Establish an SSH connection."""
        return "SSH connection established"

    def disconnect(self) -> str:
        """Close the SSH connection."""
        return "SSH connection closed"


class APIConnection:
    """Represent an API connection."""

    def connect(self) -> str:
        """Establish an API connection."""
        return "API connection established"

    def disconnect(self) -> str:
        """Close the API connection."""
        return "API connection closed"


class TelnetConnection:
    """Represent a Telnet connection."""

    def connect(self) -> str:
        """Establish a Telnet connection."""
        return "Telnet connection established"

    def disconnect(self) -> str:
        """Close the Telnet connection."""
        return "Telnet connection closed"


# ============================================================
# 2. Duck Typing Function
# ============================================================

def duck_typing_connection(connection) -> str:
    """
    Use Duck Typing to establish a connection.

    The function does not check the object's type.
    It simply assumes that the object provides connect().
    """
    return connection.connect()


# ============================================================
# 3. Protocol Definition
# ============================================================

class Connection(Protocol):
    """
    Define the expected connection behavior.

    Any object that provides connect() and disconnect()
    is compatible with this Protocol.
    """

    def connect(self) -> str:
        """Establish a connection."""
        ...

    def disconnect(self) -> str:
        """Close the connection."""
        ...


# ============================================================
# 4. Protocol Function
# ============================================================

def protocol_connection(connection: Connection) -> str:
    """
    Use a Protocol type hint for the connection.

    The Connection Protocol describes the behavior
    expected from the object.
    """
    return connection.connect()


# ============================================================
# 5. Compare Duck Typing and Protocol
# ============================================================

def compare_connections() -> None:
    """Compare Duck Typing and Protocol behavior."""

    connections = [
        SSHConnection(),
        APIConnection(),
        TelnetConnection(),
    ]

    print("=== Duck Typing ===")

    for connection in connections:
        print(duck_typing_connection(connection))

    print()

    print("=== Protocol ===")

    for connection in connections:
        print(protocol_connection(connection))


# ============================================================
# 6. Main
# ============================================================

def main() -> None:
    """Run the Protocol vs Duck Typing demonstration."""

    compare_connections()


if __name__ == "__main__":
    main()
