"""
===============================================================================
File        : 02_data_types.py
Author      : Mohammed AL-Dubai
Course      : Python Basics
Lesson      : Python Data Types

Description:
    This lesson explains Python built-in data types.
    Python provides different data types to store and manipulate information.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Understand Python built-in data types.
✔ Work with numeric data types.
✔ Understand strings.
✔ Use Boolean values.
✔ Understand NoneType.
✔ Check data types using type().
✔ Validate types using isinstance().
✔ Understand mutable and immutable objects.

===============================================================================
"""


# =============================================================================
# IMPORTS
# =============================================================================

from typing import Any


# =============================================================================
# SECTION 1 - Introduction to Python Data Types
# =============================================================================

"""
Python is a dynamically typed language.

This means:

- You do not need to declare variable types.
- Python automatically determines the type.
- A variable can reference objects of different types.

Example:

value = 100

Python automatically knows that value is an integer.
"""


def introduction_demo() -> None:
    """
    Demonstrates automatic type detection in Python.
    """

    value = 100

    print("Value:", value)
    print("Data Type:", type(value))


# =============================================================================
# SECTION 2 - Numeric Data Types
# =============================================================================

"""
Python provides three numeric types:

1. int
   - Whole numbers

2. float
   - Decimal numbers

3. complex
   - Numbers with real and imaginary parts
"""


# -----------------------------------------------------------------------------
# Integer Type
# -----------------------------------------------------------------------------


def integer_demo() -> None:
    """
    Demonstrates integer (int) data type.

    Integers represent whole numbers without decimals.
    """

    age: int = 47
    port_number: int = 443
    users_count: int = 250

    print("\nInteger Examples")
    print("-" * 40)

    print("Age:", age)
    print("Port:", port_number)
    print("Users:", users_count)

    print("Type:", type(age))


# -----------------------------------------------------------------------------
# Float Type
# -----------------------------------------------------------------------------


def float_demo() -> None:
    """
    Demonstrates floating point numbers.

    Floats represent decimal values.
    """

    temperature: float = 28.5
    cpu_usage: float = 75.8
    packet_loss: float = 0.02

    print("\nFloat Examples")
    print("-" * 40)

    print("Temperature:", temperature)
    print("CPU Usage:", cpu_usage)
    print("Packet Loss:", packet_loss)

    print("Type:", type(temperature))


# -----------------------------------------------------------------------------
# Complex Type
# -----------------------------------------------------------------------------


def complex_demo() -> None:
    """
    Demonstrates complex numbers.

    Complex numbers contain:
    - Real part
    - Imaginary part
    """

    number: complex = 3 + 5j

    print("\nComplex Number Example")
    print("-" * 40)

    print("Number:", number)
    print("Real Part:", number.real)
    print("Imaginary Part:", number.imag)

    print("Type:", type(number))


# =============================================================================
# SECTION 3 - String Data Type
# =============================================================================


def string_demo() -> None:
    """
    Demonstrates string (str) data type.

    Strings represent sequences of characters.
    """

    first_name: str = "Mohammed"
    last_name: str = "AL-Dubai"

    full_name: str = f"{first_name} {last_name}"

    print("\nString Examples")
    print("-" * 40)

    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Full Name:", full_name)

    print("Type:", type(full_name))


# =============================================================================
# SECTION 4 - Boolean Data Type
# =============================================================================


def boolean_demo() -> None:
    """
    Demonstrates Boolean values.

    Boolean values have only two states:

    True
    False
    """

    is_online: bool = True
    firewall_enabled: bool = False

    print("\nBoolean Examples")
    print("-" * 40)

    print("System Online:", is_online)
    print("Firewall Enabled:", firewall_enabled)

    print("Type:", type(is_online))


# =============================================================================
# SECTION 5 - NoneType
# =============================================================================


def none_demo() -> None:
    """
    Demonstrates NoneType.

    None represents the absence of a value.
    """

    connection_status: None = None

    print("\nNone Example")
    print("-" * 40)

    print("Connection Status:", connection_status)

    print("Type:", type(connection_status))


# =============================================================================
# SECTION 6 - Checking Data Types
# =============================================================================


def type_checking_demo() -> None:
    """
    Demonstrates type() function.
    """

    examples: list[Any] = [
        100,
        3.14,
        "Python",
        True,
        None
    ]

    print("\nType Checking")
    print("-" * 40)

    for item in examples:
        print(item, "->", type(item))

