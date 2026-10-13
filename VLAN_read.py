import csv

# Läs VLAN från CSV-filen
with open("vlan_read.py", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        vlan = row["VLAN_ID"]

        # Läs konfigurationsfilen en gång
    with open("running-config.txt", "r") as config_file:
        config = config_file.read()       

    # Läs konfigurationsfilen
        with open("running-config.txt", "r") as config_file:
            config = config_file.read()

        # Kontrollera om VLAN finns i konfigurationen
        if f"vlan {vlan}" in config:
            print(f"VLAN {vlan} finns i konfigurationen")
        else:
            print(f"VLAN {vlan} saknas i konfigurationen")