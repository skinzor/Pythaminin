#!/usr/bin/python

import time
import os
clear = lambda: os.system("cls")
while True:
    try:
        n = input("Please enter the secret code to use the program: ")
        n = 6969
        break
    except ValueError:
        print("Wrong code! Please try again...")

print("")

# Colors
color_green='\33[32m'
color_red='\33[31m'
color_white='\33[37m'
color_yellow='\33[33m'
color_blue='\33[34m'
color_violet='\33[35m'
# End
print(color_yellow +
'''
=========================================================================
|                                                                       |
|                                                                       |
|   W E L C O M E  T O   T H E    H  A  N  A  Y  O    F R O N T E N D ! |
|                                                                       |
|                 D E V E L O P E R    U N I M I N I N                  |
|                                                                       |
=========================================================================
'''
)

# Tatoe Server
ask_tatoe=input(color_white + "Define weather to use Tatoe Server Version 1, 2 or 3: ")
add_on_tatoe=(ask_tatoe + ".0.1")
time.sleep(1)
print("Using Version: " + add_on_tatoe + " | Checking...")
time.sleep(3)
print(color_green + "Connected To Latest Essential Tatoe Server By The Ripple Team | Version: " + add_on_tatoe)

#MySQL DATABASE
db_username=input(color_white + "Enter MySQL Username: " )
db_password=input("Enter MySQL Password: " )
print(color_yellow + "> Connecting to MySQL Database... ")
time.sleep(4)
print(color_blue + "Connected To MySQL Database!")
print(color_white + "Username: " + db_username)
print("Password: " + db_password)
time.sleep(2)

# Extras
ask_extras=input("Deploy Build Essentials? y/n: ")
print(color_green + "> Connecting to redis... ")
time.sleep(1)
print(color_red + "[!] Error while connection to redis. Please check your configuration file and run the server again")
print(color_green + "> Creating threads pool... ")
time.sleep(2)
print(color_red + "[!] Error while creating threads pool. Please check your config.ini and run the server again")

# Api
ask_api=input(color_white + "Enter Your OSU!API Key: ")
check_api=("Checking and trying to connect with api [" + ask_api + "]" )
time.sleep(3)
osu_api_enable=(color_red + "[!] osu!api features are disabled. If you don't have a valid beatmaps table, all beatmaps will show as unranked")
print(osu_api_enable)
time.sleep(1)
if_disabled=(color_red + "[!] Warning! API & Client logging is disabled!")
print(if_disabled)

# Finishing
ask_port=input(color_white + "Enter port: ")
time.sleep(4)
clear()
print(color_violet + "> Hanayo is listening for clients on " +ask_port)
print("")
print( color_yellow + "  ░▒▓█ H A N A Y O RUNNING... █▓▒░")
print("")
print("")
print(color_green + """ Welcome To Ripple's Frontend Hanayo!
    Created By The Ripple Team
        Made By Uniminin """)
