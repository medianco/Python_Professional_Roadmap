"""
Lesson 31.1 - CSV Basics

This lesson introduces the basic structure of CSV data.

Network Engineering Context:
CSV is commonly used to store network device inventory
in a simple tabular format.

The CSV data is stored in a separate file to keep
DATA and Python LOGIC separated.

## Network Automation

             Network Inventory
                    │
                    ▼
          network_devices.csv
                    │
                    ▼
             Python Script
                    │
                    ▼
          Processing / Validation
                    │
                    ▼
          Network Automation
"""


# -------------------------------------------------------------
# File Path
# -------------------------------------------------------------

CSV_FILE = "data/network_devices.csv"


# -------------------------------------------------------------
# Read CSV File
# -------------------------------------------------------------

with open(CSV_FILE, "r", encoding="utf-8") as file:

    csv_data = file.read()


# -------------------------------------------------------------
# Display Complete CSV Data
# -------------------------------------------------------------

print("=== CSV Data ===")
print(csv_data)


# -------------------------------------------------------------
# Split CSV into Rows
# -------------------------------------------------------------

rows = csv_data.strip().split("\n")

print("=== Rows ===")

for row in rows:
    print(row)


# -------------------------------------------------------------
# Display Header
# -------------------------------------------------------------

header = rows[0]

print("\n=== Header ===")
print(header)


# -------------------------------------------------------------
# Split Header into Columns
# -------------------------------------------------------------

columns = header.split(",")

print("\n=== Columns ===")

for column in columns:
    print(column)


# -------------------------------------------------------------
# Display Network Devices
# -------------------------------------------------------------

print("\n=== Network Devices ===")

for row in rows[1:]:

    values = row.split(",")

    hostname = values[0]
    management_ip = values[1]
    device_type = values[2]
    vendor = values[3]

    print(
        f"Hostname: {hostname} | "
        f"IP: {management_ip} | "
        f"Type: {device_type} | "
        f"Vendor: {vendor}"
    )


# -------------------------------------------------------------
# Display Number of Devices
# -------------------------------------------------------------

device_count = len(rows) - 1

print("\n=== Statistics ===")
print(f"Total Devices: {device_count}")
