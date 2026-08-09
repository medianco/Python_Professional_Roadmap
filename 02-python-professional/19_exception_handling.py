# =============================================================================
# PYTHON PROFESSIONAL ROADMAP
# LESSON 19 - EXCEPTION HANDLING
# PART 1 - EXCEPTION HANDLING FUNDAMENTALS
# =============================================================================

"""
Lesson 19 - Exception Handling

Part 1 Objectives
-----------------

✔ Understand exceptions
✔ Understand try / except
✔ Handle common Python errors
✔ Use else
✔ Use finally
✔ Understand exception messages
✔ Prevent program crashes
"""


# =============================================================================
# SECTION 01 - Basic Exception
# =============================================================================


def basic_exception_demo() -> None:
    """
    Demonstrates a basic exception.
    """

    print("\nBasic Exception")
    print("-" * 40)

    try:

        number = int("Python")

        print(number)

    except ValueError:

        print(
            "ValueError handled successfully."
        )


# =============================================================================
# SECTION 02 - Division by Zero
# =============================================================================


def division_by_zero_demo() -> None:
    """
    Demonstrates ZeroDivisionError.
    """

    print("\nDivision by Zero")
    print("-" * 40)

    try:

        result = 10 / 0

        print(result)

    except ZeroDivisionError:

        print(
            "Cannot divide by zero."
        )


# =============================================================================
# SECTION 03 - Multiple Exceptions
# =============================================================================


def multiple_exceptions_demo() -> None:
    """
    Demonstrates handling multiple exceptions.
    """

    print("\nMultiple Exceptions")
    print("-" * 40)

    try:

        value = int(
            input(
                "Enter a number: "
            )
        )

        result = 100 / value

        print(
            f"Result: {result}"
        )

    except ValueError:

        print(
            "Invalid input. "
            "Please enter a number."
        )

    except ZeroDivisionError:

        print(
            "The number cannot be zero."
        )


# =============================================================================
# SECTION 04 - Generic Exception
# =============================================================================


def generic_exception_demo() -> None:
    """
    Demonstrates catching a generic Exception.

    Generic exceptions should be used carefully.
    """

    print("\nGeneric Exception")
    print("-" * 40)

    try:

        result = 10 / 0

        print(result)

    except Exception as error:

        print(
            f"An error occurred: "
            f"{error}"
        )


# =============================================================================
# SECTION 05 - Exception Object
# =============================================================================


def exception_object_demo() -> None:
    """
    Demonstrates accessing the exception object.
    """

    print("\nException Object")
    print("-" * 40)

    try:

        number = int(
            "network"
        )

        print(number)

    except ValueError as error:

        print(
            f"Exception Type: "
            f"{type(error).__name__}"
        )

        print(
            f"Exception Message: "
            f"{error}"
        )


# =============================================================================
# SECTION 06 - try / except / else
# =============================================================================


def try_except_else_demo() -> None:
    """
    Demonstrates the else block.

    else executes only when no exception occurs.
    """

    print("\ntry / except / else")
    print("-" * 40)

    try:

        number = int("100")

    except ValueError:

        print(
            "Conversion failed."
        )

    else:

        print(
            f"Conversion successful: "
            f"{number}"
        )


# =============================================================================
# SECTION 07 - try / except / finally
# =============================================================================


def try_except_finally_demo() -> None:
    """
    Demonstrates the finally block.

    finally executes whether an exception
    occurs or not.
    """

    print("\ntry / except / finally")
    print("-" * 40)

    try:

        print(
            "Executing protected code..."
        )

        result = 20 / 4

        print(
            f"Result: {result}"
        )

    except ZeroDivisionError:

        print(
            "Division by zero."
        )

    finally:

        print(
            "Finally block executed."
        )


# =============================================================================
# SECTION 08 - FileNotFoundError
# =============================================================================


def file_not_found_demo() -> None:
    """
    Demonstrates FileNotFoundError.
    """

    print("\nFileNotFoundError")
    print("-" * 40)

    file_path = Path(
        "missing_file.txt"
    )

    try:

        content = file_path.read_text(
            encoding="utf-8"
        )

        print(content)

    except FileNotFoundError:

        print(
            f"File does not exist: "
            f"{file_path}"
        )


# =============================================================================
# SECTION 09 - KeyError
# =============================================================================


def key_error_demo() -> None:
    """
    Demonstrates KeyError.
    """

    print("\nKeyError")
    print("-" * 40)

    device = {
        "hostname": "R1",
        "ip_address": "192.168.10.1"
    }

    try:

        username = device[
            "username"
        ]

        print(username)

    except KeyError:

        print(
            "The 'username' key "
            "does not exist."
        )


# =============================================================================
# SECTION 10 - IndexError
# =============================================================================


def index_error_demo() -> None:
    """
    Demonstrates IndexError.
    """

    print("\nIndexError")
    print("-" * 40)

    devices = [
        "R1",
        "R2",
        "SW1"
    ]

    try:

        print(
            devices[10]
        )

    except IndexError:

        print(
            "The requested index "
            "does not exist."
        )


# =============================================================================
# SECTION 11 - TypeError
# =============================================================================


def type_error_demo() -> None:
    """
    Demonstrates TypeError.
    """

    print("\nTypeError")
    print("-" * 40)

    try:

        result = "10" + 5

        print(result)

    except TypeError:

        print(
            "Cannot combine string "
            "and integer directly."
        )


# =============================================================================
# SECTION 12 - AttributeError
# =============================================================================


def attribute_error_demo() -> None:
    """
    Demonstrates AttributeError.
    """

    print("\nAttributeError")
    print("-" * 40)

    device = {
        "hostname": "R1"
    }

    try:

        print(
            device.hostname
        )

    except AttributeError:

        print(
            "Dictionary does not "
            "have this attribute."
        )


# =============================================================================
# SECTION 13 - NameError
# =============================================================================


def name_error_demo() -> None:
    """
    Demonstrates NameError safely.
    """

    print("\nNameError")
    print("-" * 40)

    try:

        print(
            undefined_variable
        )

    except NameError:

        print(
            "The variable is not defined."
        )


# =============================================================================
# SECTION 14 - Exception Hierarchy
# =============================================================================


def exception_hierarchy_demo() -> None:
    """
    Demonstrates Python exception hierarchy.
    """

    print("\nException Hierarchy")
    print("-" * 40)

    print(
        "BaseException"
    )

    print(
        "    └── Exception"
    )

    print(
        "        ├── ValueError"
    )

    print(
        "        ├── TypeError"
    )

    print(
        "        ├── KeyError"
    )

    print(
        "        ├── IndexError"
    )

    print(
        "        ├── OSError"
    )

    print(
        "        │   ├── FileNotFoundError"
    )

    print(
        "        │   └── PermissionError"
    )


# =============================================================================
# SECTION 15 - Network IP Validation
# =============================================================================


def network_ip_validation_demo() -> None:
    """
    Demonstrates exception handling while
    validating an IP address.
    """

    print("\nNetwork IP Validation")
    print("-" * 40)

    ip_address = "192.168.10.1"

    try:

        address = ipaddress.ip_address(
            ip_address
        )

        print(
            f"Valid IP address: "
            f"{address}"
        )

    except ValueError:

        print(
            f"Invalid IP address: "
            f"{ip_address}"
        )


# =============================================================================
# SECTION 16 - Invalid Network Validation
# =============================================================================


def invalid_network_validation_demo() -> None:
    """
    Demonstrates handling invalid network data.
    """

    print("\nInvalid Network Validation")
    print("-" * 40)

    network = "192.168.10.999/24"

    try:

        network_object = (
            ipaddress.ip_network(
                network,
                strict=False
            )
        )

        print(
            f"Network: "
            f"{network_object}"
        )

    except ValueError:

        print(
            f"Invalid network: "
            f"{network}"
        )


# =============================================================================
# SECTION 17 - Safe Integer Conversion
# =============================================================================


def safe_integer_conversion(
    value: str
) -> int | None:
    """
    Safely converts a string into an integer.

    Returns:
        int | None
    """

    try:

        return int(value)

    except ValueError:

        return None


# =============================================================================
# SECTION 18 - Safe Integer Demo
# =============================================================================


def safe_integer_demo() -> None:
    """
    Demonstrates safe integer conversion.
    """

    print("\nSafe Integer Conversion")
    print("-" * 40)

    values = [
        "100",
        "25",
        "Python",
        "500"
    ]

    for value in values:

        result = safe_integer_conversion(
            value
        )

        if result is None:

            print(
                f"{value!r} -> Invalid"
            )

        else:

            print(
                f"{value!r} -> {result}"
            )


# =============================================================================
# SECTION 19 - Safe Dictionary Access
# =============================================================================


