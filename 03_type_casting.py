"""
===============================================================================
File        : 03_type_casting.py
Author      : Mohammed AL-Dubai
Course      : Python Basics
Lesson      : Type Casting (Type Conversion)

Description:
    This lesson explains how Python converts data from one type
    to another using implicit and explicit type conversion.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Understand type conversion.
✔ Understand implicit conversion.
✔ Perform explicit conversion.
✔ Convert between int, float, str, and bool.
✔ Handle user input data types.
✔ Avoid common conversion errors.
✔ Apply type casting in real-world scenarios.

===============================================================================
"""

# =============================================================================
# SECTION 1 - Introduction to Type Casting
# =============================================================================

"""
Type Casting means converting a value from one data type to another.

Example:

Integer ---> String

100 ---> "100"

Python provides built-in functions:

int()
float()
str()
bool()
list()
tuple()
set()
dict()
"""


def introduction_demo() -> None:
    """
    Demonstrates the concept of type casting.
    """

    number: int = 100

    print("\nIntroduction to Type Casting")
    print("-" * 40)

    print("Original Value:", number)
    print("Original Type:", type(number))

    converted_number: str = str(number)

    print("Converted Value:", converted_number)
    print("Converted Type:", type(converted_number))


# =============================================================================
# SECTION 2 - Implicit Type Conversion
# =============================================================================


def implicit_conversion_demo() -> None:
    """
    Demonstrates implicit type conversion.

    Python automatically converts smaller data types
    into larger compatible types.
    """

    print("\nImplicit Type Conversion")
    print("-" * 40)

    integer_number: int = 10
    float_number: float = 5.5

    result = integer_number + float_number

    print("Integer:", integer_number)
    print("Float:", float_number)
    print("Result:", result)
    print("Result Type:", type(result))


# =============================================================================
# SECTION 3 - Explicit Type Conversion
# =============================================================================


def explicit_conversion_demo() -> None:
    """
    Demonstrates explicit conversion.

    The programmer manually changes the data type.
    """

    print("\nExplicit Type Conversion")
    print("-" * 40)

    text_number: str = "500"

    print("Original Value:", text_number)
    print("Original Type:", type(text_number))

    converted_number: int = int(text_number)

    print("Converted Value:", converted_number)
    print("Converted Type:", type(converted_number))


# =============================================================================
# SECTION 4 - Converting to Integer (int())
# =============================================================================


def int_conversion_demo() -> None:
    """
    Demonstrates int() conversion.

    int() converts compatible values into integers.
    """

    print("\nInteger Conversion")
    print("-" * 40)

    decimal_number: float = 25.75
    string_number: str = "100"

    converted_float = int(decimal_number)
    converted_string = int(string_number)

    print("Float to Integer:", converted_float)
    print("String to Integer:", converted_string)
    print(type(converted_string))


# =============================================================================
# SECTION 5 - Converting to Float (float())
# =============================================================================


def float_conversion_demo() -> None:
    """
    Demonstrates float() conversion.
    """

    print("\nFloat Conversion")
    print("-" * 40)

    integer_value: int = 100
    string_value: str = "99.9"

    converted_integer = float(integer_value)
    converted_string = float(string_value)

    print("Integer to Float:", converted_integer)
    print("String to Float:", converted_string)
    print(type(converted_string))


# =============================================================================
# SECTION 6 - Converting to String (str())
# =============================================================================


def string_conversion_demo() -> None:
    """
    Demonstrates str() conversion.

    Any Python object can be represented as a string.
    """

    print("\nString Conversion")
    print("-" * 40)

    number: int = 2026
    status: bool = True

    number_text = str(number)
    status_text = str(status)

    print(number_text, type(number_text))
    print(status_text, type(status_text))


# =============================================================================
# SECTION 7 - Converting to Boolean (bool())
# =============================================================================


def boolean_conversion_demo() -> None:
    """
    Demonstrates bool() conversion.

    Python evaluates values as True or False.
    """

    print("\nBoolean Conversion")
    print("-" * 40)

    values = [
        0,
        1,
        "",
        "Python",
        None,
        [],
        [1, 2, 3]
    ]

    for value in values:
        print(value, "=>", bool(value))


# =============================================================================
# END OF PART 1
# =============================================================================

# =============================================================================
# SECTION 8 - Collection Type Conversion
# =============================================================================


