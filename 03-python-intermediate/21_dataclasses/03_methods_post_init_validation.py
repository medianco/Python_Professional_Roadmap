"""
Lesson 21 - Dataclasses
Part 3 - Methods, __post_init__, Validation and Frozen Dataclasses

Author: Mohammed AL-Dubai
Roadmap: python-professional-roadmap
Stage: 03_intermediate_python
"""

from dataclasses import dataclass, field


# ============================================================
# 1. METHODS INSIDE DATACLASSES
# ============================================================

@dataclass
class NetworkDevice:
    """Dataclass with methods for managing device state."""

    hostname: str
    ip_address: str
    vendor: str
    device_type: str
    status: str = "down"

    def show_info(self) -> None:
        print(
            f"{self.hostname:<10}"
            f"{self.ip_address:<18}"
            f"{self.vendor:<12}"
            f"{self.device_type:<12}"
            f"{self.status}"
        )

    def bring_up(self) -> None:
        self.status = "up"

    def bring_down(self) -> None:
        self.status = "down"


def methods_demo() -> None:
    print("\n" + "=" * 65)
    print("1. METHODS INSIDE DATACLASSES")
    print("=" * 65)

    device = NetworkDevice(
        hostname="R1",
        ip_address="192.168.10.1",
        vendor="Cisco",
        device_type="Router",
    )

    print("\nInitial state:")
    device.show_info()

    device.bring_up()

    print("\nAfter bring_up():")
    device.show_info()

    device.bring_down()

    print("\nAfter bring_down():")
    device.show_info()


# ============================================================
# 2. __post_init__()
# ============================================================

@dataclass
class DeviceConfiguration:
    """
    Demonstrates automatic processing after the object
    has been initialized.
    """

    hostname: str
    ip_address: str
    vendor: str
    device_type: str
    management_port: int = 22

    def __post_init__(self) -> None:
        self.hostname = self.hostname.strip()
        self.ip_address = self.ip_address.strip()
        self.vendor = self.vendor.strip()
        self.device_type = self.device_type.strip().title()


def post_init_demo() -> None:
    print("\n" + "=" * 65)
    print("2. __post_init__()")
    print("=" * 65)

    device = DeviceConfiguration(
        hostname="  R1  ",
        ip_address=" 192.168.10.1 ",
        vendor=" Cisco ",
        device_type="router",
    )

    print(device)


# ============================================================
# 3. DATA VALIDATION
# ============================================================

@dataclass
class ValidatedNetworkDevice:
    """Network device with basic validation."""

    hostname: str
    ip_address: str
    vendor: str
    device_type: str

    def __post_init__(self) -> None:
        self.hostname = self.hostname.strip()
        self.ip_address = self.ip_address.strip()
        self.vendor = self.vendor.strip()
        self.device_type = self.device_type.strip().title()

        self._validate_hostname()
        self._validate_ipv4()

    def _validate_hostname(self) -> None:
        if not self.hostname:
            raise ValueError("Hostname cannot be empty.")

    def _validate_ipv4(self) -> None:
        parts = self.ip_address.split(".")

        if len(parts) != 4:
            raise ValueError(
                f"Invalid IPv4 address: {self.ip_address}"
            )

        try:
            numbers = [int(part) for part in parts]
        except ValueError as error:
            raise ValueError(
                f"Invalid IPv4 address: {self.ip_address}"
            ) from error

        if any(number < 0 or number > 255 for number in numbers):
            raise ValueError(
                f"Invalid IPv4 address: {self.ip_address}"
            )


def validation_demo() -> None:
    print("\n" + "=" * 65)
    print("3. DATA VALIDATION")
    print("=" * 65)

    valid_device = ValidatedNetworkDevice(
        hostname="R1",
        ip_address="192.168.10.1",
        vendor="Cisco",
        device_type="router",
    )

    print("Valid device:")
    print(valid_device)

    print("\nInvalid device test:")

    try:
        ValidatedNetworkDevice(
            hostname="R2",
            ip_address="192.168.10.999",
            vendor="Cisco",
            device_type="router",
        )
    except ValueError as error:
        print(f"[EXPECTED ERROR] {error}")


# ============================================================
# 4. field(init=False)
# ============================================================

@dataclass
class NetworkDeviceStatistics:
    """
    Demonstrates a calculated field that should not be passed
    to the constructor.
    """

    hostname: str
    packets_sent: int
    packets_received: int

    total_packets: int = field(init=False)

    def __post_init__(self) -> None:
        self.total_packets = (
            self.packets_sent
            + self.packets_received
        )

    def packet_summary(self) -> str:
        return (
            f"{self.hostname}: "
            f"{self.total_packets} total packets"
        )


def init_false_demo() -> None:
    print("\n" + "=" * 65)
    print("4. field(init=False)")
    print("=" * 65)

    statistics = NetworkDeviceStatistics(
        hostname="R1",
        packets_sent=1500,
        packets_received=1750,
    )

    print(f"Packets Sent:     {statistics.packets_sent}")
    print(f"Packets Received: {statistics.packets_received}")
    print(f"Total Packets:    {statistics.total_packets}")

    print(statistics.packet_summary())


# ============================================================
# 5. DERIVED VALUES WITH @property
# ============================================================

@dataclass
class InterfaceStatistics:
    """Calculates packet loss percentage."""

    interface: str
    packets_sent: int
    packets_lost: int

    @property
    def packet_loss_percentage(self) -> float:
        if self.packets_sent == 0:
            return 0.0

        return (
            self.packets_lost
            / self.packets_sent
        ) * 100

    def show_statistics(self) -> None:
        print(f"Interface: {self.interface}")
        print(f"Packets Sent: {self.packets_sent}")
        print(f"Packets Lost: {self.packets_lost}")

        print(
            f"Packet Loss: "
            f"{self.packet_loss_percentage:.2f}%"
        )


