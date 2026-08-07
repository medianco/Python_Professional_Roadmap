"""
===============================================================================
File        : 08_tuples.py
Author      : Mohammed AL-Dubai
Course      : Python Basics
Lesson      : Tuples

Description:
    This lesson explains Python tuples, indexing, slicing,
    immutability, nested tuples, and practical usage.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Understand tuples.
✔ Create tuple objects.
✔ Access tuple elements.
✔ Use tuple slicing.
✔ Understand immutability.
✔ Work with nested tuples.
✔ Apply tuples in networking and cybersecurity.

===============================================================================
"""


# =============================================================================
# SECTION 1 - Introduction to Tuples
# =============================================================================


"""
A tuple is an ordered and immutable collection.

Characteristics:

✔ Ordered
✔ Immutable
✔ Allows duplicate values
✔ Faster than lists in some cases
✔ Can store different data types


Difference:

List:

[]
Mutable


Tuple:

()
Immutable
"""


def introduction_demo() -> None:
    """
    Demonstrates the concept of tuples.
    """

    print("\nIntroduction to Tuples")
    print("-" * 40)

    protocols: tuple[str, ...] = (
        "HTTP",
        "HTTPS",
        "SSH"
    )

    print("Protocols:", protocols)
    print("Type     :", type(protocols))


# =============================================================================
# SECTION 2 - Creating Tuples
# =============================================================================


def creating_tuples_demo() -> None:
    """
    Demonstrates different ways to create tuples.
    """

    print("\nCreating Tuples")
    print("-" * 40)

    numbers: tuple[int, ...] = (
        10,
        20,
        30
    )

    devices: tuple[str, ...] = (
        "Router",
        "Switch",
        "Firewall"
    )

    mixed_data: tuple = (
        "Cisco",
        443,
        True
    )

    print("Numbers :", numbers)
    print("Devices :", devices)
    print("Mixed   :", mixed_data)


# =============================================================================
# SECTION 3 - Single Item Tuple
# =============================================================================


def single_item_tuple_demo() -> None:
    """
    Demonstrates creating a tuple with one item.
    """

    print("\nSingle Item Tuple")
    print("-" * 40)

    wrong_tuple = (
        "SSH"
    )

    correct_tuple = (
        "SSH",
    )

    print(
        "Without comma:",
        type(wrong_tuple)
    )

    print(
        "With comma:",
        type(correct_tuple)
    )


# =============================================================================
# SECTION 4 - Tuple Indexing
# =============================================================================


def indexing_demo() -> None:
    """
    Demonstrates tuple indexing.
    """

    print("\nTuple Indexing")
    print("-" * 40)

    devices: tuple[str, ...] = (
        "Router",
        "Switch",
        "Firewall"
    )

    print("First :", devices[0])
    print("Second:", devices[1])
    print("Third :", devices[2])


# =============================================================================
# SECTION 5 - Negative Indexing
# =============================================================================


def negative_indexing_demo() -> None:
    """
    Demonstrates negative indexing.
    """

    print("\nNegative Indexing")
    print("-" * 40)

    services: tuple[str, ...] = (
        "HTTP",
        "HTTPS",
        "SSH",
        "DNS"
    )

    print("Last :", services[-1])
    print("Before Last:", services[-2])


# =============================================================================
# SECTION 6 - Tuple Slicing
# =============================================================================


def slicing_demo() -> None:
    """
    Demonstrates tuple slicing.
    """

    print("\nTuple Slicing")
    print("-" * 40)

    ports: tuple[int, ...] = (
        22,
        53,
        80,
        443,
        3389
    )

    print(
        ports[1:4]
    )

    print(
        ports[:3]
    )

    print(
        ports[::-1]
    )


# =============================================================================
# SECTION 7 - Tuple Length
# =============================================================================


def tuple_length_demo() -> None:
    """
    Demonstrates len() with tuples.
    """

    print("\nTuple Length")
    print("-" * 40)

    vlans: tuple[int, ...] = (
        10,
        20,
        30,
        40
    )

    print(
        "Number of VLANs:",
        len(vlans)
    )


# =============================================================================
# SECTION 8 - Nested Tuples
# =============================================================================


