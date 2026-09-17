"""
Lesson 28.8 - Exception Handling in Network Automation

This example demonstrates how exception handling
can be applied to Network Automation.

Network Engineering Context:
Network automation scripts interact with devices
that may fail for different reasons, such as:

- Connection failures
- Authentication failures
- Timeouts
- Invalid commands
- Configuration errors

Exception handling allows our automation system
to handle these failures gracefully.

            Network Device
                  │
                  ▼
             connect()
                  │
           ┌──────┴──────┐
           │             │
       Success         Failure
           │             │
           ▼             ▼
       Check Device   except
           │             │
           └──────┬──────┘
                  ▼
               finally
                  │
                  ▼
              Continue
              Next Device
"""


class NetworkConnection:
    """Simulate a network device connection."""

    def __init__(
        self,
        hostname: str,
        should_fail: bool = False,
    ) -> None:
        self.hostname = hostname
        self.should_fail = should_fail

    def connect(self) -> None:
        """
        Establish a connection to the network device.

        Raises:
            ConnectionError: If the connection fails.
        """
        print(f"Connecting to {self.hostname}...")

        if self.should_fail:
            raise ConnectionError(
                f"Unable to connect to {self.hostname}"
            )

        print(f"Connected to {self.hostname}")

    def disconnect(self) -> None:
        """Close the connection to the network device."""
        print(f"Disconnected from {self.hostname}")


def check_device(connection: NetworkConnection) -> None:
    """
    Connect to a device and perform a basic check.

    Args:
        connection: NetworkConnection object.
    """
    try:
        connection.connect()

        print(
            f"Checking device {connection.hostname}..."
        )

        print(
            f"{connection.hostname}: "
            "Device is operational"
        )

    except ConnectionError as error:
        print(
            f"Connection error: {error}"
        )

    finally:
        print(
            f"Finished processing {connection.hostname}"
        )


def main() -> None:
    """Run the Network Automation example."""

    devices = [
        NetworkConnection("R1"),
        NetworkConnection("R2", should_fail=True),
        NetworkConnection("SW1"),
    ]

    print("=== Network Automation ===")

    for device in devices:
        check_device(device)
        print("-" * 50)


if __name__ == "__main__":
    main()
