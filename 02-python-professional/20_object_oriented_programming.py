# =============================================================================
# LESSON 20 - OBJECT-ORIENTED PROGRAMMING
# PART 1 - OOP FUNDAMENTALS
# =============================================================================

"""
Lesson 20 - Object-Oriented Programming (OOP)

Part 1 Objectives
-----------------

- Understand classes
- Understand objects
- Understand attributes
- Understand methods
- Understand self
- Understand __init__()
- Create multiple objects
- Build a simple Network Device class
"""


# =============================================================================
# SECTION 01 - Simple Class
# =============================================================================


class Computer:
    """
    A simple Computer class.
    """

    pass


# =============================================================================
# SECTION 02 - Creating an Object
# =============================================================================


def simple_class_demo() -> None:
    """
    Demonstrates creating an object
    from a class.
    """

    print("\nSimple Class")
    print("-" * 40)

    computer = Computer()

    print(
        f"Object type: {type(computer)}"
    )

    print(
        f"Object created: {computer}"
    )


# =============================================================================
# SECTION 03 - Class with Attributes
# =============================================================================


class NetworkDevice:
    """
    Represents a basic network device.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        device_type: str
    ) -> None:

        self.hostname = hostname
        self.ip_address = ip_address
        self.device_type = device_type


# =============================================================================
# SECTION 04 - Network Device Object
# =============================================================================


def network_device_object_demo() -> None:
    """
    Demonstrates creating a NetworkDevice object.
    """

    print("\nNetwork Device Object")
    print("-" * 40)

    router = NetworkDevice(
        hostname="R1",
        ip_address="192.168.10.1",
        device_type="Router"
    )

    print(
        f"Hostname    : {router.hostname}"
    )

    print(
        f"IP Address  : {router.ip_address}"
    )

    print(
        f"Device Type : {router.device_type}"
    )


# =============================================================================
# SECTION 05 - Understanding self
# =============================================================================


class Device:
    """
    Demonstrates the use of self.
    """

    def __init__(
        self,
        hostname: str
    ) -> None:

        self.hostname = hostname

    def show_hostname(
        self
    ) -> None:

        print(
            f"Hostname: {self.hostname}"
        )


# =============================================================================
# SECTION 06 - self Demo
# =============================================================================


def self_demo() -> None:
    """
    Demonstrates self inside a class.
    """

    print("\nUnderstanding self")
    print("-" * 40)

    device = Device(
        "R1"
    )

    device.show_hostname()


# =============================================================================
# SECTION 07 - Methods
# =============================================================================


class NetworkDeviceWithMethods:
    """
    Network device with methods.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str
    ) -> None:

        self.hostname = hostname
        self.ip_address = ip_address
        self.status = "Offline"

    def connect(
        self
    ) -> None:

        self.status = "Online"

        print(
            f"{self.hostname} "
            f"connected successfully."
        )

    def disconnect(
        self
    ) -> None:

        self.status = "Offline"

        print(
            f"{self.hostname} "
            f"disconnected."
        )

    def show_status(
        self
    ) -> None:

        print(
            f"{self.hostname} "
            f"({self.ip_address}) "
            f"Status: {self.status}"
        )


# =============================================================================
# SECTION 08 - Methods Demo
# =============================================================================


def methods_demo() -> None:
    """
    Demonstrates object methods.
    """

    print("\nObject Methods")
    print("-" * 40)

    device = NetworkDeviceWithMethods(
        hostname="R1",
        ip_address="192.168.10.1"
    )

    device.show_status()

    device.connect()

    device.show_status()

    device.disconnect()

    device.show_status()


# =============================================================================
# SECTION 09 - Multiple Objects
# =============================================================================


def multiple_objects_demo() -> None:
    """
    Demonstrates creating multiple objects
    from the same class.
    """

    print("\nMultiple Objects")
    print("-" * 40)

    router = NetworkDevice(
        hostname="R1",
        ip_address="192.168.10.1",
        device_type="Router"
    )

    switch = NetworkDevice(
        hostname="SW1",
        ip_address="192.168.10.10",
        device_type="Switch"
    )

    firewall = NetworkDevice(
        hostname="FW1",
        ip_address="192.168.10.254",
        device_type="Firewall"
    )

    devices = [
        router,
        switch,
        firewall
    ]

    for device in devices:

        print(
            f"{device.hostname:<8}"
            f"{device.ip_address:<18}"
            f"{device.device_type}"
        )


# =============================================================================
# SECTION 10 - Object State
# =============================================================================


class DeviceState:
    """
    Demonstrates changing object state.
    """

    def __init__(
        self,
        hostname: str
    ) -> None:

        self.hostname = hostname
        self.status = "Offline"
        self.connection_count = 0

    def connect(
        self
    ) -> None:

        self.status = "Online"

        self.connection_count += 1

    def disconnect(
        self
    ) -> None:

        self.status = "Offline"


# =============================================================================
# SECTION 11 - Object State Demo
# =============================================================================


def object_state_demo() -> None:
    """
    Demonstrates object state changes.
    """

    print("\nObject State")
    print("-" * 40)

    device = DeviceState(
        "R1"
    )

    print(
        f"Status: {device.status}"
    )

    print(
        f"Connections: "
        f"{device.connection_count}"
    )

    device.connect()

    print(
        f"Status: {device.status}"
    )

    print(
        f"Connections: "
        f"{device.connection_count}"
    )

    device.disconnect()

    print(
        f"Status: {device.status}"
    )


# =============================================================================
# SECTION 12 - Method with Parameters
# =============================================================================


class CommandDevice:
    """
    Demonstrates methods with parameters.
    """

    def __init__(
        self,
        hostname: str
    ) -> None:

        self.hostname = hostname

    def execute_command(
        self,
        command: str
    ) -> None:

        print(
            f"{self.hostname} "
            f"executing: {command}"
        )


# =============================================================================
# SECTION 13 - Method Parameters Demo
# =============================================================================


def method_parameters_demo() -> None:
    """
    Demonstrates passing parameters
    to object methods.
    """

    print("\nMethod Parameters")
    print("-" * 40)

    device = CommandDevice(
        "R1"
    )

    device.execute_command(
        "show ip interface brief"
    )

    device.execute_command(
        "show running-config"
    )

    device.execute_command(
        "show version"
    )


# =============================================================================
# SECTION 14 - Returning Values
# =============================================================================


class NetworkCalculator:
    """
    Demonstrates methods returning values.
    """

    def __init__(
        self,
        hostname: str
    ) -> None:

        self.hostname = hostname

    def get_device_info(
        self
    ) -> str:

        return (
            f"Network Device: "
            f"{self.hostname}"
        )


# =============================================================================
# SECTION 15 - Return Values Demo
# =============================================================================


def return_values_demo() -> None:
    """
    Demonstrates returning data
    from methods.
    """

    print("\nReturning Values")
    print("-" * 40)

    device = NetworkCalculator(
        "R1"
    )

    information = (
        device.get_device_info()
    )

    print(
        information
    )


# =============================================================================
# SECTION 16 - Object Representation
# =============================================================================


class DeviceInfo:
    """
    Demonstrates a basic object
    information method.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        vendor: str
    ) -> None:

        self.hostname = hostname
        self.ip_address = ip_address
        self.vendor = vendor

    def show_info(
        self
    ) -> None:

        print(
            "\nDevice Information"
        )

        print(
            f"Hostname   : {self.hostname}"
        )

        print(
            f"IP Address : {self.ip_address}"
        )

        print(
            f"Vendor     : {self.vendor}"
        )


# =============================================================================
# SECTION 17 - Object Information Demo
# =============================================================================


def object_information_demo() -> None:
    """
    Demonstrates object information.
    """

    print("\nObject Information")
    print("-" * 40)

    device = DeviceInfo(
        hostname="R1",
        ip_address="192.168.10.1",
        vendor="Cisco"
    )

    device.show_info()


# =============================================================================
# SECTION 18 - Network Device Inventory
# =============================================================================


class DeviceInventory:
    """
    Stores network device objects.
    """

    def __init__(
        self
    ) -> None:

        self.devices: list[
            NetworkDevice
        ] = []

    def add_device(
        self,
        device: NetworkDevice
    ) -> None:

        self.devices.append(
            device
        )

    def show_inventory(
        self
    ) -> None:

        print(
            "\nNetwork Inventory"
        )

        print(
            "-" * 50
        )

        for device in self.devices:

            print(
                f"{device.hostname:<10}"
                f"{device.ip_address:<18}"
                f"{device.device_type}"
            )


# =============================================================================
# SECTION 19 - Inventory Demo
# =============================================================================


def inventory_demo() -> None:
    """
    Demonstrates object-based inventory.
    """

    print("\nDevice Inventory")
    print("-" * 40)

    inventory = DeviceInventory()

    inventory.add_device(
        NetworkDevice(
            "R1",
            "192.168.10.1",
            "Router"
        )
    )

    inventory.add_device(
        NetworkDevice(
            "R2",
            "192.168.10.2",
            "Router"
        )
    )

    inventory.add_device(
        NetworkDevice(
            "SW1",
            "192.168.10.10",
            "Switch"
        )
    )

    inventory.add_device(
        NetworkDevice(
            "FW1",
            "192.168.10.254",
            "Firewall"
        )
    )

    inventory.show_inventory()


# =============================================================================
# SECTION 20 - Comparing Objects
# =============================================================================


class SimpleDevice:
    """
    Simple device class for comparison.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str
    ) -> None:

        self.hostname = hostname
        self.ip_address = ip_address


# =============================================================================
# SECTION 21 - Object Comparison Demo
# =============================================================================


def object_comparison_demo() -> None:
    """
    Demonstrates that separate objects
    can contain different state.
    """

    print("\nObject Comparison")
    print("-" * 40)

    device_one = SimpleDevice(
        "R1",
        "192.168.10.1"
    )

    device_two = SimpleDevice(
        "R2",
        "192.168.10.2"
    )

    print(
        f"Device 1: "
        f"{device_one.hostname} "
        f"{device_one.ip_address}"
    )

    print(
        f"Device 2: "
        f"{device_two.hostname} "
        f"{device_two.ip_address}"
    )

    print(
        f"Same object? "
        f"{device_one is device_two}"
    )


