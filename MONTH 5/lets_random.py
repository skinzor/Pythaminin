##### RIPPLE ASCIIART SOURCE #####
##### Copyright @RIPPLE TEAM #####
#####    Made By Uniminin    #####

from random import choice
colors = ["\033[95m", "\033[94m", "\033[92m", "\033[93m", "\033[91m"]

color = (choice((colors)))
yellow = ('\033[93m')

def LETS(asciiArt=True):

	if asciiArt:
		print(" (                 (     ", yellow)
		print(" )\\ )        *   ) )\\ )  ", yellow)
		print("(()/(  (   ` )  /((()/(  ", yellow)
		print(" /(_)) )\\   ( )(_))/(_)) ", yellow)
		print("(_))  ((_) (_(_())(_))   ", yellow)
		print("| |   | __||_   _|/ __|  ", color)
		print("| |__ | _|   | |  \\__ \\  ", color)
		print("|____||___|  |_|  |___/  \n", color)

LETS()
