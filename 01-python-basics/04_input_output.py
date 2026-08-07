"""
===============================================================================
File        : 04_input_output.py
Author      : Mohammed AL-Dubai
Course      : Python Professional Roadmap
Lesson      : Input and Output

Description:
    This lesson explains how Python programs communicate with users
    through input and output operations.

Learning Objectives
-------------------
After completing this lesson, you will be able to:

✔ Understand input and output concepts.
✔ Use the print() function.
✔ Format output using different techniques.
✔ Use f-strings.
✔ Receive user input.
✔ Convert input data types.
✔ Validate user input.
✔ Build interactive programs.

===============================================================================
"""

# =============================================================================
# SECTION 1 - Introduction to Input and Output
# =============================================================================

"""
Every program follows three basic steps:

1. Input
   - Receiving data from users or external sources.

2. Processing
   - Performing operations on the data.

3. Output
   - Displaying or saving results.

Example:

Input:
    IP Address

Processing:
    Validate IP

Output:
    Validation Result
"""


def introduction_demo() -> None:
    """
    Demonstrates the basic concept of input and output.
    """

    print("\nInput and Output Concept")
    print("-" * 40)

    device_name: str = "Router"

    print("Input Data:")
    print(device_name)

    print("\nProcessing:")
    print("Checking device information...")

    print("\nOutput:")
    print("Device is ready")


# =============================================================================
# SECTION 2 - The print() Function
# =============================================================================


def print_function_demo() -> None:
    """
    Demonstrates the print() function.

    print() displays data on the console.
    """

    print("\nprint() Function")
    print("-" * 40)

    print("Hello Python")

    hostname: str = "R1"

    print(hostname)

    ip_address: str = "192.168.1.1"

    print(ip_address)

    print(hostname, ip_address)


# =============================================================================
# SECTION 3 - Using sep Parameter
# =============================================================================


def print_separator_demo() -> None:
    """
    Demonstrates the sep parameter.

    sep controls the separator between values.
    """

    print("\nsep Parameter")
    print("-" * 40)

    ip_address: str = "192.168.1.1"

    protocol: str = "SSH"

    port: int = 22

    print(
        ip_address,
        protocol,
        port
    )

    print(
        ip_address,
        protocol,
        port,
        sep=" | "
    )


# =============================================================================
# SECTION 4 - Using end Parameter
# =============================================================================


def print_end_demo() -> None:
    """
    Demonstrates the end parameter.

    end controls what appears after printing.
    """

    print("\nend Parameter")
    print("-" * 40)

    print("Loading", end=" ")

    print("Complete")

    print("Network", end="-")

    print("Security")


# =============================================================================
# SECTION 5 - String Formatting
# =============================================================================


def string_formatting_demo() -> None:
    """
    Demonstrates different string formatting methods.
    """

    print("\nString Formatting")
    print("-" * 40)

    name: str = "Mohammed"

    age: int = 47


    # Old style formatting

    print(
        "Name: %s" % name
    )


    # format() method

    print(
        "Name: {}".format(name)
    )


    # f-string (recommended)

    print(
        f"Name: {name}"
    )


    print(
        f"{name} is {age} years old"
    )


# =============================================================================
# SECTION 6 - Advanced f-string Examples
# =============================================================================


def f_string_demo() -> None:
    """
    Demonstrates practical f-string usage.
    """

    print("\nf-string Examples")
    print("-" * 40)

    hostname: str = "Core-Router"

    ip_address: str = "10.10.10.1"

    vlan_id: int = 100


    print(
        f"""
Device Information
------------------
Hostname : {hostname}
IP       : {ip_address}
VLAN     : {vlan_id}
"""
    )


# =============================================================================
# SECTION 7 - The input() Function
# =============================================================================


def input_function_demo() -> None:
    """
    Demonstrates input() function.

    Note:
    input() always returns string.
    """

    print("\ninput() Function")
    print("-" * 40)

    username: str = "admin"

    print(
        f"Welcome {username}"
    )


# =============================================================================
# END OF PART 1
# =============================================================================

# =============================================================================
# SECTION 8 - User Input and Type Conversion
# =============================================================================


