"""
============================================================
Lesson 20 - Object-Oriented Programming
============================================================

Part 1 -> OOP Fundamentals
Part 2 -> Encapsulation and Class Design
Part 3 -> Inheritance and Polymorphism
Part 4 -> Professional OOP
Part 5 -> Final Network Device Management System

Author: Mohammed AL-Dubai
Python Version: 3.x
============================================================
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar


# ============================================================
# PART 1
# OOP FUNDAMENTALS
# ============================================================

class BasicDevice:
    """A simple class representing a network device."""

    def __init__(
        self,
        hostname: str,
        ip_address: str,
    ) -> None:

        self.hostname = hostname
        self.ip_address = ip_address

    def show_info(self) -> None:

        print(
            f"Hostname: {self.hostname}"
        )

        print(
            f"IP Address: {self.ip_address}"
        )

    def ping(self) -> None:

        print(
            f"{self.hostname} "
            f"({self.ip_address}) -> Ping SUCCESS"
        )


def part_one_basic_class_demo() -> None:

    print("\n" + "=" * 70)
    print("PART 1 - OOP FUNDAMENTALS")
    print("=" * 70)

    router = BasicDevice(
        "R1",
        "192.168.10.1",
    )

    router.show_info()
    router.ping()


class DeviceCommands:
    """Demonstrates methods and object state."""

    def __init__(
        self,
        hostname: str,
    ) -> None:

        self.hostname = hostname
        self.commands: list[str] = []

    def add_command(
        self,
        command: str,
    ) -> None:

        self.commands.append(command)

    def show_commands(self) -> None:

        print(
            f"\nCommands for {self.hostname}:"
        )

        for command in self.commands:

            print(
                f"  - {command}"
            )


def part_one_methods_demo() -> None:

    print("\n--- Methods and Object State ---")

    router = DeviceCommands("R1")

    router.add_command(
        "show version"
    )

    router.add_command(
        "show ip interface brief"
    )

    router.show_commands()


# ============================================================
# PART 2
# ENCAPSULATION AND CLASS DESIGN
# ============================================================

class SecureDevice:
    """Demonstrates encapsulation."""

    def __init__(
        self,
        hostname: str,
        username: str,
    ) -> None:

        self.hostname = hostname
        self.username = username
        self._password = ""

    def set_password(
        self,
        password: str,
    ) -> None:

        if len(password) < 6:

            raise ValueError(
                "Password must contain at least 6 characters."
            )

        self._password = password

    def password_configured(self) -> bool:

        return bool(
            self._password
        )

    def show_info(self) -> None:

        print(
            f"Hostname: {self.hostname}"
        )

        print(
            f"Username: {self.username}"
        )

        print(
            "Password configured: "
            f"{self.password_configured()}"
        )


class DeviceWithProperty:
    """Demonstrates the @property decorator."""

    def __init__(
        self,
        hostname: str,
        ip_address: str,
    ) -> None:

        self.hostname = hostname
        self.ip_address = ip_address

    @property
    def ip_address(self) -> str:

        return self._ip_address

    @ip_address.setter
    def ip_address(
        self,
        value: str,
    ) -> None:

        value = value.strip()

        parts = value.split(".")

        if len(parts) != 4:

            raise ValueError(
                f"Invalid IPv4 address: {value}"
            )

        try:

            numbers = [
                int(part)
                for part in parts
            ]

        except ValueError as error:

            raise ValueError(
                f"Invalid IPv4 address: {value}"
            ) from error

        if any(
            number < 0 or number > 255
            for number in numbers
        ):

            raise ValueError(
                f"Invalid IPv4 address: {value}"
            )

        self._ip_address = value

    def show_info(self) -> None:

        print(
            f"{self.hostname} -> "
            f"{self.ip_address}"
        )


class DeviceCounter:
    """Demonstrates a class variable and class method."""

    device_count: ClassVar[int] = 0

    def __init__(
        self,
        hostname: str,
    ) -> None:

        self.hostname = hostname

        DeviceCounter.device_count += 1

    @classmethod
    def total_devices(
        cls,
    ) -> int:

        return cls.device_count


def part_two_demo() -> None:

    print("\n" + "=" * 70)
    print("PART 2 - ENCAPSULATION AND CLASS DESIGN")
    print("=" * 70)

    secure_device = SecureDevice(
        "R1",
        "admin",
    )

    secure_device.set_password(
        "network123"
    )

    secure_device.show_info()

    print("\nProperty Example:")

    device = DeviceWithProperty(
        "SW1",
        "192.168.10.10",
    )

    device.show_info()

    print("\nClass Method Example:")

    DeviceCounter("R1")
    DeviceCounter("SW1")
    DeviceCounter("FW1")

    print(
        f"Total objects: "
        f"{DeviceCounter.total_devices()}"
    )


# ============================================================
# PART 3
# INHERITANCE AND POLYMORPHISM
# ============================================================

class NetworkDevice:
    """
    Base class for ALL network devices.

    This is the ONLY base device model used
    throughout Lesson 20.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        vendor: str,
    ) -> None:

        self.hostname = hostname
        self.ip_address = ip_address
        self.vendor = vendor

        self._connected = False

    @property
    def connected(self) -> bool:

        return self._connected

    def connect(self) -> None:

        self._connected = True

        print(
            f"[CONNECTED] "
            f"{self.hostname} "
            f"({self.ip_address})"
        )

    def disconnect(self) -> None:

        self._connected = False

        print(
            f"[DISCONNECTED] "
            f"{self.hostname}"
        )

    def device_type(self) -> str:

        return "Network Device"

    def execute_command(
        self,
        command: str,
    ) -> str:

        if not self.connected:

            raise RuntimeError(
                f"{self.hostname} "
                "is not connected."
            )

        return (
            f"{self.hostname}: "
            f"executed '{command}'"
        )

    def show_info(self) -> None:

        status = (
            "UP"
            if self.connected
            else "DOWN"
        )

        print(
            f"{self.hostname:<12}"
            f"{self.ip_address:<18}"
            f"{self.device_type():<14}"
            f"{self.vendor:<14}"
            f"{status}"
        )


