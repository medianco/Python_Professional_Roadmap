"""
===============================================================================
File        : 18_file_handling.py
Author      : Mohammed AL-Dubai
Course      : Python Professional Roadmap
Stage       : Professional Python
Lesson      : File Handling
Part        : 1 - Reading Files

Description:
    Introduction to reading text files in Python.

Learning Objectives
-------------------
After completing Part 1, you will be able to:

✔ Understand file handling.
✔ Open a file safely.
✔ Read the complete content of a file.
✔ Read files line by line.
✔ Read a specific number of characters.
✔ Process file content.
✔ Handle basic file errors.
✔ Work with text encoding.

===============================================================================
"""


# =============================================================================
# SECTION 1 - Imports
# =============================================================================

from pathlib import Path


# =============================================================================
# SECTION 2 - File Handling Introduction
# =============================================================================


def file_handling_intro() -> None:
    """
    Introduces file handling concepts.
    """

    print("\nFile Handling")
    print("-" * 40)

    print("Python can work with:")
    print("✔ Text files")
    print("✔ Configuration files")
    print("✔ Log files")
    print("✔ CSV files")
    print("✔ JSON files")
    print("✔ Binary files")

    print("\nCommon operations:")
    print("✔ Read")
    print("✔ Write")
    print("✔ Append")
    print("✔ Update")


# =============================================================================
# SECTION 3 - Create Demo File
# =============================================================================


def create_demo_file() -> Path:
    """
    Creates a small text file for demonstration.

    Returns:
        Path: Path to the demo file.
    """

    file_path = Path("network_devices.txt")

    content = (
        "R1,192.168.10.1,Cisco,Router\n"
        "R2,192.168.10.2,Cisco,Router\n"
        "SW1,192.168.10.10,Cisco,Switch\n"
        "MT1,192.168.10.20,MikroTik,Router\n"
    )

    file_path.write_text(
        content,
        encoding="utf-8"
    )

    return file_path


# =============================================================================
# SECTION 4 - Open File
# =============================================================================


def open_file_demo(
    file_path: Path
) -> None:
    """
    Demonstrates opening a file using open().
    """

    print("\nOpening a File")
    print("-" * 40)

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        print(f"File opened successfully: {file.name}")


# =============================================================================
# SECTION 5 - Read Entire File
# =============================================================================


def read_entire_file(
    file_path: Path
) -> None:
    """
    Reads the complete content of a file.
    """

    print("\nRead Entire File")
    print("-" * 40)

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

    print(content)


# =============================================================================
# SECTION 6 - Read File Line by Line
# =============================================================================


def read_file_line_by_line(
    file_path: Path
) -> None:
    """
    Reads a file one line at a time.
    """

    print("\nRead File Line by Line")
    print("-" * 40)

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        for line_number, line in enumerate(
            file,
            start=1
        ):

            print(
                f"{line_number:02d}: "
                f"{line.strip()}"
            )


# =============================================================================
# SECTION 7 - readlines()
# =============================================================================


def readlines_demo(
    file_path: Path
) -> None:
    """
    Demonstrates readlines().
    """

    print("\nreadlines()")
    print("-" * 40)

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        lines = file.readlines()

    print(f"Total Lines: {len(lines)}")

    for line in lines:
        print(line.strip())


# =============================================================================
# SECTION 8 - readline()
# =============================================================================


def readline_demo(
    file_path: Path
) -> None:
    """
    Demonstrates readline().
    """

    print("\nreadline()")
    print("-" * 40)

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        first_line = file.readline()
        second_line = file.readline()

    print(f"First Line : {first_line.strip()}")
    print(f"Second Line: {second_line.strip()}")


# =============================================================================
# SECTION 9 - Read Specific Characters
# =============================================================================


def read_characters_demo(
    file_path: Path
) -> None:
    """
    Demonstrates reading a specific number
    of characters.
    """

    print("\nRead Specific Characters")
    print("-" * 40)

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read(20)

    print(f"First 20 Characters:")
    print(content)


# =============================================================================
# SECTION 10 - File Iteration
# =============================================================================


def file_iteration_demo(
    file_path: Path
) -> None:
    """
    Demonstrates iterating directly over a file.
    """

    print("\nFile Iteration")
    print("-" * 40)

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            if line.strip():
                print(
                    f"Device Entry: "
                    f"{line.strip()}"
                )


# =============================================================================
# SECTION 11 - Strip and Split
# =============================================================================


def strip_split_demo(
    file_path: Path
) -> None:
    """
    Demonstrates processing file lines
    using strip() and split().
    """

    print("\nstrip() and split()")
    print("-" * 40)

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            fields = line.split(",")

            print(
                f"Hostname : {fields[0]}"
            )

            print(
                f"IP       : {fields[1]}"
            )

            print(
                f"Vendor   : {fields[2]}"
            )

            print(
                f"Type     : {fields[3]}"
            )

            print("-" * 30)


# =============================================================================
# SECTION 12 - Search Inside a File
# =============================================================================


def search_file_demo(
    file_path: Path
) -> None:
    """
    Searches for a specific keyword
    inside a file.
    """

    print("\nSearch Inside File")
    print("-" * 40)

    keyword = "Cisco"

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        for line_number, line in enumerate(
            file,
            start=1
        ):

            if keyword.lower() in line.lower():

                print(
                    f"Found '{keyword}' "
                    f"at line {line_number}: "
                    f"{line.strip()}"
                )


# =============================================================================
# SECTION 13 - Count Lines
# =============================================================================


def count_file_lines(
    file_path: Path
) -> None:
    """
    Counts the number of lines in a file.
    """

    print("\nCount File Lines")
    print("-" * 40)

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        line_count = sum(
            1
            for _ in file
        )

    print(f"Total Lines: {line_count}")


# =============================================================================
# SECTION 14 - File Not Found Handling
# =============================================================================


