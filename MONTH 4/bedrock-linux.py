from subprocess import call
from termcolor import cprint
import time
import platform
import sys
from sys import platform as _platform

from colorama import init
init(strip=not sys.stdout.isatty())
from pyfiglet import figlet_format

# For Aesthetics
call('clear', shell=True)

def info():
    print("")
    cprint(figlet_format('BEDROCK  LINUX', font='starwars'),
           'yellow', 'on_red', attrs=['bold'])
    # just script version (python)
    version = ("0.9.1")
    print("")

info()

class bedrock_current_releases:
    x86_64 = ("https://github.com/bedrocklinux/bedrocklinux-userland/releases/download/0.7.10/bedrock-linux-0.7.10-x86_64.sh")

def supported_platform():
    while True:
        Terminal = input("Bedrock >> ")
        user_input = Terminal

        if user_input.lower() == "help":
            def help():
                print("")
                cprint("'help' : Display options and usage.", "green")
                cprint("'install bedrock!' : Installs bedrock linux.", "green")
                cprint("'exit' : Exits the script.", "green")
                cprint("'system info' : Displays the system information.", "green")
                cprint("'website' : Displays the link of official bedrock linux website.", "green")
                print("")

            help()

        elif user_input.lower() == "website":
            def website():
                call('clear', shell=True)
                cprint("https://bedrocklinux.org", "yellow")

            website()

        elif user_input.lower() == "system info":
            def systeminfo():
                call('clear', shell=True)
                cprint("DETECTED SYSTEM INFO:", 'yellow')
                time.sleep(1)
                print("Operating System:", platform.system(), platform.release())
                print("BIT:", sys.platform)
                cprint("Is compatible?: YES", "yellow")
                print("")

            systeminfo()

        elif user_input == "install bedrock!":
            def master_bedrock():
                call('clear', shell=True)
                cprint("Preparing To Install Bedrock...", "magenta")
                time.sleep(3)
                call('clear', shell=True)
                cprint("DETECTED SYSTEM INFO:", 'yellow')
                print("Operating System:", platform.system(), platform.release())
                print("BIT:", sys.platform)
                print("")
                time.sleep(1.3)
                x86_64_script = ("bedrock-linux-0.7.10-x86_64.sh")
                amd64 = bedrock_current_releases()
                call('cd ~', shell=True)
                cprint("Creating Folder to Download and execute script at ~/bedrocklinux", "green")
                call('sudo mkdir bedrocklinux && cd bedrocklinux', shell=True)
                cprint("Downloading Latest Script", "green")
                call(f'wget {amd64.x86_64}', shell=True)
                call(f'sudo sh ./{x86_64_script} --hijack', shell=True)
                cprint("Exiting Python script...", "red")
                sys.exit()

            master_bedrock()

        elif user_input.lower() == "exit":
            sys.exit()

        else:
            print("")
            cprint("Incorrect User Input! Type 'help' to view options and usage.", "red")
            print("")

def startup():
    def platformerrors():
        cprint("DETECTED SYSTEM INFO:", 'yellow')
        print("Operating System:", platform.system(), platform.release())
        print("BIT:", sys.platform)
        cprint("Is compatible?: NO", "yellow")

    while True:
        # Help menu
        unsupported_message = ("This script is not supported on this platform")
        if _platform == "linux" or _platform == "linux2":
            supported_platform()

        elif _platform == "win32" or _platform == "win64":
            platformerrors()
            cprint(unsupported_message, "red")
            break

        elif _platform == "darwin":
            platformerrors()
            cprint(unsupported_message, "red")
            break

        else:
            cprint("Unknown Error!")
            break

startup()
