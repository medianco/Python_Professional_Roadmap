"""
===============================================================================
File        : 07_lists.py
Author      : Mohammed AL-Dubai
Course      : Python Professional Roadmap
Lesson      : Lists

Description:
    This lesson explains Python lists, list indexing, slicing,
    modifying elements, nested lists, and common list operations.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Create Python lists.
✔ Access list elements using indexing.
✔ Use negative indexing.
✔ Slice lists.
✔ Modify list elements.
✔ Work with nested lists.
✔ Determine list length.
✔ Apply lists in networking and cybersecurity.

===============================================================================
"""

# =============================================================================
# SECTION 1 - Introduction to Lists
# =============================================================================

"""
A list is an ordered and mutable collection.

Characteristics:

✔ Ordered
✔ Mutable
✔ Allows duplicate values
✔ Can store different data types

Examples:

["Router", "Switch", "Firewall"]

[10, 20, 30]

["Python", 2026, True]
"""


def introduction_demo() -> None:
    """
    Demonstrates the concept of Python lists.
    """

    print("\nIntroduction to Lists")
    print("-" * 40)

    devices: list[str] = [
        "Router",
        "Switch",
        "Firewall"
    ]

    print("Devices:", devices)
    print("Type   :", type(devices))


# =============================================================================
# SECTION 2 - Creating Lists
# =============================================================================


def creating_lists_demo() -> None:
    """
    Demonstrates different ways to create lists.
    """

    print("\nCreating Lists")
    print("-" * 40)

    numbers: list[int] = [
        10,
        20,
        30
    ]

    protocols: list[str] = [
        "HTTP",
        "HTTPS",
        "SSH",
        "DNS"
    ]

    mixed_data: list = [
        "Cisco",
        443,
        True,
        3.14
    ]

    print("Numbers :", numbers)
    print("Protocols:", protocols)
    print("Mixed    :", mixed_data)


# =============================================================================
# SECTION 3 - List Indexing
# =============================================================================


def indexing_demo() -> None:
    """
    Demonstrates positive indexing.
    """

    print("\nList Indexing")
    print("-" * 40)

    devices: list[str] = [
        "Router",
        "Switch",
        "Firewall",
        "Access Point"
    ]

    print("First Device :", devices[0])
    print("Second Device:", devices[1])
    print("Last Device  :", devices[3])


# =============================================================================
# SECTION 4 - Negative Indexing
# =============================================================================


def negative_indexing_demo() -> None:
    """
    Demonstrates negative indexing.
    """

    print("\nNegative Indexing")
    print("-" * 40)

    devices: list[str] = [
        "Router",
        "Switch",
        "Firewall",
        "Access Point"
    ]

    print("Last Device      :", devices[-1])
    print("Second Last      :", devices[-2])
    print("Third Last       :", devices[-3])


# =============================================================================
# SECTION 5 - List Slicing
# =============================================================================


def slicing_demo() -> None:
    """
    Demonstrates list slicing.
    """

    print("\nList Slicing")
    print("-" * 40)

    numbers: list[int] = [
        10,
        20,
        30,
        40,
        50,
        60
    ]

    print("numbers[1:4] :", numbers[1:4])
    print("numbers[:3]  :", numbers[:3])
    print("numbers[3:]  :", numbers[3:])
    print("numbers[::2] :", numbers[::2])
    print("numbers[::-1]:", numbers[::-1])


# =============================================================================
# SECTION 6 - Modifying List Elements
# =============================================================================


def modify_elements_demo() -> None:
    """
    Demonstrates modifying list elements.
    """

    print("\nModifying List Elements")
    print("-" * 40)

    devices: list[str] = [
        "Router",
        "Switch",
        "Firewall"
    ]

    print("Before:", devices)

    devices[1] = "Layer 3 Switch"

    print("After :", devices)


# =============================================================================
# SECTION 7 - List Length
# =============================================================================


def list_length_demo() -> None:
    """
    Demonstrates len().
    """

    print("\nList Length")
    print("-" * 40)

    services: list[str] = [
        "SSH",
        "HTTP",
        "HTTPS",
        "DNS",
        "NTP"
    ]

    print("Services:", services)
    print("Length  :", len(services))


# =============================================================================
# SECTION 8 - Nested Lists
# =============================================================================