def file_not_found_demo() -> None:
    """
    Demonstrates handling a missing file.
    """

    print("\nFileNotFoundError")
    print("-" * 40)

    missing_file = Path(
        "this_file_does_not_exist.txt"
    )

    try:

        with open(
            missing_file,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

            print(content)

    except FileNotFoundError:

        print(
            f"File not found: "
            f"{missing_file}"
        )


# =============================================================================
# SECTION 15 - Permission Error Handling
# =============================================================================


def permission_error_demo() -> None:
    """
    Demonstrates the concept of handling
    permission errors.
    """

    print("\nPermissionError")
    print("-" * 40)

    print(
        "PermissionError can occur when "
        "Python does not have permission "
        "to access a file."
    )

    print(
        "\nUse try/except when file access "
        "can fail."
    )


# =============================================================================
# SECTION 16 - File Encoding
# =============================================================================


def encoding_demo(
    file_path: Path
) -> None:
    """
    Demonstrates explicit UTF-8 encoding.
    """

    print("\nFile Encoding")
    print("-" * 40)

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

    print("File successfully read using UTF-8.")
    print(f"Characters: {len(content)}")


# =============================================================================
# SECTION 17 - File Object Information
# =============================================================================


def file_object_demo(
    file_path: Path
) -> None:
    """
    Displays information about a file object.
    """

    print("\nFile Object Information")
    print("-" * 40)

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        print(f"Name      : {file.name}")
        print(f"Mode      : {file.mode}")
        print(f"Encoding  : {file.encoding}")
        print(f"Closed    : {file.closed}")

    print(
        f"Closed After with: "
        f"{file.closed}"
    )


# =============================================================================
# SECTION 18 - Network Device Inventory
# =============================================================================


def network_inventory_reader(
    file_path: Path
) -> list[dict[str, str]]:
    """
    Reads network device information
    from a text file.

    Expected format:

        hostname,ip,vendor,type
    """

    devices: list[dict[str, str]] = []

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            fields = line.split(",")

            if len(fields) != 4:
                continue

            device = {
                "hostname": fields[0],
                "ip_address": fields[1],
                "vendor": fields[2],
                "device_type": fields[3]
            }

            devices.append(device)

    return devices


# =============================================================================
# SECTION 19 - Display Inventory
# =============================================================================


def display_network_inventory(
    devices: list[dict[str, str]]
) -> None:
    """
    Displays network inventory.
    """

    print("\nNetwork Inventory")
    print("-" * 40)

    for device in devices:

        print(
            f"{device['hostname']:<6} "
            f"{device['ip_address']:<16} "
            f"{device['vendor']:<10} "
            f"{device['device_type']}"
        )


# =============================================================================
# SECTION 20 - Part One Runner
# =============================================================================


def run_part_one() -> None:
    """
    Runs all demonstrations from Part One.
    """

    print("\n" + "=" * 70)
    print("LESSON 18 - FILE HANDLING")
    print("PART 1 - READING FILES")
    print("=" * 70)

    file_handling_intro()

    file_path = create_demo_file()

    open_file_demo(
        file_path
    )

    read_entire_file(
        file_path
    )

    read_file_line_by_line(
        file_path
    )

    readlines_demo(
        file_path
    )

    readline_demo(
        file_path
    )

    read_characters_demo(
        file_path
    )

    file_iteration_demo(
        file_path
    )

    strip_split_demo(
        file_path
    )

    search_file_demo(
        file_path
    )

    count_file_lines(
        file_path
    )

    file_not_found_demo()

    permission_error_demo()

    encoding_demo(
        file_path
    )

    file_object_demo(
        file_path
    )

    devices = network_inventory_reader(
        file_path
    )

    display_network_inventory(
        devices
    )


# =============================================================================
# END OF PART 1
# =============================================================================

# =============================================================================
# SECTION 21 - Writing Files
# =============================================================================

"""
Part 2 - Writing & Appending Files

In this part we learn:

✔ Write mode
✔ Append mode
✔ Writing strings
✔ Writing multiple lines
✔ writelines()
✔ Creating configuration files
✔ Creating log files
✔ Safe file writing
"""


# =============================================================================
# SECTION 22 - Write Mode
# =============================================================================


def write_mode_demo() -> None:
    """
    Demonstrates writing data to a file.

    Mode:
        w = write

    Important:
        Write mode creates a new file or overwrites
        an existing file.
    """

    print("\nWrite Mode")
    print("-" * 40)

    file_path = Path(
        "write_demo.txt"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "Python File Handling\n"
        )

        file.write(
            "Writing data to files\n"
        )

        file.write(
            "Network Automation\n"
        )

    print(
        f"File created: "
        f"{file_path}"
    )


# =============================================================================
# SECTION 23 - Read Written File
# =============================================================================


def read_written_file_demo() -> None:
    """
    Reads the file created by write_mode_demo().
    """

    print("\nRead Written File")
    print("-" * 40)

    file_path = Path(
        "write_demo.txt"
    )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

    print(content)


# =============================================================================
# SECTION 24 - Overwriting a File
# =============================================================================


def overwrite_file_demo() -> None:
    """
    Demonstrates that write mode overwrites
    existing file content.
    """

    print("\nOverwrite File")
    print("-" * 40)

    file_path = Path(
        "overwrite_demo.txt"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "Original configuration\n"
        )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "Updated configuration\n"
        )

    print(
        file_path.read_text(
            encoding="utf-8"
        )
    )


# =============================================================================
# SECTION 25 - Append Mode
# =============================================================================


def append_mode_demo() -> None:
    """
    Demonstrates append mode.

    Mode:
        a = append

    Append adds new data to the end
    of an existing file.
    """

    print("\nAppend Mode")
    print("-" * 40)

    file_path = Path(
        "append_demo.txt"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "First Entry\n"
        )

    with open(
        file_path,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            "Second Entry\n"
        )

        file.write(
            "Third Entry\n"
        )

    print(
        file_path.read_text(
            encoding="utf-8"
        )
    )


# =============================================================================
# SECTION 26 - writelines()
# =============================================================================


def writelines_demo() -> None:
    """
    Demonstrates writelines().
    """

    print("\nwritelines()")
    print("-" * 40)

    file_path = Path(
        "devices_writelines.txt"
    )

    devices = [
        "R1,192.168.10.1,Cisco\n",
        "R2,192.168.10.2,Cisco\n",
        "SW1,192.168.10.10,Cisco\n"
    ]

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.writelines(
            devices
        )

    print(
        file_path.read_text(
            encoding="utf-8"
        )
    )


# =============================================================================
# SECTION 27 - Writing Lists
# =============================================================================


def write_list_demo() -> None:
    """
    Demonstrates writing a list of strings
    to a file.
    """

    print("\nWriting a List")
    print("-" * 40)

    file_path = Path(
        "network_commands.txt"
    )

    commands = [
        "show version",
        "show ip interface brief",
        "show ip route",
        "show running-config"
    ]

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        for command in commands:

            file.write(
                command + "\n"
            )

    print(
        file_path.read_text(
            encoding="utf-8"
        )
    )


# =============================================================================
# SECTION 28 - Network Configuration File
# =============================================================================


def create_network_config() -> None:
    """
    Creates a simple network configuration file.
    """

    print("\nNetwork Configuration File")
    print("-" * 40)

    file_path = Path(
        "router_config.txt"
    )

    configuration = [
        "hostname R1",
        "interface GigabitEthernet0/0",
        "ip address 192.168.10.1 255.255.255.0",
        "no shutdown",
        "router ospf 1",
        "network 192.168.10.0 0.0.0.255 area 0"
    ]

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        for command in configuration:

            file.write(
                command + "\n"
            )

    print(
        file_path.read_text(
            encoding="utf-8"
        )
    )


# =============================================================================
# SECTION 29 - Append Network Configuration
# =============================================================================


def append_network_config() -> None:
    """
    Appends additional configuration commands.
    """

    print("\nAppend Network Configuration")
    print("-" * 40)

    file_path = Path(
        "router_config.txt"
    )

    additional_config = [
        "interface Loopback0",
        "ip address 10.10.10.1 255.255.255.255",
        "description Management Loopback"
    ]

    with open(
        file_path,
        "a",
        encoding="utf-8"
    ) as file:

        for command in additional_config:

            file.write(
                command + "\n"
            )

    print(
        file_path.read_text(
            encoding="utf-8"
        )
    )


# =============================================================================
# SECTION 30 - Network Log File
# =============================================================================


def create_network_log() -> None:
    """
    Creates a simple network log file.
    """

    print("\nNetwork Log File")
    print("-" * 40)

    file_path = Path(
        "network.log"
    )

    timestamp = datetime.now()

    log_entry = (
        f"{timestamp:%Y-%m-%d %H:%M:%S} "
        f"INFO Network monitoring started\n"
    )

    with open(
        file_path,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            log_entry
        )

    print(
        log_entry.strip()
    )


# =============================================================================
# SECTION 31 - Security Log File
# =============================================================================


def create_security_log() -> None:
    """
    Creates a simple cybersecurity log entry.
    """

    print("\nSecurity Log")
    print("-" * 40)

    file_path = Path(
        "security.log"
    )

    timestamp = datetime.now()

    log_entry = (
        f"{timestamp:%Y-%m-%d %H:%M:%S} "
        f"WARNING Failed login detected "
        f"from 192.168.10.50\n"
    )

    with open(
        file_path,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            log_entry
        )

    print(
        log_entry.strip()
    )


# =============================================================================
# SECTION 32 - Multiple Log Entries
# =============================================================================


def multiple_log_entries_demo() -> None:
    """
    Writes multiple log entries.
    """

    print("\nMultiple Log Entries")
    print("-" * 40)

    file_path = Path(
        "events.log"
    )

    events = [
        "INFO Device R1 is UP",
        "INFO Device R2 is UP",
        "WARNING Device SW1 has high CPU usage",
        "ERROR Device MT1 is unreachable"
    ]

    with open(
        file_path,
        "a",
        encoding="utf-8"
    ) as file:

        for event in events:

            timestamp = datetime.now()

            file.write(
                f"{timestamp:%Y-%m-%d %H:%M:%S} "
                f"{event}\n"
            )

    print(
        file_path.read_text(
            encoding="utf-8"
        )
    )


# =============================================================================
# SECTION 33 - Write JSON-Compatible Text
# =============================================================================


