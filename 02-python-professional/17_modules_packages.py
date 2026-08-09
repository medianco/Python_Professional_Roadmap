"""
===============================================================================
File        : 17_modules_packages.py
Author      : Mohammed AL-Dubai
Course      : Python Professional Roadmap
Stage       : Professional Python
Lesson      : Modules & Packages
Part        : 1 - Modules

Description:
    Introduction to Python modules, imports, aliases,
    reusable functions, and practical examples.

Learning Objectives
-------------------
After completing this part, you will be able to:

✔ Understand what a Python module is.
✔ Understand how import works.
✔ Use from ... import.
✔ Use aliases with import.
✔ Understand reusable code.
✔ Organize functionality into logical modules.
✔ Understand how modules support large projects.

===============================================================================
"""


# =============================================================================
# SECTION 1 - What is a Module?
# =============================================================================

"""
A module is a Python file containing reusable code.

A module can contain:

- Variables
- Functions
- Classes
- Constants
- Other Python objects

Example:

network_utils.py

    def ping_device():
        ...


Then another Python file can import it:

import network_utils
"""


# =============================================================================
# SECTION 2 - Standard Library Module
# =============================================================================

import math


def standard_module_demo() -> None:
    """
    Demonstrates importing a standard Python module.
    """

    print("\nStandard Library Module")
    print("-" * 40)

    number: float = 25

    result: float = math.sqrt(number)

    print(f"Number       : {number}")
    print(f"Square Root  : {result}")


# =============================================================================
# SECTION 3 - import Module
# =============================================================================

import random


def import_module_demo() -> None:
    """
    Demonstrates importing and using a module.
    """

    print("\nimport Module")
    print("-" * 40)

    number: int = random.randint(1, 100)

    print(f"Random Number: {number}")


# =============================================================================
# SECTION 4 - Module Aliases
# =============================================================================

import datetime as dt


def module_alias_demo() -> None:
    """
    Demonstrates importing a module using an alias.
    """

    print("\nModule Alias")
    print("-" * 40)

    current_time = dt.datetime.now()

    print(f"Current Date and Time: {current_time}")


# =============================================================================
# SECTION 5 - from Module import
# =============================================================================

from math import pi, sqrt


def from_import_demo() -> None:
    """
    Demonstrates importing specific objects
    from a module.
    """

    print("\nfrom Module import")
    print("-" * 40)

    number: float = 64

    print(f"PI       : {pi}")
    print(f"Square Root: {sqrt(number)}")


# =============================================================================
# SECTION 6 - Multiple Imports
# =============================================================================

from os import getcwd, listdir


def multiple_import_demo() -> None:
    """
    Demonstrates importing multiple functions
    from a module.
    """

    print("\nMultiple Imports")
    print("-" * 40)

    current_directory: str = getcwd()

    print(f"Current Directory: {current_directory}")

    files = listdir(current_directory)

    print("\nDirectory Contents:")

    for file_name in files[:10]:
        print(f"- {file_name}")


# =============================================================================
# SECTION 7 - Creating Reusable Functions
# =============================================================================


def calculate_network_delay(
    packets: int,
    total_time: float
) -> float:
    """
    Calculates average network delay.
    """

    if packets <= 0:
        raise ValueError("Packets must be greater than zero.")

    return total_time / packets


def reusable_function_demo() -> None:
    """
    Demonstrates a reusable function
    that could belong to a module.
    """

    print("\nReusable Function")
    print("-" * 40)

    packets: int = 100
    total_time: float = 250.0

    average_delay = calculate_network_delay(
        packets,
        total_time
    )

    print(f"Packets       : {packets}")
    print(f"Total Time    : {total_time} ms")
    print(f"Average Delay : {average_delay} ms")


# =============================================================================
# SECTION 8 - Network Utility Example
# =============================================================================


def normalize_hostname(hostname: str) -> str:
    """
    Normalizes a network hostname.
    """

    return hostname.strip().lower()


def network_utility_demo() -> None:
    """
    Demonstrates a reusable network utility.
    """

    print("\nNetwork Utility")
    print("-" * 40)

    hostname: str = "  CORE-R1  "

    normalized = normalize_hostname(hostname)

    print(f"Original  : '{hostname}'")
    print(f"Normalized: '{normalized}'")


# =============================================================================
# SECTION 9 - Cybersecurity Utility Example
# =============================================================================


def calculate_password_length(password: str) -> int:
    """
    Returns the length of a password.
    """

    return len(password)


def security_utility_demo() -> None:
    """
    Demonstrates a reusable cybersecurity utility.
    """

    print("\nCybersecurity Utility")
    print("-" * 40)

    password: str = "SecurePassword123!"

    length = calculate_password_length(password)

    print(f"Password Length: {length}")


# =============================================================================
# SECTION 10 - Constants in Modules
# =============================================================================


DEFAULT_SSH_PORT: int = 22
DEFAULT_HTTPS_PORT: int = 443
DEFAULT_DNS_PORT: int = 53


def module_constants_demo() -> None:
    """
    Demonstrates constants that could be
    stored inside a dedicated module.
    """

    print("\nModule Constants")
    print("-" * 40)

    print(f"SSH Port  : {DEFAULT_SSH_PORT}")
    print(f"HTTPS Port: {DEFAULT_HTTPS_PORT}")
    print(f"DNS Port  : {DEFAULT_DNS_PORT}")