# =============================================================================
# SECTION 22 - OOP Workflow Demo
# =============================================================================


def oop_workflow_demo() -> None:
    """
    Demonstrates the basic OOP workflow.
    """

    print("\nOOP Workflow")
    print("-" * 40)

    print(
        "1. Define a class"
    )

    print(
        "2. Create an object"
    )

    print(
        "3. Initialize object attributes"
    )

    print(
        "4. Call object methods"
    )

    print(
        "5. Change object state"
    )

    print(
        "6. Read object data"
    )


# =============================================================================
# SECTION 23 - Part One Runner
# =============================================================================


def run_part_one() -> None:
    """
    Runs Lesson 20 Part One.
    """

    print(
        "\n" + "=" * 70
    )

    print(
        "LESSON 20 - "
        "OBJECT-ORIENTED PROGRAMMING"
    )

    print(
        "PART 1 - OOP FUNDAMENTALS"
    )

    print(
        "=" * 70
    )

    simple_class_demo()

    network_device_object_demo()

    self_demo()

    methods_demo()

    multiple_objects_demo()

    object_state_demo()

    method_parameters_demo()

    return_values_demo()

    object_information_demo()

    inventory_demo()

    object_comparison_demo()

    oop_workflow_demo()


# =============================================================================
# END OF PART 1
# =============================================================================

# =============================================================================
# LESSON 20 - PART 2
# ENCAPSULATION & CLASS DESIGN
# =============================================================================

"""
Part 2 Objectives
-----------------

- Understand instance attributes
- Understand class attributes
- Use class methods
- Use static methods
- Understand encapsulation
- Use properties
- Use setters for validation
- Design reusable network classes
"""


# =============================================================================
# SECTION 24 - Instance Attributes
# =============================================================================


class Router:
    """
    Demonstrates instance attributes.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str
    ) -> None:

        self.hostname = hostname
        self.ip_address = ip_address


# =============================================================================
# SECTION 25 - Instance Attributes Demo
# =============================================================================


def instance_attributes_demo() -> None:
    """
    Demonstrates that every object has
    its own instance attributes.
    """

    print("\nInstance Attributes")
    print("-" * 40)

    router_one = Router(
        "R1",
        "192.168.10.1"
    )

    router_two = Router(
        "R2",
        "192.168.10.2"
    )

    print(
        f"{router_one.hostname}: "
        f"{router_one.ip_address}"
    )

    print(
        f"{router_two.hostname}: "
        f"{router_two.ip_address}"
    )

    router_one.ip_address = (
        "10.10.10.1"
    )

    print(
        "\nAfter changing R1:"
    )

    print(
        f"R1: {router_one.ip_address}"
    )

    print(
        f"R2: {router_two.ip_address}"
    )


# =============================================================================
# SECTION 26 - Class Attributes
# =============================================================================


class NetworkDeviceBase:
    """
    Demonstrates class attributes.
    """

    device_count = 0

    vendor = "Cisco"

    def __init__(
        self,
        hostname: str,
        ip_address: str
    ) -> None:

        self.hostname = hostname
        self.ip_address = ip_address

        NetworkDeviceBase.device_count += 1


# =============================================================================
# SECTION 27 - Class Attribute Demo
# =============================================================================


def class_attributes_demo() -> None:
    """
    Demonstrates class-level attributes.
    """

    print("\nClass Attributes")
    print("-" * 40)

    print(
        f"Vendor: "
        f"{NetworkDeviceBase.vendor}"
    )

    print(
        f"Devices before creation: "
        f"{NetworkDeviceBase.device_count}"
    )

    router_one = NetworkDeviceBase(
        "R1",
        "192.168.10.1"
    )

    router_two = NetworkDeviceBase(
        "R2",
        "192.168.10.2"
    )

    print(
        f"Devices after creation: "
        f"{NetworkDeviceBase.device_count}"
    )

    print(
        f"R1 vendor: {router_one.vendor}"
    )

    print(
        f"R2 vendor: {router_two.vendor}"
    )


# =============================================================================
# SECTION 28 - Class Method
# =============================================================================


class DeviceCounter:
    """
    Demonstrates a class method.
    """

    device_count = 0

    def __init__(
        self,
        hostname: str
    ) -> None:

        self.hostname = hostname

        DeviceCounter.device_count += 1

    @classmethod
    def get_device_count(
        cls
    ) -> int:

        return cls.device_count


# =============================================================================
# SECTION 29 - Class Method Demo
# =============================================================================


def class_method_demo() -> None:
    """
    Demonstrates @classmethod.
    """

    print("\nClass Method")
    print("-" * 40)

    DeviceCounter(
        "R1"
    )

    DeviceCounter(
        "R2"
    )

    DeviceCounter(
        "SW1"
    )

    count = (
        DeviceCounter.get_device_count()
    )

    print(
        f"Total devices: {count}"
    )


# =============================================================================
# SECTION 30 - Alternative Constructor
# =============================================================================


class ManagedDevice:
    """
    Demonstrates an alternative constructor
    using @classmethod.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        username: str
    ) -> None:

        self.hostname = hostname
        self.ip_address = ip_address
        self.username = username

    @classmethod
    def from_string(
        cls,
        data: str
    ) -> "ManagedDevice":
        """
        Creates an object from:

        hostname,ip_address,username
        """

        hostname, ip_address, username = (
            item.strip()
            for item in data.split(",")
        )

        return cls(
            hostname,
            ip_address,
            username
        )


# =============================================================================
# SECTION 31 - Alternative Constructor Demo
# =============================================================================


def alternative_constructor_demo() -> None:
    """
    Demonstrates creating an object
    using a class method.
    """

    print("\nAlternative Constructor")
    print("-" * 40)

    device = (
        ManagedDevice.from_string(
            "R1,192.168.10.1,admin"
        )
    )

    print(
        f"Hostname   : {device.hostname}"
    )

    print(
        f"IP Address : {device.ip_address}"
    )

    print(
        f"Username   : {device.username}"
    )


# =============================================================================
# SECTION 32 - Static Method
# =============================================================================


class NetworkUtilities:
    """
    Demonstrates static methods.
    """

    @staticmethod
    def is_valid_ip(
        ip_address: str
    ) -> bool:

        try:

            ipaddress.ip_address(
                ip_address
            )

            return True

        except ValueError:

            return False

    @staticmethod
    def normalize_hostname(
        hostname: str
    ) -> str:

        return hostname.strip().upper()


# =============================================================================
# SECTION 33 - Static Method Demo
# =============================================================================


def static_method_demo() -> None:
    """
    Demonstrates @staticmethod.
    """

    print("\nStatic Methods")
    print("-" * 40)

    ip_addresses = [
        "192.168.10.1",
        "10.0.0.1",
        "999.1.1.1",
        "192.168.1.300"
    ]

    for ip_address in ip_addresses:

        result = (
            NetworkUtilities.is_valid_ip(
                ip_address
            )
        )

        print(
            f"{ip_address:<18}"
            f" -> {result}"
        )

    hostname = (
        NetworkUtilities.normalize_hostname(
            "  router-01  "
        )
    )

    print(
        f"\nNormalized hostname: "
        f"{hostname}"
    )


# =============================================================================
# SECTION 34 - Encapsulation
# =============================================================================


class SecureDevice:
    """
    Demonstrates basic encapsulation.

    The underscore indicates that the attribute
    is intended for internal class usage.
    """

    def __init__(
        self,
        hostname: str,
        username: str
    ) -> None:

        self.hostname = hostname
        self._username = username

    def get_username(
        self
    ) -> str:

        return self._username


# =============================================================================
# SECTION 35 - Encapsulation Demo
# =============================================================================


def encapsulation_demo() -> None:
    """
    Demonstrates encapsulation.
    """

    print("\nEncapsulation")
    print("-" * 40)

    device = SecureDevice(
        hostname="R1",
        username="admin"
    )

    print(
        f"Hostname: {device.hostname}"
    )

    print(
        f"Username: "
        f"{device.get_username()}"
    )


# =============================================================================
# SECTION 36 - Property
# =============================================================================


