"""
Lesson 21 - Dataclasses
Part 2 - Defaults, field() and default_factory

Author: Mohammed AL-Dubai
Roadmap: python-professional-roadmap
Stage: 03_intermediate_python
"""

from dataclasses import dataclass, field
from typing import Optional


# ============================================================
# 1. DEFAULT VALUES
# ============================================================

@dataclass
class NetworkDevice:
    """Network device with default values."""

    hostname: str
    ip_address: str
    vendor: str = "Cisco"
    device_type: str = "Router"
    enabled: bool = True


def default_values_demo() -> None:
    print("\n" + "=" * 65)
    print("1. DEFAULT VALUES")
    print("=" * 65)

    device1 = NetworkDevice(
        hostname="R1",
        ip_address="192.168.10.1",
    )

    device2 = NetworkDevice(
        hostname="FW1",
        ip_address="192.168.10.254",
        vendor="Fortinet",
        device_type="Firewall",
        enabled=False,
    )

    print(device1)
    print(device2)


# ============================================================
# 2. field() WITH DEFAULT VALUE
# ============================================================

@dataclass
class DeviceConfiguration:
    """Demonstrates field() with metadata and defaults."""

    hostname: str
    management_ip: str
    username: str = "admin"
    ssh_port: int = field(default=22)
    timeout: int = field(default=10)


def field_default_demo() -> None:
    print("\n" + "=" * 65)
    print("2. field() WITH DEFAULT VALUES")
    print("=" * 65)

    config = DeviceConfiguration(
        hostname="R1",
        management_ip="192.168.10.1",
    )

    print(f"Hostname:       {config.hostname}")
    print(f"Management IP:  {config.management_ip}")
    print(f"Username:       {config.username}")
    print(f"SSH Port:       {config.ssh_port}")
    print(f"Timeout:        {config.timeout}")


# ============================================================
# 3. default_factory FOR LISTS
# ============================================================

@dataclass
class NetworkDeviceWithTags:
    """Demonstrates safe mutable defaults."""

    hostname: str
    ip_address: str
    tags: list[str] = field(default_factory=list)


def default_factory_list_demo() -> None:
    print("\n" + "=" * 65)
    print("3. default_factory() WITH LIST")
    print("=" * 65)

    router = NetworkDeviceWithTags(
        "R1",
        "192.168.10.1",
    )

    switch = NetworkDeviceWithTags(
        "SW1",
        "192.168.10.10",
    )

    router.tags.append("core")
    router.tags.append("production")

    switch.tags.append("access")

    print(f"{router.hostname}: {router.tags}")
    print(f"{switch.hostname}: {switch.tags}")

    print("\nEach object has its own independent list.")


# ============================================================
# 4. default_factory FOR DICTIONARIES
# ============================================================

@dataclass
class DeviceInventoryRecord:
    """Dataclass containing a dictionary."""

    hostname: str
    ip_address: str
    interfaces: dict[str, str] = field(
        default_factory=dict
    )


def default_factory_dict_demo() -> None:
    print("\n" + "=" * 65)
    print("4. default_factory() WITH DICTIONARY")
    print("=" * 65)

    router = DeviceInventoryRecord(
        "R1",
        "192.168.10.1",
    )

    switch = DeviceInventoryRecord(
        "SW1",
        "192.168.10.10",
    )

    router.interfaces["Gi0/0"] = "10.10.10.1"
    router.interfaces["Gi0/1"] = "10.10.20.1"

    switch.interfaces["Gi0/1"] = "192.168.10.10"

    print(f"{router.hostname}:")
    print(router.interfaces)

    print(f"\n{switch.hostname}:")
    print(switch.interfaces)


# ============================================================
# 5. OPTIONAL FIELDS
# ============================================================

@dataclass
class DeviceContact:
    """Demonstrates Optional values."""

    hostname: str
    ip_address: str
    location: Optional[str] = None
    contact: Optional[str] = None


