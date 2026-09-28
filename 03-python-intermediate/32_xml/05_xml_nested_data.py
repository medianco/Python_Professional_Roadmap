"""
Lesson 32.5 - Nested XML Data

This lesson demonstrates how to work with nested
and hierarchical XML data using ElementTree.

Network Engineering Context:
Network devices contain hierarchical information.

For example:

Network
 │
 └──Device
      ├── Hostname
      ├── Management_ip
      ├── Interfaces
      │     ├── Interface
      │     │    ├── name
      │     │    ├── ip
      │     │    └── status
      │     │
      │     └── Interface
      │          ├── name
      │          ├── ip
      │          └── status
      │
      ├── Routing
      └── Management

XML is well suited for representing this type
of hierarchical network data.

In this lesson we will:

1. Create nested XML elements.
2. Add network interfaces.
3. Read nested elements.
4. Navigate through multiple XML levels.
5. Search nested network data.
6. Display interface information.
"""


import xml.etree.ElementTree as ET


# ---------------------------------------------------------
# 1. Create XML Root
# ---------------------------------------------------------

root = ET.Element("network")


# ---------------------------------------------------------
# 2. Create Network Device
# ---------------------------------------------------------

device = ET.SubElement(
    root,
    "device",
)

device.set(
    "id",
    "R1",
)

device.set(
    "status",
    "active",
)


# ---------------------------------------------------------
# 3. Add Device Information
# ---------------------------------------------------------

hostname = ET.SubElement(
    device,
    "hostname",
)

hostname.text = "R1"


management_ip = ET.SubElement(
    device,
    "management_ip",
)

management_ip.text = "192.168.1.1"


device_type = ET.SubElement(
    device,
    "device_type",
)

device_type.text = "router"


vendor = ET.SubElement(
    device,
    "vendor",
)

vendor.text = "Cisco"


# ---------------------------------------------------------
# 4. Create Interfaces Container
# ---------------------------------------------------------

# Instead of placing interfaces directly under
# <device>, we create an <interfaces> container.

interfaces = ET.SubElement(
    device,
    "interfaces",
)


# ---------------------------------------------------------
# 5. Create First Interface
# ---------------------------------------------------------

interface1 = ET.SubElement(
    interfaces,
    "interface",
)

interface1.set(
    "id",
    "1",
)

name1 = ET.SubElement(
    interface1,
    "name",
)

name1.text = "GigabitEthernet0/0"

ip1 = ET.SubElement(
    interface1,
    "ip",
)

ip1.text = "10.0.0.1"

status1 = ET.SubElement(
    interface1,
    "status",
)

status1.text = "up"


# ---------------------------------------------------------
# 6. Create Second Interface
# ---------------------------------------------------------

interface2 = ET.SubElement(
    interfaces,
    "interface",
)

interface2.set(
    "id",
    "2",
)

name2 = ET.SubElement(
    interface2,
    "name",
)

name2.text = "GigabitEthernet0/1"

ip2 = ET.SubElement(
    interface2,
    "ip",
)

ip2.text = "192.168.10.1"

status2 = ET.SubElement(
    interface2,
    "status",
)

status2.text = "up"


# ---------------------------------------------------------
# 7. Create Third Interface
# ---------------------------------------------------------

interface3 = ET.SubElement(
    interfaces,
    "interface",
)

interface3.set(
    "id",
    "3",
)

name3 = ET.SubElement(
    interface3,
    "name",
)

name3.text = "GigabitEthernet0/2"

ip3 = ET.SubElement(
    interface3,
    "ip",
)

ip3.text = "172.16.1.1"

status3 = ET.SubElement(
    interface3,
    "status",
)

status3.text = "down"


# ---------------------------------------------------------
# 8. Create XML Tree
# ---------------------------------------------------------

tree = ET.ElementTree(root)


# ---------------------------------------------------------
# 9. Format XML
# ---------------------------------------------------------

ET.indent(
    tree,
    space="    ",
)


# ---------------------------------------------------------
# 10. Display Complete XML
# ---------------------------------------------------------

print("=== Nested XML Structure ===")

xml_string = ET.tostring(
    root,
    encoding="unicode",
)

print(xml_string)


# ---------------------------------------------------------
# 11. Access the Interfaces Container
# ---------------------------------------------------------

print("\n=== Interfaces Container ===")

interfaces_element = device.find(
    "interfaces"
)

print(
    f"Tag: {interfaces_element.tag}"
)

print(
    f"Number of Interfaces: "
    f"{len(interfaces_element)}"
)


# ---------------------------------------------------------
# 12. Find All Interfaces
# ---------------------------------------------------------

print("\n=== All Interfaces ===")

interface_list = interfaces_element.findall(
    "interface"
)

for interface in interface_list:

    interface_id = interface.get("id")

    name = interface.find("name")
    ip = interface.find("ip")
    status = interface.find("status")

    print(
        f"ID: {interface_id} | "
        f"Name: {name.text} | "
        f"IP: {ip.text} | "
        f"Status: {status.text}"
    )


# ---------------------------------------------------------
# 13. Search for Active Interfaces
# ---------------------------------------------------------

print("\n=== Active Interfaces ===")

for interface in interface_list:

    status = interface.find("status")

    if status.text == "up":

        name = interface.find("name")
        ip = interface.find("ip")

        print(
            f"Interface: {name.text} | "
            f"IP: {ip.text}"
        )


# ---------------------------------------------------------
# 14. Search for Down Interfaces
# ---------------------------------------------------------

print("\n=== Down Interfaces ===")

for interface in interface_list:

    status = interface.find("status")

    if status.text == "down":

        name = interface.find("name")
        ip = interface.find("ip")

        print(
            f"Interface: {name.text} | "
            f"IP: {ip.text}"
        )


# ---------------------------------------------------------
# 15. Navigate Through the XML Hierarchy
# ---------------------------------------------------------

print("\n=== XML Hierarchy ===")

print(f"Root: {root.tag}")

print(
    f"Device: {device.tag}"
)

print(
    f"Interfaces: {interfaces.tag}"
)

for interface in interface_list:

    print(
        f"  Interface: {interface.tag}"
    )

    for element in interface:

        print(
            f"    {element.tag}: "
            f"{element.text}"
        )


# ---------------------------------------------------------
# 16. Network Device Summary
# ---------------------------------------------------------

print("\n=== Network Device Summary ===")

print(
    f"Hostname: {hostname.text}"
)

print(
    f"Management IP: "
    f"{management_ip.text}"
)

print(
    f"Device Type: "
    f"{device_type.text}"
)

print(
    f"Vendor: {vendor.text}"
)

print(
    f"Total Interfaces: "
    f"{len(interface_list)}"
)

up_count = sum(
    1
    for interface in interface_list
    if interface.find("status").text == "up"
)

down_count = sum(
    1
    for interface in interface_list
    if interface.find("status").text == "down"
)

print(
    f"Interfaces Up: {up_count}"
)

print(
    f"Interfaces Down: {down_count}"
)