class ValidatedDevice:
    """
    Demonstrates @property.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str
    ) -> None:

        self.hostname = hostname
        self._ip_address = ""

        self.ip_address = ip_address

    @property
    def ip_address(
        self
    ) -> str:

        return self._ip_address

    @ip_address.setter
    def ip_address(
        self,
        value: str
    ) -> None:

        try:

            ipaddress.ip_address(
                value
            )

        except ValueError as error:

            raise ValueError(
                f"Invalid IP address: "
                f"{value}"
            ) from error

        self._ip_address = value


# =============================================================================
# SECTION 37 - Property Demo
# =============================================================================


def property_demo() -> None:
    """
    Demonstrates a property with validation.
    """

    print("\nProperty Validation")
    print("-" * 40)

    device = ValidatedDevice(
        hostname="R1",
        ip_address="192.168.10.1"
    )

    print(
        f"Initial IP: "
        f"{device.ip_address}"
    )

    device.ip_address = (
        "10.10.10.1"
    )

    print(
        f"Updated IP: "
        f"{device.ip_address}"
    )

    try:

        device.ip_address = (
            "999.999.999.999"
        )

    except ValueError as error:

        print(
            f"Validation error: {error}"
        )


# =============================================================================
# SECTION 38 - Read-Only Property
# =============================================================================


class DeviceInformation:
    """
    Demonstrates a read-only property.
    """

    def __init__(
        self,
        hostname: str,
        vendor: str,
        model: str
    ) -> None:

        self.hostname = hostname
        self.vendor = vendor
        self.model = model

    @property
    def device_identifier(
        self
    ) -> str:

        return (
            f"{self.vendor}-"
            f"{self.model}-"
            f"{self.hostname}"
        )


# =============================================================================
# SECTION 39 - Read-Only Property Demo
# =============================================================================


def read_only_property_demo() -> None:
    """
    Demonstrates a calculated property.
    """

    print("\nRead-Only Property")
    print("-" * 40)

    device = DeviceInformation(
        hostname="R1",
        vendor="Cisco",
        model="ISR4331"
    )

    print(
        f"Device ID: "
        f"{device.device_identifier}"
    )


# =============================================================================
# SECTION 40 - Property with Multiple Validations
# =============================================================================


class NetworkInterface:
    """
    Represents a network interface
    with validation.
    """

    def __init__(
        self,
        name: str,
        ip_address: str,
        enabled: bool = True
    ) -> None:

        self.name = name

        self._ip_address = ""

        self._enabled = False

        self.ip_address = ip_address

        self.enabled = enabled

    @property
    def ip_address(
        self
    ) -> str:

        return self._ip_address

    @ip_address.setter
    def ip_address(
        self,
        value: str
    ) -> None:

        try:

            ipaddress.ip_address(
                value
            )

        except ValueError as error:

            raise ValueError(
                f"Invalid interface IP: "
                f"{value}"
            ) from error

        self._ip_address = value

    @property
    def enabled(
        self
    ) -> bool:

        return self._enabled

    @enabled.setter
    def enabled(
        self,
        value: bool
    ) -> None:

        if not isinstance(
            value,
            bool
        ):

            raise TypeError(
                "enabled must be "
                "True or False."
            )

        self._enabled = value


# =============================================================================
# SECTION 41 - Network Interface Demo
# =============================================================================


def network_interface_demo() -> None:
    """
    Demonstrates a professionally designed
    network interface class.
    """

    print("\nNetwork Interface")
    print("-" * 40)

    interface = NetworkInterface(
        name="GigabitEthernet0/0",
        ip_address="192.168.10.1",
        enabled=True
    )

    print(
        f"Interface : {interface.name}"
    )

    print(
        f"IP        : "
        f"{interface.ip_address}"
    )

    print(
        f"Enabled   : "
        f"{interface.enabled}"
    )

    interface.enabled = False

    print(
        f"Enabled after shutdown: "
        f"{interface.enabled}"
    )


# =============================================================================
# SECTION 42 - Class Design
# =============================================================================


class ProfessionalNetworkDevice:
    """
    Example of a reusable network device class.
    """

    vendor = "Cisco"

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        device_type: str
    ) -> None:

        self.hostname = hostname

        self._ip_address = ""

        self.device_type = device_type

        self.ip_address = ip_address

        self._connected = False

    @property
    def ip_address(
        self
    ) -> str:

        return self._ip_address

    @ip_address.setter
    def ip_address(
        self,
        value: str
    ) -> None:

        try:

            ipaddress.ip_address(
                value
            )

        except ValueError as error:

            raise ValueError(
                f"Invalid IP address: "
                f"{value}"
            ) from error

        self._ip_address = value

    @property
    def connected(
        self
    ) -> bool:

        return self._connected

    def connect(
        self
    ) -> None:

        self._connected = True

    def disconnect(
        self
    ) -> None:

        self._connected = False

    def status(
        self
    ) -> str:

        if self.connected:

            return "Connected"

        return "Disconnected"

    @classmethod
    def from_string(
        cls,
        data: str
    ) -> "ProfessionalNetworkDevice":
        """
        Creates a device from:

        hostname,ip_address,device_type
        """

        hostname, ip_address, device_type = (
            item.strip()
            for item in data.split(",")
        )

        return cls(
            hostname,
            ip_address,
            device_type
        )

    @staticmethod
    def supported_device_types() -> list[str]:
        """
        Returns supported network device types.
        """

        return [
            "Router",
            "Switch",
            "Firewall",
            "Wireless Controller"
        ]


# =============================================================================
# SECTION 43 - Professional Class Demo
# =============================================================================


def professional_class_demo() -> None:
    """
    Demonstrates the complete class design.
    """

    print("\nProfessional Network Device")
    print("-" * 40)

    device = (
        ProfessionalNetworkDevice.from_string(
            "R1,192.168.10.1,Router"
        )
    )

    print(
        f"Hostname    : "
        f"{device.hostname}"
    )

    print(
        f"IP Address  : "
        f"{device.ip_address}"
    )

    print(
        f"Device Type : "
        f"{device.device_type}"
    )

    print(
        f"Vendor      : "
        f"{device.vendor}"
    )

    print(
        f"Status      : "
        f"{device.status()}"
    )

    device.connect()

    print(
        f"After connect: "
        f"{device.status()}"
    )

    device.disconnect()

    print(
        f"After disconnect: "
        f"{device.status()}"
    )

    print(
        "\nSupported device types:"
    )

    for device_type in (
        device.supported_device_types()
    ):

        print(
            f"  - {device_type}"
        )


# =============================================================================
# SECTION 44 - Part Two Runner
# =============================================================================


def run_part_two() -> None:
    """
    Runs Lesson 20 Part Two.
    """

    print(
        "\n" + "=" * 70
    )

    print(
        "LESSON 20 - "
        "OBJECT-ORIENTED PROGRAMMING"
    )

    print(
        "PART 2 - "
        "ENCAPSULATION & CLASS DESIGN"
    )

    print(
        "=" * 70
    )

    instance_attributes_demo()

    class_attributes_demo()

    class_method_demo()

    alternative_constructor_demo()

    static_method_demo()

    encapsulation_demo()

    property_demo()

    read_only_property_demo()

    network_interface_demo()

    professional_class_demo()


# =============================================================================
# END OF PART 2
# =============================================================================

# =============================================================================
# LESSON 20 - PART 3
# INHERITANCE & POLYMORPHISM
# =============================================================================

"""
Part 3 Objectives
-----------------

- Understand inheritance
- Create parent and child classes
- Use super()
- Override methods
- Understand polymorphism
- Use isinstance()
- Use issubclass()
- Understand multiple inheritance
- Build a network device hierarchy
"""


# =============================================================================
# SECTION 45 - Basic Inheritance
# =============================================================================


class NetworkDeviceParent:
    """
    Parent class for network devices.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str
    ) -> None:

        self.hostname = hostname
        self.ip_address = ip_address

    def show_info(
        self
    ) -> None:

        print(
            f"Hostname: {self.hostname}"
        )

        print(
            f"IP Address: {self.ip_address}"
        )


class RouterChild(NetworkDeviceParent):
    """
    Child class inherited from
    NetworkDeviceParent.
    """

    pass


# =============================================================================
# SECTION 46 - Basic Inheritance Demo
# =============================================================================


def basic_inheritance_demo() -> None:
    """
    Demonstrates basic inheritance.
    """

    print("\nBasic Inheritance")
    print("-" * 40)

    router = RouterChild(
        hostname="R1",
        ip_address="192.168.10.1"
    )

    router.show_info()

    print(
        f"Class: {type(router).__name__}"
    )

    print(
        f"Is NetworkDeviceParent? "
        f"{isinstance(router, NetworkDeviceParent)}"
    )


# =============================================================================
# SECTION 47 - Inheritance with Additional Attributes
# =============================================================================


class Router(NetworkDeviceParent):
    """
    Router inherits from NetworkDeviceParent
    and adds router-specific information.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        routing_protocol: str
    ) -> None:

        super().__init__(
            hostname,
            ip_address
        )

        self.routing_protocol = (
            routing_protocol
        )


# =============================================================================
# SECTION 48 - Additional Attributes Demo
# =============================================================================


def inheritance_attributes_demo() -> None:
    """
    Demonstrates inherited and new attributes.
    """

    print("\nInherited Attributes")
    print("-" * 40)

    router = Router(
        hostname="R1",
        ip_address="192.168.10.1",
        routing_protocol="OSPF"
    )

    print(
        f"Hostname          : "
        f"{router.hostname}"
    )

    print(
        f"IP Address        : "
        f"{router.ip_address}"
    )

    print(
        f"Routing Protocol  : "
        f"{router.routing_protocol}"
    )


# =============================================================================
# SECTION 49 - super()
# =============================================================================


class Switch(NetworkDeviceParent):
    """
    Switch class using super().
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        vlan_count: int
    ) -> None:

        super().__init__(
            hostname,
            ip_address
        )

        self.vlan_count = vlan_count


# =============================================================================
# SECTION 50 - super() Demo
# =============================================================================


def super_demo() -> None:
    """
    Demonstrates calling the parent constructor
    with super().
    """

    print("\nsuper()")
    print("-" * 40)

    switch = Switch(
        hostname="SW1",
        ip_address="192.168.10.10",
        vlan_count=20
    )

    switch.show_info()

    print(
        f"VLAN Count: "
        f"{switch.vlan_count}"
    )


# =============================================================================
# SECTION 51 - Method Overriding
# =============================================================================


class GenericNetworkDevice:
    """
    Generic parent network device.
    """

    def __init__(
        self,
        hostname: str
    ) -> None:

        self.hostname = hostname

    def device_role(
        self
    ) -> str:

        return "Generic Network Device"

    def show_status(
        self
    ) -> None:

        print(
            f"{self.hostname}: "
            f"{self.device_role()}"
        )


class RouterOverride(GenericNetworkDevice):
    """
    Router overrides device_role().
    """

    def device_role(
        self
    ) -> str:

        return "Router"


class SwitchOverride(GenericNetworkDevice):
    """
    Switch overrides device_role().
    """

    def device_role(
        self
    ) -> str:

        return "Switch"


class FirewallOverride(GenericNetworkDevice):
    """
    Firewall overrides device_role().
    """

    def device_role(
        self
    ) -> str:

        return "Firewall"


# =============================================================================
# SECTION 52 - Method Overriding Demo
# =============================================================================


def method_overriding_demo() -> None:
    """
    Demonstrates method overriding.
    """

    print("\nMethod Overriding")
    print("-" * 40)

    devices = [
        GenericNetworkDevice("DEV1"),
        RouterOverride("R1"),
        SwitchOverride("SW1"),
        FirewallOverride("FW1")
    ]

    for device in devices:

        device.show_status()


# =============================================================================
# SECTION 53 - Polymorphism
# =============================================================================


def polymorphism_demo() -> None:
    """
    Demonstrates polymorphism.

    Different classes implement the same
    method name but behave differently.
    """

    print("\nPolymorphism")
    print("-" * 40)

    devices = [
        RouterOverride("R1"),
        SwitchOverride("SW1"),
        FirewallOverride("FW1")
    ]

    for device in devices:

        print(
            f"{device.hostname:<8}"
            f" -> "
            f"{device.device_role()}"
        )


# =============================================================================
# SECTION 54 - Polymorphic Operations
# =============================================================================