class NetworkRouter(NetworkDevice):
    """Router derived from NetworkDevice."""

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        vendor: str,
        routing_protocol: str = "OSPF",
    ) -> None:

        super().__init__(
            hostname,
            ip_address,
            vendor,
        )

        self.routing_protocol = (
            routing_protocol
        )

    def device_type(self) -> str:

        return "Router"

    def execute_command(
        self,
        command: str,
    ) -> str:

        if not self.connected:

            raise RuntimeError(
                f"{self.hostname} "
                "is not connected."
            )

        return (
            f"[ROUTER] "
            f"{self.hostname}: "
            f"executed '{command}'"
        )


class NetworkSwitch(NetworkDevice):
    """Switch derived from NetworkDevice."""

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        vendor: str,
        vlan_count: int = 1,
    ) -> None:

        super().__init__(
            hostname,
            ip_address,
            vendor,
        )

        self.vlan_count = vlan_count

    def device_type(self) -> str:

        return "Switch"

    def execute_command(
        self,
        command: str,
    ) -> str:

        if not self.connected:

            raise RuntimeError(
                f"{self.hostname} "
                "is not connected."
            )

        return (
            f"[SWITCH] "
            f"{self.hostname}: "
            f"executed '{command}'"
        )


class NetworkFirewall(NetworkDevice):
    """Firewall derived from NetworkDevice."""

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        vendor: str,
        policy_count: int = 0,
    ) -> None:

        super().__init__(
            hostname,
            ip_address,
            vendor,
        )

        self.policy_count = policy_count

    def device_type(self) -> str:

        return "Firewall"

    def execute_command(
        self,
        command: str,
    ) -> str:

        if not self.connected:

            raise RuntimeError(
                f"{self.hostname} "
                "is not connected."
            )

        return (
            f"[FIREWALL] "
            f"{self.hostname}: "
            f"executed '{command}'"
        )