def nested_lists_demo() -> None:
    """
    Demonstrates nested lists.
    """

    print("\nNested Lists")
    print("-" * 40)

    network_inventory: list = [
        [
            "R1",
            "Cisco"
        ],
        [
            "SW1",
            "Cisco"
        ],
        [
            "FW1",
            "Fortinet"
        ]
    ]

    print("Inventory:", network_inventory)

    print("First Device :", network_inventory[0][0])
    print("First Vendor :", network_inventory[0][1])
    print("Third Device :", network_inventory[2][0])


# =============================================================================
# END OF PART 1
# =============================================================================

# =============================================================================
# SECTION 9 - append()
# =============================================================================


def append_demo() -> None:
    """
    Demonstrates append() method.

    append() adds one item to the end of a list.
    """

    print("\nappend() Method")
    print("-" * 40)

    devices: list[str] = [
        "Router",
        "Switch"
    ]

    print("Before:", devices)

    devices.append("Firewall")

    print("After :", devices)


# =============================================================================
# SECTION 10 - extend()
# =============================================================================


def extend_demo() -> None:
    """
    Demonstrates extend() method.

    extend() adds multiple items from another iterable.
    """

    print("\nextend() Method")
    print("-" * 40)

    protocols: list[str] = [
        "HTTP",
        "HTTPS"
    ]

    new_protocols: list[str] = [
        "SSH",
        "DNS",
        "NTP"
    ]

    protocols.extend(new_protocols)

    print(protocols)


# =============================================================================
# SECTION 11 - insert()
# =============================================================================


def insert_demo() -> None:
    """
    Demonstrates insert() method.

    insert() adds an item at a specific position.
    """

    print("\ninsert() Method")
    print("-" * 40)

    interfaces: list[str] = [
        "Gi0/0",
        "Gi0/2"
    ]

    interfaces.insert(1, "Gi0/1")

    print(interfaces)


# =============================================================================
# SECTION 12 - remove()
# =============================================================================


def remove_demo() -> None:
    """
    Demonstrates remove() method.

    remove() deletes the first matching item.
    """

    print("\nremove() Method")
    print("-" * 40)

    services: list[str] = [
        "SSH",
        "HTTP",
        "HTTPS",
        "FTP"
    ]

    services.remove("FTP")

    print(services)


# =============================================================================
# SECTION 13 - pop()
# =============================================================================


def pop_demo() -> None:
    """
    Demonstrates pop() method.

    pop() removes and returns an item.
    """

    print("\npop() Method")
    print("-" * 40)

    ports: list[int] = [
        22,
        80,
        443
    ]

    removed_port: int = ports.pop()

    print("Removed:", removed_port)
    print("Remaining:", ports)


# =============================================================================
# SECTION 14 - clear()
# =============================================================================


def clear_demo() -> None:
    """
    Demonstrates clear() method.

    clear() removes all elements.
    """

    print("\nclear() Method")
    print("-" * 40)

    logs: list[str] = [
        "INFO",
        "ERROR",
        "WARNING"
    ]

    print("Before:", logs)

    logs.clear()

    print("After :", logs)


# =============================================================================
# SECTION 15 - copy()
# =============================================================================


def copy_demo() -> None:
    """
    Demonstrates copy() method.

    Creates a shallow copy of a list.
    """

    print("\ncopy() Method")
    print("-" * 40)

    original_devices: list[str] = [
        "Router",
        "Switch"
    ]

    copied_devices: list[str] = original_devices.copy()

    copied_devices.append("Firewall")

    print("Original:", original_devices)
    print("Copy    :", copied_devices)


# =============================================================================
# SECTION 16 - count()
# =============================================================================


def count_demo() -> None:
    """
    Demonstrates count() method.
    """

    print("\ncount() Method")
    print("-" * 40)

    alerts: list[str] = [
        "ERROR",
        "INFO",
        "ERROR",
        "WARNING",
        "ERROR"
    ]

    print(
        "ERROR Count:",
        alerts.count("ERROR")
    )


# =============================================================================
# SECTION 17 - index()
# =============================================================================


def index_demo() -> None:
    """
    Demonstrates index() method.

    Returns the first matching position.
    """

    print("\nindex() Method")
    print("-" * 40)

    devices: list[str] = [
        "Router",
        "Switch",
        "Firewall"
    ]

    print(
        "Switch Position:",
        devices.index("Switch")
    )


# =============================================================================
# SECTION 18 - reverse()
# =============================================================================


def reverse_demo() -> None:
    """
    Demonstrates reverse() method.
    """

    print("\nreverse() Method")
    print("-" * 40)

    commands: list[str] = [
        "show",
        "ip",
        "interface"
    ]

    commands.reverse()

    print(commands)


