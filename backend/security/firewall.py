from typing import Dict
from datetime import datetime
import subprocess


# -------------------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------------------

FIREWALL_MODE = "simulation"


# -------------------------------------------------------------------
# FIREWALL ACTIONS
# -------------------------------------------------------------------
def block_ip(ip_address: str) -> Dict:
    """
    Blocks an IP address using firewall rules.

    Args:
        ip_address (str): IP address to block

    Returns:
        Dict containing action status and metadata
    """

    timestamp = datetime.utcnow().isoformat()

    if FIREWALL_MODE == "simulation":
        return {
            "timestamp": timestamp,
            "mode": "simulation",
            "action": "block_ip",
            "target": ip_address,
            "status": "success",
            "message": f"Simulated blocking of IP {ip_address}"
        }

    try:
        subprocess.run(
            ["sudo", "iptables", "-A", "INPUT", "-s", ip_address, "-j", "DROP"],
            check=True
        )

        return {
            "timestamp": timestamp,
            "mode": "iptables",
            "action": "block_ip",
            "target": ip_address,
            "status": "success",
            "message": f"IP {ip_address} blocked using iptables"
        }

    except Exception as e:
        return {
            "timestamp": timestamp,
            "mode": "iptables",
            "action": "block_ip",
            "target": ip_address,
            "status": "error",
            "error": str(e)
        }


# -------------------------------------------------------------------
# OPTIONAL: UNBLOCK IP
# -------------------------------------------------------------------
def unblock_ip(ip_address: str) -> Dict:

    timestamp = datetime.utcnow().isoformat()

    if FIREWALL_MODE == "simulation":
        return {
            "timestamp": timestamp,
            "mode": "simulation",
            "action": "unblock_ip",
            "target": ip_address,
            "status": "success",
            "message": f"Simulated unblocking of IP {ip_address}"
        }

    try:
        subprocess.run(
            ["sudo", "iptables", "-D", "INPUT", "-s", ip_address, "-j", "DROP"],
            check=True
        )

        return {
            "timestamp": timestamp,
            "mode": "iptables",
            "action": "unblock_ip",
            "target": ip_address,
            "status": "success",
            "message": f"IP {ip_address} unblocked"
        }

    except Exception as e:
        return {
            "timestamp": timestamp,
            "mode": "iptables",
            "action": "unblock_ip",
            "target": ip_address,
            "status": "error",
            "error": str(e)
        }