def safe_dictionary_access(
    device: dict[str, str],
    key: str
) -> str | None:
    """
    Safely accesses a dictionary key.
    """

    try:

        return device[key]

    except KeyError:

        return None


# =============================================================================
# SECTION 20 - Safe Dictionary Demo
# =============================================================================


def safe_dictionary_demo() -> None:
    """
    Demonstrates safe dictionary access.
    """

    print("\nSafe Dictionary Access")
    print("-" * 40)

    device = {
        "hostname": "R1",
        "ip_address": "192.168.10.1",
        "vendor": "Cisco"
    }

    keys = [
        "hostname",
        "ip_address",
        "username"
    ]

    for key in keys:

        value = safe_dictionary_access(
            device,
            key
        )

        if value is None:

            print(
                f"{key}: Not found"
            )

        else:

            print(
                f"{key}: {value}"
            )


# =============================================================================
# SECTION 21 - Network Connection Simulation
# =============================================================================


def network_connection_simulation() -> None:
    """
    Simulates a network connection and
    demonstrates exception handling.
    """

    print("\nNetwork Connection Simulation")
    print("-" * 40)

    hostname = "R1"
    ip_address = "192.168.10.1"

    try:

        if not ip_address:

            raise ConnectionError(
                "IP address is missing."
            )

        print(
            f"Connecting to "
            f"{hostname} "
            f"({ip_address})..."
        )

        print(
            "Connection successful."
        )

    except ConnectionError as error:

        print(
            f"Connection failed: "
            f"{error}"
        )

    finally:

        print(
            "Connection attempt completed."
        )


# =============================================================================
# SECTION 22 - Exception Handling Function
# =============================================================================


def process_device(
    device: dict[str, str]
) -> None:
    """
    Processes a network device safely.
    """

    try:

        hostname = device["hostname"]
        ip_address = device["ip_address"]

        print(
            f"Processing "
            f"{hostname} "
            f"({ip_address})"
        )

    except KeyError as error:

        print(
            f"Missing device field: "
            f"{error}"
        )


# =============================================================================
# SECTION 23 - Device Processing Demo
# =============================================================================


def device_processing_demo() -> None:
    """
    Demonstrates safe network device processing.
    """

    print("\nDevice Processing")
    print("-" * 40)

    devices = [
        {
            "hostname": "R1",
            "ip_address": "192.168.10.1"
        },
        {
            "hostname": "R2",
            "ip_address": "192.168.10.2"
        },
        {
            "hostname": "SW1"
        }
    ]

    for device in devices:

        process_device(
            device
        )


# =============================================================================
# SECTION 24 - Part One Runner
# =============================================================================


def run_part_one() -> None:
    """
    Runs Lesson 19 Part One.
    """

    print("\n" + "=" * 70)
    print("LESSON 19 - EXCEPTION HANDLING")
    print("PART 1 - FUNDAMENTALS")
    print("=" * 70)

    basic_exception_demo()

    division_by_zero_demo()

    multiple_exceptions_demo()

    generic_exception_demo()

    exception_object_demo()

    try_except_else_demo()

    try_except_finally_demo()

    file_not_found_demo()

    key_error_demo()

    index_error_demo()

    type_error_demo()

    attribute_error_demo()

    name_error_demo()

    exception_hierarchy_demo()

    network_ip_validation_demo()

    invalid_network_validation_demo()

    safe_integer_demo()

    safe_dictionary_demo()

    network_connection_simulation()

    device_processing_demo()


# =============================================================================
# END OF PART 1
# =============================================================================

# =============================================================================
# LESSON 19 - PART 2
# HANDLING REAL-WORLD ERRORS
# =============================================================================

"""
Part 2 Objectives
-----------------

✔ Handle common Python exceptions
✔ Handle file-related exceptions
✔ Handle configuration errors
✔ Handle network-related errors
✔ Handle multiple exceptions
✔ Validate user input
✔ Use safe functions
✔ Understand exception propagation
"""


# =============================================================================
# SECTION 25 - Safe File Reader
# =============================================================================


def safe_read_file(
    file_path: str
) -> str | None:
    """
    Safely reads a text file.

    Handles:
        FileNotFoundError
        PermissionError
        OSError
    """

    try:

        path = Path(file_path)

        return path.read_text(
            encoding="utf-8"
        )

    except FileNotFoundError:

        print(
            f"File not found: "
            f"{file_path}"
        )

    except PermissionError:

        print(
            f"Permission denied: "
            f"{file_path}"
        )

    except OSError as error:

        print(
            f"File system error: "
            f"{error}"
        )

    return None


# =============================================================================
# SECTION 26 - Safe File Reader Demo
# =============================================================================


def safe_file_reader_demo() -> None:
    """
    Demonstrates safe file reading.
    """

    print("\nSafe File Reader")
    print("-" * 40)

    content = safe_read_file(
        "does_not_exist.txt"
    )

    if content is None:

        print(
            "No content was returned."
        )

    else:

        print(content)


# =============================================================================
# SECTION 27 - Safe JSON Reader
# =============================================================================


def safe_read_json(
    file_path: str
) -> dict | list | None:
    """
    Safely reads JSON data.
    """

    try:

        path = Path(file_path)

        content = path.read_text(
            encoding="utf-8"
        )

        return json.loads(
            content
        )

    except FileNotFoundError:

        print(
            f"JSON file not found: "
            f"{file_path}"
        )

    except json.JSONDecodeError as error:

        print(
            f"Invalid JSON: "
            f"{error}"
        )

    except PermissionError:

        print(
            f"Permission denied: "
            f"{file_path}"
        )

    except OSError as error:

        print(
            f"File system error: "
            f"{error}"
        )

    return None


# =============================================================================
# SECTION 28 - Invalid JSON Demo
# =============================================================================


def invalid_json_demo() -> None:
    """
    Demonstrates handling invalid JSON.
    """

    print("\nInvalid JSON")
    print("-" * 40)

    path = Path(
        "invalid.json"
    )

    path.write_text(
        '{"hostname": "R1", '
        '"ip_address": }',
        encoding="utf-8"
    )

    data = safe_read_json(
        str(path)
    )

    if data is None:

        print(
            "JSON processing failed safely."
        )


# =============================================================================
# SECTION 29 - Safe Integer Input
# =============================================================================


def get_integer(
    value: str
) -> int | None:
    """
    Converts a string into an integer safely.
    """

    try:

        return int(value)

    except ValueError:

        return None


# =============================================================================
# SECTION 30 - Integer Validation Demo
# =============================================================================


def integer_validation_demo() -> None:
    """
    Demonstrates integer validation.
    """

    print("\nInteger Validation")
    print("-" * 40)

    values = [
        "10",
        "50",
        "abc",
        "100",
        "10.5"
    ]

    for value in values:

        result = get_integer(
            value
        )

        if result is None:

            print(
                f"{value!r} -> Invalid integer"
            )

        else:

            print(
                f"{value!r} -> {result}"
            )


# =============================================================================
# SECTION 31 - Port Validation
# =============================================================================


def validate_port(
    port: int
) -> bool:
    """
    Validates a TCP/UDP port number.
    """

    if not isinstance(
        port,
        int
    ):

        raise TypeError(
            "Port must be an integer."
        )

    if not 1 <= port <= 65535:

        raise ValueError(
            "Port must be between "
            "1 and 65535."
        )

    return True


# =============================================================================
# SECTION 32 - Port Validation Demo
# =============================================================================


def port_validation_demo() -> None:
    """
    Demonstrates port validation.
    """

    print("\nPort Validation")
    print("-" * 40)

    ports = [
        22,
        80,
        443,
        0,
        65535,
        70000
    ]

    for port in ports:

        try:

            validate_port(
                port
            )

            print(
                f"{port:<6} -> Valid"
            )

        except (
            TypeError,
            ValueError
        ) as error:

            print(
                f"{port:<6} -> "
                f"Invalid: {error}"
            )


# =============================================================================
# SECTION 33 - IP Validation Function
# =============================================================================


def validate_ip(
    ip_address: str
) -> bool:
    """
    Validates an IPv4 or IPv6 address.
    """

    try:

        ipaddress.ip_address(
            ip_address
        )

        return True

    except ValueError:

        return False


# =============================================================================
# SECTION 34 - IP Validation Demo
# =============================================================================


def ip_validation_demo() -> None:
    """
    Demonstrates IP validation.
    """

    print("\nIP Validation")
    print("-" * 40)

    addresses = [
        "192.168.1.1",
        "10.0.0.1",
        "256.1.1.1",
        "192.168.1",
        "2001:db8::1"
    ]

    for address in addresses:

        if validate_ip(address):

            print(
                f"{address:<20} -> Valid"
            )

        else:

            print(
                f"{address:<20} -> Invalid"
            )