def nested_tuples_demo() -> None:
    """
    Demonstrates nested tuples.
    """

    print("\nNested Tuples")
    print("-" * 40)

    inventory: tuple = (
        (
            "R1",
            "10.0.0.1"
        ),
        (
            "SW1",
            "10.0.0.2"
        ),
        (
            "FW1",
            "10.0.0.3"
        )
    )

    print(
        "Inventory:",
        inventory
    )

    print(
        "First Device:",
        inventory[0][0]
    )

    print(
        "First IP:",
        inventory[0][1]
    )


# =============================================================================
# SECTION 9 - Tuple Immutability
# =============================================================================


def immutability_demo() -> None:
    """
    Demonstrates that tuples cannot be modified.
    """

    print("\nTuple Immutability")
    print("-" * 40)

    device: tuple[str, str] = (
        "Router",
        "Cisco"
    )

    print(
        "Original:",
        device
    )

    """
    The following code is invalid:

    device[0] = "Switch"

    Error:

    TypeError:
    'tuple' object does not support item assignment
    """

    print(
        "Tuples cannot be modified."
    )


# =============================================================================
# END OF PART 1
# =============================================================================

# =============================================================================
# SECTION 10 - Tuple count()
# =============================================================================


def count_demo() -> None:
    """
    Demonstrates tuple count() method.

    count() returns the number of
    occurrences of a value.
    """

    print("\nTuple count() Method")
    print("-" * 40)

    events: tuple[str, ...] = (
        "LOGIN",
        "ERROR",
        "WARNING",
        "ERROR",
        "ERROR"
    )

    print(
        "ERROR Count:",
        events.count("ERROR")
    )


# =============================================================================
# SECTION 11 - Tuple index()
# =============================================================================


def index_demo() -> None:
    """
    Demonstrates tuple index() method.

    index() returns the first position
    of a value.
    """

    print("\nTuple index() Method")
    print("-" * 40)

    protocols: tuple[str, ...] = (
        "HTTP",
        "HTTPS",
        "SSH",
        "DNS"
    )

    print(
        "SSH Position:",
        protocols.index("SSH")
    )


# =============================================================================
# SECTION 12 - Tuple Packing
# =============================================================================


def packing_demo() -> None:
    """
    Demonstrates tuple packing.

    Multiple values can be grouped
    into a tuple automatically.
    """

    print("\nTuple Packing")
    print("-" * 40)

    device = (
        "R1",
        "Cisco",
        "10.0.0.1"
    )

    print(
        "Packed Tuple:",
        device
    )


# =============================================================================
# SECTION 13 - Tuple Unpacking
# =============================================================================


def unpacking_demo() -> None:
    """
    Demonstrates tuple unpacking.

    Values are extracted into variables.
    """

    print("\nTuple Unpacking")
    print("-" * 40)

    device: tuple[str, str, str] = (
        "R1",
        "Cisco",
        "10.0.0.1"
    )

    name, vendor, ip = device

    print(
        "Name  :",
        name
    )

    print(
        "Vendor:",
        vendor
    )

    print(
        "IP    :",
        ip
    )


# =============================================================================
# SECTION 14 - Swapping Variables
# =============================================================================


def swapping_demo() -> None:
    """
    Demonstrates swapping variables
    using tuple unpacking.
    """

    print("\nVariable Swapping")
    print("-" * 40)

    interface_a: str = "Gi0/0"
    interface_b: str = "Gi0/1"

    print(
        "Before:",
        interface_a,
        interface_b
    )

    interface_a, interface_b = (
        interface_b,
        interface_a
    )

    print(
        "After:",
        interface_a,
        interface_b
    )


# =============================================================================
# SECTION 15 - Extended Unpacking
# =============================================================================


def extended_unpacking_demo() -> None:
    """
    Demonstrates extended tuple unpacking.
    """

    print("\nExtended Unpacking")
    print("-" * 40)

    ports: tuple[int, ...] = (
        22,
        80,
        443,
        3389
    )

    first, *middle, last = ports

    print(
        "First:",
        first
    )

    print(
        "Middle:",
        middle
    )

    print(
        "Last:",
        last
    )


# =============================================================================
# SECTION 16 - List vs Tuple Comparison
# =============================================================================


