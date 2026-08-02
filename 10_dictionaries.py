"""
===============================================================================
File        : 10_dictionaries.py
Author      : Mohammed AL-Dubai
Course      : Python Basics
Lesson      : Dictionaries

Description:
    This lesson explains Python dictionaries,
    key-value data structures, and practical usage.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Understand dictionaries.
✔ Create key-value data structures.
✔ Access and modify dictionary data.
✔ Add and remove dictionary items.
✔ Use dictionaries in networking and cybersecurity.

===============================================================================
"""


# =============================================================================
# SECTION 1 - Introduction to Dictionaries
# =============================================================================


"""
A dictionary is a collection of data stored as:

Key : Value


Characteristics:

✔ Ordered (Python 3.7+)

✔ Mutable

✔ Keys must be unique

✔ Values can be duplicated

✔ Accessed using keys


Examples:

Network Device Information

User Accounts

Security Events

API Responses
"""


def introduction_demo() -> None:
    """
    Demonstrates dictionary concept.
    """

    print("\nIntroduction to Dictionaries")
    print("-" * 40)

    device: dict[str, str] = {
        "hostname": "R1",
        "vendor": "Cisco",
        "status": "UP"
    }

    print(
        device
    )

    print(
        type(device)
    )


# =============================================================================
# SECTION 2 - Creating Dictionaries
# =============================================================================


def creating_dictionary_demo() -> None:
    """
    Demonstrates creating dictionaries.
    """

    print("\nCreating Dictionaries")
    print("-" * 40)

    empty_dict: dict = {}

    network_device: dict[str, str] = {
        "hostname": "SW1",
        "ip": "10.0.0.2",
        "vendor": "Cisco"
    }

    print(
        "Empty:",
        empty_dict
    )

    print(
        "Device:",
        network_device
    )


# =============================================================================
# SECTION 3 - Dictionary Keys and Values
# =============================================================================


def keys_values_demo() -> None:
    """
    Demonstrates dictionary keys and values.
    """

    print("\nDictionary Keys and Values")
    print("-" * 40)

    firewall: dict[str, str] = {
        "name": "FW1",
        "vendor": "Fortinet",
        "location": "Data Center"
    }

    print(
        "Keys:",
        firewall.keys()
    )

    print(
        "Values:",
        firewall.values()
    )


# =============================================================================
# SECTION 4 - Accessing Dictionary Values
# =============================================================================


def accessing_values_demo() -> None:
    """
    Demonstrates accessing dictionary values.
    """

    print("\nAccessing Dictionary Values")
    print("-" * 40)

    router: dict[str, str] = {
        "hostname": "R1",
        "ip": "192.168.1.1",
        "status": "UP"
    }

    print(
        "Hostname:",
        router["hostname"]
    )

    print(
        "IP:",
        router["ip"]
    )


# =============================================================================
# SECTION 5 - get() Method
# =============================================================================


def get_method_demo() -> None:
    """
    Demonstrates dictionary get() method.

    get() avoids KeyError.
    """

    print("\nget() Method")
    print("-" * 40)

    server: dict[str, str] = {
        "hostname": "WEB01",
        "os": "Linux"
    }

    print(
        server.get("hostname")
    )

    print(
        server.get(
            "ip",
            "Not Available"
        )
    )


# =============================================================================
# SECTION 6 - Adding Dictionary Items
# =============================================================================


def adding_items_demo() -> None:
    """
    Demonstrates adding new keys.
    """

    print("\nAdding Dictionary Items")
    print("-" * 40)

    device: dict[str, str] = {
        "hostname": "R1",
        "vendor": "Cisco"
    }

    device["ip"] = "10.0.0.1"

    print(
        device
    )


# =============================================================================
# SECTION 7 - Updating Dictionary Values
# =============================================================================


def updating_values_demo() -> None:
    """
    Demonstrates updating values.
    """

    print("\nUpdating Dictionary Values")
    print("-" * 40)

    interface: dict[str, str] = {
        "name": "Gi0/0",
        "status": "DOWN"
    }

    interface["status"] = "UP"

    print(
        interface
    )


