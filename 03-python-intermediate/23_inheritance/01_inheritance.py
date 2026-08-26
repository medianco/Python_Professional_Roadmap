"""
Lesson 23: Inheritance

This lesson demonstrates:
- Parent Classes
- Child Classes
- Inheritance
- Method Reuse

NetworkDevice                          
     │
 ┌───┴─────────────┐
 │                 │
CiscoDevice   JuniperDevice

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
        
    @staticmethod
    def is_valid_ip(ip_address: str) -> bool:
        """Return True if the given IPv4 address is valid."""
        parts = ip_address.split(".")
    
        if len(parts) != 4:
            return False
    
        for part in parts:
            if not part.isdigit():
                return False
    
            if not 0 <= int(part) <= 255:
                return False
    
        return True    


    @classmethod
    def from_string(
        cls,
        data: str,
    ) -> "NetworkDevice":
        """Create a network device from a comma-separated string."""
        parts = [part.strip() for part in data.split(",")]
    
        if len(parts) < 2:
            raise ValueError(
                "Expected at least: 'hostname,ip_address'"
            )
    
        hostname = parts[0]
        ip_address = parts[1]
    
        if not cls.is_valid_ip(ip_address):
            raise ValueError(
                f"Invalid IPv4 address: {ip_address}"
            )
    
        return cls(*parts)   

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
    
    cisco = CiscoDevice.from_string(
    "R3,192.168.1.3,Catalyst 9300,IOS-XE 17.12"
    )
    
    juniper = JuniperDevice.from_string(
    "R4,192.168.1.4,MX204,Junos 23.4"
    )

    print(juniper.show_info())
    print(type(juniper).__name__)
    
    print(device.show_info())
    
    print(cisco.show_info())
    print(type(cisco).__name__)
    
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
