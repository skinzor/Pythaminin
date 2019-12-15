##### RIPPLE ASCIIART SOURCE #####
##### Copyright @RIPPLE TEAM #####
#####    Made By Uniminin    #####

user_choice = input("Which Color Would you like? ")
if user_choice.lower() == "red":
    color = "\033[91m"
elif user_choice.lower() == "blue":
    color = "\033[94m"
elif user_choice.lower() == "pink":
    color = "\033[95m"
elif user_choice.lower() == "green":
    color = "\033[92m"
elif user_choice.lower() == "yellow":
    color = "\033[93m"
elif user_choice.lower() == "bold":
    color = "\033[1m"
elif user_choice.lower() == "endc":
    color = "\033[0m"
elif user_choice.lower() == "underline":
    color = "\033[4m"
else:
    print("""Choose Among the Following Ones:
    1. Red
    2. Blue
    3. Pink
    4. Green
    5. Yellow
    6. Bold
    7. Endc
    8. Underline""")

try:
    Color = color
except NameError:
    print("")

yellow = ('\033[93m')
def SHIP(asciiArt=True):
    try:
        if asciiArt:
            print(" (                 (     ", yellow)
            print(" )\\ )        *   ) )\\ )  ", yellow)
            print("(()/(  (   ` )  /((()/(  ", yellow)
            print(" /(_)) )\\   ( )(_))/(_)) ", yellow)
            print("(_))  ((_) (_(_())(_))   ", yellow)
            print("| |   | __||_   _|/ __|  ", Color)
            print("| |__ | _|   | |  \\__ \\  ", Color)
            print("|____||___|  |_|  |___/  \n", Color)
    except NameError:
        print("")
SHIP()
