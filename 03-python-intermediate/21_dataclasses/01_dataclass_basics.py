"""
Lesson 21 - Dataclasses
Part 1 - Dataclass Fundamentals

Author: Mohammed AL-Dubai
Roadmap: python-professional-roadmap
Stage: 03_intermediate_python
"""

from dataclasses import dataclass


# ============================================================
# 1. BASIC DATACLASS
# ============================================================

@dataclass
class NetworkDevice:
    """Represents basic network device information."""

    hostname: str
    ip_address: str
    vendor: str
    device_type: str


def basic_dataclass_demo() -> None:
    print("\n" + "=" * 60)
    print("1. BASIC DATACLASS")
    print("=" * 60)

    router = NetworkDevice(
        hostname="R1",
        ip_address="192.168.10.1",
        vendor="Cisco",
        device_type="Router",
    )

    print(f"Hostname:    {router.hostname}")
    print(f"IP Address:  {router.ip_address}")
    print(f"Vendor:      {router.vendor}")
    print(f"Device Type: {router.device_type}")


# ============================================================
# 2. MULTIPLE OBJECTS
# ============================================================

def multiple_devices_demo() -> None:
    print("\n" + "=" * 60)
    print("2. MULTIPLE NETWORK DEVICES")
    print("=" * 60)

    devices = [
        NetworkDevice(
            "R1",
            "192.168.10.1",
            "Cisco",
            "Router",
        ),
        NetworkDevice(
            "R2",
            "192.168.20.1",
            "Cisco",
            "Router",
        ),
        NetworkDevice(
            "SW1",
            "192.168.10.10",
            "Cisco",
            "Switch",
        ),
        NetworkDevice(
            "FW1",
            "192.168.10.254",
            "Fortinet",
            "Firewall",
        ),
    ]

    print(
        f"{'Hostname':<12}"
        f"{'IP Address':<18}"
        f"{'Vendor':<12}"
        f"Type"
    )

    print("-" * 60)

    for device in devices:
        print(
            f"{device.hostname:<12}"
            f"{device.ip_address:<18}"
            f"{device.vendor:<12}"
            f"{device.device_type}"
        )


# ============================================================
# 3. DATACLASS __repr__
# ============================================================

def repr_demo() -> None:
    print("\n" + "=" * 60)
    print("3. DATACLASS __repr__")
    print("=" * 60)

    device = NetworkDevice(
        "R10",
        "10.10.10.1",
        "Cisco",
        "Router",
    )

    print(device)


# ============================================================
# 4. DATACLASS EQUALITY
# ============================================================

def equality_demo() -> None:
    print("\n" + "=" * 60)
    print("4. DATACLASS EQUALITY")
    print("=" * 60)

    device1 = NetworkDevice(
        "R1",
        "192.168.10.1",
        "Cisco",
        "Router",
    )

    device2 = NetworkDevice(
        "R1",
        "192.168.10.1",
        "Cisco",
        "Router",
    )

    device3 = NetworkDevice(
        "R2",
        "192.168.20.1",
        "Cisco",
        "Router",
    )

    print(f"device1 == device2: {device1 == device2}")
    print(f"device1 == device3: {device1 == device3}")


# ============================================================
# 5. NETWORK INTERFACE DATACLASS
# ============================================================

@dataclass
class NetworkInterface:
    """Represents a network interface."""

    name: str
    ip_address: str
    description: str
    status: str


def interface_demo() -> None:
    print("\n" + "=" * 60)
    print("5. NETWORK INTERFACE")
    print("=" * 60)

    interface = NetworkInterface(
        name="GigabitEthernet0/0",
        ip_address="10.10.10.1",
        description="WAN Interface",
        status="up",
    )

    print(f"Interface:   {interface.name}")
    print(f"IP Address:  {interface.ip_address}")
    print(f"Description: {interface.description}")
    print(f"Status:      {interface.status}")


# ============================================================
# 6. TYPE HINTS
# ============================================================

@dataclass
class Server:
    """Simple dataclass demonstrating type hints."""

    hostname: str
    ip_address: str
    port: int
    enabled: bool


def type_hints_demo() -> None:
    print("\n" + "=" * 60)
    print("6. TYPE HINTS")
    print("=" * 60)

    server = Server(
        hostname="Ubuntu-Server",
        ip_address="192.168.100.10",
        port=22,
        enabled=True,
    )

    print(f"Hostname: {server.hostname}")
    print(f"IP Address: {server.ip_address}")
    print(f"Port: {server.port}")
    print(f"Enabled: {server.enabled}")


# ============================================================
# 7. TRADITIONAL CLASS VS DATACLASS
# ============================================================

class TraditionalDevice:
    """Traditional class for comparison."""

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        vendor: str,
        device_type: str,
    ) -> None:
        self.hostname = hostname
        self.ip_address = ip_address
        self.vendor = vendor
        self.device_type = device_type


def comparison_demo() -> None:
    print("\n" + "=" * 60)
    print("7. TRADITIONAL CLASS VS DATACLASS")
    print("=" * 60)

    traditional = TraditionalDevice(
        "R1",
        "192.168.10.1",
        "Cisco",
        "Router",
    )

    dataclass_device = NetworkDevice(
        "R1",
        "192.168.10.1",
        "Cisco",
        "Router",
    )

    print("Traditional class:")
    print(f"  {traditional.hostname}")
    print(f"  {traditional.ip_address}")

    print("\nDataclass:")
    print(f"  {dataclass_device}")


# ============================================================
# 8. PART 1 PRACTICE EXERCISE
# ============================================================

@dataclass
class ExerciseInterface:
    """
    Practice dataclass.

    Fields:
        name
        ip_address
        description
        status
    """

    name: str
    ip_address: str
    description: str
    status: str


def exercise_demo() -> None:
    print("\n" + "=" * 60)
    print("8. PRACTICE EXERCISE")
    print("=" * 60)

    interface = ExerciseInterface(
        name="GigabitEthernet0/0",
        ip_address="10.10.10.1",
        description="WAN Interface",
        status="up",
    )

    print(interface)


# ============================================================
# MAIN
# ============================================================

def main() -> None:
    print("\n" + "#" * 60)
    print("LESSON 21 - DATACLASSES")
    print("PART 1 - FUNDAMENTALS")
    print("#" * 60)

    basic_dataclass_demo()
    multiple_devices_demo()
    repr_demo()
    equality_demo()
    interface_demo()
    type_hints_demo()
    comparison_demo()
    exercise_demo()

    print("\n" + "#" * 60)
    print("PART 1 COMPLETED")
    print("#" * 60)


if __name__ == "__main__":
    main()
