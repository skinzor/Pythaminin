from getpass import getpass as user_input
from termcolor import cprint
import configparser

# Config
config = configparser.ConfigParser()
config.sections()
config.read("passwords.txt")

translation = str.maketrans({
    '0': 'x',
    '1': 'g',
    '2': 'e',
    '3': 'f',
    '4': 'q',
    '5': 'k',
    '6': 'l',
    '7': 'z',
    '8': 'b',
    '9': 'w'
})

user = input("Enter Username: ")
while 1:
    password = user_input("Enter Password to hash: ")
    if len(password) >= 6:
        cprint("Hashing your password...", "green")
        password = password.translate(translation)
        info = (f"[{user}]\nPassword: {password}\n\n")
        file = open('passwords.txt', 'a')
        file.write(info)
        file.close()
        break
    cprint("Password too Weak! Try Again and make sure it contains atleast 6 characters.", "red")

