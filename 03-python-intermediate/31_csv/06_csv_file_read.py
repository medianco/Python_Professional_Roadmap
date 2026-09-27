"""
Lesson 31.6 - CSV File Read

This lesson demonstrates how to read a CSV file
and process its data using csv.DictReader().

Network Engineering Context:
Reading CSV files is common when working with
network device inventories, IP address lists,
VLAN information, and automation input data.

The data is stored separately from the Python logic.
"""

# Import Python's built-in CSV module.
import csv


# -------------------------------------------------------------
# File Path
# -------------------------------------------------------------

# Define the path to the network device inventory.
CSV_FILE = "data/network_devices.csv"


# -------------------------------------------------------------
# Open CSV File
# -------------------------------------------------------------

# Open the CSV file in read mode.
#
# "r"              -> Read mode
# encoding="utf-8" -> UTF-8 text encoding
# newline=""       -> Recommended for CSV files
with open(CSV_FILE, "r", encoding="utf-8", newline="") as file:

    # Create a DictReader object.
    #
    # DictReader uses the first row as column names
    # and converts every following row into a dictionary.
    reader = csv.DictReader(file)


    # ---------------------------------------------------------
    # Read All Devices
    # ---------------------------------------------------------

    print("=== Network Device Inventory ===")

    # Loop through every device in the CSV file.
    for device in reader:

        # Get the hostname from the current device.
        hostname = device["hostname"]

        # Get the management IP address.
        management_ip = device["management_ip"]

        # Get the device type.
        device_type = device["device_type"]

        # Get the vendor name.
        vendor = device["vendor"]


        # Display the device information.
        print(
            f"Hostname: {hostname} | "
            f"IP: {management_ip} | "
            f"Type: {device_type} | "
            f"Vendor: {vendor}"
        )
