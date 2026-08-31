"""
Lesson 24: Multiple Inheritance & MRO

This lesson demonstrates:
- Multiple Inheritance
- Multiple Parent Classes
- Method Reuse
- Basic MRO (Method Resolution Order)
- MRO = order of method lookup/call.
  Return composition can appear in reverse because each method wraps the result returned by super

            NetworkDevice
                │
            ┌───┴─────────────┐
            │                 │
        CiscoFeature   SecurityFeature
            │                 │
            └───────┬─────────┘
                    │
            EnterpriseDevice

        NetworkDevice        MonitoringFeature
            │                     │
            └────────┬────────────┘
                     │
               ManagedDevice

Author: Mohammed AL-Dubai
"""


class NetworkDevice:
    """Represent a basic network device."""

    def show_network_info(self) -> str:
        """Return basic network information."""
        return "Network device"

    def show_status(self) -> str:
        """Return network device status."""
        return "NetworkDevice status"

    def describe(self) -> str:
        """Return basic device description."""
        return "NetworkDevice"

class CiscoFeature(NetworkDevice):
    """Provide Cisco-specific functionality."""

    def show_cisco_info(self) -> str:
        """Return Cisco-specific information."""
        return "Cisco features enabled"

    def show_status(self) -> str:
        """Return Cisco status."""

        next_status = super().show_status()
        return f"CiscoFeature + {next_status}"

    def describe(self) -> str:
        """Return Cisco feature description."""

        description = super().describe()
        return f"{description} + CiscoFeature"

class MonitoringFeature:
    """Provide monitoring functionality."""

    def show_monitoring_info(self) -> str:
        """Return monitoring information."""
        return "Monitoring enabled"

    def show_status(self) -> str:
        """Return monitoring status."""
        return "MonitoringFeature status"

class SecurityFeature(NetworkDevice):
    """Provide security functionality."""

    def show_security_info(self) -> str:
        """Return security information."""
        return "Security enabled"

    def show_status(self) -> str:
        """Return security status."""

        next_status = super().show_status()
        return f"SecurityFeature + {next_status}"

    def describe(self) -> str:
        """Return security feature description."""

        description = super().describe()
        return f"{description} + SecurityFeature"

class EnterpriseDevice(CiscoFeature, SecurityFeature):
    """Represent an enterprise device with multiple features."""

    def show_status(self) -> str:
        """Return enterprise device status."""

        next_status = super().show_status()
        return f"EnterpriseDevice + {next_status}"

    def describe(self) -> str:
        """Return enterprise device description."""

        description = super().describe()
        return f"{description} + EnterpriseDevice"

class ManagedDevice(NetworkDevice, MonitoringFeature):
    """Represent a device with network and monitoring features."""

    def show_status(self) -> str:
        """Return managed device status."""

        parent_status = super().show_status()
        return f"ManagedDevice + {parent_status}"
        
        
if __name__ == "__main__":
    
    device = ManagedDevice()
    
    enterprise_device = EnterpriseDevice()
    
    print("MRO:")
    for cls in EnterpriseDevice.mro():
        print(cls.__name__)

    print(
        EnterpriseDevice.__mro__
        == tuple(EnterpriseDevice.mro())
    )
    
    print(enterprise_device.describe())
    
    print("\nTesting method resolution:")
    print(enterprise_device.describe())
    
    print("\nTesting MRO:")

    for cls in EnterpriseDevice.mro():
        print(cls.__name__)
    
    print('=' * 100)
    print(enterprise_device.show_status())
    
    print(EnterpriseDevice.__mro__)
    print(EnterpriseDevice.mro())
    
    print('=' * 100)
    print(device.show_status())
    print(ManagedDevice.__mro__)
    print(ManagedDevice.mro())
    print('=' * 100)
    print(device.show_network_info())
    #print(device.show_monitoring_info())
    
    
    print(isinstance(device, ManagedDevice))
    print(isinstance(device, NetworkDevice))
    #print(isinstance(device, MonitoringFeature))