# =============================================================================
# SECTION 19 - sort()
# =============================================================================


def sort_demo() -> None:
    """
    Demonstrates sort() method.
    """

    print("\nsort() Method")
    print("-" * 40)

    ports: list[int] = [
        443,
        22,
        80,
        53
    ]

    ports.sort()

    print("Ascending:", ports)

    ports.sort(reverse=True)

    print("Descending:", ports)


# =============================================================================
# SECTION 20 - sorted()
# =============================================================================


def sorted_demo() -> None:
    """
    Demonstrates sorted() function.

    sorted() returns a new sorted list.
    """

    print("\nsorted() Function")
    print("-" * 40)

    vlans: list[int] = [
        30,
        10,
        20
    ]

    sorted_vlans = sorted(vlans)

    print("Original:", vlans)
    print("Sorted  :", sorted_vlans)


# =============================================================================
# SECTION 21 - Network Engineering Example
# =============================================================================


def network_list_methods_demo() -> None:
    """
    Demonstrates list methods in network engineering.
    """

    print("\nNetwork Engineering Example")
    print("-" * 40)

    interfaces: list[str] = [
        "Gi0/0",
        "Gi0/1"
    ]

    interfaces.append("Gi0/2")

    interfaces.sort()

    print("Interfaces:")
    
    for interface in interfaces:
        print(interface)


# =============================================================================
# SECTION 22 - Cybersecurity Example
# =============================================================================


def cybersecurity_list_methods_demo() -> None:
    """
    Demonstrates list methods in cybersecurity.
    """

    print("\nCybersecurity Example")
    print("-" * 40)

    suspicious_ips: list[str] = [
        "10.0.0.5",
        "192.168.1.50",
        "10.0.0.5"
    ]

    print(
        "Occurrences:",
        suspicious_ips.count("10.0.0.5")
    )

    suspicious_ips.remove("192.168.1.50")

    print(
        "Updated List:",
        suspicious_ips
    )


# =============================================================================
# END OF PART 2
# =============================================================================

# =============================================================================
# SECTION 23 - Iterating Through Lists
# =============================================================================


def list_iteration_demo() -> None:
    """
    Demonstrates iterating through lists using for loop.
    """

    print("\nList Iteration")
    print("-" * 40)

    devices: list[str] = [
        "Router",
        "Switch",
        "Firewall"
    ]

    for device in devices:
        print(device)


# =============================================================================
# SECTION 24 - enumerate()
# =============================================================================


def enumerate_demo() -> None:
    """
    Demonstrates enumerate() function.

    enumerate() returns index and value.
    """

    print("\nenumerate() Function")
    print("-" * 40)

    interfaces: list[str] = [
        "Gi0/0",
        "Gi0/1",
        "Gi0/2"
    ]

    for index, interface in enumerate(interfaces):

        print(
            f"{index}: {interface}"
        )


# =============================================================================
# SECTION 25 - zip()
# =============================================================================


def zip_demo() -> None:
    """
    Demonstrates zip() function.

    zip() combines multiple lists.
    """

    print("\nzip() Function")
    print("-" * 40)

    devices: list[str] = [
        "R1",
        "SW1",
        "FW1"
    ]

    ip_addresses: list[str] = [
        "10.0.0.1",
        "10.0.0.2",
        "10.0.0.3"
    ]

    for device, ip in zip(devices, ip_addresses):

        print(
            f"{device} --> {ip}"
        )


# =============================================================================
# SECTION 26 - List Comprehension
# =============================================================================


def list_comprehension_demo() -> None:
    """
    Demonstrates list comprehension.
    """

    print("\nList Comprehension")
    print("-" * 40)

    numbers: list[int] = [
        1,
        2,
        3,
        4,
        5
    ]

    squared_numbers: list[int] = [
        number ** 2
        for number in numbers
    ]

    print(
        "Original:",
        numbers
    )

    print(
        "Squared:",
        squared_numbers
    )


# =============================================================================
# SECTION 27 - Filtering Lists
# =============================================================================


def filtering_lists_demo() -> None:
    """
    Demonstrates filtering list elements.
    """

    print("\nFiltering Lists")
    print("-" * 40)

    ports: list[int] = [
        21,
        22,
        80,
        443,
        3389
    ]

    secure_ports: list[int] = [
        port
        for port in ports
        if port in [22, 443]
    ]

    print(
        "Secure Ports:",
        secure_ports
    )


