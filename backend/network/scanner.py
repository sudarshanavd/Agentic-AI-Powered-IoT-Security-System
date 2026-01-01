
import nmap

def scan_network(subnet="192.168.1.0/24"):
    nm = nmap.PortScanner()
    nm.scan(hosts=subnet, arguments="-sn")
    devices = []
    for host in nm.all_hosts():
        devices.append({
            "ip": host,
            "hostname": nm[host].hostname(),
            "mac": nm[host]['addresses'].get('mac'),
            "vendor": nm[host]['vendor']
        })
    return devices
