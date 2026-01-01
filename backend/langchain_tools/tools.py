
from ml.anomaly import detect_anomaly
from security.firewall import block_ip
from security.honeypot import deploy_honeypot

def anomaly_tool():
    return detect_anomaly()

def firewall_tool(ip: str):
    return block_ip(ip)

def honeypot_tool():
    return deploy_honeypot()