class NetworkDeviceBaseClass:
    """
    Base class for polymorphic operations.
    """

    def __init__(
        self,
        hostname: str
    ) -> None:

        self.hostname = hostname

    def get_configuration(
        self
    ) -> str:

        return (
            f"{self.hostname}: "
            f"Generic configuration"
        )


class RouterConfig(NetworkDeviceBaseClass):
    """
    Router implementation.
    """

    def get_configuration(
        self
    ) -> str:

        return (
            f"{self.hostname}: "
            f"Router configuration"
        )


class SwitchConfig(NetworkDeviceBaseClass):
    """
    Switch implementation.
    """

    def get_configuration(
        self
    ) -> str:

        return (
            f"{self.hostname}: "
            f"Switch configuration"
        )


class FirewallConfig(NetworkDeviceBaseClass):
    """
    Firewall implementation.
    """

    def get_configuration(
        self
    ) -> str:

        return (
            f"{self.hostname}: "
            f"Firewall configuration"
        )


# =============================================================================
# SECTION 55 - Polymorphic Configuration Demo
# =============================================================================


def polymorphic_configuration_demo() -> None:
    """
    Demonstrates polymorphic configuration retrieval.
    """

    print("\nPolymorphic Configuration")
    print("-" * 40)

    devices = [
        RouterConfig("R1"),
        SwitchConfig("SW1"),
        FirewallConfig("FW1")
    ]

    for device in devices:

        print(
            device.get_configuration()
        )


# =============================================================================
# SECTION 56 - isinstance()
# =============================================================================


def isinstance_demo() -> None:
    """
    Demonstrates isinstance().
    """

    print("\nisinstance()")
    print("-" * 40)

    router = Router(
        hostname="R1",
        ip_address="192.168.10.1",
        routing_protocol="OSPF"
    )

    switch = Switch(
        hostname="SW1",
        ip_address="192.168.10.10",
        vlan_count=20
    )

    print(
        "router is Router:",
        isinstance(router, Router)
    )

    print(
        "router is NetworkDeviceParent:",
        isinstance(
            router,
            NetworkDeviceParent
        )
    )

    print(
        "switch is Router:",
        isinstance(switch, Router)
    )

    print(
        "switch is NetworkDeviceParent:",
        isinstance(
            switch,
            NetworkDeviceParent
        )
    )


# =============================================================================
# SECTION 57 - issubclass()
# =============================================================================


def issubclass_demo() -> None:
    """
    Demonstrates issubclass().
    """

    print("\nissubclass()")
    print("-" * 40)

    print(
        "Router -> NetworkDeviceParent:",
        issubclass(
            Router,
            NetworkDeviceParent
        )
    )

    print(
        "Switch -> NetworkDeviceParent:",
        issubclass(
            Switch,
            NetworkDeviceParent
        )
    )

    print(
        "Router -> Switch:",
        issubclass(
            Router,
            Switch
        )
    )


# =============================================================================
# SECTION 58 - Multi-Level Inheritance
# =============================================================================


class CiscoDevice(NetworkDeviceParent):
    """
    Cisco device level.
    """

    def show_vendor(
        self
    ) -> None:

        print(
            f"{self.hostname}: Cisco"
        )


class CiscoRouter(CiscoDevice):
    """
    Cisco Router inherits from CiscoDevice.
    """

    def show_role(
        self
    ) -> None:

        print(
            f"{self.hostname}: Router"
        )


# =============================================================================
# SECTION 59 - Multi-Level Inheritance Demo
# =============================================================================


def multi_level_inheritance_demo() -> None:
    """
    Demonstrates multi-level inheritance.
    """

    print("\nMulti-Level Inheritance")
    print("-" * 40)

    router = CiscoRouter(
        hostname="R1",
        ip_address="192.168.10.1"
    )

    router.show_info()

    router.show_vendor()

    router.show_role()


# =============================================================================
# SECTION 60 - Multiple Inheritance
# =============================================================================


class Monitorable:
    """
    Provides monitoring behavior.
    """

    def monitor(
        self
    ) -> None:

        print(
            "Monitoring enabled."
        )


class BackupCapable:
    """
    Provides backup behavior.
    """

    def backup_config(
        self
    ) -> None:

        print(
            "Configuration backup created."
        )


class EnterpriseDevice(
    NetworkDeviceParent,
    Monitorable,
    BackupCapable
):
    """
    Demonstrates multiple inheritance.
    """

    pass


# =============================================================================
# SECTION 61 - Multiple Inheritance Demo
# =============================================================================


def multiple_inheritance_demo() -> None:
    """
    Demonstrates multiple inheritance.
    """

    print("\nMultiple Inheritance")
    print("-" * 40)

    device = EnterpriseDevice(
        hostname="R1",
        ip_address="192.168.10.1"
    )

    device.show_info()

    device.monitor()

    device.backup_config()


# =============================================================================
# SECTION 62 - Method Resolution Order
# =============================================================================


def mro_demo() -> None:
    """
    Demonstrates Method Resolution Order.
    """

    print("\nMethod Resolution Order")
    print("-" * 40)

    print(
        "EnterpriseDevice MRO:"
    )

    for cls in EnterpriseDevice.mro():

        print(
            f"  -> {cls.__name__}"
        )


# =============================================================================
# SECTION 63 - Real Network Device Hierarchy
# =============================================================================


class BaseNetworkDevice:
    """
    Base network device.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        vendor: str
    ) -> None:

        self.hostname = hostname
        self.ip_address = ip_address
        self.vendor = vendor

    def connect(
        self
    ) -> None:

        print(
            f"{self.hostname}: "
            f"Generic connection."
        )

    def show_info(
        self
    ) -> None:

        print(
            f"{self.hostname} | "
            f"{self.ip_address} | "
            f"{self.vendor}"
        )


class NetworkRouter(BaseNetworkDevice):
    """
    Network router.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        vendor: str,
        routing_protocol: str
    ) -> None:

        super().__init__(
            hostname,
            ip_address,
            vendor
        )

        self.routing_protocol = (
            routing_protocol
        )

    def connect(
        self
    ) -> None:

        print(
            f"{self.hostname}: "
            f"Connecting to router..."
        )

    def show_routing_protocol(
        self
    ) -> None:

        print(
            f"Routing Protocol: "
            f"{self.routing_protocol}"
        )


class NetworkSwitch(BaseNetworkDevice):
    """
    Network switch.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        vendor: str,
        vlan_count: int
    ) -> None:

        super().__init__(
            hostname,
            ip_address,
            vendor
        )

        self.vlan_count = vlan_count

    def connect(
        self
    ) -> None:

        print(
            f"{self.hostname}: "
            f"Connecting to switch..."
        )

    def show_vlan_count(
        self
    ) -> None:

        print(
            f"VLAN Count: "
            f"{self.vlan_count}"
        )


class NetworkFirewall(BaseNetworkDevice):
    """
    Network firewall.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        vendor: str,
        policy_count: int
    ) -> None:

        super().__init__(
            hostname,
            ip_address,
            vendor
        )

        self.policy_count = policy_count

    def connect(
        self
    ) -> None:

        print(
            f"{self.hostname}: "
            f"Connecting to firewall..."
        )

    def show_policy_count(
        self
    ) -> None:

        print(
            f"Security Policies: "
            f"{self.policy_count}"
        )


# =============================================================================
# SECTION 64 - Real Network Hierarchy Demo
# =============================================================================


def network_hierarchy_demo() -> None:
    """
    Demonstrates the complete network
    device hierarchy.
    """

    print("\nNetwork Device Hierarchy")
    print("-" * 40)

    router = NetworkRouter(
        hostname="R1",
        ip_address="192.168.10.1",
        vendor="Cisco",
        routing_protocol="OSPF"
    )

    switch = NetworkSwitch(
        hostname="SW1",
        ip_address="192.168.10.10",
        vendor="Cisco",
        vlan_count=50
    )

    firewall = NetworkFirewall(
        hostname="FW1",
        ip_address="192.168.10.254",
        vendor="Fortinet",
        policy_count=120
    )

    devices = [
        router,
        switch,
        firewall
    ]

    for device in devices:

        device.show_info()

        device.connect()

        print()


# =============================================================================
# SECTION 65 - Polymorphic Network Operations
# =============================================================================


def run_network_operation(
    device: BaseNetworkDevice
) -> None:
    """
    Executes a common operation against
    different network device types.
    """

    device.show_info()

    device.connect()


# =============================================================================
# SECTION 66 - Polymorphic Network Operations Demo
# =============================================================================


def polymorphic_network_operations_demo() -> None:
    """
    Demonstrates polymorphism with network devices.
    """

    print(
        "\nPolymorphic Network Operations"
    )

    print(
        "-" * 40
    )

    devices = [
        NetworkRouter(
            "R1",
            "192.168.10.1",
            "Cisco",
            "OSPF"
        ),

        NetworkSwitch(
            "SW1",
            "192.168.10.10",
            "Cisco",
            50
        ),

        NetworkFirewall(
            "FW1",
            "192.168.10.254",
            "Fortinet",
            120
        )
    ]

    for device in devices:

        run_network_operation(
            device
        )

        print()


# =============================================================================
# SECTION 67 - Part Three Runner
# =============================================================================


def run_part_three() -> None:
    """
    Runs Lesson 20 Part Three.
    """

    print(
        "\n" + "=" * 70
    )

    print(
        "LESSON 20 - "
        "OBJECT-ORIENTED PROGRAMMING"
    )

    print(
        "PART 3 - "
        "INHERITANCE & POLYMORPHISM"
    )

    print(
        "=" * 70
    )

    basic_inheritance_demo()

    inheritance_attributes_demo()

    super_demo()

    method_overriding_demo()

    polymorphism_demo()

    polymorphic_configuration_demo()

    isinstance_demo()

    issubclass_demo()

    multi_level_inheritance_demo()

    multiple_inheritance_demo()

    mro_demo()

    network_hierarchy_demo()

    polymorphic_network_operations_demo()


# =============================================================================
# END OF PART 3
# =============================================================================

# =============================================================================
# LESSON 20 - PART 4
# PROFESSIONAL OBJECT-ORIENTED PROGRAMMING
# =============================================================================