# =============================================================================
# SECTION 28 - Network Device Inventory
# =============================================================================


def network_inventory_demo() -> None:
    """
    Demonstrates managing network devices
    using lists.
    """

    print("\nNetwork Device Inventory")
    print("-" * 40)

    devices: list[str] = [
        "Core-Router",
        "Access-Switch",
        "Firewall"
    ]

    devices.append("Wireless-Controller")

    print("Inventory:")

    for device in devices:

        print(
            f"- {device}"
        )


# =============================================================================
# SECTION 29 - Interface Status Processing
# =============================================================================


def interface_status_demo() -> None:
    """
    Demonstrates processing interface data.
    """

    print("\nInterface Status Processing")
    print("-" * 40)

    interfaces: list[str] = [
        "Gi0/0 UP",
        "Gi0/1 DOWN",
        "Gi0/2 UP"
    ]

    active_interfaces: list[str] = [
        interface
        for interface in interfaces
        if "UP" in interface
    ]

    print(
        "Active Interfaces:"
    )

    for interface in active_interfaces:

        print(interface)


# =============================================================================
# SECTION 30 - Cybersecurity IOC Processing
# =============================================================================


def ioc_processing_demo() -> None:
    """
    Demonstrates processing Indicators of Compromise (IOC).
    """

    print("\nIOC Processing")
    print("-" * 40)

    indicators: list[str] = [
        "malicious.com",
        "192.168.1.50",
        "badfile.exe",
        "normal-domain.com"
    ]

    suspicious_items: list[str] = [
        indicator
        for indicator in indicators
        if "malicious" in indicator
        or "bad" in indicator
    ]

    print(
        "Suspicious Indicators:"
    )

    for item in suspicious_items:

        print(item)


# =============================================================================
# SECTION 31 - Log Event Analysis
# =============================================================================


def log_event_analysis_demo() -> None:
    """
    Demonstrates analyzing security events.
    """

    print("\nLog Event Analysis")
    print("-" * 40)

    events: list[str] = [
        "INFO Login successful",
        "ERROR Authentication failed",
        "WARNING Password expired",
        "ERROR Unauthorized access"
    ]

    error_events: list[str] = [
        event
        for event in events
        if event.startswith("ERROR")
    ]

    print(
        "Error Events:"
    )

    for event in error_events:

        print(event)


# =============================================================================
# END OF PART 3
# =============================================================================

# =============================================================================
# SECTION 32 - Professional Tips
# =============================================================================


def professional_tips_demo() -> None:
    """
    Demonstrates professional tips when working with lists.
    """

    print("\nProfessional Tips")
    print("-" * 40)

    """
    Professional Tips:

    ✔ Use list comprehension for simple transformations.

    ✔ Use enumerate() when index is required.

    ✔ Use zip() when processing related lists.

    ✔ Use copy() when you need an independent list.

    ✔ Prefer meaningful list names.

    ✔ Use lists for ordered collections.

    ✔ Avoid modifying lists while iterating over them.
    """

    print("Apply clean list practices in real projects.")


# =============================================================================
# SECTION 33 - Best Practices
# =============================================================================


def best_practices_demo() -> None:
    """
    Demonstrates recommended list practices.
    """

    print("\nList Best Practices")
    print("-" * 40)

    """
    Best Practices:

    ✔ Keep lists focused on one data type when possible.

    ✔ Use clear variable names.

    ✔ Check if an item exists before removing it.

    ✔ Use sorted() when the original list
      should remain unchanged.

    ✔ Validate external data before adding it.

    ✔ Avoid unnecessary list copying.
    """

    print("Write readable and maintainable list code.")


# =============================================================================
# SECTION 34 - Common Mistakes
# =============================================================================


def common_mistakes_demo() -> None:
    """
    Explains common mistakes with lists.
    """

    print("\nCommon List Mistakes")
    print("-" * 40)

    """
    Mistake 1:

    Accessing an index that does not exist.


    Mistake 2:

    Removing an item that is not available.


    Mistake 3:

    Modifying a list while looping through it.


    Mistake 4:

    Confusing copy() with assignment.


    Mistake 5:

    Using sort() when the original order
    is needed.
    """

    print("Review comments for common mistakes.")


# =============================================================================
# SECTION 35 - Performance Tips
# =============================================================================


