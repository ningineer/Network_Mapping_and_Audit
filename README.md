# Network Mapping and Security Audit Project

This project provides a basic network mapping and security audit tool using nmap in Python. It performs an IP scan within a specified range to map active hosts and open ports, displaying useful information for security audits and network monitoring.

# ⚠️ Disclaimer
This project is intended solely for educational and testing purposes on authorized networks. Unauthorized network scanning is illegal and against ethical guidelines. Ensure you have permission before scanning any network.

## Project Overview
  - Technology Used: Python, nmap (network mapping tool)
  - Purpose: Conduct a network scan to detect active hosts, their open ports, and the services they offer.
  - Output: Results are stored in a log file with timestamps for easy tracking and audit records.

## Requirements
  - Python 3.x
  - nmap library: Install using pip3 install python-nmap

## Setup and Installation

## 1. Clone this Repository
      
      git clone <URL_of_this_repository><br/>
      cd Network_Mapping_and_Audit

## 2. Install Required Libraries
Ensure the python-nmap package is installed:<br/>
      
      pip3 install python-nmap

## 3. Configure Script
Edit network_mapping_audit.py to specify the IP address or range you wish to scan:

    ip_to_scan = "192.168.1.0/24"  # Adjust this to your target IP or range

## Usage
To start the scan, run the script from the command line:

    python3 network_mapping_audit.py

The script will automatically generate a timestamped log file in the logs directory, capturing the network mapping results.

## Sample Output
The output log file includes entries for each host scanned, along with detailed port information:

    [2024-11-07 10:45:01] Starting scan on 192.168.1.0/24
    [2024-11-07 10:45:10] Host: 192.168.1.10 (device-name)
    [2024-11-07 10:45:10] State: up
    [2024-11-07 10:45:10] Protocol: tcp
    [2024-11-07 10:45:10] Port: 22 | State: open...
    [2024-11-07 10:55:30] Scan completed on 192.168.1.0/24

## Key Features
  - Network Mapping: Identifies live hosts on the network.
  - Port Scanning: Detects open ports and their states.
  - Timestamped Logs: Logs are stored with timestamps for tracking scan history.

## Future Enhancements
  - Automated Reporting: Generate summary reports.
  - Additional Protocols: Expand support for UDP and other protocols.
