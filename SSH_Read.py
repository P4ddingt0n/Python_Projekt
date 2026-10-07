with open("running-config.txt", "r") as file:
    config = file.read()

if "ip ssh" in config:
    print("SSH-inställning hittades")
else:
    print("SSH-inställning saknas")

print("ip ssh")