def list_vs_tuple_demo() -> None:
    """
    Demonstrates the difference between
    lists and tuples.
    """

    print("\nList vs Tuple")
    print("-" * 40)

    """
    List:

    ✔ Uses []

    ✔ Mutable

    ✔ More methods

    ✔ Used for changing data


    Tuple:

    ✔ Uses ()

    ✔ Immutable

    ✔ Faster in some cases

    ✔ Used for fixed data
    """

    network_devices_list: list[str] = [
        "Router",
        "Switch"
    ]

    network_devices_tuple: tuple[str, ...] = (
        "Router",
        "Switch"
    )

    print(
        "List :",
        network_devices_list
    )

    print(
        "Tuple:",
        network_devices_tuple
    )


# =============================================================================
# SECTION 17 - Network Configuration Example
# =============================================================================


def network_configuration_demo() -> None:
    """
    Demonstrates using tuples
    for fixed network information.
    """

    print("\nNetwork Configuration Example")
    print("-" * 40)

    interface: tuple[str, str, str] = (
        "GigabitEthernet0/1",
        "192.168.1.1",
        "UP"
    )

    interface_name, ip, status = interface

    print(
        "Interface:",
        interface_name
    )

    print(
        "IP Address:",
        ip
    )

    print(
        "Status:",
        status
    )


# =============================================================================
# SECTION 18 - Cybersecurity Event Example
# =============================================================================


def security_event_demo() -> None:
    """
    Demonstrates immutable security records.
    """

    print("\nCybersecurity Event Example")
    print("-" * 40)

    event: tuple[str, str, str] = (
        "FAILED LOGIN",
        "192.168.1.50",
        "SSH"
    )

    event_type, source_ip, service = event

    print(
        "Event:",
        event_type
    )

    print(
        "Source IP:",
        source_ip
    )

    print(
        "Service:",
        service
    )


# =============================================================================
# END OF PART 2
# =============================================================================

# =============================================================================
# SECTION 19 - Iterating Through Tuples
# =============================================================================


def tuple_iteration_demo() -> None:
    """
    Demonstrates iterating through tuples.
    """

    print("\nTuple Iteration")
    print("-" * 40)

    protocols: tuple[str, ...] = (
        "HTTP",
        "HTTPS",
        "SSH",
        "DNS"
    )

    for protocol in protocols:
        print(protocol)


# =============================================================================
# SECTION 20 - enumerate() with Tuples
# =============================================================================


def tuple_enumerate_demo() -> None:
    """
    Demonstrates enumerate() with tuples.
    """

    print("\nenumerate() with Tuples")
    print("-" * 40)

    interfaces: tuple[str, ...] = (
        "Gi0/0",
        "Gi0/1",
        "Gi0/2"
    )

    for index, interface in enumerate(interfaces):

        print(
            f"{index}: {interface}"
        )


# =============================================================================
# SECTION 21 - zip() with Tuples
# =============================================================================


def tuple_zip_demo() -> None:
    """
    Demonstrates zip() with tuples.
    """

    print("\nzip() with Tuples")
    print("-" * 40)

    devices: tuple[str, ...] = (
        "R1",
        "SW1",
        "FW1"
    )

    ip_addresses: tuple[str, ...] = (
        "10.0.0.1",
        "10.0.0.2",
        "10.0.0.3"
    )

    for device, ip in zip(
        devices,
        ip_addresses
    ):

        print(
            f"{device} --> {ip}"
        )


# =============================================================================
# SECTION 22 - Convert List to Tuple
# =============================================================================


def list_to_tuple_demo() -> None:
    """
    Demonstrates converting a list into tuple.
    """

    print("\nList to Tuple")
    print("-" * 40)

    devices: list[str] = [
        "Router",
        "Switch",
        "Firewall"
    ]

    devices_tuple = tuple(devices)

    print(
        "Original List:",
        devices
    )

    print(
        "Converted Tuple:",
        devices_tuple
    )


# =============================================================================
# SECTION 23 - Convert Tuple to List
# =============================================================================


def tuple_to_list_demo() -> None:
    """
    Demonstrates converting a tuple into list.
    """

    print("\nTuple to List")
    print("-" * 40)

    ports: tuple[int, ...] = (
        22,
        80,
        443
    )

    ports_list = list(ports)

    print(
        "Original Tuple:",
        ports
    )

    print(
        "Converted List:",
        ports_list
    )


# =============================================================================
# SECTION 24 - Returning Multiple Values
# =============================================================================


def get_device_information() -> tuple[str, str, str]:
    """
    Returns multiple values using tuple.
    """

    hostname: str = "R1"
    ip_address: str = "10.0.0.1"
    status: str = "UP"

    return (
        hostname,
        ip_address,
        status
    )


