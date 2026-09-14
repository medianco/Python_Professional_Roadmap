"""
Lesson 27.8 - Factory Pattern

This lesson demonstrates the Factory Design Pattern.

Topics:
- Factory Pattern
- Object creation
- Encapsulation of object creation
- Polymorphism
- Loose Coupling

Key idea:

The Factory is responsible for creating objects.

Instead of creating objects directly:

    SSHConnection()
    APIConnection()

we ask the Factory to create the required object.
"""


# ============================================================
# 1. Product Classes
# ============================================================

class SSHConnection:
    """Represent an SSH connection."""

    def connect(self) -> str:
        """Establish an SSH connection."""
        return "SSH connection established"


class APIConnection:
    """Represent an API connection."""

    def connect(self) -> str:
        """Establish an API connection."""
        return "API connection established"


class NETCONFConnection:
    """Represent a NETCONF connection."""

    def connect(self) -> str:
        """Establish a NETCONF connection."""
        return "NETCONF connection established"


# ============================================================
# 2. Factory Class
# ============================================================

class ConnectionFactory:
    """
    Create connection objects.

    The Factory hides the object creation logic
    from the rest of the application.
    """

    @staticmethod
    def create_connection(connection_type: str):
        """
        Create a connection based on the requested type.

        Args:
            connection_type: Type of connection to create.

        Returns:
            A connection object.
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
# 3. Main
# ============================================================

def main() -> None:
    """Demonstrate the Factory Pattern."""

    # --------------------------------------------------------
    # Create the Factory.
    # --------------------------------------------------------

    factory = ConnectionFactory()

    # --------------------------------------------------------
    # Ask the Factory to create an SSH connection.
    # --------------------------------------------------------

    ssh = factory.create_connection("ssh")

    print(ssh.connect())

    # --------------------------------------------------------
    # Ask the Factory to create an API connection.
    # --------------------------------------------------------

    api = factory.create_connection("api")

    print(api.connect())

    # --------------------------------------------------------
    # Ask the Factory to create a NETCONF connection.
    # --------------------------------------------------------

    netconf = factory.create_connection("netconf")

    print(netconf.connect())


if __name__ == "__main__":
    main()
