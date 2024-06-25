
import requests
import json
import readline  # or import pyreadline for windows
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
from colorama import Fore, Style

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ascii_art = r"""
            _               _    
 _ __   ___| |__   ___  ___| | __
| '_ \ / __| '_ \ / _ \/ __| |/ /
| |_) | (__| | | |  __/ (__|   < 
| .__/ \___|_| |_|\___|\___|_|\_\\
|_|                              
"""

description = """Your Personal Guard Against IP Masqueraders.
Retrieves information about the IP including whether it's a proxy, VPN, its ASN and node information.
"""

def check_ips(api_key, ip_addresses):
    for ip_address in ip_addresses:
        response = requests.get(f'https://proxycheck.io/v2/{ip_address}?key={api_key}&vpn=1&asn=1&node=1', verify=False)
        data = response.json()
        if 'proxy' in data[ip_address]:
            print('Proxy: ' + data[ip_address]['proxy'])
        if 'type' in data[ip_address]:
            print('Type: ' + data[ip_address]['type'])
        print(highlight(json.dumps(data, indent=4), JsonLexer(), TerminalFormatter()))

print(ascii_art)
print(Fore.CYAN + description + Style.RESET_ALL)

api_key = '716550-605120-904905-941c40'
ip_addresses = input("Please enter an IP addresses. If there are multiple IPs, separate by comma: ").strip().split(',')
check_ips(api_key, ip_addresses)
