"""
Lesson 31.4 - CSV DictReader

This lesson demonstrates how to use csv.DictReader()
to read CSV files using column names.

Network Engineering Context:
DictReader is very useful when working with network
device inventories because engineers can access data
using meaningful field names instead of column indexes.
"""

# Import Python's built-in CSV module.
import csv


# -------------------------------------------------------------
# File Path
# -------------------------------------------------------------

# Define the path to our network device inventory.
CSV_FILE = "data/network_devices.csv"


# -------------------------------------------------------------
# Open CSV File
# -------------------------------------------------------------

# Open the CSV file in read mode.
#
# "r"              -> Read mode
# encoding="utf-8" -> Use UTF-8 encoding
# newline=""       -> Recommended when working with CSV files
with open(CSV_FILE, "r", encoding="utf-8", newline="") as file:

    # Create a DictReader object.
    #
    # DictReader automatically uses the first row
    # of the CSV file as dictionary keys.
    reader = csv.DictReader(file)


    # ---------------------------------------------------------
    # Display CSV Field Names
    # ---------------------------------------------------------

    print("=== CSV Fields ===")

    # fieldnames contains the column names from the header.
    for field in reader.fieldnames:

        print(field)


    # ---------------------------------------------------------
    # Read Network Devices
    # ---------------------------------------------------------

    print("\n=== Network Devices ===")


    # Read each device from the CSV file.
    #
    # Each row is returned as a Python dictionary.
    for row in reader:

        # Access the device information using
        # the CSV column names instead of indexes.
        hostname = row["hostname"]
        management_ip = row["management_ip"]
        device_type = row["device_type"]
        vendor = row["vendor"]


        # Display the device information.
        print(
            f"Hostname: {hostname} | "
            f"IP: {management_ip} | "
            f"Type: {device_type} | "
            f"Vendor: {vendor}"
        )
