import socket
import time
import random

def Fake_Ping():
    while True:
        # Ask For input
        hostname = input("X: > ")
        global_hostname = hostname.lower()
        delete = "ping "
        short_cut = (global_hostname[global_hostname.find(delete)+len(delete):])
        fix = global_hostname.replace('ping ', '')
        if "ping" in global_hostname:
            ip = socket.gethostbyname(short_cut)
            # Extras/Data
            data = int(32)
            ttl = int(54)
            transmission = random.randrange(221, 449)
            received = random.randint(220, 448)
            calc_loss = int(received / transmission * 100)
            loss = int(100 - calc_loss)
            reserved = random.uniform(0.9, 1.4)
            avg = (random.uniform(0.9, 1.4) + random.uniform(0.9, 1.4) / 2)

            statistics = f'Pinging {fix} ({ip}) with {data} bytes of data.'
            print(statistics)

            for icmp_sq in range(1, random.randrange(6, 9)):
                print(f'Reply from  {fix} ({ip}):  icmp_seq={icmp_sq}  ttl={ttl}  time={random.randint(39, 88)}ms')
                time.sleep(reserved)

            print('')
            print(f'--- {fix} ping statistics ---')
            print(f'{transmission} packets transmitted, {received} recieved, {loss}% loss, Average time {int((avg) * 7)}ms ')

        else:
            print("Invalid. Example:ping www.yourdomain.com")

Fake_Ping()