"""
Part 4 Objectives
-----------------

- Understand composition
- Understand aggregation
- Use abstract base classes
- Use abstract methods
- Understand interfaces through ABC
- Use dataclasses
- Combine OOP with type hints
- Build reusable network components
- Design classes for network automation
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


# =============================================================================
# SECTION 68 - Composition
# =============================================================================


class Interface:
    """
    Represents a network interface.
    """

    def __init__(
        self,
        name: str,
        ip_address: str,
        enabled: bool = True
    ) -> None:

        self.name = name
        self.ip_address = ip_address
        self.enabled = enabled

    def show_info(
        self
    ) -> None:

        status = (
            "UP"
            if self.enabled
            else "DOWN"
        )

        print(
            f"{self.name:<20}"
            f"{self.ip_address:<18}"
            f"{status}"
        )


class RouterComposition:
    """
    Demonstrates composition.

    A router contains interfaces.
    """

    def __init__(
        self,
        hostname: str
    ) -> None:

        self.hostname = hostname

        self.interfaces: list[
            Interface
        ] = []

    def add_interface(
        self,
        interface: Interface
    ) -> None:

        self.interfaces.append(
            interface
        )

    def show_interfaces(
        self
    ) -> None:

        print(
            f"\nInterfaces of "
            f"{self.hostname}"
        )

        print(
            "-" * 55
        )

        for interface in self.interfaces:

            interface.show_info()


# =============================================================================
# SECTION 69 - Composition Demo
# =============================================================================


def composition_demo() -> None:
    """
    Demonstrates composition between
    Router and Interface objects.
    """

    print("\nComposition")
    print("-" * 40)

    router = RouterComposition(
        "R1"
    )

    router.add_interface(
        Interface(
            "GigabitEthernet0/0",
            "192.168.10.1"
        )
    )

    router.add_interface(
        Interface(
            "GigabitEthernet0/1",
            "10.10.10.1"
        )
    )

    router.add_interface(
        Interface(
            "Loopback0",
            "1.1.1.1"
        )
    )

    router.show_interfaces()


# =============================================================================
# SECTION 70 - Aggregation
# =============================================================================


class NetworkSite:
    """
    Represents a network site.

    Devices are provided from outside,
    demonstrating aggregation.
    """

    def __init__(
        self,
        name: str,
        devices: list[
            "BaseNetworkDevice"
        ]
    ) -> None:

        self.name = name
        self.devices = devices

    def show_devices(
        self
    ) -> None:

        print(
            f"\nSite: {self.name}"
        )

        for device in self.devices:

            print(
                f"  - "
                f"{device.hostname}"
            )


# =============================================================================
# SECTION 71 - Aggregation Demo
# =============================================================================


def aggregation_demo() -> None:
    """
    Demonstrates aggregation.

    The devices can exist independently
    from the site.
    """

    print("\nAggregation")
    print("-" * 40)

    router = NetworkRouter(
        "R1",
        "192.168.10.1",
        "Cisco",
        "OSPF"
    )

    switch = NetworkSwitch(
        "SW1",
        "192.168.10.10",
        "Cisco",
        50
    )

    devices = [
        router,
        switch
    ]

    site = NetworkSite(
        "Head Office",
        devices
    )

    site.show_devices()


# =============================================================================
# SECTION 72 - Abstract Base Class
# =============================================================================


class AbstractNetworkDevice(ABC):
    """
    Abstract base class for network devices.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str
    ) -> None:

        self.hostname = hostname
        self.ip_address = ip_address

    @abstractmethod
    def connect(
        self
    ) -> None:
        """
        Every child class must implement
        connect().
        """

        raise NotImplementedError

    @abstractmethod
    def get_device_type(
        self
    ) -> str:
        """
        Every child class must return
        its device type.
        """

        raise NotImplementedError

    def show_info(
        self
    ) -> None:

        print(
            f"{self.hostname} | "
            f"{self.ip_address} | "
            f"{self.get_device_type()}"
        )


# =============================================================================
# SECTION 73 - Abstract Router
# =============================================================================


class AbstractRouter(
    AbstractNetworkDevice
):
    """
    Concrete Router implementation.
    """

    def connect(
        self
    ) -> None:

        print(
            f"{self.hostname}: "
            f"Connecting to router..."
        )

    def get_device_type(
        self
    ) -> str:

        return "Router"


# =============================================================================
# SECTION 74 - Abstract Switch
# =============================================================================


class AbstractSwitch(
    AbstractNetworkDevice
):
    """
    Concrete Switch implementation.
    """

    def connect(
        self
    ) -> None:

        print(
            f"{self.hostname}: "
            f"Connecting to switch..."
        )

    def get_device_type(
        self
    ) -> str:

        return "Switch"


# =============================================================================
# SECTION 75 - Abstract Firewall
# =============================================================================


class AbstractFirewall(
    AbstractNetworkDevice
):
    """
    Concrete Firewall implementation.
    """

    def connect(
        self
    ) -> None:

        print(
            f"{self.hostname}: "
            f"Connecting to firewall..."
        )

    def get_device_type(
        self
    ) -> str:

        return "Firewall"


# =============================================================================
# SECTION 76 - Abstract Class Demo
# =============================================================================


def abstract_class_demo() -> None:
    """
    Demonstrates abstract classes.
    """

    print("\nAbstract Base Classes")
    print("-" * 40)

    devices = [
        AbstractRouter(
            "R1",
            "192.168.10.1"
        ),

        AbstractSwitch(
            "SW1",
            "192.168.10.10"
        ),

        AbstractFirewall(
            "FW1",
            "192.168.10.254"
        )
    ]

    for device in devices:

        device.show_info()

        device.connect()


# =============================================================================
# SECTION 77 - Dataclass
# =============================================================================


@dataclass
class DeviceRecord:
    """
    Simple network device record.
    """

    hostname: str
    ip_address: str
    device_type: str


# =============================================================================
# SECTION 78 - Dataclass Demo
# =============================================================================


def dataclass_demo() -> None:
    """
    Demonstrates a basic dataclass.
    """

    print("\nDataclass")
    print("-" * 40)

    device = DeviceRecord(
        hostname="R1",
        ip_address="192.168.10.1",
        device_type="Router"
    )

    print(
        device
    )


# =============================================================================
# SECTION 79 - Dataclass with Defaults
# =============================================================================


@dataclass
class DeviceConfiguration:
    """
    Dataclass with default values.
    """

    hostname: str
    ip_address: str
    username: str = "admin"
    enabled: bool = True
    timeout: int = 10


# =============================================================================
# SECTION 80 - Dataclass Defaults Demo
# =============================================================================


def dataclass_defaults_demo() -> None:
    """
    Demonstrates default values in dataclasses.
    """

    print("\nDataclass Defaults")
    print("-" * 40)

    device = DeviceConfiguration(
        hostname="R1",
        ip_address="192.168.10.1"
    )

    print(
        f"Hostname : {device.hostname}"
    )

    print(
        f"IP       : {device.ip_address}"
    )

    print(
        f"Username : {device.username}"
    )

    print(
        f"Enabled  : {device.enabled}"
    )

    print(
        f"Timeout  : {device.timeout}"
    )


# =============================================================================
# SECTION 81 - Dataclass Factory
# =============================================================================


@dataclass
class NetworkDeviceRecord:
    """
    Network device record with
    a generated identifier.
    """

    hostname: str
    ip_address: str
    device_type: str
    tags: list[str] = field(
        default_factory=list
    )


# =============================================================================
# SECTION 82 - Dataclass Factory Demo
# =============================================================================


def dataclass_factory_demo() -> None:
    """
    Demonstrates default_factory.
    """

    print("\nDataclass default_factory")
    print("-" * 40)

    router = NetworkDeviceRecord(
        hostname="R1",
        ip_address="192.168.10.1",
        device_type="Router"
    )

    router.tags.append(
        "production"
    )

    router.tags.append(
        "core"
    )

    print(
        f"Hostname: {router.hostname}"
    )

    print(
        f"Tags: {router.tags}"
    )


# =============================================================================
# SECTION 83 - Dataclass Comparison
# =============================================================================


def dataclass_comparison_demo() -> None:
    """
    Demonstrates automatic equality
    comparison provided by dataclass.
    """

    print("\nDataclass Comparison")
    print("-" * 40)

    device_one = DeviceRecord(
        "R1",
        "192.168.10.1",
        "Router"
    )

    device_two = DeviceRecord(
        "R1",
        "192.168.10.1",
        "Router"
    )

    print(
        f"Device 1: {device_one}"
    )

    print(
        f"Device 2: {device_two}"
    )

    print(
        f"Equal? "
        f"{device_one == device_two}"
    )


# =============================================================================
# SECTION 84 - Abstract Network Manager
# =============================================================================


class NetworkManager(ABC):
    """
    Abstract interface for network managers.
    """

    @abstractmethod
    def connect(
        self,
        device: AbstractNetworkDevice
    ) -> None:

        raise NotImplementedError

    @abstractmethod
    def execute_command(
        self,
        device: AbstractNetworkDevice,
        command: str
    ) -> str:

        raise NotImplementedError


# =============================================================================
# SECTION 85 - Cisco Network Manager
# =============================================================================


class CiscoNetworkManager(
    NetworkManager
):
    """
    Cisco network manager implementation.
    """

    def connect(
        self,
        device: AbstractNetworkDevice
    ) -> None:

        print(
            f"[Cisco] Connecting to "
            f"{device.hostname}"
        )

    def execute_command(
        self,
        device: AbstractNetworkDevice,
        command: str
    ) -> str:

        return (
            f"[Cisco] "
            f"{device.hostname}: "
            f"Executed '{command}'"
        )


# =============================================================================
# SECTION 86 - Generic Network Manager
# =============================================================================


class GenericNetworkManager(
    NetworkManager
):
    """
    Generic network manager implementation.
    """

    def connect(
        self,
        device: AbstractNetworkDevice
    ) -> None:

        print(
            f"[Generic] Connecting to "
            f"{device.hostname}"
        )

    def execute_command(
        self,
        device: AbstractNetworkDevice,
        command: str
    ) -> str:

        return (
            f"[Generic] "
            f"{device.hostname}: "
            f"Executed '{command}'"
        )


# =============================================================================
# SECTION 87 - Interface Demo
# =============================================================================


