"""
Lesson 22: Class Methods & Static Methods

This lesson demonstrates:
- Instance Methods
- Class Methods
- Static Methods
- Alternative Constructors

Author: Mohammed AL-Dubai
"""


class NetworkDevice:
    """Represent a basic network device."""
    
    device_count = 0

    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address
        
        NetworkDevice.device_count += 1

    def show_info(self):
        """Return basic information about the device."""
        return f"{self.hostname} - {self.ip_address}"
        
    @classmethod
    def get_device_count(cls):
        """Return the number of created network devices."""
        return cls.device_count

    @classmethod
    def from_string(cls, data):
        """Create a NetworkDevice from a comma-separated string."""
        hostname, ip_address = data.split(",")
    
        return cls(hostname, ip_address)



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

    print(router1.show_info())
    print(router2.show_info())
    print(router3.show_info())

    print(
        f"Total devices: {NetworkDevice.get_device_count()}"
    )
