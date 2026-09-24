"""
Lesson 31.5 - CSV DictWriter

This lesson demonstrates how to use csv.DictWriter()
to write Python dictionaries into a CSV file.

Network Engineering Context:
The network device data is stored separately in a JSON file.
Python reads the JSON data and converts it into a CSV file.

This demonstrates the integration between:
JSON -> Python -> CSV

This approach keeps DATA separate from LOGIC.
"""

# Import the built-in CSV module.
import csv

# Import the built-in JSON module.
# We learned json.load() in Lesson 30.
import json


# -------------------------------------------------------------
# File Paths
# -------------------------------------------------------------

# Source JSON file containing the network device inventory.
JSON_FILE = "data/devices.json"

# Destination CSV file that will be generated.
CSV_FILE = "data/generated_devices_dict.csv"


# -------------------------------------------------------------
# Read JSON Data
# -------------------------------------------------------------

# Open the JSON inventory file in read mode.
with open(JSON_FILE, "r", encoding="utf-8") as file:

    # Convert the JSON file into a Python dictionary.
    #
    # This is the same json.load() concept
    # that we learned in Lesson 30.
    inventory = json.load(file)


# -------------------------------------------------------------
# Extract Network Devices
# -------------------------------------------------------------

# Access the "devices" list inside the JSON dictionary.
#
# inventory["devices"] contains a list of dictionaries.
devices = inventory["devices"]


# -------------------------------------------------------------
# CSV Field Names
# -------------------------------------------------------------

# Define the CSV column names.
#
# These names will become the CSV header.
fieldnames = [
    "hostname",
    "management_ip",
    "device_type",
    "vendor",
]


# -------------------------------------------------------------
# Open CSV Output File
# -------------------------------------------------------------

# Open the CSV file in write mode.
#
# "w"              -> Write mode
# encoding="utf-8" -> UTF-8 encoding
# newline=""       -> Recommended for CSV files
with open(CSV_FILE, "w", encoding="utf-8", newline="") as file:

    # Create a DictWriter object.
    #
    # DictWriter converts Python dictionaries
    # into CSV rows.
    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames,
    )


    # ---------------------------------------------------------
    # Write CSV Header
    # ---------------------------------------------------------

    # Write the field names as the first row.
    writer.writeheader()


    # ---------------------------------------------------------
    # Write Network Devices
    # ---------------------------------------------------------

    # Loop through every device dictionary.
    for device in devices:

        # Write the dictionary as one CSV row.
        writer.writerow(device)


# -------------------------------------------------------------
# Confirmation
# -------------------------------------------------------------

# Display a message confirming that the conversion is complete.
print("CSV file created successfully.")

print(f"Source: {JSON_FILE}")
print(f"Output: {CSV_FILE}")

print(f"Total Devices: {len(devices)}")