# =============================================================================
# SECTION 11 - Why Use Modules?
# =============================================================================

def why_modules_demo() -> None:
    """
    Explains the main benefits of modules.
    """

    print("\nWhy Use Modules?")
    print("-" * 40)

    benefits: list[str] = [
        "Code Reusability",
        "Better Organization",
        "Easier Maintenance",
        "Reduced Duplication",
        "Clear Project Structure",
        "Easier Testing",
        "Team Collaboration"
    ]

    for benefit in benefits:
        print(f"✔ {benefit}")


# =============================================================================
# SECTION 12 - Practical Project Structure
# =============================================================================

def project_structure_demo() -> None:
    """
    Demonstrates how a project can be
    divided into modules.
    """

    print("\nPractical Project Structure")
    print("-" * 40)

    structure: list[str] = [
        "network_automation/",
        "├── devices.py",
        "├── utilities.py",
        "├── configuration.py",
        "├── logging_utils.py",
        "└── main.py"
    ]

    for line in structure:
        print(line)


# =============================================================================
# SECTION 13 - Part One Runner
# =============================================================================


def run_part_one() -> None:
    """
    Runs all demonstrations from Part One.
    """

    standard_module_demo()

    import_module_demo()

    module_alias_demo()

    from_import_demo()

    multiple_import_demo()

    reusable_function_demo()

    network_utility_demo()

    security_utility_demo()

    module_constants_demo()

    why_modules_demo()

    project_structure_demo()

# =============================================================================
# SECTION 14 - The __name__ Variable
# =============================================================================

"""
Every Python module has a special built-in variable called:

    __name__

When a Python file is executed directly:

    __name__ == "__main__"

When the file is imported as a module:

    __name__ == "module_name"
"""


# =============================================================================
# SECTION 15 - Displaying __name__
# =============================================================================


def name_variable_demo() -> None:
    """
    Demonstrates the special __name__ variable.
    """

    print("\n__name__ Variable")
    print("-" * 40)

    print(f"Current module name: {__name__}")


# =============================================================================
# SECTION 16 - Direct Execution
# =============================================================================


def direct_execution_demo() -> None:
    """
    Explains direct execution of a Python file.
    """

    print("\nDirect Execution")
    print("-" * 40)

    print("When a Python file is executed directly:")
    print("__name__ becomes '__main__'")


# =============================================================================
# SECTION 17 - Module Import Concept
# =============================================================================


def module_import_concept_demo() -> None:
    """
    Demonstrates the concept of importing a module.
    """

    print("\nModule Import Concept")
    print("-" * 40)

    print("When a file is imported:")
    print("__name__ becomes the module name.")

    print("\nExample:")
    print("import network_utils")
    print("network_utils.__name__")


# =============================================================================
# SECTION 18 - __main__ Guard
# =============================================================================


def main_guard_demo() -> None:
    """
    Demonstrates the purpose of the __main__ guard.
    """

    print("\n__main__ Guard")
    print("-" * 40)

    print("The standard pattern is:")
    print()
    print("if __name__ == '__main__':")
    print("    main()")


# =============================================================================
# SECTION 19 - Why Use the __main__ Guard?
# =============================================================================


def why_main_guard_demo() -> None:
    """
    Explains why the __main__ guard is useful.
    """

    print("\nWhy Use the __main__ Guard?")
    print("-" * 40)

    benefits: list[str] = [
        "Prevents code from running automatically when imported.",
        "Separates reusable code from executable code.",
        "Makes modules easier to reuse.",
        "Makes testing easier.",
        "Improves project organization."
    ]

    for benefit in benefits:
        print(f"✔ {benefit}")


# =============================================================================
# SECTION 20 - Reusable Module Example
# =============================================================================


def calculate_average(
    values: list[float]
) -> float:
    """
    Calculates the average of a list of values.
    """

    if not values:
        raise ValueError("The values list cannot be empty.")

    return sum(values) / len(values)


def reusable_module_demo() -> None:
    """
    Demonstrates a function that could be
    imported and reused from another module.
    """

    print("\nReusable Module Example")
    print("-" * 40)

    values: list[float] = [
        10.0,
        20.0,
        30.0,
        40.0
    ]

    average = calculate_average(values)

    print(f"Values : {values}")
    print(f"Average: {average}")


# =============================================================================
# SECTION 21 - Network Module Example
# =============================================================================


def get_device_info(
    hostname: str,
    ip_address: str
) -> dict[str, str]:
    """
    Returns basic network device information.
    """

    return {
        "hostname": hostname,
        "ip_address": ip_address
    }


def network_module_demo() -> None:
    """
    Demonstrates a function that could belong
    to a network module.
    """

    print("\nNetwork Module Example")
    print("-" * 40)

    device = get_device_info(
        "R1",
        "192.168.1.1"
    )

    print(f"Hostname : {device['hostname']}")
    print(f"IP       : {device['ip_address']}")


# =============================================================================
# SECTION 22 - Cybersecurity Module Example
# =============================================================================


def classify_security_event(
    severity: int
) -> str:
    """
    Classifies a security event according
    to its severity score.
    """

    if severity >= 8:
        return "CRITICAL"

    if severity >= 5:
        return "HIGH"

    if severity >= 3:
        return "MEDIUM"

    return "LOW"