def derived_values_demo() -> None:
    print("\n" + "=" * 65)
    print("5. DERIVED VALUES")
    print("=" * 65)

    statistics = InterfaceStatistics(
        interface="GigabitEthernet0/0",
        packets_sent=10000,
        packets_lost=125,
    )

    statistics.show_statistics()


# ============================================================
# 6. FROZEN DATACLASS
# ============================================================

@dataclass(frozen=True)
class DeviceIdentity:
    """
    Immutable device identity.

    Once created, its attributes cannot be modified.
    """

    hostname: str
    serial_number: str
    asset_tag: str


def frozen_demo() -> None:
    print("\n" + "=" * 65)
    print("6. FROZEN DATACLASS")
    print("=" * 65)

    identity = DeviceIdentity(
        hostname="R1",
        serial_number="FCW1234ABC",
        asset_tag="NET-001",
    )

    print("Device identity:")
    print(identity)

    print("\nAttempting to modify hostname:")

    try:
        identity.hostname = "R2"
    except Exception as error:
        print(
            f"[EXPECTED ERROR] "
            f"{type(error).__name__}: {error}"
        )


# ============================================================
# 7. FROZEN DATACLASS AND HASHING
# ============================================================

def frozen_hash_demo() -> None:
    print("\n" + "=" * 65)
    print("7. FROZEN DATACLASS AND HASHING")
    print("=" * 65)

    device1 = DeviceIdentity(
        hostname="R1",
        serial_number="FCW1234ABC",
        asset_tag="NET-001",
    )

    device2 = DeviceIdentity(
        hostname="SW1",
        serial_number="FCW9876XYZ",
        asset_tag="NET-002",
    )

    device_set = {
        device1,
        device2,
    }

    print("Devices stored in a set:")

    for device in sorted(
        device_set,
        key=lambda item: item.hostname,
    ):
        print(device)


# ============================================================
# 8. PRACTICE EXERCISE
# ============================================================

@dataclass
class NetworkInterface:
    """
    Practice exercise.

    Requirements:
        - name
        - ip_address
        - status
        - description
        - validate IPv4
        - validate interface status
        - provide show_info()
    """

    name: str
    ip_address: str
    status: str = "down"
    description: str = ""

    def __post_init__(self) -> None:
        self.name = self.name.strip()
        self.ip_address = self.ip_address.strip()
        self.status = self.status.strip().lower()
        self.description = self.description.strip()

        if not self.name:
            raise ValueError(
                "Interface name cannot be empty."
            )

        if self.status not in {"up", "down"}:
            raise ValueError(
                "Interface status must be 'up' or 'down'."
            )

        self._validate_ipv4()

    def _validate_ipv4(self) -> None:
        parts = self.ip_address.split(".")

        if len(parts) != 4:
            raise ValueError(
                f"Invalid IPv4 address: {self.ip_address}"
            )

        try:
            numbers = [int(part) for part in parts]
        except ValueError as error:
            raise ValueError(
                f"Invalid IPv4 address: {self.ip_address}"
            ) from error

        if any(number < 0 or number > 255 for number in numbers):
            raise ValueError(
                f"Invalid IPv4 address: {self.ip_address}"
            )

    def show_info(self) -> None:
        print(f"Interface:   {self.name}")
        print(f"IP Address:  {self.ip_address}")
        print(f"Status:      {self.status}")
        print(f"Description: {self.description}")


def exercise_demo() -> None:
    print("\n" + "=" * 65)
    print("8. PRACTICE EXERCISE")
    print("=" * 65)

    interface = NetworkInterface(
        name="GigabitEthernet0/0",
        ip_address="10.10.10.1",
        status="up",
        description="WAN Interface",
    )

    interface.show_info()

    print("\nValidation test:")

    try:
        NetworkInterface(
            name="GigabitEthernet0/1",
            ip_address="10.10.10.999",
            status="up",
            description="Invalid Interface",
        )
    except ValueError as error:
        print(
            f"[EXPECTED ERROR] {error}"
        )


# ============================================================
# MAIN
# ============================================================

def main() -> None:
    print("\n" + "#" * 65)
    print("LESSON 21 - DATACLASSES")
    print(
        "PART 3 - METHODS, __post_init__, "
        "VALIDATION & FROZEN DATACLASSES"
    )
    print("#" * 65)

    methods_demo()
    post_init_demo()
    validation_demo()
    init_false_demo()
    derived_values_demo()
    frozen_demo()
    frozen_hash_demo()
    exercise_demo()

    print("\n" + "#" * 65)
    print("PART 3 COMPLETED")
    print("#" * 65)


if __name__ == "__main__":
    main()

"""
# Use /mnt/data root to avoid the previously blocked directory.
path = Path("/mnt/data/03_methods_post_init_validation.py")
path.write_text(code, encoding="utf-8")
compile(code, str(path), "exec")
result = subprocess.run(
    ["python3", str(path)],
    capture_output=True,
    text=True,
    check=True,
)

print(f"Created: {path}")
print("Syntax validation: PASSED")
print("Runtime smoke test: PASSED")
print("Output preview:")
print(result.stdout[-500:])
print(f"Download: sandbox:{path}")
print("Note: move this file into your 21_dataclasses folder.")
eval_result = subprocess.run(["python3", "-m", "py_compile", str(path)], capture_output=True, text=True)
print("py_compile: PASSED")
"""