# =============================================================================
# SECTION 35 - Network Validation
# =============================================================================


def validate_network(
    network: str
) -> bool:
    """
    Validates a network in CIDR notation.
    """

    try:

        ipaddress.ip_network(
            network,
            strict=False
        )

        return True

    except ValueError:

        return False


# =============================================================================
# SECTION 36 - Network Validation Demo
# =============================================================================


def network_validation_demo() -> None:
    """
    Demonstrates network validation.
    """

    print("\nNetwork Validation")
    print("-" * 40)

    networks = [
        "192.168.1.0/24",
        "10.0.0.0/8",
        "172.16.0.0/16",
        "192.168.1.1/24",
        "192.168.1.0/33"
    ]

    for network in networks:

        if validate_network(network):

            print(
                f"{network:<20} -> Valid"
            )

        else:

            print(
                f"{network:<20} -> Invalid"
            )


# =============================================================================
# SECTION 37 - Device Validation
# =============================================================================


def validate_device(
    device: dict
) -> bool:
    """
    Validates required network device fields.
    """

    required_fields = [
        "hostname",
        "ip_address",
        "username"
    ]

    if not isinstance(
        device,
        dict
    ):

        raise TypeError(
            "Device must be a dictionary."
        )

    for field in required_fields:

        if field not in device:

            raise KeyError(
                f"Missing field: {field}"
            )

    if not validate_ip(
        device["ip_address"]
    ):

        raise ValueError(
            "Invalid IP address."
        )

    return True


# =============================================================================
# SECTION 38 - Device Validation Demo
# =============================================================================


def device_validation_demo() -> None:
    """
    Demonstrates network device validation.
    """

    print("\nDevice Validation")
    print("-" * 40)

    devices = [
        {
            "hostname": "R1",
            "ip_address": "192.168.10.1",
            "username": "admin"
        },
        {
            "hostname": "R2",
            "ip_address": "192.168.10.2"
        },
        {
            "hostname": "SW1",
            "ip_address": "192.168.10.10",
            "username": "admin"
        },
        {
            "hostname": "R3",
            "ip_address": "300.1.1.1",
            "username": "admin"
        }
    ]

    for device in devices:

        try:

            validate_device(
                device
            )

            print(
                f"{device.get('hostname')} "
                f"-> Valid device"
            )

        except KeyError as error:

            print(
                f"{device.get('hostname', 'Unknown')} "
                f"-> Missing field: {error}"
            )

        except ValueError as error:

            print(
                f"{device.get('hostname', 'Unknown')} "
                f"-> Invalid data: {error}"
            )

        except TypeError as error:

            print(
                f"Invalid device: {error}"
            )


# =============================================================================
# SECTION 39 - Configuration Validation
# =============================================================================


def validate_configuration(
    configuration: dict[str, str]
) -> bool:
    """
    Validates network configuration.
    """

    required = [
        "hostname",
        "ip_address",
        "username",
        "port"
    ]

    for field in required:

        if field not in configuration:

            raise KeyError(
                f"Missing configuration "
                f"field: {field}"
            )

    if not validate_ip(
        configuration["ip_address"]
    ):

        raise ValueError(
            "Invalid IP address."
        )

    try:

        port = int(
            configuration["port"]
        )

    except ValueError as error:

        raise ValueError(
            "Port must be numeric."
        ) from error

    validate_port(
        port
    )

    return True


# =============================================================================
# SECTION 40 - Configuration Validation Demo
# =============================================================================


def configuration_validation_demo() -> None:
    """
    Demonstrates configuration validation.
    """

    print("\nConfiguration Validation")
    print("-" * 40)

    configurations = [
        {
            "hostname": "R1",
            "ip_address": "192.168.10.1",
            "username": "admin",
            "port": "22"
        },
        {
            "hostname": "R2",
            "ip_address": "192.168.10.2",
            "username": "admin",
            "port": "65536"
        },
        {
            "hostname": "R3",
            "ip_address": "192.168.10.3",
            "port": "22"
        },
        {
            "hostname": "R4",
            "ip_address": "300.1.1.1",
            "username": "admin",
            "port": "22"
        }
    ]

    for configuration in configurations:

        try:

            validate_configuration(
                configuration
            )

            print(
                f"{configuration.get('hostname')} "
                f"-> Configuration valid"
            )

        except (
            KeyError,
            ValueError,
            TypeError
        ) as error:

            print(
                f"{configuration.get('hostname', 'Unknown')} "
                f"-> Configuration error: "
                f"{error}"
            )


# =============================================================================
# SECTION 41 - Connection Error Simulation
# =============================================================================


def connect_to_device(
    hostname: str,
    ip_address: str
) -> bool:
    """
    Simulates a network connection.

    This is a simulation only.
    """

    if not hostname:

        raise ValueError(
            "Hostname cannot be empty."
        )

    if not validate_ip(
        ip_address
    ):

        raise ValueError(
            f"Invalid IP: {ip_address}"
        )

    if ip_address.endswith(
        ".20"
    ):

        raise ConnectionError(
            f"Unable to connect to "
            f"{hostname} ({ip_address})"
        )

    return True


# =============================================================================
# SECTION 42 - Connection Demo
# =============================================================================


def connection_error_demo() -> None:
    """
    Demonstrates handling network connection errors.
    """

    print("\nConnection Error Handling")
    print("-" * 40)

    devices = [
        {
            "hostname": "R1",
            "ip_address": "192.168.10.1"
        },
        {
            "hostname": "R2",
            "ip_address": "192.168.10.2"
        },
        {
            "hostname": "MT1",
            "ip_address": "192.168.10.20"
        },
        {
            "hostname": "BAD",
            "ip_address": "300.1.1.1"
        }
    ]

    for device in devices:

        try:

            connect_to_device(
                device["hostname"],
                device["ip_address"]
            )

            print(
                f"{device['hostname']} "
                f"-> Connection successful"
            )

        except ConnectionError as error:

            print(
                f"{device['hostname']} "
                f"-> Connection error: "
                f"{error}"
            )

        except ValueError as error:

            print(
                f"{device['hostname']} "
                f"-> Validation error: "
                f"{error}"
            )


# =============================================================================
# SECTION 43 - CSV Processing Error Handling
# =============================================================================