def part_three_demo() -> None:

    print("\n" + "=" * 70)
    print("PART 3 - INHERITANCE AND POLYMORPHISM")
    print("=" * 70)

    devices: list[NetworkDevice] = [

        NetworkRouter(
            "R1",
            "192.168.10.1",
            "Cisco",
            "OSPF",
        ),

        NetworkSwitch(
            "SW1",
            "192.168.10.10",
            "Cisco",
            50,
        ),

        NetworkFirewall(
            "FW1",
            "192.168.10.254",
            "Fortinet",
            100,
        ),
    ]

    for device in devices:

        device.connect()

        device.show_info()

        print(
            device.execute_command(
                "show version"
            )
        )


# ============================================================
# PART 4
# PROFESSIONAL OOP
# ============================================================

class DeviceInterface:
    """Composition example."""

    def __init__(
        self,
        name: str,
        ip_address: str,
        enabled: bool = True,
    ) -> None:

        self.name = name
        self.ip_address = ip_address
        self.enabled = enabled

    def show_info(self) -> None:

        status = (
            "UP"
            if self.enabled
            else "DOWN"
        )

        print(
            f"{self.name:<24}"
            f"{self.ip_address:<18}"
            f"{status}"
        )


class RouterWithInterfaces(NetworkRouter):
    """Router composed of multiple interfaces."""

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        vendor: str,
    ) -> None:

        super().__init__(
            hostname,
            ip_address,
            vendor,
        )

        self.interfaces: list[
            DeviceInterface
        ] = []

    def add_interface(
        self,
        interface: DeviceInterface,
    ) -> None:

        self.interfaces.append(
            interface
        )

    def show_interfaces(self) -> None:

        print(
            f"\nInterfaces - "
            f"{self.hostname}"
        )

        print("-" * 55)

        for interface in self.interfaces:

            interface.show_info()


class NetworkManager(ABC):
    """Abstract base class."""

    @abstractmethod
    def connect(
        self,
        device: NetworkDevice,
    ) -> None:

        raise NotImplementedError

    @abstractmethod
    def execute_command(
        self,
        device: NetworkDevice,
        command: str,
    ) -> str:

        raise NotImplementedError


class CiscoNetworkManager(
    NetworkManager
):
    """Concrete implementation."""

    def connect(
        self,
        device: NetworkDevice,
    ) -> None:

        device.connect()

    def execute_command(
        self,
        device: NetworkDevice,
        command: str,
    ) -> str:

        return device.execute_command(
            command
        )


@dataclass
class DeviceRecord:
    """Dataclass example."""

    hostname: str
    ip_address: str
    device_type: str
    vendor: str
    tags: list[str] = field(
        default_factory=list
    )


class MonitoringService:
    """
    Demonstrates dependency injection.
    """

    def __init__(
        self,
        manager: NetworkManager,
    ) -> None:

        self.manager = manager

    def check_device(
        self,
        device: NetworkDevice,
    ) -> None:

        self.manager.connect(
            device
        )

        result = (
            self.manager.execute_command(
                device,
                "show status",
            )
        )

        print(result)


def part_four_demo() -> None:

    print("\n" + "=" * 70)
    print("PART 4 - PROFESSIONAL OOP")
    print("=" * 70)

    router = RouterWithInterfaces(
        "R10",
        "10.10.10.1",
        "Cisco",
    )

    router.add_interface(
        DeviceInterface(
            "GigabitEthernet0/0",
            "10.10.10.1",
        )
    )

    router.add_interface(
        DeviceInterface(
            "GigabitEthernet0/1",
            "10.10.20.1",
        )
    )

    router.connect()

    router.show_interfaces()

    record = DeviceRecord(
        hostname="R10",
        ip_address="10.10.10.1",
        device_type="Router",
        vendor="Cisco",
        tags=[
            "core",
            "production",
        ],
    )

    print(
        "\nDataclass:"
    )

    print(record)

    manager = CiscoNetworkManager()

    monitor = MonitoringService(
        manager
    )

    monitor.check_device(
        router
    )


