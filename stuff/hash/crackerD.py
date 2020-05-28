from termcolor import cprint
import configparser

# Config
config = configparser.ConfigParser()
config.sections()
config.read("passwords.txt")

translation = str.maketrans({
    'x': '0',
    'g': '1',
    'e': '2',
    'f': '3',
    'q': '4',
    'k': '5',
    'l': '6',
    'z': '7',
    'b': '8',
    'w': '9'
})

while 1:
    cprint("1. Hash from File\n2. Manual Hash", "green")
    choice = input("Choice: ")
    if choice == "1":
        user = input("Username: ")
        if user in config:
            hashed = config[user]['Password'].translate(translation)
            cprint(f"Encrypted Result: {hashed}", "green")
            break
        else:
            cprint("Unable to Encrypt. User Not Found!", "red")
            break
    elif choice == "2":
        h_hash = input("Hash: ")
        h_hash = h_hash.translate(translation)
        cprint(f"Encypted Result: {h_hash}")
        break
    else:
        cprint("Incorrect Input. Try again.", "red")
