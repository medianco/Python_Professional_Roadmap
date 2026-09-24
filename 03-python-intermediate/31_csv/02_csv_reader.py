"""
Lesson 31.2 - CSV Reader

This lesson demonstrates how to use csv.reader()
to read CSV files correctly.

Network Engineering Context:
csv.reader() is commonly used to read network inventories,
IP address lists, VLAN information, and device data.
"""

# Import Python's built-in CSV module.
# The csv module provides tools for reading and writing CSV files.
import csv


# -------------------------------------------------------------
# File Path
# -------------------------------------------------------------

# Define the path to our CSV inventory file.
# The actual network device data is stored separately
# from the Python code.
CSV_FILE = "data/network_devices.csv"


# -------------------------------------------------------------
# Open CSV File
# -------------------------------------------------------------

# Open the CSV file in read mode.
#
# "r"             -> Read mode
# encoding="utf-8" -> Correctly handle text characters
# newline=""       -> Recommended when working with CSV files
with open(CSV_FILE, "r", encoding="utf-8", newline="") as file:

    # Create a CSV reader object.
    #
    # csv.reader() reads the CSV file row by row
    # and converts each row into a Python list.
    reader = csv.reader(file)


    # ---------------------------------------------------------
    # Read Header
    # ---------------------------------------------------------

    # next(reader) reads the first row from the CSV file.
    #
    # In our inventory, the first row contains the column names:
    #
    # hostname, management_ip, device_type, vendor
    #
    # The result is stored as a Python list.
    header = next(reader)


    # Display the CSV header.
    print("=== CSV Header ===")


    # Loop through each column name in the header.
    for column in header:

        # Display the column name.
        print(column)


    # ---------------------------------------------------------
    # Read Network Devices
    # ---------------------------------------------------------

    print("\n=== Network Devices ===")


    # Continue reading the remaining rows.
    #
    # Each row represents one network device.
    for row in reader:

        # The first column contains the device hostname.
        hostname = row[0]

        # The second column contains the management IP address.
        management_ip = row[1]

        # The third column contains the device type.
        device_type = row[2]

        # The fourth column contains the vendor name.
        vendor = row[3]


        # Display the information of the current device.
        print(
            f"Hostname: {hostname} | "
            f"IP: {management_ip} | "
            f"Type: {device_type} | "
            f"Vendor: {vendor}"
        )