# =============================================================================
# SECTION 7 - isinstance() Function
# =============================================================================


def isinstance_demo() -> None:
    """
    Demonstrates the isinstance() function.

    isinstance() checks whether an object belongs to a specific data type.
    """

    print("\nisinstance() Examples")
    print("-" * 40)

    age: int = 47
    name: str = "Mohammed"
    status: bool = True

    print(
        "age is integer:",
        isinstance(age, int)
    )

    print(
        "name is string:",
        isinstance(name, str)
    )

    print(
        "status is boolean:",
        isinstance(status, bool)
    )


# =============================================================================
# SECTION 8 - Sequence Data Types
# =============================================================================

"""
Sequence Types store multiple values in an ordered collection.

Python provides:

1. list
2. tuple
3. range
"""


# -----------------------------------------------------------------------------
# List Type
# -----------------------------------------------------------------------------


def list_demo() -> None:
    """
    Demonstrates list data type.

    Lists are:
    - Ordered
    - Mutable
    - Allow duplicate values
    """

    devices: list[str] = [
        "Router",
        "Switch",
        "Firewall"
    ]

    print("\nList Examples")
    print("-" * 40)

    print("Devices:", devices)

    print("First Device:", devices[0])

    # Adding new item
    devices.append("Access Point")

    print("After Adding:", devices)

    # Removing item
    devices.remove("Switch")

    print("After Removing:", devices)

    print("Type:", type(devices))


# -----------------------------------------------------------------------------
# Tuple Type
# -----------------------------------------------------------------------------


def tuple_demo() -> None:
    """
    Demonstrates tuple data type.

    Tuples are:
    - Ordered
    - Immutable
    - Allow duplicate values
    """

    network_protocols: tuple[str, ...] = (
        "TCP",
        "UDP",
        "ICMP"
    )

    print("\nTuple Examples")
    print("-" * 40)

    print("Protocols:", network_protocols)

    print("First Protocol:", network_protocols[0])

    print("Type:", type(network_protocols))


# -----------------------------------------------------------------------------
# Range Type
# -----------------------------------------------------------------------------


def range_demo() -> None:
    """
    Demonstrates range data type.

    Range generates a sequence of numbers.
    """

    ports = range(1, 6)

    print("\nRange Examples")
    print("-" * 40)

    for port in ports:
        print("Port:", port)

    print("Type:", type(ports))


# =============================================================================
# SECTION 9 - Set Data Types
# =============================================================================

"""
Set Types:

1. set
2. frozenset

Sets:
- Are unordered
- Do not allow duplicate values
- Are mutable

Frozen sets:
- Are immutable sets
"""


# -----------------------------------------------------------------------------
# Set Type
# -----------------------------------------------------------------------------


def set_demo() -> None:
    """
    Demonstrates set data type.
    """

    ip_addresses: set[str] = {
        "192.168.1.10",
        "192.168.1.20",
        "192.168.1.10"
    }

    print("\nSet Examples")
    print("-" * 40)

    print("IP Addresses:", ip_addresses)

    print("Type:", type(ip_addresses))


# -----------------------------------------------------------------------------
# Frozen Set Type
# -----------------------------------------------------------------------------


def frozenset_demo() -> None:
    """
    Demonstrates frozenset.

    Frozen sets cannot be modified after creation.
    """

    allowed_protocols = frozenset(
        [
            "HTTPS",
            "SSH",
            "DNS"
        ]
    )

    print("\nFrozen Set Example")
    print("-" * 40)

    print("Protocols:", allowed_protocols)

    print("Type:", type(allowed_protocols))


# =============================================================================
# SECTION 10 - Dictionary Type
# =============================================================================


def dictionary_demo() -> None:
    """
    Demonstrates dictionary data type.

    Dictionaries store data as:

    key : value
    """

    network_device: dict[str, str] = {

        "hostname": "R1",
        "vendor": "Cisco",
        "ip_address": "192.168.1.1",
        "os": "IOS-XE"

    }

    print("\nDictionary Examples")
    print("-" * 40)

    print("Device Information")

    for key, value in network_device.items():

        print(
            f"{key}: {value}"
        )

    print("Type:", type(network_device))


# =============================================================================
# SECTION 11 - Binary Data Types
# =============================================================================

"""
Python provides three binary types:

1. bytes
2. bytearray
3. memoryview
"""


