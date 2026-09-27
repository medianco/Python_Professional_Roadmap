"""
Lesson 31.8 - CSV & Network Automation

This lesson demonstrates how to use CSV data
as input for Network Automation.

Network Engineering Context:
A CSV inventory can contain the information required
to build automation targets for tools such as:

- Netmiko
- Nornir
- Network APIs

In this lesson we will:

1. Read the CSV inventory.
2. Select the devices required for automation.
3. Build automation targets.
4. Display the prepared targets.

No real network connection is performed in this lesson.
"""


# Import Python's built-in CSV module.
import csv


# -------------------------------------------------------------
# File Path
# -------------------------------------------------------------

# Define the path to the network device inventory.
CSV_FILE = "data/network_devices.csv"


# -------------------------------------------------------------
# Load Network Inventory
# -------------------------------------------------------------

def load_inventory(filename: str) -> list[dict]:
    """
    Read the CSV inventory and return network devices.

    Args:
        filename: Path to the CSV inventory file.

    Returns:
        A list containing network device dictionaries.
    """

    # Create an empty list to store devices.
    devices = []


    # Open the CSV inventory file.
    with open(
        filename,
        "r",
        encoding="utf-8",
        newline=""
    ) as file:

        # Create a DictReader.
        #
        # Each CSV row becomes a dictionary.
        reader = csv.DictReader(file)


        # Read every device.
        for device in reader:

            # Add the device dictionary to the list.
            devices.append(device)


    # Return the complete inventory.
    return devices


# -------------------------------------------------------------
# Prepare Automation Targets
# -------------------------------------------------------------

def prepare_automation_targets(
    devices: list[dict],
) -> list[dict]:
    """
    Prepare network devices for automation.

    Only Cisco devices are selected in this example.

    Args:
        devices: List of network device dictionaries.

    Returns:
        List of automation target dictionaries.
    """

    # Create an empty list for automation targets.
    targets = []


    # Process every device.
    for device in devices:

        # Select only Cisco devices.
        if device["vendor"] != "Cisco":
            continue


        # Create a simplified automation target.
        target = {
            "hostname": device["hostname"],
            "ip": device["management_ip"],
            "device_type": device["device_type"],
            "vendor": device["vendor"],
        }


        # Add the target to the list.
        targets.append(target)


    # Return the prepared targets.
    return targets


# -------------------------------------------------------------
# Display Automation Targets
# -------------------------------------------------------------

def display_targets(targets: list[dict]) -> None:
    """
    Display prepared automation targets.
    """

    print("=== Automation Targets ===")


    # Display every automation target.
    for target in targets:

        print(
            f"Hostname: {target['hostname']} | "
            f"IP: {target['ip']} | "
            f"Type: {target['device_type']} | "
            f"Vendor: {target['vendor']}"
        )


# -------------------------------------------------------------
# Main Program
# -------------------------------------------------------------

# Load devices from the CSV inventory.
devices = load_inventory(CSV_FILE)


# Prepare devices for automation.
automation_targets = prepare_automation_targets(devices)


# Display the prepared automation targets.
display_targets(automation_targets)


# -------------------------------------------------------------
# Statistics
# -------------------------------------------------------------

print("\n=== Automation Statistics ===")

print(f"Inventory Devices: {len(devices)}")

print(
    f"Automation Targets: "
    f"{len(automation_targets)}"
)
