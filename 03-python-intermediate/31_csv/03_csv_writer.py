"""
Lesson 31.3 - CSV Writer

This lesson demonstrates how to create and write
data into a CSV file using csv.writer().

Network Engineering Context:
Network engineers can use csv.writer() to generate
device inventories, IP lists, VLAN reports, and
automation input files.
"""

# Import Python's built-in CSV module.
import csv


# -------------------------------------------------------------
# Output File
# -------------------------------------------------------------

# Define the path where the new CSV file will be created.
CSV_FILE = "data/generated_devices.csv"


# -------------------------------------------------------------
# Network Device Data
# -------------------------------------------------------------

# Store network device information as Python lists.
#
# Each inner list represents one row in the CSV file.
devices = [
    ["R1", "192.168.1.1", "router", "Cisco"],
    ["R2", "192.168.1.2", "router", "Cisco"],
    ["SW1", "192.168.1.10", "switch", "Cisco"],
    ["FW1", "192.168.1.254", "firewall", "Fortinet"],
]


# -------------------------------------------------------------
# Write Data to CSV File
# -------------------------------------------------------------

# Open the output file in write mode.
#
# "w"              -> Write mode
# encoding="utf-8" -> Use UTF-8 encoding
# newline=""       -> Recommended for CSV files
with open(CSV_FILE, "w", encoding="utf-8", newline="") as file:

    # Create a CSV writer object.
    #
    # csv.writer() allows us to write Python data
    # into CSV format.
    writer = csv.writer(file)


    # ---------------------------------------------------------
    # Write Header
    # ---------------------------------------------------------

    # Write the column names as the first row.
    writer.writerow(
        [
            "hostname",
            "management_ip",
            "device_type",
            "vendor",
        ]
    )


    # ---------------------------------------------------------
    # Write Network Devices
    # ---------------------------------------------------------

    # Write each network device as a separate CSV row.
    for device in devices:

        writer.writerow(device)


# -------------------------------------------------------------
# Confirmation
# -------------------------------------------------------------

# Display a confirmation message after the file is created.
print(f"CSV file created successfully: {CSV_FILE}")
