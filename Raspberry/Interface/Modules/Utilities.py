#import dependencies

from .Menus import *
from curses import ascii, ERR, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
from decimal import Decimal
from time import time

#keypresses helper

def keyread(window):
	character = ''
	asciiCharacter = window.getch()
	if (asciiCharacter != ERR):
		character = ascii.unctrl(asciiCharacter)
	
		if (character.find('^') != -1):
			character = ''

		if (asciiCharacter == KEY_UP):
			character = "KEY_UP"

		if (asciiCharacter == KEY_DOWN):
			character = "KEY_DOWN"

		if (asciiCharacter == KEY_LEFT):
			character = "KEY_LEFT"

		if (asciiCharacter == KEY_RIGHT):
			character = "KEY_RIGHT"

	return str(character)

#menu utility

def getMenu(val):
	for key, value in menuDict.items():
		if val == value:
			return key

#float range utility

def frange(start=0.0, stop=1.0, step=1.0):
	rangeStep = float(step)

	rangeStart = float(start)
	rangeStop = float(stop) + rangeStep

	#detect precission from step
	strStep = str(step)
	rangePrecision = abs(Decimal(strStep).as_tuple().exponent)

	count = float(0)
	while True:
		temp = rangeStart + count * rangeStep
		if rangeStep > 0 and temp >= rangeStop:
			break
		elif rangeStep < 0 and temp <= rangeStop:
			break
		yield round(temp, rangePrecision)
		count += 1


def changeinterval(val, newval, interval, lastchange):

	precission = abs(Decimal(str(interval)).as_tuple().exponent)
	
	currentime = int(time() * (10 ** precission))

	change = (currentime - lastchange) >= int((interval * (10 ** precission)))

	if (change):
		return newval, currentime

	return val, lastchange