# =============================================================================
# SECTION 8 - update() Method
# =============================================================================


def update_method_demo() -> None:
    """
    Demonstrates update() method.
    """

    print("\nupdate() Method")
    print("-" * 40)

    device: dict[str, str] = {
        "hostname": "R1",
        "vendor": "Cisco"
    }

    device.update(
        {
            "ip": "10.0.0.1",
            "status": "UP"
        }
    )

    print(
        device
    )


# =============================================================================
# SECTION 9 - Removing Items
# =============================================================================


def removing_items_demo() -> None:
    """
    Demonstrates removing dictionary items.
    """

    print("\nRemoving Dictionary Items")
    print("-" * 40)

    user: dict[str, str] = {
        "username": "admin",
        "role": "admin",
        "status": "active"
    }

    del user["status"]

    print(
        user
    )


# =============================================================================
# SECTION 10 - Dictionary Length
# =============================================================================


def dictionary_length_demo() -> None:
    """
    Demonstrates len() with dictionaries.
    """

    print("\nDictionary Length")
    print("-" * 40)

    config: dict[str, str] = {
        "ip": "10.0.0.1",
        "mask": "255.255.255.0",
        "gateway": "10.0.0.254"
    }

    print(
        "Number of Items:",
        len(config)
    )


# =============================================================================
# END OF PART 1
# =============================================================================

# =============================================================================
# SECTION 11 - items() Method
# =============================================================================


def items_demo() -> None:
    """
    Demonstrates items() method.

    items() returns key-value pairs.
    """

    print("\nitems() Method")
    print("-" * 40)

    device: dict[str, str] = {
        "hostname": "R1",
        "ip": "10.0.0.1",
        "vendor": "Cisco"
    }

    for key, value in device.items():

        print(
            f"{key}: {value}"
        )


# =============================================================================
# SECTION 12 - keys() Method
# =============================================================================


def keys_demo() -> None:
    """
    Demonstrates keys() method.
    """

    print("\nkeys() Method")
    print("-" * 40)

    firewall: dict[str, str] = {
        "name": "FW01",
        "vendor": "Fortinet",
        "status": "Active"
    }

    for key in firewall.keys():

        print(
            key
        )


# =============================================================================
# SECTION 13 - values() Method
# =============================================================================


def values_demo() -> None:
    """
    Demonstrates values() method.
    """

    print("\nvalues() Method")
    print("-" * 40)

    server: dict[str, str] = {
        "hostname": "WEB01",
        "os": "Linux",
        "role": "Web Server"
    }

    for value in server.values():

        print(
            value
        )


# =============================================================================
# SECTION 14 - pop() Method
# =============================================================================


def pop_demo() -> None:
    """
    Demonstrates pop() method.

    Removes item using key.
    """

    print("\npop() Method")
    print("-" * 40)

    user: dict[str, str] = {
        "username": "admin",
        "role": "administrator"
    }

    removed = user.pop(
        "role"
    )

    print(
        "Removed:",
        removed
    )

    print(
        user
    )


# =============================================================================
# SECTION 15 - popitem() Method
# =============================================================================


def popitem_demo() -> None:
    """
    Demonstrates popitem() method.

    Removes last inserted item.
    """

    print("\npopitem() Method")
    print("-" * 40)

    configuration: dict[str, str] = {
        "hostname": "R1",
        "ip": "10.0.0.1",
        "status": "UP"
    }

    removed = configuration.popitem()

    print(
        "Removed:",
        removed
    )

    print(
        configuration
    )


# =============================================================================
# SECTION 16 - clear() Method
# =============================================================================


def clear_dictionary_demo() -> None:
    """
    Demonstrates clear() method.
    """

    print("\nclear() Method")
    print("-" * 40)

    logs: dict[str, str] = {
        "event": "LOGIN",
        "status": "SUCCESS"
    }

    logs.clear()

    print(
        logs
    )


