from collections.abc import Sequence
"""
Lesson 23: Inheritance

This lesson demonstrates:
- Parent Classes
- Child Classes
- Inheritance
- super().__init__()
- Method Overriding
- super().show_info()
- cls
- Alternative Constructor — from_string()
- IPv4 Validation
- Exception Handling
- Method Reuse
- Polymorphism = One Interface, Multiple Implementations

             display_devices()
                     │
                     ▼
              NetworkDevice
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
     Cisco         Juniper       Arista
       │             │             │
 show_info()      show_info()   show_info()

Author: Mohammed AL-Dubai

"""


class NetworkDevice:
    """Represent a basic network device."""

    # Constructor of the parent class
    def __init__(self, hostname: str, ip_address: str) -> None:
        self.hostname = hostname
        self.ip_address = ip_address

    # Return basic information about the network device
    def show_info(self) -> str:
        """Return basic information about the device."""
        return f"{self.hostname} - {self.ip_address}"

    # Static method:
    # It does not need access to self or cls.
    # It only validates the given IPv4 address.
    @staticmethod
    def is_valid_ip(ip_address: str) -> bool:
        """Return True if the given IPv4 address is valid."""

        # Split the IP address into four parts
        parts = ip_address.split(".")

        # An IPv4 address must contain exactly four parts
        if len(parts) != 4:
            return False

        # Check every part of the IP address
        for part in parts:

            # Each part must contain only digits
            if not part.isdigit():
                return False

            # Each IPv4 octet must be between 0 and 255
            if not 0 <= int(part) <= 255:
                return False

        # All validation checks passed
        return True

    # Class method:
    # cls refers to the class that calls this method.
    #
    # This allows the method to work with:
    # NetworkDevice
    # CiscoDevice
    # JuniperDevice
    @classmethod
    def from_string(
        cls,
        data: str,
    ) -> "NetworkDevice":
        """Create a network device from a comma-separated string."""

        # Split the input string by commas
        # and remove unnecessary spaces.
        parts = [part.strip() for part in data.split(",")]

        # At least hostname and IP address are required
        if len(parts) < 2:
            raise ValueError(
                "Expected at least: 'hostname,ip_address'"
            )

        # Extract hostname
        hostname = parts[0]

        # Extract IP address
        ip_address = parts[1]

        # Validate the IPv4 address
        if not cls.is_valid_ip(ip_address):
            raise ValueError(
                f"Invalid IPv4 address: {ip_address}"
            )

        # Create an object using the class that called from_string()
        #
        # For example:
        # NetworkDevice.from_string() -> NetworkDevice
        # CiscoDevice.from_string()   -> CiscoDevice
        # JuniperDevice.from_string() -> JuniperDevice
        return cls(*parts)


class CiscoDevice(NetworkDevice):
    """Represent a Cisco network device."""

    # Constructor of the Cisco child class
    def __init__(
        self,
        hostname: str,
        ip_address: str,
        model: str,
        os_version: str,
    ) -> None:

        # Call the constructor of the parent class
        # to initialize hostname and ip_address.
        super().__init__(
            hostname,
            ip_address,
        )

        # Cisco-specific attributes
        self.model = model
        self.os_version = os_version

    # Method overriding:
    # We replace the parent's show_info()
    # with a Cisco-specific implementation.
    def show_info(self) -> str:
        """Return Cisco device information."""

        # Reuse the parent's show_info() method
        base_info = super().show_info()

        # Add Cisco-specific information
        return (
            f"{base_info} - "
            f"{self.model} - "
            f"{self.os_version}"
        )


class JuniperDevice(NetworkDevice):
    """Represent a Juniper network device."""

    # Constructor of the Juniper child class
    def __init__(
        self,
        hostname: str,
        ip_address: str,
        model: str,
        os_version: str,
    ) -> None:

        # Call the constructor of the parent class
        # to initialize hostname and ip_address.
        super().__init__(
            hostname,
            ip_address,
        )

        # Juniper-specific attributes
        self.model = model
        self.os_version = os_version

    # Method overriding:
    # We provide a Juniper-specific version of show_info().
    def show_info(self) -> str:
        """Return Juniper device information."""

        # Reuse the parent's show_info() method
        base_info = super().show_info()

        # Add Juniper-specific information
        return (
            f"{base_info} - "
            f"{self.model} - "
            f"{self.os_version}"
        )
        