def write_json_demo() -> None:
    """
    Demonstrates writing structured data
    using JSON.
    """

    print("\nWrite JSON File")
    print("-" * 40)

    file_path = Path(
        "device.json"
    )

    device = {
        "hostname": "R1",
        "ip_address": "192.168.10.1",
        "vendor": "Cisco",
        "status": "UP"
    }

    json_data = json.dumps(
        device,
        indent=4
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            json_data
        )

    print(
        file_path.read_text(
            encoding="utf-8"
        )
    )


# =============================================================================
# SECTION 34 - Safe Write Function
# =============================================================================


def safe_write_file(
    file_path: Path,
    content: str
) -> bool:
    """
    Safely writes text to a file.

    Returns:
        bool: True if successful, False otherwise.
    """

    try:

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                content
            )

        return True

    except OSError as error:

        print(
            f"File write error: {error}"
        )

        return False


# =============================================================================
# SECTION 35 - Safe Write Demo
# =============================================================================


def safe_write_demo() -> None:
    """
    Demonstrates safe file writing.
    """

    print("\nSafe File Writing")
    print("-" * 40)

    file_path = Path(
        "safe_output.txt"
    )

    success = safe_write_file(
        file_path,
        "Safe file writing example.\n"
    )

    if success:

        print(
            f"Successfully wrote: "
            f"{file_path}"
        )

    else:

        print(
            "File writing failed."
        )


# =============================================================================
# SECTION 36 - File Size
# =============================================================================


def file_size_demo() -> None:
    """
    Demonstrates retrieving file size.
    """

    print("\nFile Size")
    print("-" * 40)

    file_path = Path(
        "network.log"
    )

    if file_path.exists():

        size = file_path.stat().st_size

        print(
            f"File: {file_path}"
        )

        print(
            f"Size: {size} bytes"
        )

    else:

        print(
            "File does not exist."
        )


# =============================================================================
# SECTION 37 - Configuration Backup
# =============================================================================


def configuration_backup_demo() -> None:
    """
    Demonstrates creating a simple
    configuration backup.
    """

    print("\nConfiguration Backup")
    print("-" * 40)

    source = Path(
        "router_config.txt"
    )

    backup = Path(
        "router_config_backup.txt"
    )

    if not source.exists():

        print(
            "Source configuration does not exist."
        )

        return

    content = source.read_text(
        encoding="utf-8"
    )

    backup.write_text(
        content,
        encoding="utf-8"
    )

    print(
        f"Backup created: "
        f"{backup}"
    )


# =============================================================================
# SECTION 38 - Part Two Runner
# =============================================================================


def run_part_two() -> None:
    """
    Runs all demonstrations from Part Two.
    """

    print("\n" + "=" * 70)
    print("LESSON 18 - FILE HANDLING")
    print("PART 2 - WRITING & APPENDING FILES")
    print("=" * 70)

    write_mode_demo()

    read_written_file_demo()

    overwrite_file_demo()

    append_mode_demo()

    writelines_demo()

    write_list_demo()

    create_network_config()

    append_network_config()

    create_network_log()

    create_security_log()

    multiple_log_entries_demo()

    write_json_demo()

    safe_write_demo()

    file_size_demo()

    configuration_backup_demo()


# =============================================================================
# END OF PART 2
# =============================================================================


# =============================================================================
# LESSON 18 - PART 3
# File Modes, pathlib, CSV and Structured Data
# =============================================================================

"""
Part 3 Objectives
-----------------

✔ Understand file modes
✔ Use pathlib for file operations
✔ Work with CSV files
✔ Read CSV files
✔ Write CSV files
✔ Filter CSV data
✔ Search CSV data
✔ Build network inventory from CSV
✔ Build security event data from CSV
✔ Understand text vs structured files
"""


# =============================================================================
# SECTION 39 - File Modes
# =============================================================================


def file_modes_demo() -> None:
    """
    Demonstrates common Python file modes.
    """

    print("\nFile Modes")
    print("-" * 40)

    modes = {
        "r": "Read existing file",
        "w": "Write and overwrite file",
        "a": "Append to file",
        "x": "Create a new file",
        "r+": "Read and write"
    }

    for mode, description in modes.items():

        print(
            f"{mode:<4} -> {description}"
        )


# =============================================================================
# SECTION 40 - pathlib Basics
# =============================================================================


def pathlib_basics_demo() -> None:
    """
    Demonstrates basic pathlib operations.
    """

    print("\npathlib Basics")
    print("-" * 40)

    current_directory = Path.cwd()

    print(
        f"Current Directory: "
        f"{current_directory}"
    )

    print(
        f"Directory Name: "
        f"{current_directory.name}"
    )

    print(
        f"Parent Directory: "
        f"{current_directory.parent}"
    )


# =============================================================================
# SECTION 41 - Create Directory
# =============================================================================


def create_demo_directory() -> Path:
    """
    Creates a directory for file-handling exercises.
    """

    print("\nCreate Directory")
    print("-" * 40)

    directory = Path(
        "file_lab"
    )

    directory.mkdir(
        exist_ok=True
    )

    print(
        f"Directory ready: "
        f"{directory}"
    )

    return directory


# =============================================================================
# SECTION 42 - Create File with pathlib
# =============================================================================


def pathlib_create_file(
    directory: Path
) -> Path:
    """
    Creates a file using pathlib.
    """

    print("\nCreate File with pathlib")
    print("-" * 40)

    file_path = directory / "example.txt"

    file_path.write_text(
        "Python File Handling\n"
        "Network Automation\n"
        "Cybersecurity\n",
        encoding="utf-8"
    )

    print(
        f"Created: {file_path}"
    )

    return file_path


# =============================================================================
# SECTION 43 - Read File with pathlib
# =============================================================================


def pathlib_read_file(
    file_path: Path
) -> None:
    """
    Reads a file using pathlib.
    """

    print("\nRead File with pathlib")
    print("-" * 40)

    content = file_path.read_text(
        encoding="utf-8"
    )

    print(content)


# =============================================================================
# SECTION 44 - File Information
# =============================================================================


def pathlib_file_information(
    file_path: Path
) -> None:
    """
    Displays file metadata.
    """

    print("\nFile Information")
    print("-" * 40)

    if not file_path.exists():

        print(
            "File does not exist."
        )

        return

    information = file_path.stat()

    print(
        f"Name      : "
        f"{file_path.name}"
    )

    print(
        f"Suffix    : "
        f"{file_path.suffix}"
    )

    print(
        f"Size      : "
        f"{information.st_size} bytes"
    )

    print(
        f"Absolute  : "
        f"{file_path.resolve()}"
    )


# =============================================================================
# SECTION 45 - List Files
# =============================================================================


def pathlib_list_files(
    directory: Path
) -> None:
    """
    Lists files inside a directory.
    """

    print("\nList Files")
    print("-" * 40)

    for item in directory.iterdir():

        if item.is_file():

            print(
                f"File: {item.name}"
            )


# =============================================================================
# SECTION 46 - CSV Introduction
# =============================================================================

import csv


def csv_introduction() -> None:
    """
    Introduces CSV files.
    """

    print("\nCSV Files")
    print("-" * 40)

    print(
        "CSV = Comma-Separated Values"
    )

    print(
        "\nCSV files are commonly used for:"
    )

    print("✔ Network inventory")
    print("✔ Asset lists")
    print("✔ User lists")
    print("✔ Security events")
    print("✔ Reports")
    print("✔ Data exchange")


# =============================================================================
# SECTION 47 - Create Network CSV
# =============================================================================