def interface_demo() -> None:
    """
    Demonstrates interface-like behavior
    using an abstract base class.
    """

    print("\nNetwork Manager Interface")
    print("-" * 40)

    device = AbstractRouter(
        "R1",
        "192.168.10.1"
    )

    managers = [
        CiscoNetworkManager(),
        GenericNetworkManager()
    ]

    for manager in managers:

        manager.connect(
            device
        )

        result = (
            manager.execute_command(
                device,
                "show ip interface brief"
            )
        )

        print(
            result
        )


# =============================================================================
# SECTION 88 - Dependency Injection
# =============================================================================


class MonitoringService:
    """
    Demonstrates dependency injection.

    The service receives a NetworkManager
    instead of creating one internally.
    """

    def __init__(
        self,
        manager: NetworkManager
    ) -> None:

        self.manager = manager

    def monitor(
        self,
        device: AbstractNetworkDevice
    ) -> None:

        self.manager.connect(
            device
        )

        result = (
            self.manager.execute_command(
                device,
                "show version"
            )
        )

        print(
            result
        )


# =============================================================================
# SECTION 89 - Dependency Injection Demo
# =============================================================================


def dependency_injection_demo() -> None:
    """
    Demonstrates dependency injection.
    """

    print("\nDependency Injection")
    print("-" * 40)

    device = AbstractRouter(
        "R1",
        "192.168.10.1"
    )

    manager = (
        CiscoNetworkManager()
    )

    monitoring = MonitoringService(
        manager
    )

    monitoring.monitor(
        device
    )


# =============================================================================
# SECTION 90 - Professional Device Dataclass
# =============================================================================


@dataclass
class ProfessionalDevice:
    """
    Professional device model.

    This class represents device data,
    while operational behavior can be
    implemented in service classes.
    """

    hostname: str
    ip_address: str
    device_type: str
    vendor: str
    username: str = "admin"
    enabled: bool = True
    tags: list[str] = field(
        default_factory=list
    )

    def add_tag(
        self,
        tag: str
    ) -> None:

        tag = tag.strip()

        if not tag:

            raise ValueError(
                "Tag cannot be empty."
            )

        if tag not in self.tags:

            self.tags.append(
                tag
            )

    def remove_tag(
        self,
        tag: str
    ) -> None:

        if tag in self.tags:

            self.tags.remove(
                tag
            )

    def show_summary(
        self
    ) -> None:

        print(
            f"\n{self.hostname}"
        )

        print(
            f"  IP       : "
            f"{self.ip_address}"
        )

        print(
            f"  Type     : "
            f"{self.device_type}"
        )

        print(
            f"  Vendor   : "
            f"{self.vendor}"
        )

        print(
            f"  Username : "
            f"{self.username}"
        )

        print(
            f"  Enabled  : "
            f"{self.enabled}"
        )

        print(
            f"  Tags     : "
            f"{self.tags}"
        )


# =============================================================================
# SECTION 91 - Professional Dataclass Demo
# =============================================================================


def professional_dataclass_demo() -> None:
    """
    Demonstrates a professional dataclass.
    """

    print("\nProfessional Device Dataclass")
    print("-" * 40)

    device = ProfessionalDevice(
        hostname="R1",
        ip_address="192.168.10.1",
        device_type="Router",
        vendor="Cisco"
    )

    device.add_tag(
        "core"
    )

    device.add_tag(
        "production"
    )

    device.show_summary()

    device.remove_tag(
        "core"
    )

    print(
        "\nAfter removing 'core':"
    )

    device.show_summary()


# =============================================================================
# SECTION 92 - OOP Architecture Demo
# =============================================================================


def oop_architecture_demo() -> None:
    """
    Demonstrates how the concepts fit together.
    """

    print("\nProfessional OOP Architecture")
    print("-" * 40)

    print(
        "Data Model"
    )

    print(
        "  -> Dataclass"
    )

    print(
        "Device Behavior"
    )

    print(
        "  -> Classes / Methods"
    )

    print(
        "Shared Behavior"
    )

    print(
        "  -> Inheritance"
    )

    print(
        "Common Interface"
    )

    print(
        "  -> Abstract Base Class"
    )

    print(
        "Object Relationships"
    )

    print(
        "  -> Composition / Aggregation"
    )

    print(
        "Flexible Dependencies"
    )

    print(
        "  -> Dependency Injection"
    )

    print(
        "Multiple Implementations"
    )

    print(
        "  -> Polymorphism"
    )


# =============================================================================
# SECTION 93 - Part Four Runner
# =============================================================================


def run_part_four() -> None:
    """
    Runs Lesson 20 Part Four.
    """

    print(
        "\n" + "=" * 70
    )

    print(
        "LESSON 20 - "
        "OBJECT-ORIENTED PROGRAMMING"
    )

    print(
        "PART 4 - "
        "PROFESSIONAL OOP"
    )

    print(
        "=" * 70
    )

    composition_demo()

    aggregation_demo()

    abstract_class_demo()

    dataclass_demo()

    dataclass_defaults_demo()

    dataclass_factory_demo()

    dataclass_comparison_demo()

    interface_demo()

    dependency_injection_demo()

    professional_dataclass_demo()

    oop_architecture_demo()


# =============================================================================
# END OF PART 4
# =============================================================================


# =============================================================================
# LESSON 20 - PART 5
# FINAL PROJECT
# NETWORK DEVICE MANAGEMENT SYSTEM
# =============================================================================

"""
Lesson 20 Final Project
-----------------------

Network Device Management System

This project combines:

- Classes
- Objects
- Encapsulation
- Properties
- Inheritance
- Polymorphism
- Composition
- Aggregation
- Abstract Base Classes
- Dataclasses
- Class Methods
- Static Methods
- Type Hints
- Exception Handling
- Device Inventory
- Network Monitoring Concepts
"""


# =============================================================================
# SECTION 94 - Custom Exceptions
# =============================================================================


class DeviceManagementError(Exception):
    """
    Base exception for the project.
    """

    pass


class DeviceAlreadyExistsError(
    DeviceManagementError
):
    """
    Raised when a duplicate hostname
    is added to the inventory.
    """

    pass


class DeviceNotFoundError(
    DeviceManagementError
):
    """
    Raised when a requested device
    does not exist.
    """

    pass


class InvalidDeviceError(
    DeviceManagementError
):
    """
    Raised when device information
    is invalid.
    """

    pass


# =============================================================================
# SECTION 95 - Device Model
# =============================================================================


@dataclass
class ManagedNetworkDevice:
    """
    Represents a managed network device.
    """

    hostname: str
    ip_address: str
    device_type: str
    vendor: str
    username: str = "admin"
    enabled: bool = True
    tags: list[str] = field(
        default_factory=list
    )

    _connected: bool = field(
        default=False,
        init=False,
        repr=False
    )

    def __post_init__(
        self
    ) -> None:
        """
        Validate device information
        after initialization.
        """

        self.hostname = (
            self.hostname.strip()
        )

        self.ip_address = (
            self.ip_address.strip()
        )

        self.device_type = (
            self.device_type.strip()
        )

        self.vendor = (
            self.vendor.strip()
        )

        self.username = (
            self.username.strip()
        )

        if not self.hostname:

            raise InvalidDeviceError(
                "Hostname cannot be empty."
            )

        if not self.ip_address:

            raise InvalidDeviceError(
                "IP address cannot be empty."
            )

        if not self.device_type:

            raise InvalidDeviceError(
                "Device type cannot be empty."
            )

        if not self.vendor:

            raise InvalidDeviceError(
                "Vendor cannot be empty."
            )

        try:

            ipaddress.ip_address(
                self.ip_address
            )

        except ValueError as error:

            raise InvalidDeviceError(
                f"Invalid IP address: "
                f"{self.ip_address}"
            ) from error

    # -------------------------------------------------------------------------
    # Property
    # -------------------------------------------------------------------------

    @property
    def connected(
        self
    ) -> bool:
        """
        Returns connection status.
        """

        return self._connected

    # -------------------------------------------------------------------------
    # Connection Methods
    # -------------------------------------------------------------------------

    def connect(
        self
    ) -> None:
        """
        Simulates connecting to the device.
        """

        if not self.enabled:

            raise DeviceManagementError(
                f"{self.hostname} is disabled."
            )

        self._connected = True

        print(
            f"[CONNECTED] "
            f"{self.hostname} "
            f"({self.ip_address})"
        )

    def disconnect(
        self
    ) -> None:
        """
        Disconnects from the device.
        """

        self._connected = False

        print(
            f"[DISCONNECTED] "
            f"{self.hostname}"
        )

    # -------------------------------------------------------------------------
    # Device Information
    # -------------------------------------------------------------------------

    def show_info(
        self
    ) -> None:
        """
        Displays device information.
        """

        status = (
            "Connected"
            if self.connected
            else "Disconnected"
        )

        print(
            f"\nHostname   : "
            f"{self.hostname}"
        )

        print(
            f"IP Address : "
            f"{self.ip_address}"
        )

        print(
            f"Type       : "
            f"{self.device_type}"
        )

        print(
            f"Vendor     : "
            f"{self.vendor}"
        )

        print(
            f"Username   : "
            f"{self.username}"
        )

        print(
            f"Enabled    : "
            f"{self.enabled}"
        )

        print(
            f"Status     : "
            f"{status}"
        )

        print(
            f"Tags       : "
            f"{self.tags}"
        )

    # -------------------------------------------------------------------------
    # Tags
    # -------------------------------------------------------------------------

    def add_tag(
        self,
        tag: str
    ) -> None:
        """
        Adds a tag to the device.
        """

        tag = tag.strip()

        if not tag:

            raise ValueError(
                "Tag cannot be empty."
            )

        if tag not in self.tags:

            self.tags.append(
                tag
            )

    def remove_tag(
        self,
        tag: str
    ) -> None:
        """
        Removes a tag.
        """

        if tag in self.tags:

            self.tags.remove(
                tag
            )

    # -------------------------------------------------------------------------
    # Command Execution
    # -------------------------------------------------------------------------

    def execute_command(
        self,
        command: str
    ) -> str:
        """
        Simulates command execution.
        """

        if not self.connected:

            raise DeviceManagementError(
                f"{self.hostname} "
                f"is not connected."
            )

        return (
            f"{self.hostname}: "
            f"executed '{command}'"
        )

    # -------------------------------------------------------------------------
    # Class Method
    # -------------------------------------------------------------------------

    @classmethod
    def from_string(
        cls,
        data: str
    ) -> "ManagedNetworkDevice":
        """
        Creates a device from:

        hostname,ip_address,device_type,vendor
        """

        values = [
            item.strip()
            for item in data.split(",")
        ]

        if len(values) != 4:

            raise InvalidDeviceError(
                "Expected format: "
                "hostname,ip_address,"
                "device_type,vendor"
            )

        return cls(
            hostname=values[0],
            ip_address=values[1],
            device_type=values[2],
            vendor=values[3]
        )

    # -------------------------------------------------------------------------
    # Static Method
    # -------------------------------------------------------------------------

    @staticmethod
    def validate_ip(
        ip_address: str
    ) -> bool:
        """
        Validates an IP address.
        """

        try:

            ipaddress.ip_address(
                ip_address
            )

            return True

        except ValueError:

            return False


