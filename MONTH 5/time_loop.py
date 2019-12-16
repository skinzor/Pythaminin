import time
timeout = time.time() + 60*2   # 2 minutes from now
while True:
    test = 0
    if test == 2 or time.time() > timeout:
        break
    test = test - 1
