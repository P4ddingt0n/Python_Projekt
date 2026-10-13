RUNNING_CONFIG = "test_config.txt"

def get_existing_vlans():
    vlans = set()

    with open(RUNNING_CONFIG, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith("interface Vlan"):
                vlans.add(line.split("Vlan")[1])
    return vlans


vlans = get_existing_vlans()

if vlans:
    print("VLANs found in running-config:\n")

    for vlan_id in sorted(vlans, key=int):
        print(f"VLAN {vlan_id}")
else:
    print("No VLANs found in running-config.")