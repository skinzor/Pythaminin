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

def SHIP(asciiArt=True):
    try:
        if asciiArt:
            print("{}         _                 __".format(Color))
            print("          (_)              /  /")
            print("   ______ __ ____   ____  /  /____")
            print("  /  ___/  /  _  \\/  _  \\/  /  _  \\")
            print(" /  /  /  /  /_) /  /_) /  /  ____/")
            print("/__/  /__/  .___/  .___/__/ \\_____/")
            print("        /  /   /  /")
            print("       /__/   /__/\r\n")
            print("                          .. o  .")
            print("                         o.o o . o")
            print("                        oo...")
            print("                    __[]__")
            print("             ______/o_o_o_|__       u wot m8? ")
            print("             \\\"\"\"\"\"\"\"\"\"\"\"\"\"\"/")
            print("              \\ . ..  .. . /")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^{}".format(Color))
    except NameError:
        print("")
SHIP()