def cybersecurity_module_demo() -> None:
    """
    Demonstrates a function that could belong
    to a cybersecurity module.
    """

    print("\nCybersecurity Module Example")
    print("-" * 40)

    severity: int = 9

    classification = classify_security_event(
        severity
    )

    print(f"Severity     : {severity}")
    print(f"Classification: {classification}")


# =============================================================================
# SECTION 23 - Module API Concept
# =============================================================================


def module_api_demo() -> None:
    """
    Demonstrates the concept of a module API.

    A module API is the collection of functions,
    classes, and constants that other modules
    are expected to use.
    """

    print("\nModule API")
    print("-" * 40)

    print("A module can expose:")
    print("✔ Functions")
    print("✔ Classes")
    print("✔ Constants")
    print("✔ Objects")

    print("\nA good module should provide:")
    print("✔ Clear interfaces")
    print("✔ Meaningful names")
    print("✔ Minimal unnecessary dependencies")


# =============================================================================
# SECTION 24 - Practical Project Structure
# =============================================================================


def main_guard_project_structure_demo() -> None:
    """
    Demonstrates a practical project structure
    using multiple modules.
    """

    print("\nPractical Module Structure")
    print("-" * 40)

    structure: list[str] = [
        "network_automation/",
        "├── devices.py",
        "├── utilities.py",
        "├── configuration.py",
        "├── logging_utils.py",
        "└── main.py"
    ]

    for line in structure:
        print(line)

    print("\nExample:")
    print("main.py imports functions from other modules.")


# =============================================================================
# SECTION 25 - Part Two Runner
# =============================================================================


def run_part_two() -> None:
    """
    Runs all demonstrations from Part Two.
    """

    name_variable_demo()

    direct_execution_demo()

    module_import_concept_demo()

    main_guard_demo()

    why_main_guard_demo()

    reusable_module_demo()

    network_module_demo()

    cybersecurity_module_demo()

    module_api_demo()

    main_guard_project_structure_demo()

# =============================================================================
# SECTION 26 - What is a Package?
# =============================================================================

"""
A Python package is a directory used to organize
related Python modules.

Example:

network_automation/
│
├── __init__.py
├── devices.py
├── utilities.py
└── configuration.py


A package helps us:

✔ Organize large projects.
✔ Group related modules.
✔ Reuse code.
✔ Improve maintainability.
✔ Separate different responsibilities.
"""


# =============================================================================
# SECTION 27 - Package Structure
# =============================================================================


def package_structure_demo() -> None:
    """
    Demonstrates a basic Python package structure.
    """

    print("\nPython Package Structure")
    print("-" * 40)

    structure: list[str] = [
        "network_automation/",
        "├── __init__.py",
        "├── devices.py",
        "├── utilities.py",
        "└── configuration.py"
    ]

    for line in structure:
        print(line)


# =============================================================================
# SECTION 28 - __init__.py
# =============================================================================


def init_file_demo() -> None:
    """
    Explains the purpose of __init__.py.
    """

    print("\n__init__.py")
    print("-" * 40)

    print("__init__.py can be used to:")
    print("✔ Initialize a package.")
    print("✔ Define package-level objects.")
    print("✔ Control what the package exposes.")
    print("✔ Organize package imports.")

    print("\nExample:")
    print("network_automation/__init__.py")


# =============================================================================
# SECTION 29 - Importing a Module from a Package
# =============================================================================


def package_module_import_demo() -> None:
    """
    Demonstrates importing a module
    from a package conceptually.
    """

    print("\nImporting a Module from a Package")
    print("-" * 40)

    print("Example:")
    print("import network_automation.devices")

    print("\nOr:")
    print("from network_automation import devices")


# =============================================================================
# SECTION 30 - Importing a Function from a Package Module
# =============================================================================


def package_function_import_demo() -> None:
    """
    Demonstrates importing a function
    from a package module.
    """

    print("\nImporting a Function")
    print("-" * 40)

    print("Example:")
    print(
        "from network_automation.devices "
        "import connect_device"
    )


# =============================================================================
# SECTION 31 - Package Aliases
# =============================================================================


def package_alias_demo() -> None:
    """
    Demonstrates aliases when importing
    package modules.
    """

    print("\nPackage Alias")
    print("-" * 40)

    print("Example:")
    print(
        "import network_automation.devices "
        "as devices"
    )

    print("\nThen:")
    print("devices.connect_device()")


# =============================================================================
# SECTION 32 - Multiple Modules in a Package
# =============================================================================


def multiple_package_modules_demo() -> None:
    """
    Demonstrates a package containing
    multiple specialized modules.
    """

    print("\nMultiple Modules in a Package")
    print("-" * 40)

    modules: list[str] = [
        "devices.py",
        "configuration.py",
        "utilities.py",
        "logging_utils.py"
    ]

    for module in modules:
        print(f"✔ {module}")


# =============================================================================
# SECTION 33 - Network Automation Package
# =============================================================================


def network_package_demo() -> None:
    """
    Demonstrates a package structure
    for network automation.
    """

    print("\nNetwork Automation Package")
    print("-" * 40)

    structure: list[str] = [
        "network_automation/",
        "├── __init__.py",
        "├── devices.py",
        "├── configuration.py",
        "├── interfaces.py",
        "├── routing.py",
        "└── utilities.py"
    ]

    for line in structure:
        print(line)