def process_csv_file(
    file_path: str
) -> list[dict[str, str]]:
    """
    Safely processes a CSV file.
    """

    records: list[dict[str, str]] = []

    try:

        with open(
            file_path,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(
                file
            )

            for row in reader:

                records.append(
                    dict(row)
                )

    except FileNotFoundError:

        print(
            f"CSV file not found: "
            f"{file_path}"
        )

    except PermissionError:

        print(
            f"Permission denied: "
            f"{file_path}"
        )

    except UnicodeDecodeError:

        print(
            f"Unable to decode file: "
            f"{file_path}"
        )

    except OSError as error:

        print(
            f"CSV processing error: "
            f"{error}"
        )

    return records


# =============================================================================
# SECTION 44 - CSV Error Demo
# =============================================================================


def csv_error_handling_demo() -> None:
    """
    Demonstrates safe CSV processing.
    """

    print("\nCSV Error Handling")
    print("-" * 40)

    records = process_csv_file(
        "missing_inventory.csv"
    )

    print(
        f"Records loaded: "
        f"{len(records)}"
    )


# =============================================================================
# SECTION 45 - Exception Propagation
# =============================================================================


def low_level_network_operation() -> None:
    """
    Simulates a low-level network error.
    """

    raise ConnectionError(
        "Remote device refused connection."
    )


def network_operation() -> None:
    """
    Calls a lower-level function.
    """

    low_level_network_operation()


def exception_propagation_demo() -> None:
    """
    Demonstrates exception propagation.
    """

    print("\nException Propagation")
    print("-" * 40)

    try:

        network_operation()

    except ConnectionError as error:

        print(
            f"Exception caught at higher level: "
            f"{error}"
        )


# =============================================================================
# SECTION 46 - Safe Batch Processing
# =============================================================================


def process_devices_safely(
    devices: list[dict[str, str]]
) -> None:
    """
    Processes multiple devices.

    One failed device should not stop
    the entire batch.
    """

    print("\nSafe Batch Processing")
    print("-" * 40)

    for device in devices:

        try:

            connect_to_device(
                device["hostname"],
                device["ip_address"]
            )

            print(
                f"[SUCCESS] "
                f"{device['hostname']}"
            )

        except (
            ConnectionError,
            ValueError,
            KeyError
        ) as error:

            print(
                f"[FAILED] "
                f"{device.get('hostname', 'Unknown')} "
                f"-> {error}"
            )


# =============================================================================
# SECTION 47 - Batch Processing Demo
# =============================================================================


def batch_processing_demo() -> None:
    """
    Demonstrates resilient network processing.
    """

    devices = [
        {
            "hostname": "R1",
            "ip_address": "192.168.10.1"
        },
        {
            "hostname": "R2",
            "ip_address": "192.168.10.2"
        },
        {
            "hostname": "MT1",
            "ip_address": "192.168.10.20"
        },
        {
            "hostname": "BAD",
            "ip_address": "300.1.1.1"
        }
    ]

    process_devices_safely(
        devices
    )


# =============================================================================
# SECTION 48 - Part Two Runner
# =============================================================================


def run_part_two() -> None:
    """
    Runs Lesson 19 Part Two.
    """

    print("\n" + "=" * 70)
    print("LESSON 19 - EXCEPTION HANDLING")
    print("PART 2 - HANDLING REAL-WORLD ERRORS")
    print("=" * 70)

    safe_file_reader_demo()

    invalid_json_demo()

    integer_validation_demo()

    port_validation_demo()

    ip_validation_demo()

    network_validation_demo()

    device_validation_demo()

    configuration_validation_demo()

    connection_error_demo()

    csv_error_handling_demo()

    exception_propagation_demo()

    batch_processing_demo()


# =============================================================================
# END OF PART 2
# =============================================================================

# =============================================================================
# LESSON 19 - PART 3
# RAISING & CUSTOM EXCEPTIONS
# =============================================================================

"""
Part 3 Objectives
-----------------

✔ Understand raise
✔ Create custom exceptions
✔ Use exception inheritance
✔ Validate network devices
✔ Validate configurations
✔ Use exception chaining
✔ Separate validation from processing
✔ Build reusable error handling
"""


# =============================================================================
# SECTION 49 - Basic raise
# =============================================================================


def basic_raise_demo() -> None:
    """
    Demonstrates the raise statement.
    """

    print("\nBasic raise")
    print("-" * 40)

    try:

        raise ValueError(
            "This error was intentionally raised."
        )

    except ValueError as error:

        print(
            f"Caught exception: {error}"
        )


# =============================================================================
# SECTION 50 - Raise with Validation
# =============================================================================


def validate_hostname(
    hostname: str
) -> bool:
    """
    Validates a network hostname.
    """

    if not isinstance(
        hostname,
        str
    ):

        raise TypeError(
            "Hostname must be a string."
        )

    hostname = hostname.strip()

    if not hostname:

        raise ValueError(
            "Hostname cannot be empty."
        )

    if len(hostname) > 63:

        raise ValueError(
            "Hostname is too long."
        )

    return True


# =============================================================================
# SECTION 51 - Hostname Validation Demo
# =============================================================================


def hostname_validation_demo() -> None:
    """
    Demonstrates hostname validation.
    """

    print("\nHostname Validation")
    print("-" * 40)

    hostnames = [
        "R1",
        "SW1",
        "Core-Router",
        "",
        100
    ]

    for hostname in hostnames:

        try:

            validate_hostname(
                hostname
            )

            print(
                f"{hostname!r} -> Valid"
            )

        except (
            TypeError,
            ValueError
        ) as error:

            print(
                f"{hostname!r} -> "
                f"Invalid: {error}"
            )


# =============================================================================
# SECTION 52 - Custom Exception: NetworkError
# =============================================================================


class NetworkError(Exception):
    """
    Base exception for network-related errors.
    """

    pass


# =============================================================================
# SECTION 53 - Custom Exception: DeviceConnectionError
# =============================================================================


class DeviceConnectionError(
    NetworkError
):
    """
    Raised when a network device
    cannot be reached.
    """

    pass


# =============================================================================
# SECTION 54 - Custom Exception: DeviceAuthenticationError
# =============================================================================


class DeviceAuthenticationError(
    NetworkError
):
    """
    Raised when device authentication fails.
    """

    pass


# =============================================================================
# SECTION 55 - Custom Exception: ConfigurationError
# =============================================================================


class ConfigurationError(
    NetworkError
):
    """
    Raised when a device configuration
    is invalid.
    """

    pass


# =============================================================================
# SECTION 56 - Custom Exception Hierarchy
# =============================================================================


def custom_exception_hierarchy_demo() -> None:
    """
    Demonstrates custom exception inheritance.
    """

    print("\nCustom Exception Hierarchy")
    print("-" * 40)

    print(
        "NetworkError"
    )

    print(
        "├── DeviceConnectionError"
    )

    print(
        "├── DeviceAuthenticationError"
    )

    print(
        "└── ConfigurationError"
    )


# =============================================================================
# SECTION 57 - Simulated Device Connection
# =============================================================================


def connect_device_secure(
    hostname: str,
    ip_address: str,
    username: str
) -> bool:
    """
    Simulates a secure device connection.

    Raises:
        DeviceConnectionError
        DeviceAuthenticationError
        ValueError
    """

    validate_hostname(
        hostname
    )

    if not validate_ip(
        ip_address
    ):

        raise ValueError(
            f"Invalid IP address: "
            f"{ip_address}"
        )

    if not username:

        raise DeviceAuthenticationError(
            "Username cannot be empty."
        )

    if ip_address.endswith(
        ".20"
    ):

        raise DeviceConnectionError(
            f"Unable to connect to "
            f"{hostname} ({ip_address})."
        )

    return True


# =============================================================================
# SECTION 58 - Secure Connection Demo
# =============================================================================


def secure_connection_demo() -> None:
    """
    Demonstrates custom network exceptions.
    """

    print("\nSecure Device Connection")
    print("-" * 40)

    devices = [
        {
            "hostname": "R1",
            "ip_address": "192.168.10.1",
            "username": "admin"
        },
        {
            "hostname": "R2",
            "ip_address": "192.168.10.2",
            "username": "admin"
        },
        {
            "hostname": "MT1",
            "ip_address": "192.168.10.20",
            "username": "admin"
        },
        {
            "hostname": "SW1",
            "ip_address": "192.168.10.10",
            "username": ""
        }
    ]

    for device in devices:

        try:

            connect_device_secure(
                device["hostname"],
                device["ip_address"],
                device["username"]
            )

            print(
                f"[SUCCESS] "
                f"{device['hostname']}"
            )

        except DeviceConnectionError as error:

            print(
                f"[CONNECTION ERROR] "
                f"{device['hostname']}: "
                f"{error}"
            )

        except DeviceAuthenticationError as error:

            print(
                f"[AUTHENTICATION ERROR] "
                f"{device['hostname']}: "
                f"{error}"
            )

        except ValueError as error:

            print(
                f"[VALIDATION ERROR] "
                f"{device['hostname']}: "
                f"{error}"
            )


# =============================================================================
# SECTION 59 - Configuration Validator
# =============================================================================


def validate_router_configuration(
    configuration: dict[str, object]
) -> bool:
    """
    Validates a router configuration.
    """

    required_fields = [
        "hostname",
        "ip_address",
        "username",
        "port",
        "protocol"
    ]

    for field in required_fields:

        if field not in configuration:

            raise ConfigurationError(
                f"Missing configuration "
                f"field: {field}"
            )

    if not isinstance(
        configuration["hostname"],
        str
    ):

        raise ConfigurationError(
            "Hostname must be a string."
        )

    if not validate_ip(
        str(
            configuration["ip_address"]
        )
    ):

        raise ConfigurationError(
            "Invalid IP address."
        )

    try:

        port = int(
            configuration["port"]
        )

    except (
        TypeError,
        ValueError
    ) as error:

        raise ConfigurationError(
            "Port must be an integer."
        ) from error

    try:

        validate_port(
            port
        )

    except (
        TypeError,
        ValueError
    ) as error:

        raise ConfigurationError(
            f"Invalid port: {error}"
        ) from error

    supported_protocols = {
        "ssh",
        "https"
    }

    protocol = str(
        configuration["protocol"]
    ).lower()

    if protocol not in supported_protocols:

        raise ConfigurationError(
            f"Unsupported protocol: "
            f"{protocol}"
        )

    return True


# =============================================================================
# SECTION 60 - Configuration Validator Demo
# =============================================================================


def router_configuration_demo() -> None:
    """
    Demonstrates custom configuration errors.
    """

    print("\nRouter Configuration Validation")
    print("-" * 40)

    configurations = [
        {
            "hostname": "R1",
            "ip_address": "192.168.10.1",
            "username": "admin",
            "port": 22,
            "protocol": "ssh"
        },
        {
            "hostname": "R2",
            "ip_address": "192.168.10.2",
            "username": "admin",
            "port": 443,
            "protocol": "https"
        },
        {
            "hostname": "R3",
            "ip_address": "192.168.10.3",
            "username": "admin",
            "port": 99999,
            "protocol": "ssh"
        },
        {
            "hostname": "R4",
            "ip_address": "192.168.10.4",
            "username": "admin",
            "port": 22,
            "protocol": "ftp"
        },
        {
            "hostname": "R5",
            "ip_address": "invalid",
            "username": "admin",
            "port": 22,
            "protocol": "ssh"
        }
    ]

    for configuration in configurations:

        try:

            validate_router_configuration(
                configuration
            )

            print(
                f"{configuration['hostname']} "
                f"-> Configuration valid"
            )

        except ConfigurationError as error:

            print(
                f"{configuration.get('hostname', 'Unknown')} "
                f"-> Configuration error: "
                f"{error}"
            )


# =============================================================================
# SECTION 61 - Exception Chaining
# =============================================================================


def load_device_port(
    value: str
) -> int:
    """
    Converts a device port into an integer.

    Demonstrates exception chaining.
    """

    try:

        return int(value)

    except ValueError as error:

        raise ConfigurationError(
            f"Invalid port value: {value!r}"
        ) from error


# =============================================================================
# SECTION 62 - Exception Chaining Demo
# =============================================================================


def exception_chaining_demo() -> None:
    """
    Demonstrates 'raise ... from error'.
    """

    print("\nException Chaining")
    print("-" * 40)

    try:

        load_device_port(
            "SSH"
        )

    except ConfigurationError as error:

        print(
            f"ConfigurationError: "
            f"{error}"
        )

        if error.__cause__:

            print(
                f"Original exception: "
                f"{error.__cause__}"
            )


# =============================================================================
# SECTION 63 - Security Validation Exception
# =============================================================================


class SecurityValidationError(
    Exception
):
    """
    Raised when security validation fails.
    """

    pass


# =============================================================================
# SECTION 64 - Password Policy Validation
# =============================================================================


def validate_password_policy(
    password: str
) -> bool:
    """
    Validates a basic password policy.

    Requirements:

    ✔ At least 12 characters
    ✔ Contains uppercase
    ✔ Contains lowercase
    ✔ Contains a digit
    """

    if not isinstance(
        password,
        str
    ):

        raise SecurityValidationError(
            "Password must be a string."
        )

    if len(password) < 12:

        raise SecurityValidationError(
            "Password must contain "
            "at least 12 characters."
        )

    if not any(
        character.isupper()
        for character in password
    ):

        raise SecurityValidationError(
            "Password must contain "
            "an uppercase character."
        )

    if not any(
        character.islower()
        for character in password
    ):

        raise SecurityValidationError(
            "Password must contain "
            "a lowercase character."
        )

    if not any(
        character.isdigit()
        for character in password
    ):

        raise SecurityValidationError(
            "Password must contain "
            "a digit."
        )

    return True


# =============================================================================
# SECTION 65 - Security Validation Demo
# =============================================================================


def security_validation_demo() -> None:
    """
    Demonstrates security validation.
    """

    print("\nSecurity Validation")
    print("-" * 40)

    passwords = [
        "password",
        "Password123",
        "StrongPassword123",
        "NetworkAdmin2026",
        "short1A"
    ]

    for password in passwords:

        try:

            validate_password_policy(
                password
            )

            print(
                f"{password!r} -> "
                f"Password policy valid"
            )

        except SecurityValidationError as error:

            print(
                f"{password!r} -> "
                f"Rejected: {error}"
            )


# =============================================================================
# SECTION 66 - Security Event Exception
# =============================================================================


class SecurityEventError(
    Exception
):
    """
    Represents a security-related processing error.
    """

    pass


# =============================================================================
# SECTION 67 - Security Event Processor
# =============================================================================


def process_security_event(
    event: dict[str, str]
) -> bool:
    """
    Validates and processes a security event.
    """

    required_fields = [
        "event_type",
        "source_ip",
        "severity"
    ]

    for field in required_fields:

        if field not in event:

            raise SecurityEventError(
                f"Missing security event "
                f"field: {field}"
            )

    if not validate_ip(
        event["source_ip"]
    ):

        raise SecurityEventError(
            f"Invalid source IP: "
            f"{event['source_ip']}"
        )

    allowed_severity = {
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL"
    }

    severity = (
        event["severity"]
        .upper()
    )

    if severity not in allowed_severity:

        raise SecurityEventError(
            f"Invalid severity: "
            f"{severity}"
        )

    return True


# =============================================================================
# SECTION 68 - Security Event Demo
# =============================================================================


def security_event_demo() -> None:
    """
    Demonstrates security event validation.
    """

    print("\nSecurity Event Processing")
    print("-" * 40)

    events = [
        {
            "event_type": "Failed Login",
            "source_ip": "192.168.10.50",
            "severity": "MEDIUM"
        },
        {
            "event_type": "Port Scan",
            "source_ip": "192.168.10.51",
            "severity": "HIGH"
        },
        {
            "event_type": "Malware Detection",
            "source_ip": "192.168.10.60",
            "severity": "CRITICAL"
        },
        {
            "event_type": "Invalid Event",
            "source_ip": "999.999.999.999",
            "severity": "HIGH"
        },
        {
            "event_type": "Unknown",
            "source_ip": "192.168.10.70",
            "severity": "UNKNOWN"
        }
    ]

    for event in events:

        try:

            process_security_event(
                event
            )

            print(
                f"[ACCEPTED] "
                f"{event['event_type']}"
            )

        except SecurityEventError as error:

            print(
                f"[REJECTED] "
                f"{event.get('event_type', 'Unknown')}: "
                f"{error}"
            )


# =============================================================================
# SECTION 69 - Network Device Manager
# =============================================================================


class NetworkDeviceManager:
    """
    Simple network device manager
    using custom exceptions.
    """

    def __init__(
        self
    ) -> None:

        self.devices: dict[
            str,
            dict[str, str]
        ] = {}

    def add_device(
        self,
        hostname: str,
        ip_address: str
    ) -> None:
        """
        Adds a device after validation.
        """

        try:

            validate_hostname(
                hostname
            )

            if not validate_ip(
                ip_address
            ):

                raise ValueError(
                    f"Invalid IP address: "
                    f"{ip_address}"
                )

            if hostname in self.devices:

                raise NetworkError(
                    f"Device {hostname} "
                    f"already exists."
                )

            self.devices[hostname] = {
                "hostname": hostname,
                "ip_address": ip_address
            }

        except (
            TypeError,
            ValueError,
            NetworkError
        ):

            raise

    def get_device(
        self,
        hostname: str
    ) -> dict[str, str]:
        """
        Retrieves a device.
        """

        if hostname not in self.devices:

            raise NetworkError(
                f"Device {hostname} "
                f"does not exist."
            )

        return self.devices[
            hostname
        ]


# =============================================================================
# SECTION 70 - Network Device Manager Demo
# =============================================================================


def device_manager_demo() -> None:
    """
    Demonstrates custom exceptions in a class.
    """

    print("\nNetwork Device Manager")
    print("-" * 40)

    manager = (
        NetworkDeviceManager()
    )

    devices = [
        (
            "R1",
            "192.168.10.1"
        ),
        (
            "R2",
            "192.168.10.2"
        ),
        (
            "R1",
            "192.168.10.100"
        ),
        (
            "SW1",
            "invalid"
        )
    ]

    for hostname, ip_address in devices:

        try:

            manager.add_device(
                hostname,
                ip_address
            )

            print(
                f"[ADDED] "
                f"{hostname}"
            )

        except (
            NetworkError,
            ValueError,
            TypeError
        ) as error:

            print(
                f"[FAILED] "
                f"{hostname}: "
                f"{error}"
            )

    print(
        f"\nDevices stored: "
        f"{len(manager.devices)}"
    )


# =============================================================================
# SECTION 71 - Custom Exception Summary
# =============================================================================


def custom_exception_summary() -> None:
    """
    Displays the custom exception architecture.
    """

    print("\nCustom Exception Architecture")
    print("-" * 40)

    print(
        "Exception"
    )

    print(
        "├── NetworkError"
    )

    print(
        "│   ├── DeviceConnectionError"
    )

    print(
        "│   ├── DeviceAuthenticationError"
    )

    print(
        "│   └── ConfigurationError"
    )

    print(
        "├── SecurityValidationError"
    )

    print(
        "└── SecurityEventError"
    )


# =============================================================================
# SECTION 72 - Part Three Runner
# =============================================================================


def run_part_three() -> None:
    """
    Runs Lesson 19 Part Three.
    """

    print("\n" + "=" * 70)
    print("LESSON 19 - EXCEPTION HANDLING")
    print("PART 3 - RAISING & CUSTOM EXCEPTIONS")
    print("=" * 70)

    basic_raise_demo()

    hostname_validation_demo()

    custom_exception_hierarchy_demo()

    secure_connection_demo()

    router_configuration_demo()

    exception_chaining_demo()

    security_validation_demo()

    security_event_demo()

    device_manager_demo()

    custom_exception_summary()


# =============================================================================
# END OF PART 3
# =============================================================================

# =============================================================================
# LESSON 19 - PART 4
# PROFESSIONAL ERROR HANDLING
# =============================================================================

"""
Part 4 Objectives
-----------------

✔ Use logging with exception handling
✔ Capture traceback information
✔ Create reusable error handlers
✔ Implement retry mechanisms
✔ Handle network failures
✔ Use context managers safely
✔ Separate errors by severity
✔ Build resilient automation workflows
"""


# =============================================================================
# SECTION 73 - Logging Configuration
# =============================================================================


def configure_logging() -> logging.Logger:
    """
    Creates and configures a lesson logger.
    """

    logger = logging.getLogger(
        "python_exception_handling"
    )

    if not logger.handlers:

        logger.setLevel(
            logging.DEBUG
        )

        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(message)s"
        )

        handler.setFormatter(
            formatter
        )

        logger.addHandler(
            handler
        )

    return logger


