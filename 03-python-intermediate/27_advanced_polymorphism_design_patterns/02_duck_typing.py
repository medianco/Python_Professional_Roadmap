"""
Lesson 27.2 - Duck Typing

This lesson demonstrates Duck Typing in Python.

Focus:
- Duck Typing
- Behavior over type
- Polymorphism without inheritance
- Network Automation example

## Duck Typing 
#  without:
#    - Inheritance
#    - ABC
#    - Protocol
"""


class SSHConnection:
    """Represent an SSH connection."""

    def connect(self) -> str:
        return "SSH connection established"


class APIConnection:
    """Represent an API connection."""

    def connect(self) -> str:
        return "API connection established"


class TelnetConnection:
    """Represent a Telnet connection."""

    def connect(self) -> str:
        return "Telnet connection established"


def establish_connection(connection) -> str:
    """
    Establish a connection using Duck Typing.

    The function does not care about the object's class.
    It only expects the object to provide a connect() method.
    """
    return connection.connect()


def main() -> None:
    """Create different connection objects and test Duck Typing."""

    connections = [
        SSHConnection(),
        APIConnection(),
        TelnetConnection(),
    ]

    for connection in connections:
        print(establish_connection(connection))


if __name__ == "__main__":
    main()