def collection_conversion_demo() -> None:
    """
    Demonstrates converting between collection data types.

    Python allows conversion between:
    - list
    - tuple
    - set
    """

    print("\nCollection Type Conversion")
    print("-" * 40)

    devices: list[str] = [
        "Router",
        "Switch",
        "Firewall",
        "Router"
    ]

    print("Original List:")
    print(devices)

    devices_tuple = tuple(devices)

    print("\nList to Tuple:")
    print(devices_tuple)

    devices_set = set(devices)

    print("\nList to Set:")
    print(devices_set)

    print("\nData Types:")
    print(type(devices_tuple))
    print(type(devices_set))


# =============================================================================
# SECTION 9 - String and List Conversion
# =============================================================================


def string_list_conversion_demo() -> None:
    """
    Demonstrates converting strings into lists
    and lists into strings.
    """

    print("\nString and List Conversion")
    print("-" * 40)

    protocol_string: str = "TCP,UDP,ICMP"

    protocols: list[str] = protocol_string.split(",")

    print("String to List:")
    print(protocols)

    joined_protocols: str = "-".join(protocols)

    print("\nList to String:")
    print(joined_protocols)


# =============================================================================
# SECTION 10 - User Input and Type Casting
# =============================================================================


def input_conversion_demo() -> None:
    """
    Demonstrates converting user input.

    Important:
    The input() function always returns a string.
    """

    print("\nUser Input Conversion")
    print("-" * 40)

    user_age: str = "47"

    print("Before Conversion:")
    print(user_age)
    print(type(user_age))

    age: int = int(user_age)

    print("\nAfter Conversion:")
    print(age)
    print(type(age))


# =============================================================================
# SECTION 11 - Handling Conversion Errors
# =============================================================================


def conversion_error_demo() -> None:
    """
    Demonstrates handling invalid conversions.

    Invalid conversions raise ValueError.
    """

    print("\nHandling Conversion Errors")
    print("-" * 40)

    invalid_number: str = "Python"

    try:

        number = int(invalid_number)

        print(number)

    except ValueError:

        print(
            "Cannot convert string to integer"
        )


# =============================================================================
# SECTION 12 - Type Conversion with Boolean Values
# =============================================================================


def boolean_conversion_details_demo() -> None:
    """
    Explains truthy and falsy values in Python.
    """

    print("\nBoolean Conversion Details")
    print("-" * 40)

    values = [
        False,
        True,
        0,
        100,
        "",
        "Security",
        [],
        [1]
    ]

    for value in values:

        print(
            f"{value!r:<15} => {bool(value)}"
        )


# =============================================================================
# SECTION 13 - Network Engineering Example
# =============================================================================


def network_engineering_casting_demo() -> None:
    """
    Demonstrates type casting in network automation.

    Example:
    VLAN IDs and interface numbers are often received
    as strings from users or APIs.
    """

    print("\nNetwork Engineering Type Casting")
    print("-" * 40)

    vlan_input: str = "100"

    interface_count_input: str = "48"


    vlan_id: int = int(vlan_input)

    interface_count: int = int(interface_count_input)


    print(
        "VLAN ID:",
        vlan_id,
        type(vlan_id)
    )

    print(
        "Interfaces:",
        interface_count,
        type(interface_count)
    )


# =============================================================================
# SECTION 14 - Cybersecurity Example
# =============================================================================


def cybersecurity_casting_demo() -> None:
    """
    Demonstrates type casting in cybersecurity.

    Example:
    Converting hexadecimal values and bytes.
    """

    print("\nCybersecurity Type Casting")
    print("-" * 40)

    hex_value: str = "FF"

    decimal_value: int = int(
        hex_value,
        16
    )

    print(
        "Hexadecimal:",
        hex_value
    )

    print(
        "Decimal:",
        decimal_value
    )


    packet_size: int = 1024

    packet_text: str = str(packet_size)

    print(
        "Packet Size:",
        packet_text,
        type(packet_text)
    )


# =============================================================================
# SECTION 15 - JSON Data Conversion Preview
# =============================================================================


def json_conversion_preview() -> None:
    """
    Demonstrates preparing data for JSON conversion.

    JSON is widely used in:
    - REST APIs
    - Network Automation
    - Security Tools
    """

    print("\nJSON Data Preparation")
    print("-" * 40)

    device = {

        "hostname": "R1",

        "ip_address": "192.168.1.1",

        "port": 22,

        "ssh_enabled": True

    }


    for key, value in device.items():

        print(
            key,
            "=>",
            value,
            type(value)
        )


# =============================================================================
# END OF PART 2
# =============================================================================

# =============================================================================
# SECTION 16 - Type Casting Best Practices
# =============================================================================