# =============================================================================
# SECTION 34 - Cybersecurity Package
# =============================================================================


def cybersecurity_package_demo() -> None:
    """
    Demonstrates a package structure
    for cybersecurity automation.
    """

    print("\nCybersecurity Package")
    print("-" * 40)

    structure: list[str] = [
        "security_tools/",
        "├── __init__.py",
        "├── scanner.py",
        "├── logs.py",
        "├── alerts.py",
        "├── network.py",
        "└── utilities.py"
    ]

    for line in structure:
        print(line)


# =============================================================================
# SECTION 35 - Subpackages
# =============================================================================


def subpackage_demo() -> None:
    """
    Demonstrates nested packages (subpackages).
    """

    print("\nSubpackages")
    print("-" * 40)

    structure: list[str] = [
        "automation/",
        "├── __init__.py",
        "│",
        "├── network/",
        "│   ├── __init__.py",
        "│   ├── devices.py",
        "│   └── routing.py",
        "│",
        "└── security/",
        "    ├── __init__.py",
        "    ├── scanner.py",
        "    └── alerts.py"
    ]

    for line in structure:
        print(line)


# =============================================================================
# SECTION 36 - Relative Imports
# =============================================================================


def relative_import_demo() -> None:
    """
    Demonstrates the concept of relative imports.
    """

    print("\nRelative Imports")
    print("-" * 40)

    print("Inside a package, modules can use:")
    print()
    print("from .devices import connect_device")
    print()
    print("The dot means:")
    print("Current package")


# =============================================================================
# SECTION 37 - Parent Package Import
# =============================================================================


def parent_package_import_demo() -> None:
    """
    Demonstrates importing from a parent package.
    """

    print("\nParent Package Import")
    print("-" * 40)

    print("Relative import example:")
    print()
    print("from ..utilities import normalize_hostname")

    print("\n.. means:")
    print("Parent package")


# =============================================================================
# SECTION 38 - Package Responsibilities
# =============================================================================


def package_responsibilities_demo() -> None:
    """
    Demonstrates separation of responsibilities
    inside a package.
    """

    print("\nPackage Responsibilities")
    print("-" * 40)

    responsibilities: dict[str, str] = {
        "devices.py": "Device connection and management",
        "configuration.py": "Configuration operations",
        "interfaces.py": "Interface operations",
        "routing.py": "Routing operations",
        "utilities.py": "Reusable helper functions"
    }

    for module, responsibility in responsibilities.items():
        print(f"{module:<20} -> {responsibility}")


# =============================================================================
# SECTION 39 - Good Package Design
# =============================================================================


def good_package_design_demo() -> None:
    """
    Demonstrates principles of good package design.
    """

    print("\nGood Package Design")
    print("-" * 40)

    principles: list[str] = [
        "Keep modules focused.",
        "Use meaningful module names.",
        "Avoid unnecessary dependencies.",
        "Separate responsibilities.",
        "Avoid circular imports.",
        "Keep public interfaces simple.",
        "Document important modules."
    ]

    for principle in principles:
        print(f"✔ {principle}")


# =============================================================================
# SECTION 40 - Package Example for the Roadmap
# =============================================================================


def roadmap_package_demo() -> None:
    """
    Demonstrates how packages will be used
    later in the Python Professional Roadmap.
    """

    print("\nRoadmap Package Example")
    print("-" * 40)

    structure: list[str] = [
        "network_toolkit/",
        "├── __init__.py",
        "│",
        "├── devices/",
        "│   ├── __init__.py",
        "│   ├── cisco.py",
        "│   ├── mikrotik.py",
        "│   └── arista.py",
        "│",
        "├── utilities/",
        "│   ├── __init__.py",
        "│   ├── ip_utils.py",
        "│   └── config_utils.py",
        "│",
        "└── main.py"
    ]

    for line in structure:
        print(line)


# =============================================================================
# SECTION 41 - Part Three Runner
# =============================================================================


def run_part_three() -> None:
    """
    Runs all demonstrations from Part Three.
    """

    package_structure_demo()

    init_file_demo()

    package_module_import_demo()

    package_function_import_demo()

    package_alias_demo()

    multiple_package_modules_demo()

    network_package_demo()

    cybersecurity_package_demo()

    subpackage_demo()

    relative_import_demo()

    parent_package_import_demo()

    package_responsibilities_demo()

    good_package_design_demo()

    roadmap_package_demo()


# =============================================================================
# SECTION 42 - Standard Library
# =============================================================================

"""
Python Standard Library
=======================

Python comes with a large collection of built-in modules.

These modules provide functionality for:

- Operating system interaction
- File and directory management
- JSON processing
- Date and time
- System information
- Random operations
- Data structures
- Mathematics
- Logging
- Networking

No external installation is required.
"""


# =============================================================================
# SECTION 43 - os Module
# =============================================================================

import os


def os_module_demo() -> None:
    """
    Demonstrates basic functionality from the os module.
    """

    print("\nos Module")
    print("-" * 40)

    current_directory = os.getcwd()

    print(f"Current Directory: {current_directory}")

    print("\nEnvironment Information:")

    python_path = os.environ.get("PATH")

    if python_path:
        print("PATH variable is available.")
    else:
        print("PATH variable is not available.")


# =============================================================================
# SECTION 44 - sys Module
# =============================================================================