class AristaDevice(NetworkDevice):
    """Represent an Arista network device."""

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
        """Return Arista device information."""
        base_info = super().show_info()

        return (
            f"{base_info} - "
            f"{self.model} - "
            f"{self.os_version}"
        )
        

def display_devices(devices: list[NetworkDevice]) -> None:
    """Display information for a collection of network devices."""
    
    for device in devices:
        print(device.show_info())
        
def display_devices_Sequence(
    devices: Sequence[NetworkDevice],
) -> None:
    """Display information for a sequence of network devices."""

    for device in devices:
        print(device.show_info())


# This block runs only when this file is executed directly.
# It will not run when the file is imported as a module.
if __name__ == "__main__":

    # Create a CiscoDevice object
    router = CiscoDevice(
        "R1",
        "192.168.1.1",
        "Catalyst 9300",
        "IOS-XE 17.12",
    )

    # Create a JuniperDevice object
    router2 = JuniperDevice(
        "R2",
        "192.168.1.2",
        "MX204",
        "Junos 23.4",
    )

    # Create a NetworkDevice object using the
    # alternative constructor from_string()
    device = NetworkDevice.from_string(
        "SW1,192.168.1.10"
    )

    # Create a CiscoDevice using from_string()
    #
    # Because CiscoDevice inherits from NetworkDevice,
    # it can use the parent's class method.
    cisco = CiscoDevice.from_string(
        "R3,192.168.1.3,Catalyst 9300,IOS-XE 17.12"
    )

    # Create a JuniperDevice using from_string()
    juniper = JuniperDevice.from_string(
        "R4,192.168.1.4,MX204,Junos 23.4"
    )
    
    
    devices = [
    CiscoDevice.from_string(
        "R01,192.168.1.1,Catalyst 9300,IOS-XE 17.12"
    ),
    JuniperDevice.from_string(
        "R02,192.168.1.2,MX204,Junos 23.4"
    ),
    CiscoDevice.from_string(
        "SW01,192.168.1.10,Catalyst 9200,IOS-XE 17.9"
    ),
    
        AristaDevice.from_string(
        "SW02,192.168.1.20,7050X3,EOS 4.31"
    ),
    ]
    
    display_devices(devices)
    print("=" * 65)
    
    devices.append(
    JuniperDevice.from_string(
        "R03,192.168.1.3,SRX345,Junos 23.4"
    )
    )
    
    display_devices(devices)
    print("=" * 65)
    
    for device in devices:
        print(device.show_info())
            
    print("=" * 65)
    
    for device in devices:
        print(
            f"{type(device).__name__}: "
            f"{device.show_info()}"
        )

    print("*" * 65)
    
    test_devices = (
    CiscoDevice.from_string(
        "R10,10.0.0.1,Catalyst 9300,IOS-XE 17.12"
    ),
    JuniperDevice.from_string(
        "R20,10.0.0.2,MX204,Junos 23.4"
    ),
    AristaDevice.from_string(
        "SW10,10.0.0.10,7050X3,EOS 4.31"
    ),
    )

    display_devices_Sequence(test_devices)
    print("*" * 65)
    # Display Juniper information
    print(juniper.show_info())

    # Display the class name of the object
    print(type(juniper).__name__)

    # Display basic NetworkDevice information
    print(device.show_info())

    # Display Cisco information
    print(cisco.show_info())

    # Display the class name
    print(type(cisco).__name__)

    # Display Cisco router information
    print(router.show_info())

    # Display Juniper router information
    print(router2.show_info())

    # Display the actual class names
    print(type(router).__name__)
    print(type(router2).__name__)

    # Check whether router is a CiscoDevice
    print(isinstance(router, CiscoDevice))

    # Check whether router is also a NetworkDevice
    # because CiscoDevice inherits from NetworkDevice.
    print(isinstance(router, NetworkDevice))

    # Check whether router2 is a JuniperDevice
    print(isinstance(router2, JuniperDevice))

    # Check whether router2 is also a NetworkDevice
    # because JuniperDevice inherits from NetworkDevice.
    print(isinstance(router2, NetworkDevice))


    # -------------------------------------------------
    # Direct attribute access
    # -------------------------------------------------
    #
    # These attributes are inherited or defined
    # inside CiscoDevice.
    #
    # print(router.hostname)
    # print(router.ip_address)
    # print(router.model)
    # print(router.os_version)