# =============================================================================
# SECTION 96 - Specialized Router
# =============================================================================


class ManagedRouter(
    ManagedNetworkDevice
):
    """
    Specialized Router class.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        vendor: str,
        routing_protocol: str = "OSPF"
    ) -> None:

        super().__init__(
            hostname=hostname,
            ip_address=ip_address,
            device_type="Router",
            vendor=vendor
        )

        self.routing_protocol = (
            routing_protocol
        )

    def execute_command(
        self,
        command: str
    ) -> str:
        """
        Router-specific command execution.
        """

        if not self.connected:

            raise DeviceManagementError(
                f"{self.hostname} "
                f"is not connected."
            )

        return (
            f"[ROUTER] "
            f"{self.hostname}: "
            f"executed '{command}'"
        )

    def show_routing_protocol(
        self
    ) -> None:

        print(
            f"Routing Protocol: "
            f"{self.routing_protocol}"
        )


# =============================================================================
# SECTION 97 - Specialized Switch
# =============================================================================


class ManagedSwitch(
    ManagedNetworkDevice
):
    """
    Specialized Switch class.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        vendor: str,
        vlan_count: int = 1
    ) -> None:

        super().__init__(
            hostname=hostname,
            ip_address=ip_address,
            device_type="Switch",
            vendor=vendor
        )

        self.vlan_count = vlan_count

    def execute_command(
        self,
        command: str
    ) -> str:
        """
        Switch-specific command execution.
        """

        if not self.connected:

            raise DeviceManagementError(
                f"{self.hostname} "
                f"is not connected."
            )

        return (
            f"[SWITCH] "
            f"{self.hostname}: "
            f"executed '{command}'"
        )

    def show_vlan_count(
        self
    ) -> None:

        print(
            f"VLAN Count: "
            f"{self.vlan_count}"
        )


# =============================================================================
# SECTION 98 - Specialized Firewall
# =============================================================================


class ManagedFirewall(
    ManagedNetworkDevice
):
    """
    Specialized Firewall class.
    """

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        vendor: str,
        policy_count: int = 0
    ) -> None:

        super().__init__(
            hostname=hostname,
            ip_address=ip_address,
            device_type="Firewall",
            vendor=vendor
        )

        self.policy_count = policy_count

    def execute_command(
        self,
        command: str
    ) -> str:
        """
        Firewall-specific command execution.
        """

        if not self.connected:

            raise DeviceManagementError(
                f"{self.hostname} "
                f"is not connected."
            )

        return (
            f"[FIREWALL] "
            f"{self.hostname}: "
            f"executed '{command}'"
        )

    def show_policy_count(
        self
    ) -> None:

        print(
            f"Security Policies: "
            f"{self.policy_count}"
        )


# =============================================================================
# SECTION 99 - Device Inventory
# =============================================================================


class DeviceInventory:
    """
    Manages a collection of network devices.

    This class demonstrates composition,
    encapsulation and collection management.
    """

    def __init__(
        self
    ) -> None:

        self._devices: dict[
            str,
            ManagedNetworkDevice
        ] = {}

    @property
    def device_count(
        self
    ) -> int:

        return len(
            self._devices
        )

    def add_device(
        self,
        device: ManagedNetworkDevice
    ) -> None:
        """
        Adds a device to the inventory.
        """

        if (
            device.hostname
            in self._devices
        ):

            raise DeviceAlreadyExistsError(
                f"Device '{device.hostname}' "
                f"already exists."
            )

        self._devices[
            device.hostname
        ] = device

        print(
            f"[INVENTORY] Added "
            f"{device.hostname}"
        )

    def remove_device(
        self,
        hostname: str
    ) -> None:
        """
        Removes a device.
        """

        if (
            hostname
            not in self._devices
        ):

            raise DeviceNotFoundError(
                f"Device '{hostname}' "
                f"not found."
            )

        del self._devices[
            hostname
        ]

        print(
            f"[INVENTORY] Removed "
            f"{hostname}"
        )

    def get_device(
        self,
        hostname: str
    ) -> ManagedNetworkDevice:
        """
        Returns a device by hostname.
        """

        if (
            hostname
            not in self._devices
        ):

            raise DeviceNotFoundError(
                f"Device '{hostname}' "
                f"not found."
            )

        return self._devices[
            hostname
        ]

    def get_all_devices(
        self
    ) -> list[
        ManagedNetworkDevice
    ]:
        """
        Returns all devices.
        """

        return list(
            self._devices.values()
        )

    def find_by_type(
        self,
        device_type: str
    ) -> list[
        ManagedNetworkDevice
    ]:
        """
        Finds devices by type.
        """

        return [
            device
            for device
            in self._devices.values()
            if device.device_type.lower()
            == device_type.lower()
        ]

    def show_inventory(
        self
    ) -> None:
        """
        Displays the complete inventory.
        """

        print(
            "\nNetwork Device Inventory"
        )

        print(
            "-" * 75
        )

        print(
            f"{'Hostname':<15}"
            f"{'IP Address':<18}"
            f"{'Type':<15}"
            f"{'Vendor':<15}"
            f"Status"
        )

        print(
            "-" * 75
        )

        for device in (
            self._devices.values()
        ):

            status = (
                "Connected"
                if device.connected
                else "Offline"
            )

            print(
                f"{device.hostname:<15}"
                f"{device.ip_address:<18}"
                f"{device.device_type:<15}"
                f"{device.vendor:<15}"
                f"{status}"
            )


# =============================================================================
# SECTION 100 - Network Monitor
# =============================================================================


class NetworkMonitor:
    """
    Provides monitoring operations
    for network devices.
    """

    def __init__(
        self,
        inventory: DeviceInventory
    ) -> None:

        self.inventory = inventory

    def check_device(
        self,
        device: ManagedNetworkDevice
    ) -> str:
        """
        Returns the simulated device status.
        """

        if not device.enabled:

            return "Disabled"

        if device.connected:

            return "UP"

        return "DOWN"

    def monitor_all(
        self
    ) -> None:
        """
        Monitors every device in inventory.
        """

        print(
            "\nNetwork Monitoring"
        )

        print(
            "-" * 50
        )

        for device in (
            self.inventory.get_all_devices()
        ):

            status = self.check_device(
                device
            )

            print(
                f"{device.hostname:<15}"
                f" {status}"
            )


# =============================================================================
# SECTION 101 - Network Automation Service
# =============================================================================


class NetworkAutomationService:
    """
    Executes commands against devices.

    Demonstrates dependency injection
    by receiving an inventory object.
    """

    def __init__(
        self,
        inventory: DeviceInventory
    ) -> None:

        self.inventory = inventory

    def execute_on_device(
        self,
        hostname: str,
        command: str
    ) -> None:
        """
        Executes a command on one device.
        """

        try:

            device = (
                self.inventory.get_device(
                    hostname
                )
            )

            if not device.connected:

                device.connect()

            result = (
                device.execute_command(
                    command
                )
            )

            print(
                result
            )

        except DeviceManagementError as error:

            print(
                f"[ERROR] {error}"
            )

    def execute_on_all(
        self,
        command: str
    ) -> None:
        """
        Executes the same command
        on every device.
        """

        print(
            "\nExecuting command on "
            "all devices"
        )

        print(
            "-" * 50
        )

        for device in (
            self.inventory.get_all_devices()
        ):

            try:

                if not device.connected:

                    device.connect()

                result = (
                    device.execute_command(
                        command
                    )
                )

                print(
                    result
                )

            except DeviceManagementError as error:

                print(
                    f"[ERROR] {error}"
                )


# =============================================================================
# SECTION 102 - Configuration Backup Service
# =============================================================================


class ConfigurationBackupService:
    """
    Simulates configuration backups.
    """

    def __init__(
        self,
        inventory: DeviceInventory
    ) -> None:

        self.inventory = inventory

    def backup_device(
        self,
        hostname: str
    ) -> str:
        """
        Creates a simulated backup.
        """

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

    def backup_all(
        self
    ) -> None:
        """
        Creates backups for all devices.
        """

        print(
            "\nConfiguration Backups"
        )

        print(
            "-" * 50
        )

        for device in (
            self.inventory.get_all_devices()
        ):

            try:

                result = (
                    self.backup_device(
                        device.hostname
                    )
                )

                print(
                    result
                )

            except DeviceManagementError as error:

                print(
                    f"[ERROR] {error}"
                )


# =============================================================================
# SECTION 103 - Device Factory
# =============================================================================


class DeviceFactory:
    """
    Factory responsible for creating
    specialized network devices.
    """

    @staticmethod
    def create(
        device_type: str,
        hostname: str,
        ip_address: str,
        vendor: str,
        **kwargs
    ) -> ManagedNetworkDevice:
        """
        Creates a specialized device.
        """

        normalized_type = (
            device_type.strip().lower()
        )

        if normalized_type == "router":

            return ManagedRouter(
                hostname=hostname,
                ip_address=ip_address,
                vendor=vendor,
                routing_protocol=kwargs.get(
                    "routing_protocol",
                    "OSPF"
                )
            )

        if normalized_type == "switch":

            return ManagedSwitch(
                hostname=hostname,
                ip_address=ip_address,
                vendor=vendor,
                vlan_count=kwargs.get(
                    "vlan_count",
                    1
                )
            )

        if normalized_type == "firewall":

            return ManagedFirewall(
                hostname=hostname,
                ip_address=ip_address,
                vendor=vendor,
                policy_count=kwargs.get(
                    "policy_count",
                    0
                )
            )

        raise InvalidDeviceError(
            f"Unsupported device type: "
            f"{device_type}"
        )


