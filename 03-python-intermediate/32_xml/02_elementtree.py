"""
Lesson 32.2 - ElementTree

This lesson introduces Python's built-in XML library:

    xml.etree.ElementTree

ElementTree allows us to create, read, navigate,
and manipulate XML documents.

Network Engineering Context:
We can use ElementTree to build structured XML
representations of network devices and their data.
"""

import xml.etree.ElementTree as ET


# ---------------------------------------------------------
# 1. Create a Root Element
# ---------------------------------------------------------

# ET.Element() creates a new XML element.
# Here, "network" will be the root element.

root = ET.Element("network")

print("=== Root Element ===")
print(root)


# ---------------------------------------------------------
# 2. Create a Child Element
# ---------------------------------------------------------

# ET.SubElement() creates a child element
# inside another element.

device = ET.SubElement(root, "device")

print("\n=== Device Element ===")
print(device)


# ---------------------------------------------------------
# 3. Add Elements to the Device
# ---------------------------------------------------------

hostname = ET.SubElement(device, "hostname")
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
# 4. Create an XML Tree
# ---------------------------------------------------------

# ElementTree represents the complete XML document.

tree = ET.ElementTree(root)

print("\n=== XML Tree Created ===")
print(tree)


# ---------------------------------------------------------
# 5. Access the Root Element
# ---------------------------------------------------------

# getroot() returns the root element of the XML tree.

xml_root = tree.getroot()

print("\n=== XML Root ===")
print(xml_root.tag)


# ---------------------------------------------------------
# 6. Access Element Tags
# ---------------------------------------------------------

print("\n=== Element Tags ===")

print(f"Root Tag: {root.tag}")
print(f"Device Tag: {device.tag}")
print(f"Hostname Tag: {hostname.tag}")
print(f"IP Tag: {management_ip.tag}")
print(f"Type Tag: {device_type.tag}")
print(f"Vendor Tag: {vendor.tag}")


# ---------------------------------------------------------
# 7. Access Element Text
# ---------------------------------------------------------

print("\n=== Element Text ===")

print(f"Hostname: {hostname.text}")
print(f"Management IP: {management_ip.text}")
print(f"Device Type: {device_type.text}")
print(f"Vendor: {vendor.text}")


# ---------------------------------------------------------
# 8. Add XML Attributes
# ---------------------------------------------------------

# XML elements can have attributes.

device.set("id", "R1")
device.set("status", "active")

print("\n=== Device Attributes ===")

print(f"ID: {device.get('id')}")
print(f"Status: {device.get('status')}")


# ---------------------------------------------------------
# 9. Display All Device Attributes
# ---------------------------------------------------------

print("\n=== All Attributes ===")

for key, value in device.attrib.items():
    print(f"{key}: {value}")


# ---------------------------------------------------------
# 10. Create Another Device
# ---------------------------------------------------------

device2 = ET.SubElement(root, "device")

hostname2 = ET.SubElement(
    device2,
    "hostname",
)
hostname2.text = "SW1"

management_ip2 = ET.SubElement(
    device2,
    "management_ip",
)
management_ip2.text = "192.168.1.10"

device_type2 = ET.SubElement(
    device2,
    "device_type",
)
device_type2.text = "switch"

vendor2 = ET.SubElement(
    device2,
    "vendor",
)
vendor2.text = "Cisco"


# ---------------------------------------------------------
# 11. Display XML Structure
# ---------------------------------------------------------

print("\n=== XML Structure ===")

print(f"Root: {root.tag}")

for current_device in root:
    print(f"Device: {current_device.tag}")

    for element in current_device:
        print(
            f"  {element.tag}: "
            f"{element.text}"
        )


# ---------------------------------------------------------
# 12. Convert XML Tree to String
# ---------------------------------------------------------

# ET.tostring() converts the XML tree into
# a byte string representation.

xml_string = ET.tostring(
    root,
    encoding="unicode",
)

print("\n=== Generated XML ===")
print(xml_string)


# ---------------------------------------------------------
# 13. Pretty Print XML
# ---------------------------------------------------------

# indent() formats the XML tree with indentation.
# This makes the XML easier for humans to read.

ET.indent(tree, space="    ")

pretty_xml = ET.tostring(
    root,
    encoding="unicode",
)

print("\n=== Pretty XML ===")
print(pretty_xml)


# ---------------------------------------------------------
# 14. Network Engineering Summary
# ---------------------------------------------------------

print("=== Network Engineering Summary ===")

print("XML Root       :", root.tag)
print("Total Devices  :", len(root))

print("\nDevices:")

for current_device in root:
    hostname_element = current_device.find("hostname")
    ip_element = current_device.find("management_ip")
    type_element = current_device.find("device_type")
    vendor_element = current_device.find("vendor")

    print(
        f"Hostname: {hostname_element.text} | "
        f"IP: {ip_element.text} | "
        f"Type: {type_element.text} | "
        f"Vendor: {vendor_element.text}"
    )
