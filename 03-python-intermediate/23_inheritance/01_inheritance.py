"""
Lesson 23: Inheritance

This lesson demonstrates:
- Parent Classes
- Child Classes
- Inheritance
- Method Reuse

Author: Mohammed AL-Dubai
"""


class NetworkDevice:
    """Represent a basic network device."""

    def __init__(self, hostname: str, ip_address: str) -> None:
        self.hostname = hostname
        self.ip_address = ip_address

    def show_info(self) -> str:
        """Return basic information about the device."""
        return f"{self.hostname} - {self.ip_address}"

    @classmethod
    def from_string(cls, data: str) -> "NetworkDevice":
        """Create a network device from a comma-separated string."""
        try:
            hostname, ip_address = data.split(",")
    
        except ValueError as error:
            raise ValueError(
                "Expected format: 'hostname,ip_address'"
            ) from error
    
        hostname = hostname.strip()
        ip_address = ip_address.strip()
    
        if not cls.is_valid_ip(ip_address):
            raise ValueError(
                f"Invalid IPv4 address: {ip_address}"
            )
    
        return cls(hostname, ip_address)

class CiscoDevice(NetworkDevice):
    """Represent a Cisco network device."""

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        model: str,
        os_version: str,
    ) -> None:
        super().__init__(
            hostname,
            ip_address,
        )

        self.model = model
        self.os_version = os_version
    
    def show_info(self) -> str:
        """Return Cisco device information."""
        base_info = super().show_info()
        return (
            f"{base_info} - "
            f"{self.model} - "
            f"{self.os_version}"
        )
    
    
class JuniperDevice(NetworkDevice):
    """Represent a Juniper network device."""

    def __init__(
        self,
        hostname: str,
        ip_address: str,
        model: str,
        os_version: str,
    ) -> None:
        super().__init__(
            hostname,
            ip_address,
        )

        self.model = model
        self.os_version = os_version

    def show_info(self) -> str:
        """Return Juniper device information."""
        base_info = super().show_info()

        return (
            f"{base_info} - "
            f"{self.model} - "
            f"{self.os_version}"
        )        


if __name__ == "__main__":

    router = CiscoDevice(
        "R1",
        "192.168.1.1",
        "Catalyst 9300",
        "IOS-XE 17.12",
    )
    
    
    router2 = JuniperDevice(
        "R2",
        "192.168.1.2",
        "MX204",
        "Junos 23.4",
    )
    
    device = NetworkDevice.from_string(
        "SW1,192.168.1.10"
    )

    print(device.show_info())

    print(router.show_info())
    print(router2.show_info())
    
    
    print(type(router).__name__)
    print(type(router2).__name__)
    
    print(isinstance(router, CiscoDevice))
    print(isinstance(router, NetworkDevice))
    
    print(isinstance(router2, JuniperDevice))
    print(isinstance(router2, NetworkDevice))
        
    #print(router.hostname)
    #print(router.ip_address)
    #print(router.model)
    #print(router.os_version)
