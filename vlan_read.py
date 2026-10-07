import csv

# Läs CSV-filen
with open("cvs_tabell", "r") as file:
    reader = csv.DictReader(file)

    # Läs running-config en gång
    with open("running-config.txt", "r") as config_file:
        config = config_file.read()

    # Gå igenom VLAN från CSV
    for row in reader:
        vlan = row["VLAN_ID"]

        # Kontrollera om VLAN finns
        if f"vlan {vlan}" in config:
            print(f"VLAN {vlan} finns i konfigurationen")
        else:
            print(f"VLAN {vlan} saknas i konfigurationen")