def optional_fields_demo() -> None:
    print("\n" + "=" * 65)
    print("5. OPTIONAL FIELDS")
    print("=" * 65)

    device1 = DeviceContact(
        hostname="R1",
        ip_address="192.168.10.1",
    )

    device2 = DeviceContact(
        hostname="SW1",
        ip_address="192.168.10.10",
        location="Data Center A",
        contact="NOC Team",
    )

    print(device1)
    print(device2)


# ============================================================
# 6. DEVICE INVENTORY USING default_factory
# ============================================================

@dataclass
class Inventory:
    """Simple network device inventory."""

    name: str
    devices: list[NetworkDeviceWithTags] = field(
        default_factory=list
    )

    def add_device(
        self,
        device: NetworkDeviceWithTags,
    ) -> None:
        self.devices.append(device)

    def show_devices(self) -> None:
        print(f"\nInventory: {self.name}")
        print("-" * 50)

        for device in self.devices:
            print(
                f"{device.hostname:<10}"
                f"{device.ip_address:<18}"
                f"{device.tags}"
            )


def inventory_demo() -> None:
    print("\n" + "=" * 65)
    print("6. NETWORK DEVICE INVENTORY")
    print("=" * 65)

    inventory = Inventory(
        name="HomeLab"
    )

    inventory.add_device(
        NetworkDeviceWithTags(
            "R1",
            "192.168.10.1",
            ["router", "core"],
        )
    )

    inventory.add_device(
        NetworkDeviceWithTags(
            "SW1",
            "192.168.10.10",
            ["switch", "access"],
        )
    )

    inventory.add_device(
        NetworkDeviceWithTags(
            "FW1",
            "192.168.10.254",
            ["firewall", "security"],
        )
    )

    inventory.show_devices()


# ============================================================
# 7. WHY NOT USE [] DIRECTLY?
# ============================================================

def mutable_default_explanation() -> None:
    print("\n" + "=" * 65)
    print("7. SAFE MUTABLE DEFAULTS")
    print("=" * 65)

    print(
        "Do not use mutable defaults such as [] or {} "
        "for dataclass fields."
    )

    print(
        "Use field(default_factory=list) "
        "for lists."
    )

    print(
        "Use field(default_factory=dict) "
        "for dictionaries."
    )

    print("\nRecommended:")
    print(
        "tags: list[str] = "
        "field(default_factory=list)"
    )

    print(
        "interfaces: dict[str, str] = "
        "field(default_factory=dict)"
    )


# ============================================================
# 8. PRACTICE EXERCISE
# ============================================================

@dataclass
class NetworkProject:
    """
    Practice exercise.

    Create a project object with:
        name
        description
        devices
        technologies
    """

    name: str
    description: str
    devices: list[str] = field(
        default_factory=list
    )
    technologies: list[str] = field(
        default_factory=list
    )


def exercise_demo() -> None:
    print("\n" + "=" * 65)
    print("8. PRACTICE EXERCISE")
    print("=" * 65)

    project = NetworkProject(
        name="Enterprise Lab",
        description="Enterprise network automation lab",
    )

    project.devices.extend(
        [
            "R1",
            "R2",
            "SW1",
            "SW2",
            "FW1",
        ]
    )

    project.technologies.extend(
        [
            "OSPF",
            "VLAN",
            "HSRP",
            "SSH",
            "Python",
        ]
    )

    print(f"Project: {project.name}")
    print(f"Description: {project.description}")
    print(f"Devices: {project.devices}")
    print(
        f"Technologies: "
        f"{project.technologies}"
    )


# ============================================================
# MAIN
# ============================================================

def main() -> None:
    print("\n" + "#" * 65)
    print("LESSON 21 - DATACLASSES")
    print("PART 2 - DEFAULTS, field() & default_factory")
    print("#" * 65)

    default_values_demo()
    field_default_demo()
    default_factory_list_demo()
    default_factory_dict_demo()
    optional_fields_demo()
    inventory_demo()
    mutable_default_explanation()
    exercise_demo()

    print("\n" + "#" * 65)
    print("PART 2 COMPLETED")
    print("#" * 65)


if __name__ == "__main__":
    main()
