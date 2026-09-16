"""
Lesson 28.4 - else and finally

This example demonstrates the use of:
- try
- except
- else
- finally

Network Engineering Context:
The finally block is useful for cleanup operations,
such as closing network connections or releasing resources.
"""


class NetworkConnection:
    """Simulate a network connection."""

    def __init__(self, hostname: str) -> None:
        self.hostname = hostname
        self.connected = False

    def connect(self) -> None:
        """Establish a simulated network connection."""

        print(f"Connecting to {self.hostname}...")
        self.connected = True
        print(f"Connected to {self.hostname}")

    def disconnect(self) -> None:
        """Close the network connection."""

        if self.connected:
            print(f"Disconnecting from {self.hostname}...")
            self.connected = False
            print(f"Disconnected from {self.hostname}")
        else:
            print(f"No active connection to {self.hostname}")


def check_device(connection: NetworkConnection) -> None:
    """
    Check a network device using try, except, else, and finally.

    Args:
        connection: NetworkConnection object.
    """

    try:
        # Attempt to establish the connection.
        connection.connect()

        # Simulate a network operation.
        print(f"Checking device {connection.hostname}...")

    except ConnectionError:
        # Handle connection failures.
        print(f"Connection failed: {connection.hostname}")

    else:
        # Runs only when no exception occurs.
        print(f"Device {connection.hostname} checked successfully")

    finally:
        # Always runs, whether an exception occurs or not.
        connection.disconnect()


def main() -> None:
    """Run the network connection examples."""

    print("=== Successful Connection ===")

    router = NetworkConnection("R1")
    check_device(router)

    print("\n=== Another Connection ===")

    switch = NetworkConnection("SW1")
    check_device(switch)


if __name__ == "__main__":
    main()
