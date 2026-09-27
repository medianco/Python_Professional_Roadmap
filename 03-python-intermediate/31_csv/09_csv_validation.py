"""
Lesson 31.9 - CSV Validation

This lesson demonstrates how to validate
a network device CSV inventory.

Network Engineering Context:
Before using an inventory for Network Automation,
we should verify that the data is complete and valid.

Validation includes:

- Required columns
- Empty values
- IP address format
- Device type
- Vendor
"""

# Import Python's built-in CSV module.
import csv

# Import ipaddress to validate IP addresses.
import ipaddress


# -------------------------------------------------------------
# File Path
# -------------------------------------------------------------

# Define the path to the network device inventory.
CSV_FILE = "data/network_devices.csv"


# -------------------------------------------------------------
# Expected CSV Fields
# -------------------------------------------------------------

# Define the fields that must exist in the CSV file.
REQUIRED_FIELDS = [
    "hostname",
    "management_ip",
    "device_type",
    "vendor",
]


# -------------------------------------------------------------
# Allowed Values
# -------------------------------------------------------------

# Define the supported device types.
ALLOWED_DEVICE_TYPES = {
    "router",
    "switch",
    "firewall",
}


# Define the supported vendors.
ALLOWED_VENDORS = {
    "Cisco",
    "Fortinet",
}


# -------------------------------------------------------------
# Validate IP Address
# -------------------------------------------------------------

def is_valid_ip(ip_address: str) -> bool:
    """
    Validate an IPv4 or IPv6 address.

    Args:
        ip_address: IP address as a string.

    Returns:
        True if the IP address is valid.
        False otherwise.
    """

    try:

        # ip_address() validates the actual IP address.
        ipaddress.ip_address(ip_address)

        return True

    except ValueError:

        # The value is not a valid IP address.
        return False


# -------------------------------------------------------------
# Validate Required Fields
# -------------------------------------------------------------

def validate_required_fields(fieldnames: list[str]) -> list[str]:
    """
    Check whether all required CSV fields exist.

    Args:
        fieldnames: CSV column names.

    Returns:
        List of missing fields.
    """

    # Find fields that are missing from the CSV header.
    missing_fields = [
        field
        for field in REQUIRED_FIELDS
        if field not in fieldnames
    ]

    return missing_fields


# -------------------------------------------------------------
# Validate Device
# -------------------------------------------------------------

def validate_device(
    device: dict,
    row_number: int,
) -> list[str]:
    """
    Validate one network device.

    Args:
        device: Network device dictionary.
        row_number: CSV row number.

    Returns:
        List of validation errors.
    """

    # Store validation errors.
    errors = []


    # ---------------------------------------------------------
    # Validate Empty Values
    # ---------------------------------------------------------

    # Check every required field.
    for field in REQUIRED_FIELDS:

        # Get the field value.
        value = device.get(field, "").strip()


        # Check whether the value is empty.
        if not value:

            errors.append(
                f"Row {row_number}: "
                f"{field} is empty"
            )


    # ---------------------------------------------------------
    # Validate IP Address
    # ---------------------------------------------------------

    # Get the management IP address.
    management_ip = device.get(
        "management_ip",
        ""
    ).strip()


    # Validate the IP only if it is not empty.
    if management_ip:

        if not is_valid_ip(management_ip):

            errors.append(
                f"Row {row_number}: "
                f"Invalid IP address: {management_ip}"
            )


    # ---------------------------------------------------------
    # Validate Device Type
    # ---------------------------------------------------------

    # Get the device type.
    device_type = device.get(
        "device_type",
        ""
    ).strip()


    # Check whether the device type is supported.
    if (
        device_type
        and device_type not in ALLOWED_DEVICE_TYPES
    ):

        errors.append(
            f"Row {row_number}: "
            f"Unsupported device type: {device_type}"
        )


    # ---------------------------------------------------------
    # Validate Vendor
    # ---------------------------------------------------------

    # Get the vendor name.
    vendor = device.get(
        "vendor",
        ""
    ).strip()


    # Check whether the vendor is supported.
    if (
        vendor
        and vendor not in ALLOWED_VENDORS
    ):

        errors.append(
            f"Row {row_number}: "
            f"Unsupported vendor: {vendor}"
        )


    # Return all errors found for this device.
    return errors


# -------------------------------------------------------------
# Main Validation Process
# -------------------------------------------------------------

print("=== CSV Inventory Validation ===")


# Open the CSV inventory.
with open(
    CSV_FILE,
    "r",
    encoding="utf-8",
    newline=""
) as file:

    # Create a DictReader.
    reader = csv.DictReader(file)


    # ---------------------------------------------------------
    # Validate CSV Header
    # ---------------------------------------------------------

    # Get the CSV field names.
    fieldnames = reader.fieldnames or []


    # Check for missing required fields.
    missing_fields = validate_required_fields(
        fieldnames
    )


    # If fields are missing, stop validation.
    if missing_fields:

        print("\nValidation Failed!")

        print(
            "Missing fields: "
            + ", ".join(missing_fields)
        )

    else:

        # -----------------------------------------------------
        # Validate Devices
        # -----------------------------------------------------

        all_errors = []

        # CSV data starts after the header.
        for row_number, device in enumerate(
            reader,
            start=2
        ):

            # Validate the current device.
            errors = validate_device(
                device,
                row_number
            )


            # Add errors to the global error list.
            all_errors.extend(errors)


        # -----------------------------------------------------
        # Display Validation Result
        # -----------------------------------------------------

        if all_errors:

            print("\nValidation Failed!")

            print("\n=== Errors ===")

            # Display every validation error.
            for error in all_errors:

                print(f"- {error}")

        else:

            print(
                "\nInventory validation successful."
            )

            print(
                "CSV inventory is ready "
                "for Network Automation."
            )
