import threading
from time import sleep


def mp3Player():
    while True:
        print("Alright")
        sleep(1.5)


def mp3Player2():
    while True:
        print("Alright6")
        sleep(1.4)


a = threading.Thread(target=mp3Player2)
t = threading.Thread(target=mp3Player)
t.start()
a.start()
while True:
    print("u wot m8?")
    sleep(1.2)
