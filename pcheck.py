#!/usr/bin/env python3

import requests
import json
import readline  # or import pyreadline for windows
import getpass
import os
import ipaddress
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
from colorama import Fore, Style

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Assign the environment variables to the api_key and abuse_key variables here
api_key = os.getenv('API_KEY')
abuse_key = os.getenv('ABUSE_KEY')

ascii_art = r"""
            _               _    
 _ __   ___| |__   ___  ___| | __
| '_ \ / __| '_ \ / _ \/ __| |/ /
| |_) | (__| | | |  __/ (__|   < 
| .__/ \___|_| |_|\___|\___|_|\_\\
|_|                              
"""

description = """Your Personal Guard Against IP Masqueraders.
Retrieves information about the IP including whether it's a proxy, VPN, its ASN and node information.
\
It will also output abuse information via AbuseIPB.
\n
If there are multiple IPs, separate by comma.
\n
exit -- exits the tool
"""

def validate_ip(ip_input):
  ip_addresses = ip_input.split(',')
  for ip in ip_addresses:
    try:
      ipaddress.ip_address(ip)
    except ValueError as e:
      print(f"Invalid IP address: {e}")
      return False
  return True

def check_ips(api_key, ip_addresses):
  for ip_address in ip_addresses:
    ip = ipaddress.ip_address(ip_address.strip())
    if ip.is_private:
      print(f"{ip_address} is a private IP address, and is only used in internal network environments.")
      continue

    response = requests.get(f'https://proxycheck.io/v2/{ip_address}?key={api_key}&vpn=1&asn=1&node=1', verify=False)
    data = response.json()
    output_data = {}

    # Check for the presence of each key before adding it to the output_data dictionary
    if 'status' in data[ip_address]: output_data['status'] = data[ip_address]['status']
    if 'node' in data[ip_address]: output_data['node'] = data[ip_address]['node']
    if 'asn' in data[ip_address]: output_data['asn'] = data[ip_address]['asn']
    if 'range' in data[ip_address]: output_data['range'] = data[ip_address]['range']
    if 'hostname' in data[ip_address]: output_data['hostname'] = data[ip_address]['hostname']
    if 'provider' in data[ip_address]: output_data['provider'] = data[ip_address]['provider']
    if 'organization' in data[ip_address]: output_data['organization'] = data[ip_address]['organization']
    if 'continent' in data[ip_address]: output_data['continent'] = data[ip_address]['continent']
    if 'country' in data[ip_address]: output_data['country'] = data[ip_address]['country']
    if 'continent code' in data[ip_address]: output_data['continent code'] = data[ip_address]['continent code']
    if 'region' in data[ip_address]: output_data['region'] = data[ip_address]['region']
    if 'city' in data[ip_address]: output_data['city'] = data[ip_address]['city']
    if 'proxy' in data[ip_address]: output_data['proxy'] = data[ip_address]['proxy']
    if 'type' in data[ip_address]: output_data['type'] = data[ip_address]['type']

    print("    IP Address: ", ip_address)
    print(highlight(json.dumps(output_data, indent=4), JsonLexer(), TerminalFormatter()))

    # Add this code to access the AbuseIPDB API
    abuse_response = requests.get(f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}&maxAgeInDays=365', headers={'Key': abuse_key}, verify=False)
    abuse_data = abuse_response.json()

    try:
      abuse_data_filtered = {
        'totalReports': abuse_data['data'].get('totalReports'),
        'lastReportedAt': abuse_data['data'].get('lastReportedAt'),
        'reference': f'https://www.abuseipdb.com/check/{ip_address}'
      }
    except KeyError:
      print("Unexpected API response: 'data' key not found.")
      continue

    abuse_data_filtered = {k: v for k, v in abuse_data_filtered.items() if v is not None}

    print("    " + Fore.RED + "Abuse Information (via AbuseIPDB): " + Style.RESET_ALL)
    print(highlight(json.dumps(abuse_data_filtered, indent=4), JsonLexer(), TerminalFormatter()))

print(ascii_art)
print(Fore.CYAN + description + Style.RESET_ALL)

def sanitize_ip(ip):
  return ip.strip()

while True:
  ip_input = input("    Please enter an IP address: ").strip().lower().replace(' ', '')
  print()

  if ip_input == 'exit':
    print("Exiting...")
    break

  # Sanitize the IP address
  ip_input = sanitize_ip(ip_input)

  if not validate_ip(ip_input):
    print(Fore.RED + "Invalid IP address." + Style.RESET_ALL)
    print()
    continue
  print()  # create an additional line break
  if ip_input == 'exit':
    print("Exiting...")
    break
  ip_addresses = ip_input.split(',')
  check_ips(api_key, ip_addresses)
  more_ips = getpass.getpass("More IPs to query? (y/n) ")
  if more_ips.lower() != 'y':
    print("Exiting...")
    break