def multiple_return_demo() -> None:
    """
    Demonstrates receiving multiple
    returned values.
    """

    print("\nMultiple Return Values")
    print("-" * 40)

    hostname, ip, status = (
        get_device_information()
    )

    print(
        "Hostname:",
        hostname
    )

    print(
        "IP:",
        ip
    )

    print(
        "Status:",
        status
    )


# =============================================================================
# SECTION 25 - Tuple Function Parameters
# =============================================================================


def display_device(
    device: tuple[str, str, str]
) -> None:
    """
    Receives a tuple as a function parameter.
    """

    hostname, vendor, ip = device

    print(
        "\nDevice Information"
    )

    print(
        "Hostname:",
        hostname
    )

    print(
        "Vendor:",
        vendor
    )

    print(
        "IP:",
        ip
    )


def tuple_parameter_demo() -> None:
    """
    Demonstrates passing tuples to functions.
    """

    print("\nTuple as Function Parameter")
    print("-" * 40)

    router: tuple[str, str, str] = (
        "R1",
        "Cisco",
        "10.0.0.1"
    )

    display_device(router)


# =============================================================================
# SECTION 26 - Network Automation Example
# =============================================================================


def network_tuple_inventory_demo() -> None:
    """
    Demonstrates using tuples for
    fixed network inventory data.
    """

    print("\nNetwork Tuple Inventory")
    print("-" * 40)

    inventory: tuple = (
        (
            "R1",
            "Cisco",
            "10.0.0.1"
        ),
        (
            "SW1",
            "Cisco",
            "10.0.0.2"
        ),
        (
            "FW1",
            "Fortinet",
            "10.0.0.3"
        )
    )

    for device in inventory:

        name, vendor, ip = device

        print(
            f"{name} | {vendor} | {ip}"
        )


# =============================================================================
# SECTION 27 - Cybersecurity Hash Record Example
# =============================================================================


def security_hash_record_demo() -> None:
    """
    Demonstrates immutable security records.
    """

    print("\nSecurity Hash Record")
    print("-" * 40)

    file_record: tuple[str, str, str] = (
        "malware.exe",
        "SHA256",
        "a84f92c1"
    )

    filename, algorithm, hash_value = file_record

    print(
        "File:",
        filename
    )

    print(
        "Algorithm:",
        algorithm
    )

    print(
        "Hash:",
        hash_value
    )


# =============================================================================
# END OF PART 3
# =============================================================================

# =============================================================================
# SECTION 28 - Professional Tips
# =============================================================================


def professional_tips_demo() -> None:
    """
    Demonstrates professional tips
    when working with tuples.
    """

    print("\nProfessional Tuple Tips")
    print("-" * 40)

    """
    Professional Tips:

    ✔ Use tuples for data that should not change.

    ✔ Use tuple unpacking for cleaner code.

    ✔ Use tuples to return multiple values.

    ✔ Use tuples for fixed configuration data.

    ✔ Prefer tuples for read-only records.

    ✔ Use meaningful variable names.
    """

    print("Use tuples when data integrity is important.")


# =============================================================================
# SECTION 29 - Best Practices
# =============================================================================


def best_practices_demo() -> None:
    """
    Demonstrates tuple best practices.
    """

    print("\nTuple Best Practices")
    print("-" * 40)

    """
    Best Practices:

    ✔ Use tuples for constant values.

    ✔ Use type hints with tuples.

    ✔ Keep tuple data logically related.

    ✔ Avoid converting tuples and lists
      unnecessarily.

    ✔ Use unpacking to improve readability.
    """

    print("Write clean and predictable tuple code.")


# =============================================================================
# SECTION 30 - Common Mistakes
# =============================================================================


def common_mistakes_demo() -> None:
    """
    Explains common tuple mistakes.
    """

    print("\nCommon Tuple Mistakes")
    print("-" * 40)

    """
    Mistake 1:

    Forgetting comma in single-item tuples.


    Mistake 2:

    Trying to modify tuple elements.


    Mistake 3:

    Using tuples when data needs frequent changes.


    Mistake 4:

    Confusing tuple() conversion with list().
    """

    print("Review tuple rules carefully.")


# =============================================================================
# SECTION 31 - Performance Tips
# =============================================================================