# =============================================================================
# SECTION 17 - copy() Method
# =============================================================================


def copy_demo() -> None:
    """
    Demonstrates dictionary copy.
    """

    print("\ncopy() Method")
    print("-" * 40)

    original: dict[str, str] = {
        "hostname": "R1",
        "ip": "10.0.0.1"
    }

    backup = original.copy()

    print(
        "Original:",
        original
    )

    print(
        "Backup:",
        backup
    )


# =============================================================================
# SECTION 18 - Looping Through Dictionaries
# =============================================================================


def dictionary_loop_demo() -> None:
    """
    Demonstrates looping through dictionaries.
    """

    print("\nLooping Through Dictionary")
    print("-" * 40)

    device: dict[str, str] = {
        "hostname": "SW1",
        "ip": "10.0.0.2",
        "status": "UP"
    }

    for key, value in device.items():

        print(
            key,
            "=>",
            value
        )


# =============================================================================
# SECTION 19 - Nested Dictionaries
# =============================================================================


def nested_dictionary_demo() -> None:
    """
    Demonstrates nested dictionaries.
    """

    print("\nNested Dictionaries")
    print("-" * 40)

    network_device: dict = {

        "device": {

            "hostname": "R1",
            "vendor": "Cisco",

        },

        "network": {

            "ip": "10.0.0.1",
            "vlan": 10

        }
    }

    print(
        network_device
    )

    print(
        "Hostname:",
        network_device["device"]["hostname"]
    )


# =============================================================================
# SECTION 20 - List of Dictionaries
# =============================================================================


def list_of_dictionaries_demo() -> None:
    """
    Demonstrates list containing dictionaries.
    """

    print("\nList of Dictionaries")
    print("-" * 40)

    devices: list[dict[str, str]] = [

        {
            "hostname": "R1",
            "ip": "10.0.0.1"
        },

        {
            "hostname": "SW1",
            "ip": "10.0.0.2"
        },

        {
            "hostname": "FW1",
            "ip": "10.0.0.3"
        }

    ]

    for device in devices:

        print(
            device["hostname"],
            device["ip"]
        )


# =============================================================================
# SECTION 21 - Network Inventory Example
# =============================================================================


def network_inventory_demo() -> None:
    """
    Demonstrates network inventory
    using dictionaries.
    """

    print("\nNetwork Inventory")
    print("-" * 40)

    inventory: dict[str, dict[str, str]] = {

        "R1": {

            "ip": "10.0.0.1",
            "vendor": "Cisco",
            "type": "Router"

        },

        "SW1": {

            "ip": "10.0.0.2",
            "vendor": "Cisco",
            "type": "Switch"

        }

    }


    for hostname, data in inventory.items():

        print(
            hostname,
            "=>",
            data
        )


# =============================================================================
# SECTION 22 - Security Event Record
# =============================================================================


def security_event_dictionary_demo() -> None:
    """
    Demonstrates security event storage
    using dictionaries.
    """

    print("\nSecurity Event Record")
    print("-" * 40)

    event: dict[str, str] = {

        "type": "FAILED LOGIN",

        "source_ip": "192.168.1.50",

        "service": "SSH",

        "severity": "HIGH"

    }


    for key, value in event.items():

        print(
            f"{key}: {value}"
        )


# =============================================================================
# END OF PART 2
# =============================================================================

# =============================================================================
# SECTION 23 - Dictionary Comprehension
# =============================================================================


def dictionary_comprehension_demo() -> None:
    """
    Demonstrates dictionary comprehension.
    """

    print("\nDictionary Comprehension")
    print("-" * 40)

    ports: list[int] = [
        22,
        80,
        443
    ]

    port_status: dict[int, str] = {

        port: "OPEN"

        for port in ports

    }

    print(
        port_status
    )


# =============================================================================
# SECTION 24 - Filtering Dictionary
# =============================================================================