def create_network_csv(
    directory: Path
) -> Path:
    """
    Creates a CSV network inventory.
    """

    print("\nCreate Network CSV")
    print("-" * 40)

    csv_path = directory / "network_inventory.csv"

    devices = [
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

    fieldnames = [
        "hostname",
        "ip_address",
        "vendor",
        "device_type",
        "status"
    ]

    with open(
        csv_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(
            devices
        )

    print(
        f"CSV created: "
        f"{csv_path}"
    )

    return csv_path


# =============================================================================
# SECTION 48 - Read Network CSV
# =============================================================================


def read_network_csv(
    csv_path: Path
) -> list[dict[str, str]]:
    """
    Reads network inventory from CSV.
    """

    print("\nRead Network CSV")
    print("-" * 40)

    devices: list[dict[str, str]] = []

    with open(
        csv_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(
            file
        )

        for row in reader:

            devices.append(
                dict(row)
            )

    return devices


# =============================================================================
# SECTION 49 - Display CSV Inventory
# =============================================================================


def display_csv_inventory(
    devices: list[dict[str, str]]
) -> None:
    """
    Displays CSV inventory.
    """

    print("\nCSV Network Inventory")
    print("-" * 40)

    for device in devices:

        print(
            f"{device['hostname']:<6}"
            f"{device['ip_address']:<16}"
            f"{device['vendor']:<10}"
            f"{device['device_type']:<10}"
            f"{device['status']}"
        )


# =============================================================================
# SECTION 50 - Filter Active Devices
# =============================================================================


def filter_active_devices(
    devices: list[dict[str, str]]
) -> list[dict[str, str]]:
    """
    Returns only devices with UP status.
    """

    active_devices = [
        device
        for device in devices
        if device["status"] == "UP"
    ]

    return active_devices


# =============================================================================
# SECTION 51 - Filter Vendor
# =============================================================================


def filter_devices_by_vendor(
    devices: list[dict[str, str]],
    vendor: str
) -> list[dict[str, str]]:
    """
    Filters devices by vendor.
    """

    return [
        device
        for device in devices
        if device["vendor"].lower()
        == vendor.lower()
    ]


# =============================================================================
# SECTION 52 - Search Inventory
# =============================================================================


def search_inventory(
    devices: list[dict[str, str]],
    keyword: str
) -> list[dict[str, str]]:
    """
    Searches hostname, IP and vendor fields.
    """

    keyword = keyword.lower()

    results: list[dict[str, str]] = []

    for device in devices:

        searchable_text = " ".join(
            [
                device["hostname"],
                device["ip_address"],
                device["vendor"],
                device["device_type"]
            ]
        ).lower()

        if keyword in searchable_text:

            results.append(
                device
            )

    return results


# =============================================================================
# SECTION 53 - Save Filtered Inventory
# =============================================================================


def save_filtered_inventory(
    directory: Path,
    devices: list[dict[str, str]]
) -> Path:
    """
    Saves filtered devices into another CSV file.
    """

    output_path = (
        directory /
        "active_devices.csv"
    )

    if not devices:

        print(
            "No devices to save."
        )

        return output_path

    fieldnames = list(
        devices[0].keys()
    )

    with open(
        output_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(
            devices
        )

    print(
        f"Filtered inventory saved: "
        f"{output_path}"
    )

    return output_path


# =============================================================================
# SECTION 54 - Security Events CSV
# =============================================================================


def create_security_events_csv(
    directory: Path
) -> Path:
    """
    Creates a cybersecurity event CSV file.
    """

    print("\nSecurity Events CSV")
    print("-" * 40)

    csv_path = (
        directory /
        "security_events.csv"
    )

    events = [
        {
            "timestamp": "2026-08-01 10:00:00",
            "source_ip": "192.168.10.50",
            "event": "Failed Login",
            "severity": "HIGH"
        },
        {
            "timestamp": "2026-08-01 10:02:00",
            "source_ip": "192.168.10.51",
            "event": "Port Scan",
            "severity": "MEDIUM"
        },
        {
            "timestamp": "2026-08-01 10:05:00",
            "source_ip": "192.168.10.50",
            "event": "Failed Login",
            "severity": "HIGH"
        },
        {
            "timestamp": "2026-08-01 10:10:00",
            "source_ip": "10.10.10.50",
            "event": "Malware Detected",
            "severity": "CRITICAL"
        }
    ]

    fieldnames = [
        "timestamp",
        "source_ip",
        "event",
        "severity"
    ]

    with open(
        csv_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(
            events
        )

    print(
        f"Security CSV created: "
        f"{csv_path}"
    )

    return csv_path


# =============================================================================
# SECTION 55 - Read Security Events
# =============================================================================


def read_security_events(
    csv_path: Path
) -> list[dict[str, str]]:
    """
    Reads cybersecurity events.
    """

    events: list[dict[str, str]] = []

    with open(
        csv_path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(
            file
        )

        for row in reader:

            events.append(
                dict(row)
            )

    return events


# =============================================================================
# SECTION 56 - Filter Critical Events
# =============================================================================


def filter_critical_events(
    events: list[dict[str, str]]
) -> list[dict[str, str]]:
    """
    Returns HIGH and CRITICAL security events.
    """

    critical_levels = {
        "HIGH",
        "CRITICAL"
    }

    return [
        event
        for event in events
        if event["severity"] in critical_levels
    ]


# =============================================================================
# SECTION 57 - Security Event Statistics
# =============================================================================


def security_event_statistics(
    events: list[dict[str, str]]
) -> dict[str, int]:
    """
    Counts security events by severity.
    """

    statistics_result = Counter()

    for event in events:

        severity = event.get(
            "severity",
            "UNKNOWN"
        )

        statistics_result[
            severity
        ] += 1

    return dict(
        statistics_result
    )


# =============================================================================
# SECTION 58 - Display Security Statistics
# =============================================================================


def display_security_statistics(
    events: list[dict[str, str]]
) -> None:
    """
    Displays security event statistics.
    """

    print("\nSecurity Event Statistics")
    print("-" * 40)

    statistics_result = (
        security_event_statistics(
            events
        )
    )

    for severity, count in (
        statistics_result.items()
    ):

        print(
            f"{severity:<10} -> "
            f"{count}"
        )


# =============================================================================
# SECTION 59 - CSV to JSON
# =============================================================================


def csv_to_json_demo(
    directory: Path,
    devices: list[dict[str, str]]
) -> Path:
    """
    Converts CSV-style data into JSON.
    """

    print("\nCSV to JSON")
    print("-" * 40)

    json_path = (
        directory /
        "network_inventory.json"
    )

    json_path.write_text(
        json.dumps(
            devices,
            indent=4
        ),
        encoding="utf-8"
    )

    print(
        f"JSON file created: "
        f"{json_path}"
    )

    return json_path


# =============================================================================
# SECTION 60 - Part Three Runner
# =============================================================================


def run_part_three() -> None:
    """
    Runs all demonstrations from Part Three.
    """

    print("\n" + "=" * 70)
    print("LESSON 18 - FILE HANDLING")
    print("PART 3 - PATHLIB & CSV")
    print("=" * 70)

    file_modes_demo()

    pathlib_basics_demo()

    directory = create_demo_directory()

    example_file = pathlib_create_file(
        directory
    )

    pathlib_read_file(
        example_file
    )

    pathlib_file_information(
        example_file
    )

    pathlib_list_files(
        directory
    )

    csv_introduction()

    csv_path = create_network_csv(
        directory
    )

    devices = read_network_csv(
        csv_path
    )

    display_csv_inventory(
        devices
    )

    active_devices = filter_active_devices(
        devices
    )

    print(
        f"\nActive Devices: "
        f"{len(active_devices)}"
    )

    cisco_devices = filter_devices_by_vendor(
        devices,
        "Cisco"
    )

    print(
        f"Cisco Devices: "
        f"{len(cisco_devices)}"
    )

    search_results = search_inventory(
        devices,
        "192.168.10"
    )

    print(
        f"Search Results: "
        f"{len(search_results)}"
    )

    save_filtered_inventory(
        directory,
        active_devices
    )

    security_csv = create_security_events_csv(
        directory
    )

    security_events = read_security_events(
        security_csv
    )

    critical_events = filter_critical_events(
        security_events
    )

    print(
        f"\nHigh/Critical Events: "
        f"{len(critical_events)}"
    )

    display_security_statistics(
        security_events
    )

    csv_to_json_demo(
        directory,
        devices
    )


# =============================================================================
# END OF PART 3
# =============================================================================


# =============================================================================
# LESSON 18 - PART 4
# JSON, Logs, Configuration Files & File Processing
# =============================================================================

"""
Part 4 Objectives
-----------------

✔ Read JSON files
✔ Write JSON files
✔ Update JSON data
✔ Process network configuration files
✔ Search multiple files
✔ Analyze log files
✔ Filter security events
✔ Count log severity levels
✔ Create simple reports
✔ Work with directories
"""


# =============================================================================
# SECTION 61 - JSON File Creation
# =============================================================================


def create_json_inventory_file(
    directory: Path
) -> Path:
    """
    Creates a JSON network inventory file.
    """

    print("\nCreate JSON Inventory")
    print("-" * 40)

    json_path = (
        directory /
        "devices_inventory.json"
    )

    inventory = {
        "generated_by": "Python",
        "project": "Network Automation Lab",
        "devices": [
            {
                "hostname": "R1",
                "ip_address": "192.168.10.1",
                "vendor": "Cisco",
                "type": "Router",
                "status": "UP"
            },
            {
                "hostname": "R2",
                "ip_address": "192.168.10.2",
                "vendor": "Cisco",
                "type": "Router",
                "status": "UP"
            },
            {
                "hostname": "SW1",
                "ip_address": "192.168.10.10",
                "vendor": "Cisco",
                "type": "Switch",
                "status": "UP"
            }
        ]
    }

    json_path.write_text(
        json.dumps(
            inventory,
            indent=4
        ),
        encoding="utf-8"
    )

    print(
        f"JSON file created: "
        f"{json_path}"
    )

    return json_path


# =============================================================================
# SECTION 62 - Read JSON File
# =============================================================================


def read_json_inventory(
    json_path: Path
) -> dict[str, object]:
    """
    Reads JSON inventory from a file.
    """

    print("\nRead JSON Inventory")
    print("-" * 40)

    content = json_path.read_text(
        encoding="utf-8"
    )

    inventory = json.loads(
        content
    )

    print(
        f"Project: "
        f"{inventory['project']}"
    )

    return inventory


# =============================================================================
# SECTION 63 - Display JSON Devices
# =============================================================================


def display_json_devices(
    inventory: dict[str, object]
) -> None:
    """
    Displays devices stored in JSON.
    """

    print("\nJSON Devices")
    print("-" * 40)

    devices = inventory.get(
        "devices",
        []
    )

    if not isinstance(
        devices,
        list
    ):
        return

    for device in devices:

        if not isinstance(
            device,
            dict
        ):
            continue

        print(
            f"{device.get('hostname', 'N/A'):<6}"
            f"{device.get('ip_address', 'N/A'):<16}"
            f"{device.get('vendor', 'N/A'):<10}"
            f"{device.get('status', 'N/A')}"
        )


# =============================================================================
# SECTION 64 - Update JSON Inventory
# =============================================================================


def update_json_inventory(
    json_path: Path
) -> None:
    """
    Adds a new device to the JSON inventory.
    """

    print("\nUpdate JSON Inventory")
    print("-" * 40)

    inventory = json.loads(
        json_path.read_text(
            encoding="utf-8"
        )
    )

    devices = inventory.get(
        "devices",
        []
    )

    if isinstance(
        devices,
        list
    ):

        devices.append(
            {
                "hostname": "MT1",
                "ip_address": "192.168.10.20",
                "vendor": "MikroTik",
                "type": "Router",
                "status": "DOWN"
            }
        )

    json_path.write_text(
        json.dumps(
            inventory,
            indent=4
        ),
        encoding="utf-8"
    )

    print(
        "JSON inventory updated."
    )


# =============================================================================
# SECTION 65 - Configuration File
# =============================================================================


def create_configuration_file(
    directory: Path
) -> Path:
    """
    Creates a simple application configuration file.
    """

    print("\nConfiguration File")
    print("-" * 40)

    config_path = (
        directory /
        "network_tool.conf"
    )

    configuration = (
        "APP_NAME=NetworkToolkit\n"
        "LOG_LEVEL=INFO\n"
        "NETWORK=192.168.10.0/24\n"
        "TIMEOUT=5\n"
        "MAX_RETRIES=3\n"
    )

    config_path.write_text(
        configuration,
        encoding="utf-8"
    )

    print(
        f"Configuration created: "
        f"{config_path}"
    )

    return config_path


# =============================================================================
# SECTION 66 - Read Configuration
# =============================================================================


def read_configuration_file(
    config_path: Path
) -> dict[str, str]:
    """
    Reads KEY=VALUE configuration data.
    """

    print("\nRead Configuration")
    print("-" * 40)

    configuration: dict[str, str] = {}

    with open(
        config_path,
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            if "=" not in line:
                continue

            key, value = line.split(
                "=",
                maxsplit=1
            )

            configuration[
                key.strip()
            ] = value.strip()

    for key, value in configuration.items():

        print(
            f"{key:<15} = {value}"
        )

    return configuration


# =============================================================================
# SECTION 67 - Configuration Network Validation
# =============================================================================


def validate_configured_network(
    configuration: dict[str, str]
) -> None:
    """
    Validates the NETWORK configuration.
    """

    print("\nValidate Configured Network")
    print("-" * 40)

    network_value = configuration.get(
        "NETWORK"
    )

    if not network_value:

        print(
            "NETWORK setting not found."
        )

        return

    try:

        network = ipaddress.ip_network(
            network_value,
            strict=False
        )

        print(
            f"Network : {network}"
        )

        print(
            f"Prefix  : /{network.prefixlen}"
        )

        print(
            f"Hosts   : {network.num_addresses}"
        )

    except ValueError:

        print(
            f"Invalid network: "
            f"{network_value}"
        )


# =============================================================================
# SECTION 68 - Create Application Log
# =============================================================================


def create_application_log(
    directory: Path
) -> Path:
    """
    Creates an application log.
    """

    print("\nApplication Log")
    print("-" * 40)

    log_path = (
        directory /
        "application.log"
    )

    log_entries = [
        "INFO Application started",
        "INFO Loading network inventory",
        "INFO Connecting to devices",
        "WARNING Device MT1 is unreachable",
        "ERROR Connection failed to MT1",
        "INFO Application completed"
    ]

    with open(
        log_path,
        "w",
        encoding="utf-8"
    ) as file:

        for entry in log_entries:

            timestamp = datetime.now()

            file.write(
                f"{timestamp:%Y-%m-%d %H:%M:%S} "
                f"{entry}\n"
            )

    print(
        f"Log created: "
        f"{log_path}"
    )

    return log_path


# =============================================================================
# SECTION 69 - Read Log File
# =============================================================================


def read_log_file(
    log_path: Path
) -> list[str]:
    """
    Reads all log lines.
    """

    print("\nRead Log File")
    print("-" * 40)

    lines = log_path.read_text(
        encoding="utf-8"
    ).splitlines()

    for line in lines:

        print(line)

    return lines


# =============================================================================
# SECTION 70 - Count Log Levels
# =============================================================================


def count_log_levels(
    log_lines: list[str]
) -> dict[str, int]:
    """
    Counts INFO, WARNING and ERROR messages.
    """

    levels = Counter()

    for line in log_lines:

        for level in (
            "INFO",
            "WARNING",
            "ERROR",
            "CRITICAL"
        ):

            if f" {level} " in line:

                levels[level] += 1

                break

    return dict(levels)


# =============================================================================
# SECTION 71 - Display Log Statistics
# =============================================================================


def display_log_statistics(
    log_lines: list[str]
) -> None:
    """
    Displays log statistics.
    """

    print("\nLog Statistics")
    print("-" * 40)

    statistics_result = count_log_levels(
        log_lines
    )

    for level, count in (
        statistics_result.items()
    ):

        print(
            f"{level:<10} -> {count}"
        )


# =============================================================================
# SECTION 72 - Search Log Keyword
# =============================================================================


def search_log_keyword(
    log_path: Path,
    keyword: str
) -> list[str]:
    """
    Searches for a keyword in a log file.
    """

    print(
        f"\nSearch Log: {keyword}"
    )

    print("-" * 40)

    results: list[str] = []

    with open(
        log_path,
        "r",
        encoding="utf-8"
    ) as file:

        for line_number, line in enumerate(
            file,
            start=1
        ):

            if keyword.lower() in line.lower():

                result = (
                    f"Line {line_number}: "
                    f"{line.strip()}"
                )

                results.append(
                    result
                )

                print(result)

    return results


# =============================================================================
# SECTION 73 - Security Log Analyzer
# =============================================================================


def security_log_analyzer(
    log_path: Path
) -> dict[str, int]:
    """
    Analyzes security-related keywords.
    """

    print("\nSecurity Log Analyzer")
    print("-" * 40)

    keywords = {
        "failed": 0,
        "warning": 0,
        "error": 0,
        "critical": 0,
        "attack": 0,
        "unauthorized": 0
    }

    with open(
        log_path,
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            line_lower = line.lower()

            for keyword in keywords:

                if keyword in line_lower:

                    keywords[keyword] += 1

    for keyword, count in keywords.items():

        if count > 0:

            print(
                f"{keyword:<15} -> {count}"
            )

    return keywords


# =============================================================================
# SECTION 74 - Create Security Log
# =============================================================================


def create_security_analysis_log(
    directory: Path
) -> Path:
    """
    Creates a sample security log.
    """

    print("\nCreate Security Analysis Log")
    print("-" * 40)

    log_path = (
        directory /
        "security_analysis.log"
    )

    entries = [
        "INFO User authentication successful",
        "WARNING Multiple failed login attempts",
        "ERROR Unauthorized access attempt",
        "WARNING Port scan detected",
        "CRITICAL Malware detected",
        "INFO Security monitoring active"
    ]

    with open(
        log_path,
        "w",
        encoding="utf-8"
    ) as file:

        for entry in entries:

            timestamp = datetime.now()

            file.write(
                f"{timestamp:%Y-%m-%d %H:%M:%S} "
                f"{entry}\n"
            )

    return log_path


# =============================================================================
# SECTION 75 - Search All Files
# =============================================================================


def search_all_files(
    directory: Path,
    keyword: str
) -> None:
    """
    Searches text files in a directory.
    """

    print(
        f"\nSearch All Files: {keyword}"
    )

    print("-" * 40)

    for file_path in directory.iterdir():

        if not file_path.is_file():
            continue

        if file_path.suffix.lower() not in {
            ".txt",
            ".log",
            ".conf"
        }:
            continue

        try:

            content = file_path.read_text(
                encoding="utf-8"
            )

        except UnicodeDecodeError:

            continue

        if keyword.lower() in content.lower():

            print(
                f"Match found: "
                f"{file_path.name}"
            )


# =============================================================================
# SECTION 76 - Find Files by Extension
# =============================================================================


def find_files_by_extension(
    directory: Path,
    extension: str
) -> list[Path]:
    """
    Finds files with a specific extension.
    """

    print(
        f"\nFind *{extension} Files"
    )

    print("-" * 40)

    results: list[Path] = []

    for file_path in directory.iterdir():

        if (
            file_path.is_file()
            and file_path.suffix.lower()
            == extension.lower()
        ):

            results.append(
                file_path
            )

            print(
                file_path.name
            )

    return results


# =============================================================================
# SECTION 77 - Generate File Report
# =============================================================================


def generate_file_report(
    directory: Path
) -> dict[str, object]:
    """
    Generates a report about files in a directory.
    """

    files = [
        item
        for item in directory.iterdir()
        if item.is_file()
    ]

    total_size = sum(
        file.stat().st_size
        for file in files
    )

    extensions = Counter()

    for file in files:

        extension = (
            file.suffix.lower()
            or "[no extension]"
        )

        extensions[extension] += 1

    report: dict[str, object] = {
        "directory": str(
            directory.resolve()
        ),
        "total_files": len(files),
        "total_size_bytes": total_size,
        "extensions": dict(
            extensions
        )
    }

    return report


# =============================================================================
# SECTION 78 - Display File Report
# =============================================================================


def display_file_report(
    report: dict[str, object]
) -> None:
    """
    Displays a file report.
    """

    print("\nFile Report")
    print("-" * 40)

    print(
        f"Directory: "
        f"{report['directory']}"
    )

    print(
        f"Total Files: "
        f"{report['total_files']}"
    )

    print(
        f"Total Size: "
        f"{report['total_size_bytes']} bytes"
    )

    print(
        f"Extensions: "
        f"{report['extensions']}"
    )


# =============================================================================
# SECTION 79 - Save File Report
# =============================================================================


def save_file_report(
    directory: Path,
    report: dict[str, object]
) -> Path:
    """
    Saves the file report as JSON.
    """

    report_path = (
        directory /
        "file_report.json"
    )

    report_path.write_text(
        json.dumps(
            report,
            indent=4
        ),
        encoding="utf-8"
    )

    print(
        f"\nReport saved: "
        f"{report_path}"
    )

    return report_path


# =============================================================================
# SECTION 80 - Part Four Runner
# =============================================================================


def run_part_four() -> None:
    """
    Runs all demonstrations from Part Four.
    """

    print("\n" + "=" * 70)
    print("LESSON 18 - FILE HANDLING")
    print("PART 4 - JSON, LOGS & FILE PROCESSING")
    print("=" * 70)

    directory = Path(
        "file_lab"
    )

    directory.mkdir(
        exist_ok=True
    )

    # -------------------------------------------------------------------------
    # JSON
    # -------------------------------------------------------------------------

    json_path = create_json_inventory_file(
        directory
    )

    inventory = read_json_inventory(
        json_path
    )

    display_json_devices(
        inventory
    )

    update_json_inventory(
        json_path
    )

    # -------------------------------------------------------------------------
    # Configuration
    # -------------------------------------------------------------------------

    config_path = create_configuration_file(
        directory
    )

    configuration = read_configuration_file(
        config_path
    )

    validate_configured_network(
        configuration
    )

    # -------------------------------------------------------------------------
    # Application Logs
    # -------------------------------------------------------------------------

    application_log = create_application_log(
        directory
    )

    log_lines = read_log_file(
        application_log
    )

    display_log_statistics(
        log_lines
    )

    search_log_keyword(
        application_log,
        "ERROR"
    )

    # -------------------------------------------------------------------------
    # Security Logs
    # -------------------------------------------------------------------------

    security_log = create_security_analysis_log(
        directory
    )

    security_log_analyzer(
        security_log
    )

    search_log_keyword(
        security_log,
        "WARNING"
    )

    # -------------------------------------------------------------------------
    # File Searching
    # -------------------------------------------------------------------------

    search_all_files(
        directory,
        "Network"
    )

    find_files_by_extension(
        directory,
        ".log"
    )

    # -------------------------------------------------------------------------
    # File Report
    # -------------------------------------------------------------------------

    report = generate_file_report(
        directory
    )

    display_file_report(
        report
    )

    save_file_report(
        directory,
        report
    )


# =============================================================================
# END OF PART 4
# =============================================================================

# =============================================================================
# LESSON 18 - PART 5
# FINAL PROJECT - NETWORK FILE MANAGEMENT & ANALYZER
# =============================================================================

"""
Final Project
-------------

Network File Management & Analyzer

This project demonstrates:

✔ File handling
✔ pathlib
✔ CSV
✔ JSON
✔ Configuration files
✔ Log processing
✔ Network inventory
✔ Security event analysis
✔ File reports
✔ Configuration backups
✔ Error handling
✔ Modular Python design

Project Structure
-----------------

file_management_lab/
│
├── inventory/
├── configurations/
├── logs/
├── reports/
└── backups/
"""


# =============================================================================
# SECTION 81 - Project Directories
# =============================================================================


def create_project_directories() -> dict[str, Path]:
    """
    Creates the directory structure for the final project.
    """

    print("\nCreate Project Directories")
    print("-" * 40)

    base_directory = Path(
        "file_management_lab"
    )

    directories = {
        "base": base_directory,
        "inventory": base_directory / "inventory",
        "configurations": base_directory / "configurations",
        "logs": base_directory / "logs",
        "reports": base_directory / "reports",
        "backups": base_directory / "backups"
    }

    for directory in directories.values():

        directory.mkdir(
            parents=True,
            exist_ok=True
        )

    for name, directory in directories.items():

        print(
            f"{name:<15} -> {directory}"
        )

    return directories


# =============================================================================
# SECTION 82 - Create Network Inventory
# =============================================================================


def create_final_inventory(
    directories: dict[str, Path]
) -> Path:
    """
    Creates the final network inventory CSV.
    """

    print("\nCreate Final Network Inventory")
    print("-" * 40)

    inventory_path = (
        directories["inventory"]
        / "network_inventory.csv"
    )

    devices = [
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
            "hostname": "SW2",
            "ip_address": "192.168.10.11",
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

    fieldnames = [
        "hostname",
        "ip_address",
        "vendor",
        "device_type",
        "status"
    ]

    with open(
        inventory_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(devices)

    print(
        f"Inventory created: "
        f"{inventory_path}"
    )

    return inventory_path


# =============================================================================
# SECTION 83 - Load Inventory
# =============================================================================


def load_final_inventory(
    inventory_path: Path
) -> list[dict[str, str]]:
    """
    Loads the network inventory.
    """

    devices: list[dict[str, str]] = []

    try:

        with open(
            inventory_path,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(
                file
            )

            for row in reader:

                devices.append(
                    dict(row)
                )

    except FileNotFoundError:

        print(
            "Inventory file not found."
        )

    except OSError as error:

        print(
            f"Inventory read error: "
            f"{error}"
        )

    return devices


# =============================================================================
# SECTION 84 - Inventory Statistics
# =============================================================================


def inventory_statistics(
    devices: list[dict[str, str]]
) -> dict[str, object]:
    """
    Generates inventory statistics.
    """

    vendor_counter = Counter()
    type_counter = Counter()
    status_counter = Counter()

    for device in devices:

        vendor_counter[
            device.get(
                "vendor",
                "Unknown"
            )
        ] += 1

        type_counter[
            device.get(
                "device_type",
                "Unknown"
            )
        ] += 1

        status_counter[
            device.get(
                "status",
                "Unknown"
            )
        ] += 1

    return {
        "total_devices": len(devices),
        "vendors": dict(vendor_counter),
        "device_types": dict(type_counter),
        "statuses": dict(status_counter)
    }


# =============================================================================
# SECTION 85 - Display Inventory Statistics
# =============================================================================


def display_inventory_statistics(
    statistics_data: dict[str, object]
) -> None:
    """
    Displays inventory statistics.
    """

    print("\nInventory Statistics")
    print("-" * 40)

    print(
        f"Total Devices: "
        f"{statistics_data['total_devices']}"
    )

    print(
        f"Vendors: "
        f"{statistics_data['vendors']}"
    )

    print(
        f"Device Types: "
        f"{statistics_data['device_types']}"
    )

    print(
        f"Statuses: "
        f"{statistics_data['statuses']}"
    )


# =============================================================================
# SECTION 86 - Create Device Configurations
# =============================================================================


def create_device_configurations(
    directories: dict[str, Path]
) -> list[Path]:
    """
    Creates sample device configuration files.
    """

    print("\nCreate Device Configurations")
    print("-" * 40)

    configurations = {
        "R1": [
            "hostname R1",
            "interface GigabitEthernet0/0",
            "ip address 192.168.10.1 255.255.255.0",
            "no shutdown",
            "router ospf 1",
            "network 192.168.10.0 0.0.0.255 area 0"
        ],
        "R2": [
            "hostname R2",
            "interface GigabitEthernet0/0",
            "ip address 192.168.10.2 255.255.255.0",
            "no shutdown",
            "router ospf 1",
            "network 192.168.10.0 0.0.0.255 area 0"
        ],
        "SW1": [
            "hostname SW1",
            "interface GigabitEthernet0/1",
            "switchport mode trunk",
            "switchport trunk allowed vlan 10,20,30",
            "spanning-tree mode rapid-pvst"
        ]
    }

    created_files: list[Path] = []

    for hostname, commands in configurations.items():

        config_path = (
            directories["configurations"]
            / f"{hostname}.cfg"
        )

        with open(
            config_path,
            "w",
            encoding="utf-8"
        ) as file:

            for command in commands:

                file.write(
                    command + "\n"
                )

        created_files.append(
            config_path
        )

        print(
            f"Created: "
            f"{config_path.name}"
        )

    return created_files


# =============================================================================
# SECTION 87 - Configuration Analysis
# =============================================================================


def analyze_configuration(
    config_path: Path
) -> dict[str, object]:
    """
    Analyzes a network configuration file.
    """

    analysis = {
        "file": config_path.name,
        "hostname": None,
        "interfaces": 0,
        "ip_addresses": 0,
        "ospf": False,
        "vlans": [],
        "commands": 0
    }

    try:

        lines = config_path.read_text(
            encoding="utf-8"
        ).splitlines()

    except OSError as error:

        print(
            f"Configuration error: "
            f"{error}"
        )

        return analysis

    for line in lines:

        line = line.strip()

        if not line:
            continue

        analysis["commands"] += 1

        if line.startswith(
            "hostname "
        ):

            analysis["hostname"] = (
                line.split(
                    maxsplit=1
                )[1]
            )

        elif line.startswith(
            "interface "
        ):

            analysis["interfaces"] += 1

        elif line.startswith(
            "ip address "
        ):

            analysis["ip_addresses"] += 1

        elif line.startswith(
            "router ospf "
        ):

            analysis["ospf"] = True

        elif "vlan" in line.lower():

            vlan_numbers = [
                part
                for part in line.split()
                if part.isdigit()
            ]

            analysis["vlans"].extend(
                vlan_numbers
            )

    return analysis


# =============================================================================
# SECTION 88 - Configuration Report
# =============================================================================


def configuration_report(
    config_files: list[Path]
) -> list[dict[str, object]]:
    """
    Analyzes all configuration files.
    """

    print("\nConfiguration Analysis")
    print("-" * 40)

    results: list[dict[str, object]] = []

    for config_file in config_files:

        result = analyze_configuration(
            config_file
        )

        results.append(
            result
        )

        print(
            f"\nFile: "
            f"{result['file']}"
        )

        print(
            f"Hostname: "
            f"{result['hostname']}"
        )

        print(
            f"Interfaces: "
            f"{result['interfaces']}"
        )

        print(
            f"IP Addresses: "
            f"{result['ip_addresses']}"
        )

        print(
            f"OSPF: "
            f"{result['ospf']}"
        )

        print(
            f"VLANs: "
            f"{result['vlans']}"
        )

    return results


# =============================================================================
# SECTION 89 - Create Monitoring Log
# =============================================================================


def create_final_monitoring_log(
    directories: dict[str, Path]
) -> Path:
    """
    Creates a network monitoring log.
    """

    log_path = (
        directories["logs"]
        / "network_monitoring.log"
    )

    events = [
        "INFO R1 status UP",
        "INFO R2 status UP",
        "INFO SW1 status UP",
        "INFO SW2 status UP",
        "WARNING MT1 status DOWN",
        "ERROR Connection failed to MT1",
        "INFO Network monitoring completed"
    ]

    with open(
        log_path,
        "w",
        encoding="utf-8"
    ) as file:

        for event in events:

            timestamp = datetime.now()

            file.write(
                f"{timestamp:%Y-%m-%d %H:%M:%S} "
                f"{event}\n"
            )

    print(
        f"\nMonitoring log created: "
        f"{log_path}"
    )

    return log_path


# =============================================================================
# SECTION 90 - Analyze Monitoring Log
# =============================================================================


def analyze_monitoring_log(
    log_path: Path
) -> dict[str, object]:
    """
    Analyzes network monitoring events.
    """

    levels = Counter()
    down_devices: list[str] = []
    errors: list[str] = []

    try:

        lines = log_path.read_text(
            encoding="utf-8"
        ).splitlines()

    except OSError as error:

        print(
            f"Log error: {error}"
        )

        return {
            "levels": {},
            "down_devices": [],
            "errors": []
        }

    for line in lines:

        for level in (
            "INFO",
            "WARNING",
            "ERROR",
            "CRITICAL"
        ):

            if f" {level} " in line:

                levels[level] += 1

                break

        if "status DOWN" in line:

            parts = line.split()

            if len(parts) >= 5:

                down_devices.append(
                    parts[3]
                )

        if "ERROR" in line:

            errors.append(
                line
            )

    return {
        "levels": dict(levels),
        "down_devices": down_devices,
        "errors": errors
    }


# =============================================================================
# SECTION 91 - Security Events
# =============================================================================


def create_final_security_log(
    directories: dict[str, Path]
) -> Path:
    """
    Creates a security event log.
    """

    log_path = (
        directories["logs"]
        / "security_events.log"
    )

    events = [
        "INFO User authentication successful",
        "WARNING Failed login from 192.168.10.50",
        "WARNING Port scan detected from 192.168.10.51",
        "ERROR Unauthorized access attempt",
        "CRITICAL Malware detected on host 192.168.10.60",
        "INFO Security monitoring completed"
    ]

    with open(
        log_path,
        "w",
        encoding="utf-8"
    ) as file:

        for event in events:

            timestamp = datetime.now()

            file.write(
                f"{timestamp:%Y-%m-%d %H:%M:%S} "
                f"{event}\n"
            )

    print(
        f"Security log created: "
        f"{log_path}"
    )

    return log_path


# =============================================================================
# SECTION 92 - Analyze Security Log
# =============================================================================


def analyze_security_log(
    log_path: Path
) -> dict[str, object]:
    """
    Analyzes security log events.
    """

    result = {
        "total_events": 0,
        "severity": {},
        "failed_logins": 0,
        "port_scans": 0,
        "unauthorized_access": 0,
        "malware_events": 0
    }

    try:

        lines = log_path.read_text(
            encoding="utf-8"
        ).splitlines()

    except OSError as error:

        print(
            f"Security log error: "
            f"{error}"
        )

        return result

    severity_counter = Counter()

    for line in lines:

        result["total_events"] += 1

        line_upper = line.upper()

        for level in (
            "INFO",
            "WARNING",
            "ERROR",
            "CRITICAL"
        ):

            if f" {level} " in line_upper:

                severity_counter[level] += 1

                break

        line_lower = line.lower()

        if "failed login" in line_lower:

            result["failed_logins"] += 1

        if "port scan" in line_lower:

            result["port_scans"] += 1

        if "unauthorized access" in line_lower:

            result["unauthorized_access"] += 1

        if "malware" in line_lower:

            result["malware_events"] += 1

    result["severity"] = dict(
        severity_counter
    )

    return result


# =============================================================================
# SECTION 93 - Save JSON Report
# =============================================================================


def save_final_report(
    directories: dict[str, Path],
    report: dict[str, object]
) -> Path:
    """
    Saves the final project report as JSON.
    """

    report_path = (
        directories["reports"]
        / "final_report.json"
    )

    report_path.write_text(
        json.dumps(
            report,
            indent=4
        ),
        encoding="utf-8"
    )

    print(
        f"\nFinal report saved: "
        f"{report_path}"
    )

    return report_path


# =============================================================================
# SECTION 94 - Configuration Backup
# =============================================================================


def backup_configurations(
    directories: dict[str, Path],
    config_files: list[Path]
) -> None:
    """
    Creates backups of configuration files.
    """

    print("\nConfiguration Backups")
    print("-" * 40)

    for config_file in config_files:

        backup_file = (
            directories["backups"]
            / f"{config_file.stem}_backup.cfg"
        )

        try:

            content = config_file.read_text(
                encoding="utf-8"
            )

            backup_file.write_text(
                content,
                encoding="utf-8"
            )

            print(
                f"Backup created: "
                f"{backup_file.name}"
            )

        except OSError as error:

            print(
                f"Backup failed for "
                f"{config_file.name}: "
                f"{error}"
            )


# =============================================================================
# SECTION 95 - Final Project Summary
# =============================================================================


def display_final_project_summary(
    report: dict[str, object]
) -> None:
    """
    Displays the final project summary.
    """

    print("\n" + "=" * 70)
    print("FINAL PROJECT SUMMARY")
    print("=" * 70)

    print(
        f"Total Devices: "
        f"{report['inventory']['total_devices']}"
    )

    print(
        f"Configurations: "
        f"{len(report['configurations'])}"
    )

    monitoring = report[
        "monitoring"
    ]

    print(
        f"Monitoring Levels: "
        f"{monitoring['levels']}"
    )

    print(
        f"Down Devices: "
        f"{monitoring['down_devices']}"
    )

    security = report[
        "security"
    ]

    print(
        f"Security Events: "
        f"{security['total_events']}"
    )

    print(
        f"Failed Logins: "
        f"{security['failed_logins']}"
    )

    print(
        f"Port Scans: "
        f"{security['port_scans']}"
    )

    print(
        f"Malware Events: "
        f"{security['malware_events']}"
    )


# =============================================================================
# SECTION 96 - FINAL PROJECT RUNNER
# =============================================================================


def run_final_project() -> None:
    """
    Runs the complete Lesson 18 final project.
    """

    print("\n" + "=" * 70)
    print("LESSON 18 - FINAL PROJECT")
    print("NETWORK FILE MANAGEMENT & ANALYZER")
    print("=" * 70)

    # -------------------------------------------------------------------------
    # 1. Create project directories
    # -------------------------------------------------------------------------

    directories = (
        create_project_directories()
    )

    # -------------------------------------------------------------------------
    # 2. Network inventory
    # -------------------------------------------------------------------------

    inventory_path = (
        create_final_inventory(
            directories
        )
    )

    devices = load_final_inventory(
        inventory_path
    )

    inventory_data = (
        inventory_statistics(
            devices
        )
    )

    display_inventory_statistics(
        inventory_data
    )

    # -------------------------------------------------------------------------
    # 3. Device configurations
    # -------------------------------------------------------------------------

    config_files = (
        create_device_configurations(
            directories
        )
    )

    configuration_data = (
        configuration_report(
            config_files
        )
    )

    # -------------------------------------------------------------------------
    # 4. Network monitoring
    # -------------------------------------------------------------------------

    monitoring_log = (
        create_final_monitoring_log(
            directories
        )
    )

    monitoring_data = (
        analyze_monitoring_log(
            monitoring_log
        )
    )

    # -------------------------------------------------------------------------
    # 5. Security monitoring
    # -------------------------------------------------------------------------

    security_log = (
        create_final_security_log(
            directories
        )
    )

    security_data = (
        analyze_security_log(
            security_log
        )
    )

    # -------------------------------------------------------------------------
    # 6. Configuration backups
    # -------------------------------------------------------------------------

    backup_configurations(
        directories,
        config_files
    )

    # -------------------------------------------------------------------------
    # 7. Final report
    # -------------------------------------------------------------------------

    final_report: dict[str, object] = {
        "project": (
            "Network File Management & Analyzer"
        ),
        "lesson": "18 - File Handling",
        "inventory": inventory_data,
        "configurations": configuration_data,
        "monitoring": monitoring_data,
        "security": security_data,
        "generated_at": (
            datetime.now().isoformat(
                timespec="seconds"
            )
        )
    }

    save_final_report(
        directories,
        final_report
    )

    display_final_project_summary(
        final_report
    )


# =============================================================================
# SECTION 97 - MAIN
# =============================================================================


def main() -> None:
    """
    Main program entry point.
    """

    print("\n" + "=" * 70)
    print("PYTHON PROFESSIONAL ROADMAP")
    print("LESSON 18 - FILE HANDLING")
    print("=" * 70)

    print("\nSelect an option:")

    print("1. Run Part 1 - Reading Files")
    print("2. Run Part 2 - Writing & Appending")
    print("3. Run Part 3 - pathlib & CSV")
    print("4. Run Part 4 - JSON, Logs & Processing")
    print("5. Run Part 5 - Final Project")
    print("6. Run Complete Lesson")

    choice = input(
        "\nEnter your choice: "
    ).strip()

    if choice == "1":

        run_part_one()

    elif choice == "2":

        run_part_two()

    elif choice == "3":

        run_part_three()

    elif choice == "4":

        run_part_four()

    elif choice == "5":

        run_final_project()

    elif choice == "6":

        run_part_one()

        run_part_two()

        run_part_three()

        run_part_four()

        run_final_project()

    else:

        print(
            "\nInvalid choice."
        )


# =============================================================================
# PROGRAM ENTRY POINT
# =============================================================================


if __name__ == "__main__":

    main()


# =============================================================================
# END OF LESSON 18
# =============================================================================
