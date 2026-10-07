import csv

with open("cvs tabell.cvs", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        vlan = row["vlan"]
        name = row["name"]
        network = row["network"]
        default_router = row["default_router"]

        config = f"""!
vlan {vlan}
 name {name}
!
interface vlan {vlan}
 ip address {default_router} 255.255.255.0
!
"""

        print(config)