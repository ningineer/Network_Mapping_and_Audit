import nmap
from datetime import datetime
import os

# Initialize the nmap scanner
scanner = nmap.PortScanner()

# Define the IP range or specific IP to scan
ip_to_scan = "192.168.1.0/24"  # Adjust this to your target IP or range

# Define the directory and file for logging
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# File path with a timestamp for uniqueness
log_file_path = os.path.join(log_dir, f"network_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

# Function to get the current timestamp
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Start the scan
with open(log_file_path, "w") as log_file:
    log_file.write(f"[{get_timestamp()}] Starting scan on {ip_to_scan}\n")
    scanner.scan(hosts=ip_to_scan, arguments="-sV")

    # Loop through scanned hosts
    for host in scanner.all_hosts():
        log_file.write(f"[{get_timestamp()}] Host: {host} ({scanner[host].hostname()})\n")
        log_file.write(f"[{get_timestamp()}] State: {scanner[host].state()}\n")
        
        # Loop through the protocols (like TCP, UDP) found on the host
        for protocol in scanner[host].all_protocols():
            log_file.write(f"[{get_timestamp()}] Protocol: {protocol}\n")
            
            # Get all the ports in this protocol
            ports = scanner[host][protocol].keys()
            for port in ports:
                port_state = scanner[host][protocol][port]["state"]
                log_file.write(f"[{get_timestamp()}] Port: {port} | State: {port_state}\n")

    log_file.write(f"[{get_timestamp()}] Scan completed on {ip_to_scan}\n")

print(f"Scan results saved to {log_file_path}")