def filtering_dictionary_demo() -> None:
    """
    Demonstrates filtering dictionaries.
    """

    print("\nFiltering Dictionary")
    print("-" * 40)

    devices: dict[str, str] = {

        "R1": "Router",

        "SW1": "Switch",

        "FW1": "Firewall"

    }


    routers: dict[str, str] = {

        name: device_type

        for name, device_type
        in devices.items()

        if device_type == "Router"

    }


    print(
        routers
    )


# =============================================================================
# SECTION 25 - Dictionary Merge Using update()
# =============================================================================


def merge_dictionary_demo() -> None:
    """
    Demonstrates merging dictionaries.
    """

    print("\nMerging Dictionaries")
    print("-" * 40)


    network_info: dict[str, str] = {

        "hostname": "R1",

        "vendor": "Cisco"

    }


    ip_info: dict[str, str] = {

        "ip": "10.0.0.1",

        "status": "UP"

    }


    network_info.update(
        ip_info
    )


    print(
        network_info
    )


# =============================================================================
# SECTION 26 - Dictionary Merge Operator
# =============================================================================


def dictionary_merge_operator_demo() -> None:
    """
    Demonstrates dictionary merge operator |.
    """

    print("\nDictionary Merge Operator |")
    print("-" * 40)


    hardware: dict[str, str] = {

        "vendor": "Cisco",

        "model": "ISR4331"

    }


    software: dict[str, str] = {

        "ios": "17.3",

        "status": "Active"

    }


    device = hardware | software


    print(
        device
    )


# =============================================================================
# SECTION 27 - fromkeys() Method
# =============================================================================


def fromkeys_demo() -> None:
    """
    Demonstrates fromkeys() method.
    """

    print("\nfromkeys() Method")
    print("-" * 40)


    interfaces: list[str] = [

        "Gi0/0",

        "Gi0/1",

        "Gi0/2"

    ]


    interface_status = dict.fromkeys(

        interfaces,

        "DOWN"

    )


    print(
        interface_status
    )


# =============================================================================
# SECTION 28 - Default Values
# =============================================================================


def default_values_demo() -> None:
    """
    Demonstrates setdefault() method.
    """

    print("\nsetdefault() Method")
    print("-" * 40)


    device: dict[str, str] = {

        "hostname": "R1"

    }


    device.setdefault(

        "status",

        "UNKNOWN"

    )


    print(
        device
    )


# =============================================================================
# SECTION 29 - Dictionary as Function Parameter
# =============================================================================


def display_device_info(
    device: dict[str, str]
) -> None:
    """
    Receives dictionary as parameter.
    """

    print(
        "\nDevice Information"
    )


    for key, value in device.items():

        print(
            f"{key}: {value}"
        )


def dictionary_parameter_demo() -> None:
    """
    Demonstrates passing dictionaries
    to functions.
    """

    print("\nDictionary Function Parameter")
    print("-" * 40)


    router: dict[str, str] = {

        "hostname": "R1",

        "ip": "10.0.0.1",

        "vendor": "Cisco"

    }


    display_device_info(
        router
    )


# =============================================================================
# SECTION 30 - Returning Dictionary From Function
# =============================================================================


def create_security_alert() -> dict[str, str]:
    """
    Returns security event
    as dictionary.
    """

    return {

        "event": "PORT SCAN",

        "source": "192.168.1.20",

        "severity": "HIGH"

    }



def return_dictionary_demo() -> None:
    """
    Demonstrates returning dictionaries.
    """

    print("\nReturn Dictionary")
    print("-" * 40)


    alert = create_security_alert()


    print(
        alert
    )


# =============================================================================
# SECTION 31 - JSON Like Data Structure
# =============================================================================


def json_structure_demo() -> None:
    """
    Demonstrates dictionary structure
    similar to JSON.
    """

    print("\nJSON Like Structure")
    print("-" * 40)


    api_response: dict = {


        "device": {

            "name": "Router1",

            "ip": "10.0.0.1"

        },


        "interfaces": [

            {

                "name": "Gi0/0",

                "status": "UP"

            },

            {

                "name": "Gi0/1",

                "status": "DOWN"

            }

        ]

    }


    print(
        api_response
    )