# ============================================================
# PART 5
# FINAL PROJECT
# NETWORK DEVICE MANAGEMENT SYSTEM
# ============================================================

class DeviceManagementError(
    Exception
):
    """Base project exception."""


class DeviceAlreadyExistsError(
    DeviceManagementError
):
    """Duplicate hostname."""


class DeviceNotFoundError(
    DeviceManagementError
):
    """Device was not found."""


class DeviceInventory:
    """
    Central device inventory.

    IMPORTANT:
    It stores NetworkDevice objects only.
    """

    def __init__(self) -> None:

        self._devices: dict[
            str,
            NetworkDevice,
        ] = {}

    @property
    def device_count(self) -> int:

        return len(
            self._devices
        )

    def add_device(
        self,
        device: NetworkDevice,
    ) -> None:

        if (
            device.hostname
            in self._devices
        ):

            raise DeviceAlreadyExistsError(
                f"Device '{device.hostname}' "
                "already exists."
            )

        self._devices[
            device.hostname
        ] = device

        print(
            f"[INVENTORY] "
            f"Added {device.hostname}"
        )

    def get_device(
        self,
        hostname: str,
    ) -> NetworkDevice:

        if (
            hostname
            not in self._devices
        ):

            raise DeviceNotFoundError(
                f"Device '{hostname}' "
                "not found."
            )

        return self._devices[
            hostname
        ]

    def remove_device(
        self,
        hostname: str,
    ) -> None:

        if (
            hostname
            not in self._devices
        ):

            raise DeviceNotFoundError(
                f"Device '{hostname}' "
                "not found."
            )

        del self._devices[
            hostname
        ]

    def get_all_devices(
        self,
    ) -> list[NetworkDevice]:

        return list(
            self._devices.values()
        )

    def find_by_type(
        self,
        device_type: str,
    ) -> list[NetworkDevice]:

        return [
            device
            for device
            in self._devices.values()
            if (
                device.device_type().lower()
                == device_type.lower()
            )
        ]

    def show_inventory(self) -> None:

        print(
            "\nNetwork Device Inventory"
        )

        print("-" * 75)

        print(
            f"{'Hostname':<12}"
            f"{'IP Address':<18}"
            f"{'Type':<14}"
            f"{'Vendor':<14}"
            f"Status"
        )

        print("-" * 75)

        for device in (
            self._devices.values()
        ):

            status = (
                "UP"
                if device.connected
                else "DOWN"
            )

            print(
                f"{device.hostname:<12}"
                f"{device.ip_address:<18}"
                f"{device.device_type():<14}"
                f"{device.vendor:<14}"
                f"{status}"
            )


class NetworkMonitor:
    """Network monitoring service."""

    def __init__(
        self,
        inventory: DeviceInventory,
    ) -> None:

        self.inventory = inventory

    def check_device(
        self,
        device: NetworkDevice,
    ) -> str:

        return (
            "UP"
            if device.connected
            else "DOWN"
        )

    def monitor_all(self) -> None:

        print(
            "\nNetwork Monitoring"
        )

        print("-" * 45)

        for device in (
            self.inventory.get_all_devices()
        ):

            print(
                f"{device.hostname:<12}"
                f"{self.check_device(device)}"
            )


class NetworkAutomationService:
    """Network automation service."""

    def __init__(
        self,
        inventory: DeviceInventory,
    ) -> None:

        self.inventory = inventory

    def execute_on_device(
        self,
        hostname: str,
        command: str,
    ) -> None:

        try:

            device = (
                self.inventory.get_device(
                    hostname
                )
            )

            if not device.connected:

                device.connect()

            print(
                device.execute_command(
                    command
                )
            )

        except (
            DeviceManagementError,
            RuntimeError,
        ) as error:

            print(
                f"[ERROR] {error}"
            )

    def execute_on_all(
        self,
        command: str,
    ) -> None:

        print(
            "\nAutomation - All Devices"
        )

        print("-" * 55)

        for device in (
            self.inventory.get_all_devices()
        ):

            try:

                if not device.connected:

                    device.connect()

                print(
                    device.execute_command(
                        command
                    )
                )

            except RuntimeError as error:

                print(
                    f"[ERROR] {error}"
                )


