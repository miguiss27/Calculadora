#import dependencies

from time import sleep
from Modules.Interface import *
from Modules.Menu_processing import *
from Modules.Utilities import *
from Modules.Menus import *
from Modules.Constants import *
from Modules.Tables import *
import Modules.Flags

#main program

def main(window):

	#configuration
	curses.curs_set(visibility)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

	window.clear()
	window.nodelay(nodelay)

	#default values
	menu = menu0
	comand = ''
	result = ''
	key = ''

	flags = Modules.Flags.flags

	cursor = [0,1]
	cursorLimits = [[-1, 0],[3,34]]
	showcursor = True
	lastBlink = 0

	while True:	
		menu, comand, result, cursor, cursorLimits, flags = processmenu(key, menu, comand, result, cursor, cursorLimits, flags)

		#result = str(flags)

		if (flags["embedded"]):
			cursorLimits = embedMenu(window, result, cursor, cursorLimits)

		else:
			cursorLimits = showmenu(window, menu, comand, result, cursor, cursorLimits, showcursor)

		key = str(keyread(window))

		sleep(timeSleep) #help with overloading processor

		#blink cursor
		showcursor, lastBlink = changeinterval(showcursor, not showcursor, blinkinterval, lastBlink)




	
	
#main program execution(In safe mode for any errors)

curses.wrapper(main)