# =============================================================================
# SECTION 32 - Network Automation Configuration
# =============================================================================


def network_configuration_demo() -> None:
    """
    Demonstrates network configuration
    using dictionaries.
    """

    print("\nNetwork Configuration")
    print("-" * 40)


    configuration: dict = {


        "hostname": "SW1",

        "vlans": {

            10: "Users",

            20: "Servers",

            30: "Management"

        },


        "interfaces": {

            "Gi0/1": "Access",

            "Gi0/2": "Trunk"

        }

    }


    print(
        configuration
    )


# =============================================================================
# SECTION 33 - SOC Alert Analysis
# =============================================================================


def soc_alert_analysis_demo() -> None:
    """
    Demonstrates SOC alert processing.
    """

    print("\nSOC Alert Analysis")
    print("-" * 40)


    alerts: list[dict[str, str]] = [

        {

            "type": "Malware",

            "severity": "HIGH"

        },


        {

            "type": "Login Failure",

            "severity": "MEDIUM"

        }

    ]


    for alert in alerts:

        if alert["severity"] == "HIGH":

            print(
                "Critical Alert:",
                alert
            )


# =============================================================================
# END OF PART 3
# =============================================================================

# =============================================================================
# SECTION 34 - Professional Tips
# =============================================================================


def professional_tips_demo() -> None:
    """
    Demonstrates professional tips
    when working with dictionaries.
    """

    print("\nProfessional Dictionary Tips")
    print("-" * 40)

    """
    Professional Tips:

    ✔ Use dictionaries for key-value data.

    ✔ Use meaningful key names.

    ✔ Use get() when keys may not exist.

    ✔ Use items() when processing
      both keys and values.

    ✔ Use dictionaries for JSON data.

    ✔ Keep structures organized.
    """

    print(
        "Use dictionaries to represent structured data."
    )


# =============================================================================
# SECTION 35 - Best Practices
# =============================================================================


def best_practices_demo() -> None:
    """
    Demonstrates dictionary best practices.
    """

    print("\nDictionary Best Practices")
    print("-" * 40)

    """
    Best Practices:

    ✔ Keep keys consistent.

    ✔ Avoid deeply nested dictionaries.

    ✔ Validate external data.

    ✔ Use type hints.

    ✔ Use clear naming conventions.

    ✔ Separate data from logic.
    """

    print(
        "Write clean and maintainable dictionary code."
    )


# =============================================================================
# SECTION 36 - Common Mistakes
# =============================================================================


def common_mistakes_demo() -> None:
    """
    Explains common dictionary mistakes.
    """

    print("\nCommon Dictionary Mistakes")
    print("-" * 40)

    """
    Mistake 1:

    Accessing missing keys directly.


    Mistake 2:

    Using duplicate keys.


    Mistake 3:

    Changing dictionary while iterating.


    Mistake 4:

    Creating unnecessary nested structures.


    Mistake 5:

    Mixing different data formats.
    """

    print(
        "Understand dictionary limitations."
    )


# =============================================================================
# SECTION 37 - Performance Tips
# =============================================================================


def performance_tips_demo() -> None:
    """
    Demonstrates dictionary performance tips.
    """

    print("\nDictionary Performance Tips")
    print("-" * 40)

    """
    Performance Tips:

    ✔ Dictionary lookup is very fast.

    ✔ Use dictionaries instead of
      repeated list searches.

    ✔ Avoid unnecessary copying.

    ✔ Use appropriate data structures.

    ✔ Keep large dictionaries organized.
    """

    print(
        "Choose dictionaries for fast lookups."
    )


# =============================================================================
# SECTION 38 - Dictionary Cheat Sheet
# =============================================================================