# =============================================================================
# SECTION 74 - Basic Logging Demo
# =============================================================================


def logging_error_demo() -> None:
    """
    Demonstrates logging different
    exception levels.
    """

    print("\nLogging Error Handling")
    print("-" * 40)

    logger = configure_logging()

    logger.info(
        "Starting error handling demo."
    )

    try:

        result = 10 / 0

        print(result)

    except ZeroDivisionError as error:

        logger.error(
            f"Division failed: {error}"
        )

    logger.warning(
        "The operation was recovered safely."
    )

    logger.info(
        "Demo completed."
    )


# =============================================================================
# SECTION 75 - Logging Exception Traceback
# =============================================================================


def logging_exception_demo() -> None:
    """
    Demonstrates logger.exception().
    """

    print("\nLogging Exception Traceback")
    print("-" * 40)

    logger = configure_logging()

    try:

        value = int(
            "network"
        )

        print(value)

    except ValueError:

        logger.exception(
            "Failed to convert value."
        )


# =============================================================================
# SECTION 76 - Traceback Module
# =============================================================================


def traceback_demo() -> None:
    """
    Demonstrates traceback information.
    """

    print("\nTraceback Information")
    print("-" * 40)

    try:

        numbers = [1, 2, 3]

        print(
            numbers[10]
        )

    except IndexError:

        traceback_text = (
            traceback.format_exc()
        )

        print(
            traceback_text
        )


