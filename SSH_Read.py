with open("running-config.txt", "r") as file:
    config = file.read()

ssh_found = False

for line in config.splitlines():
    if "ip ssh" in line.lower():
        ssh_found = True
        break

if ssh_found:
    print("IP SSH-inställning hittades")
else:
    print("IP SSH-inställning saknas")