import sys


def sys_module_demo() -> None:
    """
    Demonstrates basic functionality from the sys module.
    """

    print("\nsys Module")
    print("-" * 40)

    print(f"Python Version: {sys.version.split()[0]}")
    print(f"Platform      : {sys.platform}")
    print(f"Executable    : {sys.executable}")


# =============================================================================
# SECTION 45 - pathlib Module
# =============================================================================

from pathlib import Path


def pathlib_module_demo() -> None:
    """
    Demonstrates modern path handling using pathlib.
    """

    print("\npathlib Module")
    print("-" * 40)

    current_path = Path.cwd()

    print(f"Current Path: {current_path}")

    print("\nPath Information:")

    print(f"Name      : {current_path.name}")
    print(f"Parent    : {current_path.parent}")
    print(f"Absolute  : {current_path.is_absolute()}")


# =============================================================================
# SECTION 46 - pathlib File Operations
# =============================================================================


def pathlib_file_demo() -> None:
    """
    Demonstrates basic file path operations.
    """

    print("\npathlib File Operations")
    print("-" * 40)

    file_path = Path("network_devices.txt")

    print(f"File Name: {file_path.name}")
    print(f"Suffix   : {file_path.suffix}")
    print(f"Exists   : {file_path.exists()}")


# =============================================================================
# SECTION 47 - json Module
# =============================================================================

import json


def json_module_demo() -> None:
    """
    Demonstrates converting Python data
    into JSON and back.
    """

    print("\njson Module")
    print("-" * 40)

    device = {
        "hostname": "R1",
        "ip_address": "192.168.1.1",
        "vendor": "Cisco",
        "status": "UP"
    }

    json_data = json.dumps(
        device,
        indent=4
    )

    print("Python Dictionary:")
    print(device)

    print("\nJSON Data:")
    print(json_data)


# =============================================================================
# SECTION 48 - JSON Deserialization
# =============================================================================


def json_deserialization_demo() -> None:
    """
    Demonstrates converting JSON data
    back into a Python object.
    """

    print("\nJSON Deserialization")
    print("-" * 40)

    json_data = """
    {
        "hostname": "SW1",
        "ip_address": "192.168.1.10",
        "status": "UP"
    }
    """

    device = json.loads(json_data)

    print(f"Hostname : {device['hostname']}")
    print(f"IP       : {device['ip_address']}")
    print(f"Status   : {device['status']}")


# =============================================================================
# SECTION 49 - datetime Module
# =============================================================================

from datetime import datetime, timedelta


def datetime_module_demo() -> None:
    """
    Demonstrates datetime functionality.
    """

    print("\ndatetime Module")
    print("-" * 40)

    current_time = datetime.now()

    print(f"Current Time: {current_time}")
    print(
        "Formatted Time: "
        f"{current_time:%Y-%m-%d %H:%M:%S}"
    )


# =============================================================================
# SECTION 50 - timedelta
# =============================================================================


def timedelta_demo() -> None:
    """
    Demonstrates date/time calculations.
    """

    print("\ntimedelta")
    print("-" * 40)

    current_time = datetime.now()

    future_time = current_time + timedelta(
        hours=2
    )

    print(f"Current Time: {current_time:%H:%M:%S}")
    print(f"After 2 Hours: {future_time:%H:%M:%S}")


# =============================================================================
# SECTION 51 - collections Module
# =============================================================================

from collections import Counter


def collections_counter_demo() -> None:
    """
    Demonstrates Counter from collections.
    """

    print("\ncollections.Counter")
    print("-" * 40)

    events: list[str] = [
        "login_failed",
        "port_scan",
        "login_failed",
        "malware",
        "login_failed",
        "port_scan"
    ]

    event_counter = Counter(events)

    print("Security Events:")

    for event, count in event_counter.items():
        print(f"{event:<15} -> {count}")


# =============================================================================
# SECTION 52 - defaultdict
# =============================================================================

from collections import defaultdict


def defaultdict_demo() -> None:
    """
    Demonstrates defaultdict.
    """

    print("\ndefaultdict")
    print("-" * 40)

    devices_by_vendor = defaultdict(list)

    devices = [
        ("Cisco", "R1"),
        ("Cisco", "R2"),
        ("MikroTik", "MT1"),
        ("Cisco", "SW1"),
        ("MikroTik", "MT2")
    ]

    for vendor, hostname in devices:
        devices_by_vendor[vendor].append(hostname)

    for vendor, hostnames in devices_by_vendor.items():
        print(
            f"{vendor:<10} -> "
            f"{hostnames}"
        )


# =============================================================================
# SECTION 53 - statistics Module
# =============================================================================

import statistics


def statistics_module_demo() -> None:
    """
    Demonstrates basic statistics.
    """

    print("\nstatistics Module")
    print("-" * 40)

    latency: list[float] = [
        10.5,
        20.2,
        15.8,
        30.1,
        25.4
    ]

    average = statistics.mean(latency)
    median = statistics.median(latency)

    print(f"Latency Values: {latency}")
    print(f"Average       : {average:.2f} ms")
    print(f"Median        : {median:.2f} ms")


# =============================================================================
# SECTION 54 - ipaddress Module
# =============================================================================

import ipaddress