def user_input_conversion_demo() -> None:
    """
    Demonstrates converting user input.

    input() always returns string,
    so conversion is required for numbers.
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
# SECTION 9 - Integer Input Example
# =============================================================================


def integer_input_demo() -> None:
    """
    Demonstrates integer conversion from input.

    Example:
    User enters a port number.
    """

    print("\nInteger Input Example")
    print("-" * 40)

    port_input: str = "443"

    port_number: int = int(port_input)

    print(
        "Port Number:",
        port_number
    )

    print(
        "Data Type:",
        type(port_number)
    )


# =============================================================================
# SECTION 10 - Float Input Example
# =============================================================================


def float_input_demo() -> None:
    """
    Demonstrates float conversion.

    Example:
    Network performance values.
    """

    print("\nFloat Input Example")
    print("-" * 40)

    latency_input: str = "15.5"

    latency: float = float(latency_input)

    print(
        "Latency:",
        latency,
        "ms"
    )

    print(
        "Data Type:",
        type(latency)
    )


# =============================================================================
# SECTION 11 - Boolean Input Handling
# =============================================================================


def boolean_input_demo() -> None:
    """
    Demonstrates handling boolean input.

    User input must be converted manually.
    """

    print("\nBoolean Input Example")
    print("-" * 40)

    ssh_status: str = "enabled"

    ssh_enabled: bool = ssh_status.lower() == "enabled"

    print(
        "SSH Enabled:",
        ssh_enabled
    )

    print(
        "Data Type:",
        type(ssh_enabled)
    )


# =============================================================================
# SECTION 12 - Input Validation
# =============================================================================


def input_validation_demo() -> None:
    """
    Demonstrates validating user input.

    try/except prevents program crashes.
    """

    print("\nInput Validation")
    print("-" * 40)

    user_port: str = "abc"

    try:

        port: int = int(user_port)

        print(
            "Port:",
            port
        )

    except ValueError:

        print(
            "Invalid port number"
        )


# =============================================================================
# SECTION 13 - Network Engineering Input Example
# =============================================================================


def network_device_input_demo() -> None:
    """
    Demonstrates collecting network device information.

    This pattern is common in automation scripts.
    """

    print("\nNetwork Device Information")
    print("-" * 40)

    hostname: str = "R1"

    ip_address: str = "192.168.1.1"

    vendor: str = "Cisco"

    vlan_id: int = 100

    interface_count: int = 48


    print(
        f"""
Device Information
------------------
Hostname        : {hostname}
IP Address      : {ip_address}
Vendor          : {vendor}
VLAN ID         : {vlan_id}
Interfaces      : {interface_count}
"""
    )


# =============================================================================
# SECTION 14 - Cybersecurity Input Example
# =============================================================================


def cybersecurity_input_demo() -> None:
    """
    Demonstrates security tool configuration input.

    Example:
    Preparing data for a security scan.
    """

    print("\nCybersecurity Input Example")
    print("-" * 40)

    target_ip: str = "192.168.1.50"

    scan_type: str = "TCP SYN"

    target_port: int = 443


    print(
        f"""
