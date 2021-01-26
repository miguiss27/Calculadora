#import dependencies

from .Menus import *
from .Utilities import *
from .Flags import processFlags, flagDictionary
from .Cursor import processCursor, updateCursor

#import proccesing libraries

#import matplotlib
#import numpy
#import sympy

#reimport e constant a E to prevent coliding with e from keyboard
from math import *
del e
from math import e as E

#import system utilities
import curses

import subprocess as sub
import sys



#menu proccesing function

def processmenu(key, menu, comand, result, cursor, cursorLimits, flags):
	
	#update cursor position

	cursor = updateCursor("", len(comand), cursor, cursorLimits)
	
	delete = False
	cmd = ""
	mn = 0

	index = cursor[1] + (cursor[0] * cursorLimits[1][1]) - cursor[0]

	if ((key != '') and (key in keys)):
		cmd = menu[keys[key]]
		mn = getMenu(menu)
		
	if ((key != '') and (flags["keyboardMode"])):
#		cmd = key
		mn = getMenu(menu)

	if (cmd == "delete"):
		if (index < len(comand)):
			comand = comand[:(index - 1)] + comand[(index):]
		else:
			comand = comand[:-1]
		cmd = ""
		delete = True
	
	if (cmd == "clear"):
		comand = ""
		result = ""
		cmd = ""

	if (cmd == "clear result"):
		result = ""
		cmd = ""
	
	if (cmd in flagDictionary):
		
		flags = processFlags(cmd, flags)
		if(flagDictionary[cmd] == "tableMode"):
			comand = "createTable("

		cmd = ""
		
	if (cmd == "execute") or ((cmd == "=") and not(flags["verifyMode"])):
		result, flags = executeComand(comand, flags)
		cmd = ""

	if (cmd == "quit"):
		quit()
	
	if (cmd in redirections["menu"]):
		menu = redirections["menu"][cmd]
		cmd = ""

	if ((cmd == "back") and (mn in redirections["back"])):
		menu = redirections["back"][mn]
		cmd = ""
		
	if ((cmd == "next") and (mn in redirections["next"])):
		menu = redirections["next"][mn]
		cmd = ""
		
	if (cmd in menuReplace):
		cmd= menuReplace[cmd]

	if (cmd in externalComands):
		curses.endwin()
	
		sub.run(externalComands[cmd], stdin= sys.stdin, shell=True)
		cmd = ""

	comand = comand[:(index)] + cmd + comand[(index):]

	#update and process cursor position again

	if (delete):
		cmd = "delete"

	cursor = updateCursor(cmd, len(comand), cursor, cursorLimits)

	cursor = processCursor(key, cursor, cursorLimits)


	return menu, comand, result, cursor, cursorLimits, flags


#operation execution helper

def executeComand(comand, flags):

	res= ""

	if (comand in menuReplace):
		comand = execReplace[comand]

	for cmd in execReplace.keys():
		comand = comand.replace(cmd, execReplace[cmd])

	
	if ((flags["tableMode"]) and not(flags["embedded"])):
		flags["embedded"] = True


	try:
		res = eval(comand)
		pass


	except ZeroDivisionError:
		res = "Zero Division Error"
		
	except SyntaxError:
		res = "Syntax Error"
	
	except RecursionError:
		res = "Recursion Error (Limit: " + sys.getrecursionlimit() + ")" 

	except:
		res = "Error"


	return str(res), flags