# =============================================================================
# SECTION 104 - Factory Demo
# =============================================================================


def device_factory_demo() -> None:
    """
    Demonstrates the Factory Pattern.
    """

    print(
        "\nDevice Factory"
    )

    print(
        "-" * 50
    )

    router = DeviceFactory.create(
        "router",
        "R1",
        "192.168.10.1",
        "Cisco",
        routing_protocol="OSPF"
    )

    switch = DeviceFactory.create(
        "switch",
        "SW1",
        "192.168.10.10",
        "Cisco",
        vlan_count=50
    )

    firewall = DeviceFactory.create(
        "firewall",
        "FW1",
        "192.168.10.254",
        "Fortinet",
        policy_count=100
    )

    devices = [
        router,
        switch,
        firewall
    ]

    for device in devices:

        print(
            f"{device.hostname:<10}"
            f"{device.device_type:<12}"
            f"{device.vendor}"
        )


# =============================================================================
# SECTION 105 - Inventory Population
# =============================================================================


def populate_inventory(
    inventory: DeviceInventory
) -> None:
    """
    Creates and adds devices to inventory.
    """

    router = DeviceFactory.create(
        "router",
        "R1",
        "192.168.10.1",
        "Cisco",
        routing_protocol="OSPF"
    )

    switch = DeviceFactory.create(
        "switch",
        "SW1",
        "192.168.10.10",
        "Cisco",
        vlan_count=50
    )

    firewall = DeviceFactory.create(
        "firewall",
        "FW1",
        "192.168.10.254",
        "Fortinet",
        policy_count=120
    )

    router_two = DeviceFactory.create(
        "router",
        "R2",
        "192.168.20.1",
        "Cisco",
        routing_protocol="EIGRP"
    )

    inventory.add_device(
        router
    )

    inventory.add_device(
        switch
    )

    inventory.add_device(
        firewall
    )

    inventory.add_device(
        router_two
    )


# =============================================================================
# SECTION 106 - Inventory Demo
# =============================================================================


def final_inventory_demo() -> DeviceInventory:
    """
    Demonstrates complete inventory management.
    """

    print(
        "\n" + "=" * 70
    )

    print(
        "NETWORK DEVICE MANAGEMENT SYSTEM"
    )

    print(
        "=" * 70
    )

    inventory = DeviceInventory()

    populate_inventory(
        inventory
    )

    print(
        f"\nTotal Devices: "
        f"{inventory.device_count}"
    )

    inventory.show_inventory()

    return inventory


# =============================================================================
# SECTION 107 - Device Information Demo
# =============================================================================


def final_device_information_demo(
    inventory: DeviceInventory
) -> None:
    """
    Displays information about a device.
    """

    print(
        "\nDevice Information"
    )

    print(
        "-" * 50
    )

    try:

        device = (
            inventory.get_device("R1")
        )

        device.show_info()

        if isinstance(
            device,
            ManagedRouter
        ):

            device.show_routing_protocol()

    except DeviceNotFoundError as error:

        print(
            f"[ERROR] {error}"
        )


# =============================================================================
# SECTION 108 - Connection Demo
# =============================================================================


def final_connection_demo(
    inventory: DeviceInventory
) -> None:
    """
    Demonstrates device connections.
    """

    print(
        "\nDevice Connections"
    )

    print(
        "-" * 50
    )

    for device in (
        inventory.get_all_devices()
    ):

        try:

            device.connect()

        except DeviceManagementError as error:

            print(
                f"[ERROR] {error}"
            )


# =============================================================================
# SECTION 109 - Monitoring Demo
# =============================================================================


def final_monitoring_demo(
    inventory: DeviceInventory
) -> None:
    """
    Demonstrates network monitoring.
    """

    monitor = NetworkMonitor(
        inventory
    )

    monitor.monitor_all()


# =============================================================================
# SECTION 110 - Automation Demo
# =============================================================================


def final_automation_demo(
    inventory: DeviceInventory
) -> None:
    """
    Demonstrates network automation.
    """

    automation = (
        NetworkAutomationService(
            inventory
        )
    )

    automation.execute_on_device(
        "R1",
        "show ip interface brief"
    )

    automation.execute_on_all(
        "show version"
    )


# =============================================================================
# SECTION 111 - Backup Demo
# =============================================================================


def final_backup_demo(
    inventory: DeviceInventory
) -> None:
    """
    Demonstrates configuration backup.
    """

    backup_service = (
        ConfigurationBackupService(
            inventory
        )
    )

    backup_service.backup_all()


# =============================================================================
# SECTION 112 - Search Demo
# =============================================================================


def final_search_demo(
    inventory: DeviceInventory
) -> None:
    """
    Demonstrates searching the inventory.
    """

    print(
        "\nSearch Devices by Type"
    )

    print(
        "-" * 50
    )

    routers = inventory.find_by_type(
        "Router"
    )

    print(
        f"Routers found: "
        f"{len(routers)}"
    )

    for router in routers:

        print(
            f"  - "
            f"{router.hostname} "
            f"({router.ip_address})"
        )


# =============================================================================
# SECTION 113 - Error Handling Demo
# =============================================================================


def final_error_handling_demo(
    inventory: DeviceInventory
) -> None:
    """
    Demonstrates custom exception handling.
    """

    print(
        "\nError Handling"
    )

    print(
        "-" * 50
    )

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

        duplicate = DeviceFactory.create(
            "router",
            "R1",
            "10.10.10.1",
            "Cisco"
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
            "unknown",
            "DEV1",
            "10.10.10.10",
            "Unknown"
        )

    except InvalidDeviceError as error:

        print(
            f"[EXPECTED ERROR] "
            f"{error}"
        )


# =============================================================================
# SECTION 114 - Tags Demo
# =============================================================================


def final_tags_demo(
    inventory: DeviceInventory
) -> None:
    """
    Demonstrates device tags.
    """

    print(
        "\nDevice Tags"
    )

    print(
        "-" * 50
    )

    try:

        router = inventory.get_device(
            "R1"
        )

        router.add_tag(
            "core"
        )

        router.add_tag(
            "production"
        )

        router.add_tag(
            "ospf"
        )

        print(
            f"{router.hostname}: "
            f"{router.tags}"
        )

        router.remove_tag(
            "ospf"
        )

        print(
            f"After removing ospf: "
            f"{router.tags}"
        )

    except DeviceNotFoundError as error:

        print(
            f"[ERROR] {error}"
        )


# =============================================================================
# SECTION 115 - Polymorphism Demo
# =============================================================================


def final_polymorphism_demo(
    inventory: DeviceInventory
) -> None:
    """
    Demonstrates polymorphism.

    All device types expose execute_command()
    but each specialized class provides
    its own implementation.
    """

    print(
        "\nPolymorphism"
    )

    print(
        "-" * 50
    )

    command = (
        "show system information"
    )

    for device in (
        inventory.get_all_devices()
    ):

        try:

            result = (
                device.execute_command(
                    command
                )
            )

            print(
                result
            )

        except DeviceManagementError as error:

            print(
                f"[ERROR] {error}"
            )


# =============================================================================
# SECTION 116 - Final Project Summary
# =============================================================================


def final_project_summary() -> None:
    """
    Displays the concepts used in the project.
    """

    print(
        "\n" + "=" * 70
    )

    print(
        "LESSON 20 - FINAL PROJECT SUMMARY"
    )

    print(
        "=" * 70
    )

    concepts = [
        "Classes & Objects",
        "Encapsulation",
        "Properties",
        "Inheritance",
        "Polymorphism",
        "Composition",
        "Aggregation",
        "Abstract Base Classes",
        "Dataclasses",
        "Class Methods",
        "Static Methods",
        "Type Hints",
        "Custom Exceptions",
        "Factory Pattern",
        "Dependency Injection",
        "Device Inventory",
        "Network Monitoring",
        "Network Automation",
        "Configuration Backup"
    ]

    for number, concept in enumerate(
        concepts,
        start=1
    ):

        print(
            f"{number:02d}. {concept}"
        )


# =============================================================================
# SECTION 117 - Lesson 20 Final Runner
# =============================================================================


def run_part_five() -> None:
    """
    Runs Lesson 20 Part Five.
    """

    print(
        "\n" + "=" * 70
    )

    print(
        "LESSON 20"
    )

    print(
        "PART 5 - FINAL PROJECT"
    )

    print(
        "NETWORK DEVICE MANAGEMENT SYSTEM"
    )

    print(
        "=" * 70
    )

    # -------------------------------------------------------------------------
    # Create inventory
    # -------------------------------------------------------------------------

    inventory = (
        final_inventory_demo()
    )

    # -------------------------------------------------------------------------
    # Device information
    # -------------------------------------------------------------------------

    final_device_information_demo(
        inventory
    )

    # -------------------------------------------------------------------------
    # Connections
    # -------------------------------------------------------------------------

    final_connection_demo(
        inventory
    )

    # -------------------------------------------------------------------------
    # Monitoring
    # -------------------------------------------------------------------------

    final_monitoring_demo(
        inventory
    )

    # -------------------------------------------------------------------------
    # Automation
    # -------------------------------------------------------------------------

    final_automation_demo(
        inventory
    )

    # -------------------------------------------------------------------------
    # Backup
    # -------------------------------------------------------------------------

    final_backup_demo(
        inventory
    )

    # -------------------------------------------------------------------------
    # Search
    # -------------------------------------------------------------------------

    final_search_demo(
        inventory
    )

    # -------------------------------------------------------------------------
    # Tags
    # -------------------------------------------------------------------------

    final_tags_demo(
        inventory
    )

    # -------------------------------------------------------------------------
    # Polymorphism
    # -------------------------------------------------------------------------

    final_polymorphism_demo(
        inventory
    )

    # -------------------------------------------------------------------------
    # Error handling
    # -------------------------------------------------------------------------

    final_error_handling_demo(
        inventory
    )

    # -------------------------------------------------------------------------
    # Factory
    # -------------------------------------------------------------------------

    device_factory_demo()

    # -------------------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------------------

    final_project_summary()


# =============================================================================
# END OF LESSON 20 - PART 5
# =============================================================================
