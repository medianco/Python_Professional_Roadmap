"""
Lesson 22: Class Methods & Static Methods

This lesson demonstrates:
- Instance Methods
- Class Methods
- Static Methods
- Alternative Constructors

Author: Mohammed AL-Dubai

┌──────────────────────┬──────────┬────────────────────────────┐
│ Method               │ Parameter│ Purpose                    │
├──────────────────────┼──────────┼────────────────────────────┤
│ Instance Method      │ self     │ Object-specific behavior   │
│ Class Method         │ cls      │ Class-level behavior       │
│ Static Method        │ None     │ Independent utility logic  │
└──────────────────────┴──────────┴────────────────────────────┘
"""


class NetworkDevice:
    """Represent a basic network device."""
    
    device_count = 0

    def __init__(self, hostname: str, ip_address: str) -> None:
        self.hostname = hostname
        self.ip_address = ip_address
        
        NetworkDevice.device_count += 1

    def show_info(self) -> str:
        """Return basic information about the device."""
        return f"{self.hostname} - {self.ip_address}"
        
    @classmethod
    def get_device_count(cls) -> int:
        """Return the number of created network devices."""
        return cls.device_count
        
        
    '''
    @classmethod
    def from_string(cls, data: str) -> "NetworkDevice":
        """Create a NetworkDevice from a comma-separated string."""
        """ Alternative Constructor """
        hostname, ip_address = data.split(",")
    
        return cls(hostname, ip_address)
    '''
    
    @classmethod
    def from_string(cls, data: str) -> "NetworkDevice":
        """Create a NetworkDevice from a comma-separated string."""
        try:
            hostname, ip_address = data.split(",")
    
        except ValueError as error:
            raise ValueError(
                "Expected format: 'hostname,ip_address'"
            ) from error
    
        return cls(hostname.strip(), ip_address.strip())

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



if __name__ == "__main__":
    router1 = NetworkDevice(
        "R1",
        "192.168.1.1",
    )

    router2 = NetworkDevice(
        "R2",
        "192.168.1.2",
    )
    
    router3 = NetworkDevice.from_string(
        "R3,192.168.1.3"
    )

    test_ips = [
        "192.168.1.1",
        "10.0.0.1",
        "172.16.0.1",
        "255.255.255.255",
        "0.0.0.0",
        "192.168.1.300",
        "192.168.1",
        "192.168.1.1.5",
        "abc.def.1.1",
        "192.168.-1.1",
        "",
    ]
    
    print(router1.show_info())
    print(router2.show_info())
    print(router3.show_info())

    print(
        f"Total devices: {NetworkDevice.get_device_count()}"
    )
    
    print('=' * 30)
    print(
        NetworkDevice.is_valid_ip("192.168.1.1")
    )
    
    print(
        NetworkDevice.is_valid_ip("192.168.1.300")
    )
    
    print(
    NetworkDevice.is_valid_ip("abc.def.1.1")
    )
    
    for ip in test_ips:
        result = NetworkDevice.is_valid_ip(ip)
        print(f"{ip!r:20} -> {result}")
