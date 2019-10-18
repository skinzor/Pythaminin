import time

try:
    print("Counting for 5 seconds")
    for countdown in range(1, 6):
        print(f"{countdown} seconds")
        time.sleep(1)

except KeyboardInterrupt:
    print('You cancelled the operation.')