def ipaddress_module_demo() -> None:
    """
    Demonstrates IP address validation.
    """

    print("\nipaddress Module")
    print("-" * 40)

    addresses: list[str] = [
        "192.168.1.1",
        "10.0.0.1",
        "8.8.8.8"
    ]

    for address in addresses:

        ip = ipaddress.ip_address(address)

        print(
            f"{address:<15} -> "
            f"Private: {ip.is_private}"
        )


# =============================================================================
# SECTION 55 - Network Calculation with ipaddress
# =============================================================================


def network_calculation_demo() -> None:
    """
    Demonstrates network calculations.
    """

    print("\nNetwork Calculation")
    print("-" * 40)

    network = ipaddress.ip_network(
        "192.168.10.0/24"
    )

    print(f"Network Address : {network.network_address}")
    print(f"Broadcast       : {network.broadcast_address}")
    print(f"Prefix Length   : {network.prefixlen}")
    print(f"Number of Hosts : {network.num_addresses}")


# =============================================================================
# SECTION 56 - Practical Network Inventory
# =============================================================================


def network_inventory_demo() -> None:
    """
    Demonstrates combining standard library
    modules for network inventory processing.
    """

    print("\nNetwork Inventory")
    print("-" * 40)

    devices = [
        {
            "hostname": "R1",
            "ip": "192.168.1.1",
            "vendor": "Cisco"
        },
        {
            "hostname": "R2",
            "ip": "192.168.1.2",
            "vendor": "Cisco"
        },
        {
            "hostname": "SW1",
            "ip": "192.168.1.10",
            "vendor": "Cisco"
        }
    ]

    print(
        json.dumps(
            devices,
            indent=4
        )
    )


# =============================================================================
# SECTION 57 - Practical Cybersecurity Example
# =============================================================================


def security_event_timestamp_demo() -> None:
    """
    Demonstrates adding timestamps
    to security events.
    """

    print("\nSecurity Event Timestamp")
    print("-" * 40)

    event = {
        "type": "Failed Login",
        "source_ip": "192.168.1.50",
        "severity": "HIGH",
        "timestamp": datetime.now().isoformat()
    }

    print(
        json.dumps(
            event,
            indent=4
        )
    )


# =============================================================================
# SECTION 58 - Standard Library Summary
# =============================================================================


def standard_library_summary() -> None:
    """
    Summarizes the standard library modules
    covered in this part.
    """

    print("\nStandard Library Summary")
    print("-" * 40)

    modules: dict[str, str] = {
        "os": "Operating system interaction",
        "sys": "Python runtime and system information",
        "pathlib": "File and path management",
        "json": "JSON data processing",
        "datetime": "Date and time operations",
        "collections": "Specialized data structures",
        "statistics": "Statistical calculations",
        "ipaddress": "IP address and network operations"
    }

    for module, purpose in modules.items():
        print(f"{module:<12} -> {purpose}")


# =============================================================================
# SECTION 59 - Part Four Runner
# =============================================================================


def run_part_four() -> None:
    """
    Runs all demonstrations from Part Four.
    """

    os_module_demo()

    sys_module_demo()

    pathlib_module_demo()

    pathlib_file_demo()

    json_module_demo()

    json_deserialization_demo()

    datetime_module_demo()

    timedelta_demo()

    collections_counter_demo()

    defaultdict_demo()

    statistics_module_demo()

    ipaddress_module_demo()

    network_calculation_demo()

    network_inventory_demo()

    security_event_timestamp_demo()

    standard_library_summary()


# =============================================================================
# SECTION 60 - Mini Project Overview
# =============================================================================

"""
===============================================================================
MINI PROJECT
===============================================================================

Project Name:
    Network Toolkit

Purpose:
    Demonstrate how Modules, Packages, and the Python Standard Library
    can be combined to build a small reusable network-oriented toolkit.

Concepts Used:
    - Functions
    - Modules
    - Packages
    - JSON
    - pathlib
    - datetime
    - collections
    - ipaddress
    - Type Hints
    - Dictionaries
    - Lists

Project Architecture:

    network_toolkit/
    |
    +-- devices.py
    +-- inventory.py
    +-- utilities.py
    +-- reports.py
    +-- main.py

In this lesson everything is demonstrated inside one file.
Later, the same logic will be separated into real modules.
"""


# =============================================================================
# SECTION 61 - Mini Project Device Data
# =============================================================================


def toolkit_get_devices() -> list[dict[str, object]]:
    """
    Returns sample network device inventory.
    """

    devices: list[dict[str, object]] = [
        {
            "hostname": "R1",
            "ip_address": "192.168.10.1",
            "vendor": "Cisco",
            "device_type": "Router",
            "status": "UP"
        },
        {
            "hostname": "R2",
            "ip_address": "192.168.10.2",
            "vendor": "Cisco",
            "device_type": "Router",
            "status": "UP"
        },
        {
            "hostname": "SW1",
            "ip_address": "192.168.10.10",
            "vendor": "Cisco",
            "device_type": "Switch",
            "status": "UP"
        },
        {
            "hostname": "MT1",
            "ip_address": "192.168.10.20",
            "vendor": "MikroTik",
            "device_type": "Router",
            "status": "DOWN"
        }
    ]

    return devices


# =============================================================================
# SECTION 62 - Device Validation
# =============================================================================