def best_practices_demo() -> None:
    """
    Demonstrates recommended practices when using type casting.
    """

    print("\nType Casting Best Practices")
    print("-" * 40)

    """
    Best Practices:

    ✔ Validate data before conversion.

    ✔ Use try/except when conversion may fail.

    ✔ Convert data close to where it is needed.

    ✔ Avoid unnecessary conversions.

    ✔ Use meaningful variable names.

    ✔ Remember that input() returns string.

    ✔ Understand the original data type.
    """

    user_port: str = "443"

    port_number: int = int(user_port)

    print("Port:", port_number)


# =============================================================================
# SECTION 17 - Common Type Casting Mistakes
# =============================================================================


def common_mistakes_demo() -> None:
    """
    Explains common mistakes during type conversion.
    """

    print("\nCommon Type Casting Mistakes")
    print("-" * 40)

    """
    Mistake 1:
    Converting invalid strings.

    Example:
    int("Python")

    Result:
    ValueError


    Mistake 2:
    Forgetting that input() returns string.


    Mistake 3:
    Losing decimal values.

    Example:
    int(10.9)

    Result:
    10


    Mistake 4:
    Incorrect boolean conversion.

    Example:
    bool("False")

    Result:
    True

    Because the string is not empty.
    """

    print("Check comments for examples.")


# =============================================================================
# SECTION 18 - Type Casting Comparison
# =============================================================================


def casting_comparison_demo() -> None:
    """
    Displays common type conversion examples.
    """

    print("\nType Casting Comparison")
    print("-" * 40)

    examples = [
        ("100", int("100")),
        ("10.5", float("10.5")),
        (2026, str(2026)),
        (1, bool(1)),
        (0, bool(0))
    ]

    for original, converted in examples:
        print(f"{original!r} --> {converted!r}")


# =============================================================================
# SECTION 19 - Interview Questions
# =============================================================================


"""
Interview Questions

1. What is type casting in Python?

2. What is the difference between implicit
and explicit conversion?

3. Why does input() always return a string?

4. What happens when converting invalid
data using int()?

5. What is the difference between:
   int(10.8)
   and
   round(10.8)

6. Why does bool("False") return True?

7. When do we use type casting in
network automation?

8. How can type casting errors be handled?

9. What is the difference between:
   str()
   and
   repr()

10. Why is data validation important
before conversion?
"""


# =============================================================================
# SECTION 20 - Coding Exercises
# =============================================================================


"""
Exercise 1:

Create:

age = "30"

Convert it into integer.

Calculate:

age + 5


Exercise 2:

Convert:

"192.168.1.1"

into a list of octets.


Exercise 3:

Convert:

["TCP", "UDP", "ICMP"]

into:

"TCP-UDP-ICMP"


Exercise 4:

Create a program that converts:

Port Number

from string to integer.


Exercise 5:

Handle invalid input:

number = "abc"

using try/except.


Exercise 6:

Create a dictionary representing
a network device.

Convert selected values
to the correct data types.
"""


# =============================================================================
# SECTION 21 - Mini Project
# =============================================================================


def mini_project_description() -> None:
    """
    Mini Project:

    Network Device Data Converter

    Scenario:
    A network engineer receives device
    information as strings from a CSV file.

    Requirements:

    Input Data:

    hostname
    vlan_id
    interface_count
    ssh_enabled


    Tasks:

    1. Convert VLAN ID to integer.

    2. Convert interface count to integer.

    3. Convert SSH status to boolean.

    4. Create a formatted report.

    5. Display data types.


    Example:

    Original:

    {
        "hostname": "R1",
        "vlan_id": "100",
        "interface_count": "48",
        "ssh_enabled": "True"
    }


    Converted:

    {
        "hostname": "R1",
        "vlan_id": 100,
        "interface_count": 48,
        "ssh_enabled": True
    }


    Skills Practiced:

    ✔ Type Casting

    ✔ Dictionary Handling

    ✔ Data Validation

    ✔ Network Automation Concepts
    """

    print("\nMini Project: Network Device Data Converter")
    print("See project requirements above.")


# =============================================================================
# SECTION 22 - Final Main Function Update
# =============================================================================

def main() -> None:
    """
    Main function that runs all demonstrations.
    """

    # Part One
    introduction_demo()
    implicit_conversion_demo()
    explicit_conversion_demo()
    int_conversion_demo()
    float_conversion_demo()
    string_conversion_demo()
    boolean_conversion_demo()

    # Part Two
    collection_conversion_demo()
    string_list_conversion_demo()
    input_conversion_demo()
    conversion_error_demo()
    boolean_conversion_details_demo()
    network_engineering_casting_demo()
    cybersecurity_casting_demo()
    json_conversion_preview()

    # Part Three
    best_practices_demo()
    common_mistakes_demo()
    casting_comparison_demo()
    mini_project_description()


if __name__ == "__main__":
    main()

