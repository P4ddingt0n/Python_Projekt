RUNNING_CONFIG = "running-config.txt"


def get_trunks():
    trunks = {}
    interface = None

    with open(RUNNING_CONFIG, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith("interface "):
                interface = line.split()[1]

            elif line.startswith("switchport mode trunk") and interface:
                trunks.setdefault(interface, [])

            elif line.startswith("switchport trunk allowed vlan") and interface:
                vlans = line.split()[-1].split(",")
                trunks[interface] = vlans

            elif line.startswith("!"):
                interface = None

    return trunks


trunks = get_trunks()

if trunks:
    print("Trunk configuration found:\n")

    for interface, vlans in trunks.items():
        print(f"Interface: {interface}")
        print(f"Allowed VLANs: {', '.join(vlans) if vlans else 'Not specified'}")
        print()
else:
    print("No trunk ports found in running-config.")