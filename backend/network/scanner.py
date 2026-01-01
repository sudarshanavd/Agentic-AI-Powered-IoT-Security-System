from typing import List, Dict
from datetime import datetime
import nmap


# -------------------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------------------

DEFAULT_SUBNET = "192.168.1.0/24"


# -------------------------------------------------------------------
# NETWORK SCANNING
# -------------------------------------------------------------------
def scan_network(subnet: str = DEFAULT_SUBNET) -> List[Dict]:
    """
    Scans the local network to discover connected devices.

    Args:
        subnet (str): Network subnet to scan

    Returns:
        List of discovered devices with metadata
    """

    scanner = nmap.PortScanner()
    scanner.scan(hosts=subnet, arguments="-sn")

    devices = []

    for host in scanner.all_hosts():
        host_data = scanner[host]

        device = {
            "ip_address": host,
            "hostname": host_data.hostname(),
            "mac_address": host_data["addresses"].get("mac"),
            "vendor": host_data.get("vendor", {}),
            "status": host_data.state(),
            "first_seen": datetime.utcnow().isoformat(),
        }

        devices.append(device)

    return devices


# -------------------------------------------------------------------
# DEVICE TYPE HEURISTIC (OPTIONAL EXTENSION)
# -------------------------------------------------------------------
def infer_device_type(vendor: str) -> str:
    """
    Infers device type based on vendor name.

    This is a heuristic and can be improved with ML later.
    """

    if not vendor:
        return "Unknown"

    vendor = vendor.lower()

    if "camera" in vendor or "hikvision" in vendor:
        return "IP Camera"
    if "samsung" in vendor or "lg" in vendor:
        return "Smart TV"
    if "tp-link" in vendor or "netgear" in vendor:
        return "Network Device"
    if "amazon" in vendor or "google" in vendor:
        return "Smart Assistant"

    return "IoT Device"


# -------------------------------------------------------------------
# ENRICH DEVICE DATA (OPTIONAL)
# -------------------------------------------------------------------
def enrich_devices(devices: List[Dict]) -> List[Dict]:
    """
    Adds inferred device type to each device.
    """

    enriched = []

    for device in devices:
        vendor_info = device.get("vendor")
        vendor_name = (
            list(vendor_info.values())[0]
            if isinstance(vendor_info, dict) and vendor_info
            else ""
        )

        device["device_type"] = infer_device_type(vendor_name)
        enriched.append(device)

    return enriched
