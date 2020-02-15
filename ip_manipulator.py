from ipaddress import ip_network
from config import allowed_ip_range
from config import allowed_ip_range_2

def get_london_ips():
    london_ips = list(ip_network(allowed_ip_range).hosts()) + list(ip_network(allowed_ip_range_2).hosts())
    extracted_ips = []
    for ip in london_ips:
        extracted_ips.append(str(ip))
    return extracted_ips
