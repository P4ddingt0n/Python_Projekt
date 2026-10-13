filnamn = "running-config.txt"

print("--- ANTECKNAR DHCP-POOLER FRÅN CONFIG --- \n")

# Öppna config-filen
with open(filnamn, "r") as fil:
    
    # Loopa igenom varje rad i filen
    for rad in fil:
        # Ta bort extra mellanslag i början och slutet av raden
        rensad_rad = rad.strip()
        
        # --------------------------------------------------
        # REGEL 1: Hitta raden där en ny DHCP-pool startar
        # --------------------------------------------------
        if rensad_rad.startswith("ip dhcp pool"):
            # Dela upp raden på mellanslag och ta det sista ordet (namnet)
            pool_namn = rensad_rad.split()[-1]
            print(f"📌 Hittade DHCP-pool: {pool_namn.upper()}")
            
        # --------------------------------------------------
        # REGEL 2: Hitta nätverksinställningarna för poolen
        # --------------------------------------------------
        elif rensad_rad.startswith("network"):
            # Plocka ut ip och nätmask från raden
            delar = rensad_rad.split()
            ip_natverk = delar[1]
            natmask = delar[2]
            print(f"   ↳ Nätverk: {ip_natverk} med nätmask {natmask}")
            
        # --------------------------------------------------
        # REGEL 3: Hitta routerns gateway (default-router)
        # --------------------------------------------------
        elif rensad_rad.startswith("default-router"):
            # Plocka ut gateway-adressen
            gateway = rensad_rad.split()[1]
            print(f"   ↳ Gateway (Default-Router): {gateway}\n")

print("--- AVSLUTAT ---")