"""
Dictionary Cheat Sheet
======================


Create:

data = {

    "key": "value"

}


Access:

data["key"]


Safe Access:

data.get("key")


Add:

data["new"] = value


Update:

update()


Remove:

del

pop()

popitem()


Methods:

keys()

values()

items()


Copy:

copy()


Length:

len()


Loop:

for key, value in data.items()


Advanced:

Dictionary Comprehension


Example:

{

key: value

for key, value in data.items()

}
"""


# =============================================================================
# SECTION 39 - Interview Questions
# =============================================================================


"""
Interview Questions
-------------------


1. What is a dictionary in Python?


2. What is the difference between
   dictionary and list?


3. Can dictionary keys be duplicated?


4. What types can be dictionary keys?


5. Difference between:

   get()

   and

   []


6. What is dictionary comprehension?


7. How are dictionaries related
   to JSON?


8. Why are dictionaries useful
   in network automation?


9. How can dictionaries be used
   in SOC systems?


10. Difference between:

    copy()

    and

    assignment
"""


# =============================================================================
# SECTION 40 - Coding Exercises
# =============================================================================


"""
Coding Exercises
----------------


Exercise 1:

Create a dictionary for a router:

hostname

IP

vendor

status



Exercise 2:

Update device status
from DOWN to UP.



Exercise 3:

Create a list of dictionaries
for multiple devices.



Exercise 4:

Search for devices by vendor.



Exercise 5:

Create a security alert
dictionary and analyze severity.
"""


# =============================================================================
# SECTION 41 - Mini Project
# =============================================================================


def mini_project_description() -> None:
    """
    Mini Project:

    Network Inventory Manager


    Scenario:

    Build a simple inventory system
    for network devices using dictionaries.


    Requirements:


    Store:

    - Hostname

    - IP Address

    - Vendor

    - Device Type

    - Status


    Functions:


    1. Add Device.


    2. Remove Device.


    3. Search Device.


    4. Display Inventory.


    5. Filter Devices.


    Example:


    Inventory:

    R1

    IP:
    10.0.0.1

    Vendor:
    Cisco

    Type:
    Router


    Skills Practiced:


    ✔ Dictionaries

    ✔ Lists

    ✔ Functions

    ✔ Data Processing

    ✔ Network Automation Concepts
    """

    print(
        "\nMini Project: Network Inventory Manager"
    )

    print(
        "See project requirements above."
    )


# =============================================================================
# SECTION 42 - What's Next?
# =============================================================================


"""
What's Next?

Next Lesson:

11_if_else.py


Topics:

✔ Conditional Statements

✔ if

✔ elif

✔ else

✔ Comparison Operators

✔ Logical Operators

✔ Nested Conditions

✔ Network Troubleshooting Examples

✔ Security Decision Logic
"""


# =============================================================================
# SECTION 43 - Main Function
# =============================================================================


def main() -> None:
    """
    Main function that runs all demonstrations.
    """

    # Part One

    introduction_demo()
    creating_dictionary_demo()
    keys_values_demo()
    accessing_values_demo()
    get_method_demo()
    adding_items_demo()
    updating_values_demo()
    update_method_demo()
    removing_items_demo()
    dictionary_length_demo()


    # Part Two

    items_demo()
    keys_demo()
    values_demo()
    pop_demo()
    popitem_demo()
    clear_dictionary_demo()
    copy_demo()
    dictionary_loop_demo()
    nested_dictionary_demo()
    list_of_dictionaries_demo()
    network_inventory_demo()
    security_event_dictionary_demo()


    # Part Three

    dictionary_comprehension_demo()
    filtering_dictionary_demo()
    merge_dictionary_demo()
    dictionary_merge_operator_demo()
    fromkeys_demo()
    default_values_demo()
    dictionary_parameter_demo()
    return_dictionary_demo()
    json_structure_demo()
    network_configuration_demo()
    soc_alert_analysis_demo()


    # Part Four

    professional_tips_demo()
    best_practices_demo()
    common_mistakes_demo()
    performance_tips_demo()
    mini_project_description()


if __name__ == "__main__":
    main()
