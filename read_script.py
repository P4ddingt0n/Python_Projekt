import csv
import ipaddress


CSV_FILE = "csv_tabell"


def generate_config(row):
    vlan_id = row["VLAN_ID"]
    vlan_name = row["VLAN_Namn"]
    subnet = ipaddress.ip_network(row["Subnät"])

    # Första användbara IP-adressen används som default gateway
    gateway = next(subnet.hosts())
    netmask = subnet.netmask

    return f"""!
vlan {vlan_id}
 name {vlan_name}
!
interface vlan {vlan_id}
 description {row["Beskrivning"]}
 ip address {gateway} {netmask}
!
"""


with open(CSV_FILE) as file:
    reader = csv.DictReader(file)

    for row in reader:
        
        print(generate_config(row))