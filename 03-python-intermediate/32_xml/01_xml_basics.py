"""
Lesson 32.1 - XML Basics

This lesson introduces the basic structure of XML.

XML (eXtensible Markup Language) is used to store
and exchange structured data between systems.

Network Engineering Context:
XML can be used to represent network devices,
interfaces, configurations, and inventory data.
"""


# ---------------------------------------------------------
# 1. Basic XML Document
# ---------------------------------------------------------

xml_data = """<?xml version="1.0" encoding="UTF-8"?>

<device>
    <hostname>R1</hostname>
    <management_ip>192.168.1.1</management_ip>
    <device_type>router</device_type>
    <vendor>Cisco</vendor>
</device>
"""


print("=== XML Document ===")
print(xml_data)


# ---------------------------------------------------------
# 2. XML Root Element
# ---------------------------------------------------------

print("=== Root Element ===")
print("<device>")


# ---------------------------------------------------------
# 3. XML Elements
# ---------------------------------------------------------

print("\n=== XML Elements ===")

print("<hostname>R1</hostname>")
print("<management_ip>192.168.1.1</management_ip>")
print("<device_type>router</device_type>")
print("<vendor>Cisco</vendor>")


# ---------------------------------------------------------
# 4. XML Element Structure
# ---------------------------------------------------------

print("\n=== XML Element Structure ===")

element_example = "<hostname>R1</hostname>"

print(f"Complete Element: {element_example}")
print("Opening Tag: <hostname>")
print("Text: R1")
print("Closing Tag: </hostname>")


# ---------------------------------------------------------
# 5. XML Attributes
# ---------------------------------------------------------

print("\n=== XML Attributes ===")

device_with_attributes = """
<device type="router" vendor="Cisco">
    <hostname>R1</hostname>
    <management_ip>192.168.1.1</management_ip>
</device>
"""

print(device_with_attributes)


# ---------------------------------------------------------
# 6. Nested XML Elements
# ---------------------------------------------------------

print("=== Nested XML Elements ===")

network_xml = """
<network>
    <device>
        <hostname>R1</hostname>
        <management_ip>192.168.1.1</management_ip>
    </device>

    <device>
        <hostname>SW1</hostname>
        <management_ip>192.168.1.10</management_ip>
    </device>
</network>
"""

print(network_xml)


# ---------------------------------------------------------
# 7. XML Comments
# ---------------------------------------------------------

print("=== XML Comments ===")

xml_with_comment = """
<device>

    <!-- Network device information -->

    <hostname>R1</hostname>
    <management_ip>192.168.1.1</management_ip>

</device>
"""

print(xml_with_comment)


# ---------------------------------------------------------
# 8. Network Engineering Example
# ---------------------------------------------------------

print("=== Network Device XML ===")

network_device = """
<device>
    <hostname>R1</hostname>
    <management_ip>192.168.1.1</management_ip>
    <device_type>router</device_type>
    <vendor>Cisco</vendor>
    <location>Data Center</location>
</device>
"""

print(network_device)


# ---------------------------------------------------------
# 9. Important XML Concepts
# ---------------------------------------------------------

print("=== XML Concepts ===")

print("Root Element  : <device>")
print("Element       : <hostname>R1</hostname>")
print("Tag           : hostname")
print("Text          : R1")
print("Attribute     : type=\"router\"")
print("Nested Element: <management_ip>192.168.1.1</management_ip>")


# ---------------------------------------------------------
# 10. Summary
# ---------------------------------------------------------

print("\n=== Summary ===")

print("XML stores structured and hierarchical data.")
print("Elements contain data.")
print("Attributes provide additional information.")
print("XML documents have a root element.")
print("Elements can contain other elements.")
print("XML is commonly used in enterprise and network systems.")