def performance_tips_demo() -> None:
    """
    Demonstrates tuple performance tips.
    """

    print("\nTuple Performance Tips")
    print("-" * 40)

    """
    Performance Tips:

    ✔ Tuples usually consume less memory
      than lists.

    ✔ Tuples can be slightly faster
      for iteration.

    ✔ Use tuples for fixed datasets.

    ✔ Use lists for dynamic datasets.
    """

    print("Choose the correct data structure.")


# =============================================================================
# SECTION 32 - Tuple Cheat Sheet
# =============================================================================


"""
Tuple Cheat Sheet
=================


Creation:

data = (1, 2, 3)


Single Item:

item = ("Python",)


Access:

tuple[index]


Slicing:

tuple[start:end]


Methods:

count()

index()


Packing:

data = (
    value1,
    value2
)


Unpacking:

a, b = data


Conversion:

tuple(list)

list(tuple)


Common Uses:

✔ Fixed configuration

✔ Database records

✔ Function return values

✔ Network inventory
"""


# =============================================================================
# SECTION 33 - Interview Questions
# =============================================================================


"""
Interview Questions
-------------------


1. What is a tuple in Python?


2. What is the difference between
   list and tuple?


3. Why are tuples immutable?


4. Can tuples contain mutable objects?


5. What are tuple packing
   and unpacking?


6. How can a function return
   multiple values?


7. When should you use tuple
   instead of list?


8. Why are tuples useful in
   network automation?


9. What happens when you modify
   a tuple?


10. What tuple methods are available?
"""


# =============================================================================
# SECTION 34 - Coding Exercises
# =============================================================================


"""
Coding Exercises
----------------


Exercise 1:

Create a tuple containing:

Router name

IP address

Vendor


Exercise 2:

Extract values using
tuple unpacking.


Exercise 3:

Create a tuple of ports
and count port 443.


Exercise 4:

Convert a list of devices
into a tuple.


Exercise 5:

Create a function that returns:

Hostname

IP

Status


using a tuple.
"""


# =============================================================================
# SECTION 35 - Mini Project
# =============================================================================


def mini_project_description() -> None:
    """
    Mini Project:

    Network Configuration Validator


    Scenario:

    A network engineer stores
    fixed device configuration
    records using tuples.


    Requirements:


    Store:

    - Device Name

    - IP Address

    - Vendor

    - Status


    Tasks:


    1. Display configuration.

    2. Validate IP address exists.

    3. Check device status.

    4. Generate configuration report.


    Example:

    Device:
    R1

    Vendor:
    Cisco

    IP:
    10.0.0.1

    Status:
    UP


    Skills Practiced:

    ✔ Tuples

    ✔ Functions

    ✔ Unpacking

    ✔ Data Validation
    """

    print("\nMini Project: Network Configuration Validator")
    print("See project requirements above.")


# =============================================================================
# SECTION 36 - What's Next?
# =============================================================================


"""
What's Next?

Next Lesson:

09_sets.py


Topics:

✔ Creating Sets

✔ Set Properties

✔ Adding and Removing Items

✔ Set Operations

✔ Union

✔ Intersection

✔ Difference

✔ Security Examples

✔ Network Examples
"""


# =============================================================================
# SECTION 37 - Main Function
# =============================================================================


def main() -> None:
    """
    Main function that runs all demonstrations.
    """

    # Part One
    introduction_demo()
    creating_tuples_demo()
    single_item_tuple_demo()
    indexing_demo()
    negative_indexing_demo()
    slicing_demo()
    tuple_length_demo()
    nested_tuples_demo()
    immutability_demo()

    # Part Two
    count_demo()
    index_demo()
    packing_demo()
    unpacking_demo()
    swapping_demo()
    extended_unpacking_demo()
    list_vs_tuple_demo()
    network_configuration_demo()
    security_event_demo()

    # Part Three
    tuple_iteration_demo()
    tuple_enumerate_demo()
    tuple_zip_demo()
    list_to_tuple_demo()
    tuple_to_list_demo()
    multiple_return_demo()
    tuple_parameter_demo()
    network_tuple_inventory_demo()
    security_hash_record_demo()

    # Part Four
    professional_tips_demo()
    best_practices_demo()
    common_mistakes_demo()
    performance_tips_demo()
    mini_project_description()


if __name__ == "__main__":
    main()
