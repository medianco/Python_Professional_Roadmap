from dataclasses import dataclass


@dataclass
class NetworkDevice:

    hostname: str
    ip_address: str
    vendor: str
    device_type: str


router = NetworkDevice(
    hostname="R1",
    ip_address="192.168.10.1",
    vendor="Cisco",
    device_type="Router"
)


print("Network Device")
print("-" * 30)

print(f"Hostname: {router.hostname}")
print(f"IP Address: {router.ip_address}")
print(f"Vendor: {router.vendor}")
print(f"Device Type: {router.device_type}")

print("Network Device")
print("-" * 30)

devices = [

    NetworkDevice(
        "R1",
        "192.168.10.1",
        "Cisco",
        "Router"
    ),

    NetworkDevice(
        "R2",
        "192.168.20.1",
        "Cisco",
        "Router"
    ),

    NetworkDevice(
        "SW1",
        "192.168.10.10",
        "Cisco",
        "Switch"
    ),

    NetworkDevice(
        "FW1",
        "192.168.10.254",
        "Fortinet",
        "Firewall"
    ),
]


for device in devices:

    print(
        f"{device.hostname:<6}"
        f"{device.ip_address:<18}"
        f"{device.vendor:<10}"
        f"{device.device_type}"
    )