# =============================================================================
# SECTION 77 - Reusable Error Handler
# =============================================================================


def handle_exception(
    error: Exception,
    operation: str
) -> None:
    """
    Centralized exception handler.
    """

    logger = configure_logging()

    logger.error(
        f"Operation failed: "
        f"{operation} | "
        f"Error: {error}"
    )


# =============================================================================
# SECTION 78 - Centralized Error Handler Demo
# =============================================================================


def centralized_error_handler_demo() -> None:
    """
    Demonstrates centralized error handling.
    """

    print("\nCentralized Error Handler")
    print("-" * 40)

    try:

        data = {
            "hostname": "R1"
        }

        print(
            data["ip_address"]
        )

    except KeyError as error:

        handle_exception(
            error,
            "Reading device IP address"
        )


# =============================================================================
# SECTION 79 - Retry Mechanism
# =============================================================================


def retry_operation(
    operation: Callable[[], object],
    retries: int = 3,
    delay: float = 1.0
) -> object | None:
    """
    Executes an operation with retries.

    Args:
        operation:
            Function to execute.

        retries:
            Maximum number of attempts.

        delay:
            Delay between attempts.
    """

    logger = configure_logging()

    for attempt in range(
        1,
        retries + 1
    ):

        try:

            return operation()

        except Exception as error:

            logger.warning(
                f"Attempt "
                f"{attempt}/{retries} failed: "
                f"{error}"
            )

            if attempt < retries:

                time.sleep(
                    delay
                )

    logger.error(
        "All retry attempts failed."
    )

    return None


# =============================================================================
# SECTION 80 - Simulated Unstable Operation
# =============================================================================


class UnstableOperation:
    """
    Simulates an unreliable operation.
    """

    def __init__(
        self,
        failures_before_success: int
    ) -> None:

        self.failures_remaining = (
            failures_before_success
        )

    def execute(self) -> str:
        """
        Executes the simulated operation.
        """

        if self.failures_remaining > 0:

            self.failures_remaining -= 1

            raise ConnectionError(
                "Temporary connection failure."
            )

        return (
            "Operation completed successfully."
        )


# =============================================================================
# SECTION 81 - Retry Demo
# =============================================================================


def retry_demo() -> None:
    """
    Demonstrates retry logic.
    """

    print("\nRetry Mechanism")
    print("-" * 40)

    operation = (
        UnstableOperation(
            failures_before_success=2
        )
    )

    result = retry_operation(
        operation.execute,
        retries=4,
        delay=0.2
    )

    print(
        f"Result: {result}"
    )


# =============================================================================
# SECTION 82 - Network Retry
# =============================================================================


def network_retry_operation(
    hostname: str,
    ip_address: str
) -> str:
    """
    Simulates a network operation
    that may temporarily fail.
    """

    if not validate_ip(
        ip_address
    ):

        raise ValueError(
            f"Invalid IP address: "
            f"{ip_address}"
        )

    if ip_address.endswith(
        ".30"
    ):

        raise ConnectionError(
            f"Temporary connection "
            f"failure to {hostname}"
        )

    return (
        f"Connected to "
        f"{hostname} ({ip_address})"
    )


# =============================================================================
# SECTION 83 - Network Retry Demo
# =============================================================================


def network_retry_demo() -> None:
    """
    Demonstrates retrying network operations.
    """

    print("\nNetwork Retry")
    print("-" * 40)

    devices = [
        {
            "hostname": "R1",
            "ip_address": "192.168.10.1"
        },
        {
            "hostname": "R2",
            "ip_address": "192.168.10.2"
        },
        {
            "hostname": "R3",
            "ip_address": "192.168.10.30"
        }
    ]

    for device in devices:

        try:

            result = retry_operation(
                lambda: network_retry_operation(
                    device["hostname"],
                    device["ip_address"]
                ),
                retries=3,
                delay=0.2
            )

            print(
                f"{device['hostname']} "
                f"-> {result}"
            )

        except (
            ValueError,
            ConnectionError
        ) as error:

            print(
                f"{device['hostname']} "
                f"-> Failed: {error}"
            )


# =============================================================================
# SECTION 84 - Context Manager
# =============================================================================


def safe_file_context_demo() -> None:
    """
    Demonstrates safe file handling
    using a context manager.
    """

    print("\nSafe File Context Manager")
    print("-" * 40)

    file_path = Path(
        "device_output.txt"
    )

    try:

        with file_path.open(
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "Router R1\n"
            )

            file.write(
                "Status: Online\n"
            )

        print(
            "File written successfully."
        )

    except OSError as error:

        handle_exception(
            error,
            "Writing device output"
        )


# =============================================================================
# SECTION 85 - JSON Configuration Loader
# =============================================================================


def load_configuration(
    file_path: str
) -> dict:
    """
    Loads a JSON configuration safely.
    """

    try:

        path = Path(
            file_path
        )

        content = path.read_text(
            encoding="utf-8"
        )

        configuration = json.loads(
            content
        )

        if not isinstance(
            configuration,
            dict
        ):

            raise ConfigurationError(
                "Configuration must be "
                "a JSON object."
            )

        return configuration

    except FileNotFoundError as error:

        raise ConfigurationError(
            f"Configuration file not found: "
            f"{file_path}"
        ) from error

    except json.JSONDecodeError as error:

        raise ConfigurationError(
            f"Invalid JSON configuration: "
            f"{file_path}"
        ) from error

    except OSError as error:

        raise ConfigurationError(
            f"Unable to read configuration: "
            f"{file_path}"
        ) from error


# =============================================================================
# SECTION 86 - Configuration Loader Demo
# =============================================================================


def configuration_loader_demo() -> None:
    """
    Demonstrates professional configuration loading.
    """

    print("\nConfiguration Loader")
    print("-" * 40)

    configuration_file = Path(
        "network_config.json"
    )

    configuration_file.write_text(
        json.dumps(
            {
                "hostname": "R1",
                "ip_address": "192.168.10.1",
                "username": "admin",
                "port": 22,
                "protocol": "ssh"
            },
            indent=4
        ),
        encoding="utf-8"
    )

    try:

        configuration = (
            load_configuration(
                str(configuration_file)
            )
        )

        print(
            "Configuration loaded:"
        )

        for key, value in (
            configuration.items()
        ):

            print(
                f"  {key}: {value}"
            )

    except ConfigurationError as error:

        print(
            f"Configuration error: "
            f"{error}"
        )