Security Scan Configuration
---------------------------
Target IP  : {target_ip}
Scan Type  : {scan_type}
Port       : {target_port}
"""
    )


# =============================================================================
# SECTION 15 - Multiple Values Input Concept
# =============================================================================


def multiple_values_input_demo() -> None:
    """
    Demonstrates processing multiple values.

    Example:
    Network protocols received as text.
    """

    print("\nMultiple Values Input")
    print("-" * 40)

    protocols_input: str = "SSH,HTTP,DNS"

    protocols: list[str] = protocols_input.split(",")

    print(
        "Protocols:"
    )

    for protocol in protocols:

        print(
            protocol
        )


# =============================================================================
# SECTION 16 - Formatted Output Report
# =============================================================================


def formatted_report_demo() -> None:
    """
    Demonstrates generating formatted reports.
    """

    print("\nFormatted Report")
    print("-" * 40)

    device = {

        "hostname": "Firewall-01",

        "ip": "10.0.0.1",

        "status": "Active"

    }


    print(
        "Device Report"
    )

    print(
        "-" * 20
    )

    for key, value in device.items():

        print(
            f"{key:<10}: {value}"
        )


# =============================================================================
# END OF PART 2
# =============================================================================

# =============================================================================
# SECTION 17 - Print vs Logging
# =============================================================================


def print_vs_logging_demo() -> None:
    """
    Explains the difference between print()
    and logging in real applications.
    """

    print("\nPrint vs Logging")
    print("-" * 40)

    """
    print():

    ✔ Simple output.
    ✔ Used for learning and debugging.
    ✔ Not suitable for production systems.


    logging:

    ✔ Used in professional applications.
    ✔ Supports different levels:

        DEBUG
        INFO
        WARNING
        ERROR
        CRITICAL


    Network automation and security tools
    usually use logging instead of print().
    """

    print("For production: use logging.")


# =============================================================================
# SECTION 18 - Input and Output Best Practices
# =============================================================================


def best_practices_demo() -> None:
    """
    Demonstrates recommended input/output practices.
    """

    print("\nInput Output Best Practices")
    print("-" * 40)

    """
    Best Practices:

    ✔ Always validate user input.

    ✔ Use clear input messages.

    ✔ Convert data to the correct type.

    ✔ Use f-strings for formatting.

    ✔ Avoid exposing sensitive information.

    ✔ Use logging for production systems.

    ✔ Keep output readable and organized.
    """

    hostname: str = "Core-Switch"

    print(
        f"Connecting to {hostname}"
    )


# =============================================================================
# SECTION 19 - Common Input Output Mistakes
# =============================================================================


def common_mistakes_demo() -> None:
    """
    Explains common mistakes with input and output.
    """

    print("\nCommon Input Output Mistakes")
    print("-" * 40)

    """
    Mistake 1:

    Forgetting input() returns string.

    Example:

    port = input("Port: ")

    port + 1

    Result:

    TypeError


    Mistake 2:

    No input validation.


    Mistake 3:

    Poor output formatting.


    Mistake 4:

    Printing sensitive information:

    Passwords
    API Keys
    Tokens
    """

    print("Review comments for examples.")


# =============================================================================
# SECTION 20 - Interview Questions
# =============================================================================


"""
Interview Questions
-------------------

1. What is the difference between input()
and print()?


2. What data type does input() return?


3. Why do we need type conversion after input()?


4. What is the difference between
print() and logging?


5. How can you validate user input?


6. How do you format output in Python?


7. Why are f-strings preferred?


8. How can input validation improve security?


9. How would you collect network device
information using Python?


10. Why should security tools avoid
printing sensitive information?
"""


# =============================================================================
# SECTION 21 - Coding Exercises
# =============================================================================


"""
Exercise 1:

Create a program that asks the user for:

Name
Age
Country

Then display:

User Profile


Exercise 2:

Create a network device information collector:

Hostname
IP Address
Vendor
Model
OS Version


Exercise 3:

Create a security scan configuration:

Target IP
Port
Scan Type


Exercise 4:

Convert user input:

"22"

into integer.

Then calculate:

port + 10


Exercise 5:

Create a formatted report using f-string.
"""


# =============================================================================
# SECTION 22 - Mini Project
# =============================================================================


def mini_project_description() -> None:
    """
    Mini Project:

    Network Configuration Collector

    Scenario:

    A network engineer needs a Python tool
    to collect device information.


    Requirements:

    Collect:

    - Device Hostname
    - IP Address
    - Vendor
    - SSH Port
    - VLAN ID
    - Device Status


    Tasks:

    1. Receive information.

    2. Convert numeric values.

    3. Validate the input.

    4. Generate formatted output.

    5. Display device summary.


    Example Output:

    Device Configuration
    --------------------
    Hostname : R1
    IP       : 192.168.1.1
    Vendor   : Cisco
    SSH Port : 22
    VLAN     : 100
    Status   : Active


    Skills Practiced:

    ✔ input()

    ✔ print()

    ✔ f-string

    ✔ Type Conversion

    ✔ Data Validation

    ✔ Network Automation Basics
    """

    print("\nMini Project: Network Configuration Collector")
    print("See project requirements above.")


# =============================================================================
# SECTION 23 - Final Main Function Update
# =============================================================================

def main() -> None:
    """
    Main function that runs all demonstrations.
    """

    # Part One
    introduction_demo()
    print_function_demo()
    print_separator_demo()
    print_end_demo()
    string_formatting_demo()
    f_string_demo()
    input_function_demo()

    # Part Two
    user_input_conversion_demo()
    integer_input_demo()
    float_input_demo()
    boolean_input_demo()
    input_validation_demo()
    network_device_input_demo()
    cybersecurity_input_demo()
    multiple_values_input_demo()
    formatted_report_demo()

    # Part Three
    print_vs_logging_demo()
    best_practices_demo()
    common_mistakes_demo()
    mini_project_description()


if __name__ == "__main__":
    main()