def toolkit_validate_ip(ip_address: str) -> bool:
    """
    Validates an IPv4 or IPv6 address.
    """

    try:
        ipaddress.ip_address(ip_address)

    except ValueError:
        return False

    return True


def toolkit_validate_devices(
    devices: list[dict[str, object]]
) -> list[dict[str, object]]:
    """
    Returns only devices with valid IP addresses.
    """

    valid_devices: list[dict[str, object]] = []

    for device in devices:

        ip_address = device.get("ip_address")

        if not isinstance(ip_address, str):
            continue

        if toolkit_validate_ip(ip_address):
            valid_devices.append(device)

    return valid_devices


# =============================================================================
# SECTION 63 - Device Filtering
# =============================================================================


def toolkit_get_active_devices(
    devices: list[dict[str, object]]
) -> list[dict[str, object]]:
    """
    Returns devices whose status is UP.
    """

    active_devices: list[dict[str, object]] = []

    for device in devices:

        if device.get("status") == "UP":
            active_devices.append(device)

    return active_devices


# =============================================================================
# SECTION 64 - Vendor Statistics
# =============================================================================


def toolkit_vendor_statistics(
    devices: list[dict[str, object]]
) -> dict[str, int]:
    """
    Counts devices by vendor.
    """

    vendors = Counter()

    for device in devices:

        vendor = device.get("vendor")

        if isinstance(vendor, str):
            vendors[vendor] += 1

    return dict(vendors)


# =============================================================================
# SECTION 65 - Device Type Statistics
# =============================================================================


def toolkit_device_type_statistics(
    devices: list[dict[str, object]]
) -> dict[str, int]:
    """
    Counts devices by device type.
    """

    device_types = Counter()

    for device in devices:

        device_type = device.get("device_type")

        if isinstance(device_type, str):
            device_types[device_type] += 1

    return dict(device_types)


# =============================================================================
# SECTION 66 - Network Address Information
# =============================================================================


def toolkit_network_information(
    network: str
) -> dict[str, object]:
    """
    Returns information about an IP network.
    """

    ip_network = ipaddress.ip_network(
        network,
        strict=False
    )

    return {
        "network": str(ip_network.network_address),
        "broadcast": str(ip_network.broadcast_address),
        "prefix": ip_network.prefixlen,
        "total_addresses": ip_network.num_addresses
    }


# =============================================================================
# SECTION 67 - Inventory Report
# =============================================================================


def toolkit_generate_report(
    devices: list[dict[str, object]]
) -> dict[str, object]:
    """
    Generates a network inventory report.
    """

    valid_devices = toolkit_validate_devices(
        devices
    )

    active_devices = toolkit_get_active_devices(
        valid_devices
    )

    vendor_statistics = toolkit_vendor_statistics(
        valid_devices
    )

    device_type_statistics = (
        toolkit_device_type_statistics(
            valid_devices
        )
    )

    report: dict[str, object] = {
        "generated_at": datetime.now().isoformat(),
        "total_devices": len(valid_devices),
        "active_devices": len(active_devices),
        "vendors": vendor_statistics,
        "device_types": device_type_statistics,
        "devices": valid_devices
    }

    return report


# =============================================================================
# SECTION 68 - JSON Report
# =============================================================================


def toolkit_print_json_report(
    report: dict[str, object]
) -> None:
    """
    Prints the inventory report as formatted JSON.
    """

    print("\nJSON Inventory Report")
    print("-" * 40)

    print(
        json.dumps(
            report,
            indent=4
        )
    )


# =============================================================================
# SECTION 69 - Network Report
# =============================================================================


def toolkit_print_network_report() -> None:
    """
    Prints network information.
    """

    print("\nNetwork Information")
    print("-" * 40)

    network = toolkit_network_information(
        "192.168.10.0/24"
    )

    print(
        f"Network Address : "
        f"{network['network']}"
    )

    print(
        f"Broadcast       : "
        f"{network['broadcast']}"
    )

    print(
        f"Prefix Length   : "
        f"/{network['prefix']}"
    )

    print(
        f"Total Addresses : "
        f"{network['total_addresses']}"
    )


# =============================================================================
# SECTION 70 - Save Report to File
# =============================================================================


def toolkit_save_report(
    report: dict[str, object],
    filename: str = "network_inventory_report.json"
) -> Path:
    """
    Saves a JSON report to a file.

    Returns:
        Path: Path of the generated file.
    """

    output_path = Path(filename)

    output_path.write_text(
        json.dumps(
            report,
            indent=4
        ),
        encoding="utf-8"
    )

    return output_path


# =============================================================================
# SECTION 71 - File Report Demo
# =============================================================================


def toolkit_file_report_demo(
    report: dict[str, object]
) -> None:
    """
    Demonstrates saving the report to disk.
    """

    print("\nFile Report")
    print("-" * 40)

    output_path = toolkit_save_report(
        report
    )

    print(
        f"Report saved to: "
        f"{output_path.resolve()}"
    )

    print(
        f"File exists: "
        f"{output_path.exists()}"
    )


# =============================================================================
# SECTION 72 - Toolkit Summary
# =============================================================================


def toolkit_summary(
    report: dict[str, object]
) -> None:
    """
    Displays a short summary of the toolkit report.
    """

    print("\nNetwork Toolkit Summary")
    print("-" * 40)

    print(
        f"Total Devices : "
        f"{report['total_devices']}"
    )

    print(
        f"Active Devices: "
        f"{report['active_devices']}"
    )

    print(
        f"Vendors       : "
        f"{report['vendors']}"
    )

    print(
        f"Device Types  : "
        f"{report['device_types']}"
    )


