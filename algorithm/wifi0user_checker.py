import os
ip = "192.168.0."

connected_devices = 0

for ips in range(100, 106 + 1):
    response = os.system("ping -c 1 " + ip + str(ips))

    if response == 0:
        connected_devices += 1

print("Number Of Connected Devices: ", connected_devices)