def performance_tips_demo() -> None:
    """
    Demonstrates performance recommendations.
    """

    print("\nList Performance Tips")
    print("-" * 40)

    """
    Performance Tips:

    ✔ Use append() instead of creating new lists repeatedly.

    ✔ Use list comprehension for efficient filtering.

    ✔ Avoid searching large lists repeatedly.

    ✔ Use sets for frequent membership checks.

    ✔ Avoid unnecessary nested loops.
    """

    print("Choose the correct data structure for the task.")


# =============================================================================
# SECTION 36 - List Cheat Sheet
# =============================================================================


"""
List Cheat Sheet
================


Creation:

items = []


Access:

list[index]


Slicing:

list[start:end]


Add:

append()
extend()
insert()


Remove:

remove()
pop()
clear()


Search:

index()
count()


Ordering:

sort()
sorted()
reverse()


Copy:

copy()


Processing:

enumerate()
zip()

Comprehension:

[item for item in list] 

Method          Description
------------------------------------------
append()        Add one item
extend()        Add multiple items
insert()        Insert at position
remove()        Remove first occurrence
pop()           Remove by index
clear()         Remove all items
sort()          Sort list
reverse()       Reverse list
copy()          Copy list
count()         Count occurrences
index()         Return item index
"""


# =============================================================================
# SECTION 37 - Interview Questions
# =============================================================================


"""
Interview Questions
-------------------

1. What is a Python list?

2. What is the difference between
   list and tuple?

3. Are lists mutable or immutable?

4. What is the difference between:

   append()

   and

   extend()


5. What is list comprehension?

6. What is the difference between:

   sort()

   and

   sorted()?


7. What does enumerate() do?

8. Why do we use zip()?

9. How can lists be used in network automation?

10. How can lists help in log analysis?
"""


# =============================================================================
# SECTION 38 - Coding Exercises
# =============================================================================


"""
Coding Exercises
----------------


Exercise 1:

Create a list of network devices.

Add:

Router
Switch
Firewall


Exercise 2:

Remove an offline device
from an inventory list.


Exercise 3:

Find the number of failed
login attempts in a log list.


Exercise 4:

Create a list of open ports
and filter secure ports.


Exercise 5:

Use zip() to combine:

Device Names

and

IP Addresses.
"""


# =============================================================================
# SECTION 39 - Mini Project
# =============================================================================


def mini_project_description() -> None:
    """
    Mini Project:

    Network Device Inventory Manager


    Scenario:

    A network engineer needs
    a simple Python tool to manage
    network devices.


    Requirements:

    Store:

    - Device Name
    - IP Address
    - Vendor
    - Device Type


    Functions:

    1. Add a new device.

    2. Remove a device.

    3. Search for a device.

    4. Display inventory.

    5. Sort devices.


    Example Output:

    Network Inventory
    -----------------

    R1
    10.0.0.1
    Cisco
    Router


    Skills Practiced:

    ✔ Lists

    ✔ List Methods

    ✔ Loops

    ✔ Conditions

    ✔ Data Processing
    """

    print("\nMini Project: Network Device Inventory Manager")
    print("See project requirements above.")


# =============================================================================
# SECTION 40 - What's Next?
# =============================================================================


"""
What's Next?

Next Lesson:

08_tuples.py


Topics:

✔ Tuple Creation

✔ Tuple Indexing

✔ Tuple Slicing

✔ Tuple Methods

✔ Tuple Packing

✔ Tuple Unpacking

✔ Network Engineering Examples

✔ Cybersecurity Examples
"""


# =============================================================================
# SECTION 41 - Main Function
# =============================================================================


def main() -> None:
    """
    Main function that runs all demonstrations.
    """

    # Part One
    introduction_demo()
    creating_lists_demo()
    indexing_demo()
    negative_indexing_demo()
    slicing_demo()
    modify_elements_demo()
    list_length_demo()
    nested_lists_demo()

    # Part Two
    append_demo()
    extend_demo()
    insert_demo()
    remove_demo()
    pop_demo()
    clear_demo()
    copy_demo()
    count_demo()
    index_demo()
    reverse_demo()
    sort_demo()
    sorted_demo()
    network_list_methods_demo()
    cybersecurity_list_methods_demo()

    # Part Three
    list_iteration_demo()
    enumerate_demo()
    zip_demo()
    list_comprehension_demo()
    filtering_lists_demo()
    network_inventory_demo()
    interface_status_demo()
    ioc_processing_demo()
    log_event_analysis_demo()

    # Part Four
    professional_tips_demo()
    best_practices_demo()
    common_mistakes_demo()
    performance_tips_demo()
    mini_project_description()


if __name__ == "__main__":
    main()

