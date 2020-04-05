from pynput.keyboard import Controller
from time import sleep

keyboard = Controller()


def main():
    chars = input('Characters:~ ')
    sleep(1)
    for characters in chars:
        keyboard.press(characters)
        keyboard.release(characters)
        sleep(0.1)


main()