# -----------------------------------------------------------------------------
# Bytes Type
# -----------------------------------------------------------------------------


def bytes_demo() -> None:
    """
    Demonstrates bytes data type.

    Bytes are immutable binary sequences.
    """

    data: bytes = b"Python"

    print("\nBytes Example")
    print("-" * 40)

    print("Data:", data)

    print("Type:", type(data))


# -----------------------------------------------------------------------------
# Bytearray Type
# -----------------------------------------------------------------------------


def bytearray_demo() -> None:
    """
    Demonstrates bytearray.

    Bytearray is a mutable version of bytes.
    """

    data: bytearray = bytearray(
        b"Network"
    )

    print("\nBytearray Example")
    print("-" * 40)

    print("Original:", data)

    data[0] = 80

    print("Modified:", data)

    print("Type:", type(data))


# -----------------------------------------------------------------------------
# Memoryview Type
# -----------------------------------------------------------------------------


def memoryview_demo() -> None:
    """
    Demonstrates memoryview.

    Memoryview provides access to the internal
    memory representation of binary data.
    """

    data = b"CyberSecurity"

    view = memoryview(data)

    print("\nMemoryview Example")
    print("-" * 40)

    print("Original Data:", data)

    print("First Byte:", view[0])

    print("Type:", type(view))


# =============================================================================
# SECTION 12 - Running Part Two Examples
# =============================================================================


def run_part_two() -> None:
    """
    Executes all examples from Part Two.
    """

    isinstance_demo()

    list_demo()

    tuple_demo()

    range_demo()

    set_demo()

    frozenset_demo()

    dictionary_demo()

    bytes_demo()

    bytearray_demo()

    memoryview_demo()


# =============================================================================
# END OF PART 2
# =============================================================================

# =============================================================================
# SECTION 13 - Mutable vs Immutable Objects
# =============================================================================

"""
Python objects can be divided into two categories:

1. Immutable Objects
--------------------
Objects that cannot be changed after creation.

Examples:
    int
    float
    bool
    str
    tuple


2. Mutable Objects
------------------
Objects that can be modified after creation.

Examples:
    list
    set
    dictionary
"""


def immutable_demo() -> None:
    """
    Demonstrates immutable objects.

    Strings are immutable.
    Any modification creates a new object.
    """

    print("\nImmutable Object Example")
    print("-" * 40)

    message: str = "Python"

    print("Original:", message)
    print("Memory:", id(message))

    message = "Python Security"

    print("Modified:", message)
    print("Memory:", id(message))


def mutable_demo() -> None:
    """
    Demonstrates mutable objects.

    Lists can be modified without creating a new object.
    """

    print("\nMutable Object Example")
    print("-" * 40)

    devices: list[str] = [
        "Router",
        "Switch"
    ]

    print("Before:", devices)
    print("Memory:", id(devices))

    devices.append("Firewall")

    print("After:", devices)
    print("Memory:", id(devices))


# =============================================================================
# SECTION 14 - Comparing Python Data Types
# =============================================================================


def comparison_demo() -> None:
    """
    Compares different Python data types.
    """

    print("\nData Types Comparison")
    print("-" * 40)

    data = {

        "Integer": 100,

        "Float": 10.5,

        "String": "Python",

        "Boolean": True,

        "List": ["A", "B"],

        "Tuple": ("A", "B"),

        "Set": {"A", "B"},

        "Dictionary": {
            "key": "value"
        }

    }

    for name, value in data.items():

        print(
            f"{name:<15} -> {type(value)}"
        )


# =============================================================================
# SECTION 15 - Network Engineering Example
# =============================================================================


def network_engineering_example() -> None:
    """
    Demonstrates data types used in network automation.
    """

    print("\nNetwork Engineering Example")
    print("-" * 40)

    device_name: str = "Core-Router-01"

    ip_address: str = "10.10.10.1"

    interfaces: list[str] = [

        "GigabitEthernet0/1",
        "GigabitEthernet0/2"

    ]

    vlan_id: int = 100

    uptime_hours: float = 245.5

    ssh_enabled: bool = True


    print(f"Device       : {device_name}")
    print(f"IP Address   : {ip_address}")
    print(f"Interfaces   : {interfaces}")
    print(f"VLAN ID      : {vlan_id}")
    print(f"Uptime       : {uptime_hours}")
    print(f"SSH Enabled  : {ssh_enabled}")


# =============================================================================
# SECTION 16 - Cybersecurity Example
# =============================================================================


