from time import sleep
n = 10 # 10 seconds from now
while True:
    sleep(1)
    n -= 1
    if n == 0:
        exit()

        