# =============================================================================
# SECTION 87 - Error Classification
# =============================================================================


def classify_error(
    error: Exception
) -> str:
    """
    Classifies an exception by category.
    """

    if isinstance(
        error,
        DeviceConnectionError
    ):

        return "NETWORK"

    if isinstance(
        error,
        DeviceAuthenticationError
    ):

        return "AUTHENTICATION"

    if isinstance(
        error,
        ConfigurationError
    ):

        return "CONFIGURATION"

    if isinstance(
        error,
        SecurityValidationError
    ):

        return "SECURITY"

    if isinstance(
        error,
        FileNotFoundError
    ):

        return "FILE"

    if isinstance(
        error,
        ValueError
    ):

        return "VALIDATION"

    return "GENERAL"


# =============================================================================
# SECTION 88 - Error Classification Demo
# =============================================================================


def error_classification_demo() -> None:
    """
    Demonstrates exception classification.
    """

    print("\nError Classification")
    print("-" * 40)

    errors = [
        DeviceConnectionError(
            "Router unreachable."
        ),
        DeviceAuthenticationError(
            "Authentication failed."
        ),
        ConfigurationError(
            "Invalid configuration."
        ),
        SecurityValidationError(
            "Security policy violation."
        ),
        ValueError(
            "Invalid value."
        )
    ]

    for error in errors:

        category = classify_error(
            error
        )

        print(
            f"{type(error).__name__:<30}"
            f" -> {category}"
        )


# =============================================================================
# SECTION 89 - Safe Batch Automation
# =============================================================================


def run_device_task(
    device: dict[str, str]
) -> str:
    """
    Executes a simulated device task.
    """

    hostname = device[
        "hostname"
    ]

    ip_address = device[
        "ip_address"
    ]

    if not validate_ip(
        ip_address
    ):

        raise ValueError(
            f"Invalid IP: "
            f"{ip_address}"
        )

    if ip_address.endswith(
        ".40"
    ):

        raise DeviceConnectionError(
            f"Device {hostname} "
            f"is unreachable."
        )

    if ip_address.endswith(
        ".50"
    ):

        raise DeviceAuthenticationError(
            f"Authentication failed "
            f"for {hostname}."
        )

    return (
        f"Task completed on "
        f"{hostname}"
    )


# =============================================================================
# SECTION 90 - Safe Batch Automation Demo
# =============================================================================


def safe_batch_automation_demo() -> None:
    """
    Demonstrates professional batch processing.
    """

    print("\nSafe Batch Automation")
    print("-" * 40)

    logger = configure_logging()

    devices = [
        {
            "hostname": "R1",
            "ip_address": "192.168.10.1"
        },
        {
            "hostname": "R2",
            "ip_address": "192.168.10.40"
        },
        {
            "hostname": "R3",
            "ip_address": "192.168.10.50"
        },
        {
            "hostname": "R4",
            "ip_address": "300.1.1.1"
        }
    ]

    successful = 0
    failed = 0

    for device in devices:

        try:

            result = run_device_task(
                device
            )

            logger.info(
                result
            )

            successful += 1

        except Exception as error:

            failed += 1

            category = classify_error(
                error
            )

            logger.error(
                f"{device.get('hostname', 'Unknown')} "
                f"| Category: {category} "
                f"| Error: {error}"
            )

    print(
        f"\nSuccessful: {successful}"
    )

    print(
        f"Failed: {failed}"
    )


# =============================================================================
# SECTION 91 - Fail-Safe Operation
# =============================================================================


def fail_safe_operation(
    operation: Callable[[], object]
) -> object | None:
    """
    Executes an operation safely.

    The function never allows an unexpected
    exception to terminate the calling workflow.
    """

    try:

        return operation()

    except Exception as error:

        logger = configure_logging()

        logger.exception(
            f"Unexpected operation failure: "
            f"{error}"
        )

        return None


# =============================================================================
# SECTION 92 - Fail-Safe Demo
# =============================================================================


def fail_safe_demo() -> None:
    """
    Demonstrates fail-safe execution.
    """

    print("\nFail-Safe Operation")
    print("-" * 40)

    def unstable_function() -> str:

        raise RuntimeError(
            "Unexpected runtime failure."
        )

    result = fail_safe_operation(
        unstable_function
    )

    print(
        f"Returned value: {result}"
    )


# =============================================================================
# SECTION 93 - Error Statistics
# =============================================================================


def error_statistics_demo() -> None:
    """
    Demonstrates collecting error statistics.
    """

    print("\nError Statistics")
    print("-" * 40)

    errors = [
        DeviceConnectionError(
            "R1 unreachable"
        ),
        DeviceConnectionError(
            "R2 unreachable"
        ),
        ConfigurationError(
            "Invalid port"
        ),
        ValueError(
            "Invalid IP"
        ),
        DeviceConnectionError(
            "R3 unreachable"
        ),
        SecurityValidationError(
            "Weak password"
        )
    ]

    statistics = Counter(
        type(error).__name__
        for error in errors
    )

    for error_type, count in (
        statistics.items()
    ):

        print(
            f"{error_type:<35}"
            f" -> {count}"
        )


# =============================================================================
# SECTION 94 - Professional Error Workflow
# =============================================================================


def professional_error_workflow_demo() -> None:
    """
    Demonstrates a complete error handling workflow.
    """

    print("\nProfessional Error Workflow")
    print("-" * 40)

    logger = configure_logging()

    device = {
        "hostname": "R1",
        "ip_address": "192.168.10.1"
    }

    try:

        logger.info(
            "Starting device validation."
        )

        validate_hostname(
            device["hostname"]
        )

        if not validate_ip(
            device["ip_address"]
        ):

            raise ConfigurationError(
                "Invalid device IP."
            )

        logger.info(
            "Device validation successful."
        )

        logger.info(
            "Starting device operation."
        )

        result = run_device_task(
            device
        )

        logger.info(
            result
        )

    except ConfigurationError as error:

        logger.error(
            f"Configuration problem: "
            f"{error}"
        )

    except NetworkError as error:

        logger.error(
            f"Network problem: "
            f"{error}"
        )

    except Exception as error:

        logger.exception(
            f"Unexpected error: "
            f"{error}"
        )

    finally:

        logger.info(
            "Device workflow completed."
        )


# =============================================================================
# SECTION 95 - Part Four Runner
# =============================================================================


def run_part_four() -> None:
    """
    Runs Lesson 19 Part Four.
    """

    print("\n" + "=" * 70)
    print("LESSON 19 - EXCEPTION HANDLING")
    print("PART 4 - PROFESSIONAL ERROR HANDLING")
    print("=" * 70)

    logging_error_demo()

    logging_exception_demo()

    traceback_demo()

    centralized_error_handler_demo()

    retry_demo()

    network_retry_demo()

    safe_file_context_demo()

    configuration_loader_demo()

    error_classification_demo()

    safe_batch_automation_demo()

    fail_safe_demo()

    error_statistics_demo()

    professional_error_workflow_demo()


# =============================================================================
# END OF PART 4
# =============================================================================

# =============================================================================
# LESSON 19 - PART 5
# FINAL PROJECT
# NETWORK DEVICE ERROR HANDLING & MONITORING SYSTEM
# =============================================================================

"""
Part 5 - Final Project

This project combines the main concepts learned in Lesson 19:

    - try / except
    - else / finally
    - raise
    - Custom Exceptions
    - Exception Chaining
    - Input Validation
    - IP Validation
    - Configuration Validation
    - Logging
    - Retry Mechanisms
    - Error Classification
    - Safe Batch Processing
    - Error Statistics

Project Scenario
----------------

We simulate a small network automation system that:

    1. Loads network devices
    2. Validates device information
    3. Attempts connections
    4. Handles connection failures
    5. Handles authentication failures
    6. Retries temporary failures
    7. Logs errors
    8. Classifies errors
    9. Generates a final report
"""


# =============================================================================
# SECTION 96 - Network Monitoring System
# =============================================================================