# =============================================================================
# SECTION 73 - Module Mapping
# =============================================================================


def toolkit_module_mapping_demo() -> None:
    """
    Shows how the current mini project could be
    divided into real modules.
    """

    print("\nModule Mapping")
    print("-" * 40)

    mapping: dict[str, str] = {
        "devices.py":
            "Device information and validation",

        "inventory.py":
            "Inventory processing and statistics",

        "utilities.py":
            "IP and general helper functions",

        "reports.py":
            "JSON and file reports",

        "main.py":
            "Application entry point"
    }

    for module, responsibility in mapping.items():

        print(
            f"{module:<18} -> "
            f"{responsibility}"
        )


# =============================================================================
# SECTION 74 - Final Project Structure
# =============================================================================


def toolkit_final_structure_demo() -> None:
    """
    Displays the final project structure.
    """

    print("\nFinal Project Structure")
    print("-" * 40)

    structure: list[str] = [
        "network_toolkit/",
        "│",
        "├── __init__.py",
        "│",
        "├── devices.py",
        "├── inventory.py",
        "├── utilities.py",
        "├── reports.py",
        "│",
        "└── main.py"
    ]

    for line in structure:
        print(line)


# =============================================================================
# SECTION 75 - Part Five Runner
# =============================================================================


def run_part_five() -> None:
    """
    Runs the complete Network Toolkit mini project.
    """

    print("\n" + "=" * 70)
    print("PART 5 - NETWORK TOOLKIT MINI PROJECT")
    print("=" * 70)

    devices = toolkit_get_devices()

    valid_devices = toolkit_validate_devices(
        devices
    )

    report = toolkit_generate_report(
        valid_devices
    )

    toolkit_summary(
        report
    )

    toolkit_print_json_report(
        report
    )

    toolkit_print_network_report()

    toolkit_file_report_demo(
        report
    )

    toolkit_module_mapping_demo()

    toolkit_final_structure_demo()


# =============================================================================
# SECTION 76 - Lesson Summary
# =============================================================================


def modules_packages_lesson_summary() -> None:
    """
    Displays the complete lesson summary.
    """

    print("\n" + "=" * 70)
    print("LESSON 17 SUMMARY")
    print("=" * 70)

    topics: list[str] = [
        "Modules",
        "import",
        "from ... import",
        "Import Aliases",
        "__name__",
        "__main__",
        "if __name__ == '__main__'",
        "Packages",
        "__init__.py",
        "Subpackages",
        "Relative Imports",
        "Python Standard Library",
        "os",
        "sys",
        "pathlib",
        "json",
        "datetime",
        "collections",
        "statistics",
        "ipaddress",
        "Network Toolkit Mini Project"
    ]

    for number, topic in enumerate(
        topics,
        start=1
    ):
        print(
            f"{number:02d}. {topic}"
        )


# =============================================================================
# SECTION 77 - Key Takeaways
# =============================================================================


def modules_packages_key_takeaways() -> None:
    """
    Displays the most important lessons.
    """

    print("\nKey Takeaways")
    print("-" * 40)

    takeaways: list[str] = [
        "A module is a Python file containing reusable code.",
        "A package organizes related modules.",
        "__name__ identifies the current module.",
        "__main__ identifies direct execution.",
        "The main guard prevents unwanted execution during import.",
        "The Standard Library provides many ready-to-use modules.",
        "pathlib is useful for modern file and path handling.",
        "json is widely used for structured data exchange.",
        "ipaddress is useful for network automation.",
        "Large projects should separate responsibilities."
    ]

    for takeaway in takeaways:
        print(f"✔ {takeaway}")


# =============================================================================
# SECTION 78 - Next Lesson
# =============================================================================

"""
Next Lesson
-----------

18_file_handling.py

Topics:

✔ Reading Files
✔ Writing Files
✔ Appending Files
✔ with open()
✔ File Modes
✔ Encoding
✔ pathlib
✔ CSV
✔ JSON Files
✔ Working with Logs
✔ Practical Network Configuration Files
"""


# =============================================================================
# SECTION 79 - Main Function
# =============================================================================


def main() -> None:
    """
    Runs the complete Lesson 17.
    """

    print("\n" + "=" * 70)
    print("LESSON 17 - MODULES & PACKAGES")
    print("=" * 70)

    # -------------------------------------------------------------------------
    # Part 1
    # -------------------------------------------------------------------------

    run_part_one()

    # -------------------------------------------------------------------------
    # Part 2
    # -------------------------------------------------------------------------

    run_part_two()

    # -------------------------------------------------------------------------
    # Part 3
    # -------------------------------------------------------------------------

    run_part_three()

    # -------------------------------------------------------------------------
    # Part 4
    # -------------------------------------------------------------------------

    run_part_four()

    # -------------------------------------------------------------------------
    # Part 5
    # -------------------------------------------------------------------------

    run_part_five()

    # -------------------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------------------

    modules_packages_lesson_summary()

    modules_packages_key_takeaways()


# =============================================================================
# PROGRAM ENTRY POINT
# =============================================================================


if __name__ == "__main__":
    main()
