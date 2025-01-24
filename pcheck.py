#!/usr/bin/env python3

import requests
import json
import readline  # or import pyreadline for windows
import getpass
import os
import ipaddress
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import Fore, Style

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Assign the environment variable to the api_key variable here
api_key = os.getenv('API_KEY')

ascii_art = r"""
                        _                          _  
     _ __   ___| |__   ___   ___| | __
    | '_ \ / __| '_ \ / _ \/ __| |/ /
    | |_) | (__| | | |  __/ (__|   < 
    | .__/ \___|_| |_|\___|\___|_|\_\
    |_|                                
"""

description = """Your Personal Guard Against IP Masqueraders.
Retrieves information about the IP including whether it's a proxy, VPN, its ASN and node information.

If there are multiple IPs, separate by comma.

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
            print(
                f"{ip_address} is a private IP address, and is only used in internal network environments."
            )
            continue

        response = requests.get(
            f'https://proxycheck.io/v2/{ip_address}?key={api_key}&vpn=1&asn=1&node=1',
            verify=False)
        data = response.json()

        print(f"  IP Address: {ip_address}")
        print("-" * 30)  # Separator for better readability

        if 'status' in data[ip_address]:
            print(Fore.YELLOW + "  Status: " + Style.RESET_ALL +
                  f"{data[ip_address]['status']}")
        if 'node' in data[ip_address]:
            print(Fore.YELLOW + "  Node: " + Style.RESET_ALL +
                  f"{data[ip_address]['node']}")
        if 'asn' in data[ip_address]:
            print(Fore.YELLOW + "  ASN: " + Style.RESET_ALL +
                  f"{data[ip_address]['asn']}")
        if 'range' in data[ip_address]:
            print(Fore.YELLOW + "  Range: " + Style.RESET_ALL +
                  f"{data[ip_address]['range']}")
        if 'hostname' in data[ip_address]:
            print(Fore.YELLOW + "  Hostname: " + Style.RESET_ALL +
                  f"{data[ip_address]['hostname']}")
        if 'provider' in data[ip_address]:
            print(Fore.YELLOW + "  Provider: " + Style.RESET_ALL +
                  f"{data[ip_address]['provider']}")
        if 'organization' in data[ip_address]:
            print(Fore.YELLOW + "  Organization: " + Style.RESET_ALL +
                  f"{data[ip_address]['organization']}")
        if 'continent' in data[ip_address]:
            print(Fore.YELLOW + "  Continent: " + Style.RESET_ALL +
                  f"{data[ip_address]['continent']}")
        if 'country' in data[ip_address]:
            print(Fore.YELLOW + "  Country: " + Style.RESET_ALL +
                  f"{data[ip_address]['country']}")
        if 'continent code' in data[ip_address]:
            print(Fore.YELLOW + "  Continent Code: " + Style.RESET_ALL +
                  f"{data[ip_address]['continent code']}")
        if 'region' in data[ip_address]:
            print(Fore.YELLOW + "  Region: " + Style.RESET_ALL +
                  f"{data[ip_address]['region']}")
        if 'city' in data[ip_address]:
            print(Fore.YELLOW + "  City: " + Style.RESET_ALL +
                  f"{data[ip_address]['city']}")
        if 'proxy' in data[ip_address]:
            print(Fore.YELLOW + "  Proxy: " + Style.RESET_ALL +
                  f"{data[ip_address]['proxy']}")
        if 'type' in data[ip_address]:
            print(Fore.YELLOW + "  Type: " + Style.RESET_ALL +
                  f"{data[ip_address]['type']}")

        print("-" * 30)
        print()  # Add an extra newline for clarity


print(ascii_art)
print(Fore.CYAN + description + Style.RESET_ALL)


def sanitize_ip(ip):
    return ip.strip()


while True:
    ip_input = input("   Please enter an IP address: ").strip().lower().replace(
        ' ', '')
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