class NetworkMonitoringSystem:
    """
    Network monitoring and error handling system.
    """

    def __init__(
        self,
        devices: list[dict[str, str]]
    ) -> None:

        self.devices = devices

        self.successful_devices: list[
            str
        ] = []

        self.failed_devices: list[
            str
        ] = []

        self.error_types: Counter = Counter()

        self.logger = configure_logging()


    # -------------------------------------------------------------------------
    # Validate Device
    # -------------------------------------------------------------------------

    def validate_device(
        self,
        device: dict[str, str]
    ) -> bool:
        """
        Validates a network device.
        """

        required_fields = [
            "hostname",
            "ip_address",
            "username"
        ]

        for field in required_fields:

            if field not in device:

                raise ConfigurationError(
                    f"Missing required field: "
                    f"{field}"
                )

        validate_hostname(
            device["hostname"]
        )

        if not validate_ip(
            device["ip_address"]
        ):

            raise ConfigurationError(
                f"Invalid IP address: "
                f"{device['ip_address']}"
            )

        if not device["username"]:

            raise DeviceAuthenticationError(
                "Username cannot be empty."
            )

        return True


    # -------------------------------------------------------------------------
    # Connect Device
    # -------------------------------------------------------------------------

    def connect_device(
        self,
        device: dict[str, str]
    ) -> str:
        """
        Simulates connecting to a device.
        """

        hostname = device["hostname"]

        ip_address = device["ip_address"]

        username = device["username"]

        return connect_device_secure(
            hostname,
            ip_address,
            username
        )


    # -------------------------------------------------------------------------
    # Monitor Device
    # -------------------------------------------------------------------------

    def monitor_device(
        self,
        device: dict[str, str]
    ) -> bool:
        """
        Validates and monitors one device.
        """

        hostname = device.get(
            "hostname",
            "Unknown"
        )

        try:

            self.logger.info(
                f"Starting monitoring for "
                f"{hostname}"
            )

            self.validate_device(
                device
            )

            result = retry_operation(
                lambda: self.connect_device(
                    device
                ),
                retries=3,
                delay=0.2
            )

            if result is None:

                raise DeviceConnectionError(
                    f"All connection attempts "
                    f"failed for {hostname}"
                )

            self.successful_devices.append(
                hostname
            )

            self.logger.info(
                f"{hostname} monitoring "
                f"completed successfully."
            )

            return True

        except (
            DeviceConnectionError,
            DeviceAuthenticationError,
            ConfigurationError,
            ValueError,
            TypeError,
            KeyError
        ) as error:

            self.failed_devices.append(
                hostname
            )

            error_type = type(
                error
            ).__name__

            self.error_types[
                error_type
            ] += 1

            category = classify_error(
                error
            )

            self.logger.error(
                f"{hostname} | "
                f"Category: {category} | "
                f"Error: {error}"
            )

            return False

        except Exception as error:

            self.failed_devices.append(
                hostname
            )

            self.error_types[
                type(error).__name__
            ] += 1

            self.logger.exception(
                f"Unexpected error while "
                f"monitoring {hostname}: "
                f"{error}"
            )

            return False

        finally:

            self.logger.info(
                f"Monitoring attempt finished "
                f"for {hostname}"
            )


    # -------------------------------------------------------------------------
    # Monitor All Devices
    # -------------------------------------------------------------------------

    def monitor_all_devices(
        self
    ) -> None:
        """
        Monitors all devices safely.
        """

        print(
            "\nStarting network monitoring..."
        )

        print(
            "-" * 60
        )

        for device in self.devices:

            self.monitor_device(
                device
            )


    # -------------------------------------------------------------------------
    # Generate Report
    # -------------------------------------------------------------------------

    def generate_report(
        self
    ) -> None:
        """
        Generates a final monitoring report.
        """

        total = len(
            self.devices
        )

        successful = len(
            self.successful_devices
        )

        failed = len(
            self.failed_devices
        )

        print(
            "\n" + "=" * 60
        )

        print(
            "NETWORK MONITORING REPORT"
        )

        print(
            "=" * 60
        )

        print(
            f"Total Devices     : {total}"
        )

        print(
            f"Successful        : {successful}"
        )

        print(
            f"Failed            : {failed}"
        )

        if total:

            success_rate = (
                successful / total
            ) * 100

        else:

            success_rate = 0

        print(
            f"Success Rate      : "
            f"{success_rate:.2f}%"
        )

        print(
            "-" * 60
        )

        print(
            "Successful Devices:"
        )

        if self.successful_devices:

            for hostname in (
                self.successful_devices
            ):

                print(
                    f"  [OK] {hostname}"
                )

        else:

            print(
                "  None"
            )

        print(
            "-" * 60
        )

        print(
            "Failed Devices:"
        )

        if self.failed_devices:

            for hostname in (
                self.failed_devices
            ):

                print(
                    f"  [FAILED] {hostname}"
                )

        else:

            print(
                "  None"
            )

        print(
            "-" * 60
        )

        print(
            "Error Statistics:"
        )

        if self.error_types:

            for error_type, count in (
                self.error_types.items()
            ):

                print(
                    f"  {error_type:<35}"
                    f"{count}"
                )

        else:

            print(
                "  No errors recorded."
            )


# =============================================================================
# SECTION 97 - Export Monitoring Report
# =============================================================================


def export_monitoring_report(
    system: NetworkMonitoringSystem,
    file_path: str
) -> None:
    """
    Exports monitoring results to JSON.
    """

    report = {
        "total_devices": len(
            system.devices
        ),
        "successful_devices": (
            system.successful_devices
        ),
        "failed_devices": (
            system.failed_devices
        ),
        "error_statistics": dict(
            system.error_types
        )
    }

    try:

        path = Path(
            file_path
        )

        path.write_text(
            json.dumps(
                report,
                indent=4
            ),
            encoding="utf-8"
        )

        print(
            f"\nReport exported to: "
            f"{file_path}"
        )

    except OSError as error:

        system.logger.error(
            f"Unable to export report: "
            f"{error}"
        )


# =============================================================================
# SECTION 98 - Final Project Demo
# =============================================================================


def final_project_demo() -> None:
    """
    Runs the complete Lesson 19 project.
    """

    print(
        "\n" + "#" * 70
    )

    print(
        "LESSON 19 FINAL PROJECT"
    )

    print(
        "NETWORK DEVICE ERROR HANDLING "
        "& MONITORING SYSTEM"
    )

    print(
        "#" * 70
    )

    devices = [
        {
            "hostname": "R1",
            "ip_address": "192.168.10.1",
            "username": "admin"
        },

        {
            "hostname": "R2",
            "ip_address": "192.168.10.2",
            "username": "admin"
        },

        {
            "hostname": "SW1",
            "ip_address": "192.168.10.10",
            "username": "admin"
        },

        {
            "hostname": "MT1",
            "ip_address": "192.168.10.20",
            "username": "admin"
        },

        {
            "hostname": "FW1",
            "ip_address": "192.168.10.30",
            "username": "admin"
        },

        {
            "hostname": "AUTH1",
            "ip_address": "192.168.10.40",
            "username": ""
        },

        {
            "hostname": "BAD-IP",
            "ip_address": "300.1.1.1",
            "username": "admin"
        },

        {
            "hostname": "MISSING"
        }
    ]

    monitoring_system = (
        NetworkMonitoringSystem(
            devices
        )
    )

    monitoring_system.monitor_all_devices()

    monitoring_system.generate_report()

    export_monitoring_report(
        monitoring_system,
        "network_monitoring_report.json"
    )


# =============================================================================
# SECTION 99 - Lesson 19 Summary
# =============================================================================


def lesson_19_summary() -> None:
    """
    Displays the concepts covered in Lesson 19.
    """

    print(
        "\n" + "=" * 70
    )

    print(
        "LESSON 19 SUMMARY"
    )

    print(
        "=" * 70
    )

    topics = [
        "try / except",
        "else / finally",
        "raise",
        "Built-in Exceptions",
        "Custom Exceptions",
        "Exception Inheritance",
        "Exception Chaining",
        "Input Validation",
        "Network Validation",
        "Configuration Validation",
        "Logging",
        "Traceback",
        "Retry Mechanisms",
        "Error Classification",
        "Safe Batch Processing",
        "Error Statistics",
        "Network Monitoring"
    ]

    for number, topic in enumerate(
        topics,
        start=1
    ):

        print(
            f"{number:02d}. {topic}"
        )


# =============================================================================
# SECTION 100 - Final Main
# =============================================================================


def main() -> None:
    """
    Main entry point for Lesson 19.
    """

    print(
        "\n" + "=" * 70
    )

    print(
        "PYTHON PROFESSIONAL ROADMAP"
    )

    print(
        "LESSON 19 - EXCEPTION HANDLING"
    )

    print(
        "=" * 70
    )

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
    # Part 5 - Final Project
    # -------------------------------------------------------------------------

    final_project_demo()

    # -------------------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------------------

    lesson_19_summary()

    print(
        "\n" + "=" * 70
    )

    print(
        "LESSON 19 COMPLETED SUCCESSFULLY"
    )

    print(
        "=" * 70
    )


# =============================================================================
# PROGRAM ENTRY POINT
# =============================================================================


if __name__ == "__main__":

    main()


# =============================================================================
# END OF LESSON 19
# =============================================================================