class ConfigurationBackupService:
    """Configuration backup service."""

    def __init__(
        self,
        inventory: DeviceInventory,
    ) -> None:

        self.inventory = inventory

    def backup_device(
        self,
        hostname: str,
    ) -> str:

        device = (
            self.inventory.get_device(
                hostname
            )
        )

        timestamp = (
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

        return (
            f"Backup created for "
            f"{device.hostname} "
            f"at {timestamp}"
        )

    def backup_all(self) -> None:

        print(
            "\nConfiguration Backups"
        )

        print("-" * 55)

        for device in (
            self.inventory.get_all_devices()
        ):

            try:

                print(
                    self.backup_device(
                        device.hostname
                    )
                )

            except DeviceManagementError as error:

                print(
                    f"[ERROR] {error}"
                )


class DeviceFactory:
    """
    Factory Pattern.

    Creates the correct NetworkDevice
    subclass from a device type.
    """

    @staticmethod
    def create(
        device_type: str,
        hostname: str,
        ip_address: str,
        vendor: str,
        **kwargs,
    ) -> NetworkDevice:

        device_type = (
            device_type.strip().lower()
        )

        if device_type == "router":

            return NetworkRouter(
                hostname,
                ip_address,
                vendor,
                kwargs.get(
                    "routing_protocol",
                    "OSPF",
                ),
            )

        if device_type == "switch":

            return NetworkSwitch(
                hostname,
                ip_address,
                vendor,
                kwargs.get(
                    "vlan_count",
                    1,
                ),
            )

        if device_type == "firewall":

            return NetworkFirewall(
                hostname,
                ip_address,
                vendor,
                kwargs.get(
                    "policy_count",
                    0,
                ),
            )

        raise ValueError(
            f"Unsupported device type: "
            f"{device_type}"
        )


def build_inventory() -> DeviceInventory:

    inventory = DeviceInventory()

    devices = [

        DeviceFactory.create(
            "router",
            "R1",
            "192.168.10.1",
            "Cisco",
            routing_protocol="OSPF",
        ),

        DeviceFactory.create(
            "router",
            "R2",
            "192.168.20.1",
            "Cisco",
            routing_protocol="EIGRP",
        ),

        DeviceFactory.create(
            "switch",
            "SW1",
            "192.168.10.10",
            "Cisco",
            vlan_count=50,
        ),

        DeviceFactory.create(
            "firewall",
            "FW1",
            "192.168.10.254",
            "Fortinet",
            policy_count=120,
        ),
    ]

    for device in devices:

        inventory.add_device(
            device
        )

    return inventory


def final_inventory_demo(
    inventory: DeviceInventory,
) -> None:

    print("\n" + "=" * 70)
    print(
        "FINAL PROJECT - "
        "NETWORK DEVICE MANAGEMENT SYSTEM"
    )
    print("=" * 70)

    print(
        f"\nTotal Devices: "
        f"{inventory.device_count}"
    )

    inventory.show_inventory()


def final_connection_demo(
    inventory: DeviceInventory,
) -> None:

    print(
        "\nDevice Connections"
    )

    print("-" * 45)

    for device in (
        inventory.get_all_devices()
    ):

        device.connect()


def final_monitoring_demo(
    inventory: DeviceInventory,
) -> None:

    monitor = NetworkMonitor(
        inventory
    )

    monitor.monitor_all()


def final_automation_demo(
    inventory: DeviceInventory,
) -> None:

    automation = (
        NetworkAutomationService(
            inventory
        )
    )

    automation.execute_on_device(
        "R1",
        "show ip interface brief",
    )

    automation.execute_on_all(
        "show version",
    )


def final_backup_demo(
    inventory: DeviceInventory,
) -> None:

    backup = (
        ConfigurationBackupService(
            inventory
        )
    )

    backup.backup_all()


def final_search_demo(
    inventory: DeviceInventory,
) -> None:

    print(
        "\nRouter Search"
    )

    print("-" * 45)

    routers = (
        inventory.find_by_type(
            "Router"
        )
    )

    for router in routers:

        print(
            f"{router.hostname} | "
            f"{router.ip_address} | "
            f"{router.vendor}"
        )


def final_error_demo(
    inventory: DeviceInventory,
) -> None:

    print(
        "\nError Handling"
    )

    print("-" * 45)

    try:

        inventory.get_device(
            "UNKNOWN"
        )

    except DeviceNotFoundError as error:

        print(
            f"[EXPECTED ERROR] "
            f"{error}"
        )

    try:

        duplicate = (
            DeviceFactory.create(
                "router",
                "R1",
                "10.10.10.1",
                "Cisco",
            )
        )

        inventory.add_device(
            duplicate
        )

    except DeviceAlreadyExistsError as error:

        print(
            f"[EXPECTED ERROR] "
            f"{error}"
        )

    try:

        DeviceFactory.create(
            "unsupported",
            "DEV1",
            "10.10.10.10",
            "Unknown",
        )

    except ValueError as error:

        print(
            f"[EXPECTED ERROR] "
            f"{error}"
        )


def final_polymorphism_demo(
    inventory: DeviceInventory,
) -> None:

    print(
        "\nPolymorphism"
    )

    print("-" * 45)

    command = (
        "show system information"
    )

    for device in (
        inventory.get_all_devices()
    ):

        try:

            print(
                device.execute_command(
                    command
                )
            )

        except RuntimeError as error:

            print(
                f"[ERROR] {error}"
            )


def final_project_summary() -> None:

    print("\n" + "=" * 70)
    print("LESSON 20 - FINAL SUMMARY")
    print("=" * 70)

    concepts = [

        "Classes and Objects",

        "Instance Methods",

        "Encapsulation",

        "Properties",

        "Class Variables",

        "Class Methods",

        "Inheritance",

        "Method Overriding",

        "Polymorphism",

        "Composition",

        "Abstract Base Classes",

        "Dataclasses",

        "Type Hints",

        "Custom Exceptions",

        "Factory Pattern",

        "Dependency Injection",

        "Device Inventory",

        "Network Monitoring",

        "Network Automation",

        "Configuration Backup",
    ]

    for number, concept in enumerate(
        concepts,
        start=1,
    ):

        print(
            f"{number:02d}. {concept}"
        )


def run_part_five() -> None:

    inventory = (
        build_inventory()
    )

    final_inventory_demo(
        inventory
    )

    final_connection_demo(
        inventory
    )

    final_monitoring_demo(
        inventory
    )

    final_automation_demo(
        inventory
    )

    final_backup_demo(
        inventory
    )

    final_search_demo(
        inventory
    )

    final_polymorphism_demo(
        inventory
    )

    final_error_demo(
        inventory
    )

    final_project_summary()


# ============================================================
# MAIN
# ============================================================

def main() -> None:
    """
    Single entry point for Lesson 20.
    """

    print("\n" + "#" * 70)

    print(
        "LESSON 20 - "
        "OBJECT-ORIENTED PROGRAMMING"
    )

    print("#" * 70)

    # Part 1
    part_one_basic_class_demo()
    part_one_methods_demo()

    # Part 2
    part_two_demo()

    # Part 3
    part_three_demo()

    # Part 4
    part_four_demo()

    # Part 5
    run_part_five()

    print("\n" + "#" * 70)

    print(
        "LESSON 20 COMPLETED SUCCESSFULLY"
    )

    print("#" * 70)


if __name__ == "__main__":
    main()