def cybersecurity_example() -> None:
    """
    Demonstrates data types used in cybersecurity scripts.
    """

    print("\nCybersecurity Example")
    print("-" * 40)


    target: str = "192.168.1.50"

    open_ports: list[int] = [

        22,
        80,
        443

    ]


    services: dict[int, str] = {
        22: "SSH",
        80: "HTTP",
        443: "HTTPS"
    }


    scan_completed: bool = True


    print(f"Target       : {target}")
    print(f"Open Ports   : {open_ports}")
    print(f"Services     : {services}")
    print(f"Completed    : {scan_completed}")


# =============================================================================
# SECTION 17 - Best Practices
# =============================================================================


def best_practices_demo() -> None:
    """
    Demonstrates recommended practices when using variables.
    """

    print("\nBest Practices")
    print("-" * 40)


    # Good naming

    network_device_count: int = 50

    firewall_status: bool = True


    print(network_device_count)

    print(firewall_status)


    """
    Recommendations:
    ✔ Use meaningful names.
    ✔ Follow snake_case.
    ✔ Use type hints when possible.
    ✔ Avoid unnecessary variables.
    ✔ Choose the correct data type.
    ✔ Keep data structures simple.
    """


# =============================================================================
# SECTION 18 - Common Mistakes
# =============================================================================


def common_mistakes_demo() -> None:
    """
    Shows common mistakes when working with data types.
    """

    print("\nCommon Mistakes")
    print("-" * 40)


    """
    Mistake 1:
    Treating string as number.

    Example:
    age = "25"
    age + 5

    This causes TypeError.
    
    Mistake 2:
    Modifying immutable objects.
    
    Mistake 3:
    Using list when tuple is more suitable.
    
    Mistake 4:
    Ignoring data validation.

    """


# =============================================================================
# SECTION 19 - Coding Exercises
# =============================================================================


"""
Exercise 1
-----------
Create variables representing:
- Username
- Password
- Login Status
- Number of Failed Attempts
Print their data types.

Exercise 2
-----------
Create a network device dictionary:
hostname
ip_address
vendor
model
os_version

Exercise 3
-----------
Create a list of five cybersecurity tools.
Print each tool.

Exercise 4
-----------
Create a tuple containing:
TCP
UDP
ICMP

Exercise 5
-----------
Create a set of unique IP addresses.
"""


# =============================================================================
# SECTION 20 - Interview Questions
# =============================================================================


"""
Question 1:
------------
What are Python built-in data types?

Question 2:
------------
What is the difference between list and tuple?

Question 3:
------------
What is mutable and immutable?

Question 4:
------------
Why are strings immutable?

Question 5:
------------
What is the difference between type()
and isinstance()?

Question 6:
------------
When would you use a dictionary?

Question 7:
------------
What is NoneType?

Question 8:
------------
What is the difference between bytes and bytearray?

Question 9:
------------
Why are sets useful in cybersecurity?

Question 10:
-------------
Why should engineers understand data types?
"""

# =============================================================================
# SECTION 21 - Mini Project
# =============================================================================

"""
Mini Project:
Network Device Inventory System

Requirements:
Create a dictionary containing:
Device Name
Vendor
Model
IP Address
MAC Address
Operating System
VLANs
Interfaces
SSH Status
Uptime

Then:
1. Print device information.
2. Display data types.
3. Add a new interface.
4. Update device status.
5. Export the information later to JSON.

This project prepares you for:
- Network Automation
- REST APIs
- Netmiko
- Nornir
- pyATS
"""

# =============================================================================
# SECTION 22 - Update Main Function
# =============================================================================


# =============================================================================
# MAIN FUNCTION
# =============================================================================

def main() -> None:
    """
    Main function that runs all demonstrations.
    """

    # Part One

    introduction_demo()
    integer_demo()
    float_demo()
    complex_demo()
    string_demo()
    boolean_demo()
    none_demo()
    type_checking_demo()


    # Part Two

    isinstance_demo()
    list_demo()
    tuple_demo()
    range_demo()
    set_demo()
    frozenset_demo()
    dictionary_demo()
    bytes_demo()
    bytearray_demo()
    memoryview_demo()


    # Part Three

    immutable_demo()
    mutable_demo()
    comparison_demo()
    network_engineering_example()
    cybersecurity_example()
    best_practices_demo()
    common_mistakes_demo()


if __name__ == "__main__":
    main()
