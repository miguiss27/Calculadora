#cursor management helper

import curses


def processCursor(key, cursor, cursorLimits):

	#prepare y and x range in which the cursor must be
	yRange = []
	xRange = []
	
	#genetate y and x range in which the cursor must be
	for y in range((cursorLimits[0][0] + 1), cursorLimits[1][0]):
		yRange.append(y)
	
	for x in range((cursorLimits[0][1] + 1), cursorLimits[1][1]):
		xRange.append(x)


	if (key == "KEY_UP") and (cursor[0] in yRange):
		cursor[0] += 1
	
	elif (not(cursor[0] in yRange)):
		cursor[0] = yRange[-1]
	
	if (key == "KEY_DOWN") and (cursor[0] in yRange):
		cursor[0] -= 1
	
	elif (not(cursor[0] in yRange)):
		cursor[0] = yRange[0]
	
	if (key == "KEY_LEFT") and (cursor[1] in xRange):
		cursor[1] -= 1
	
	elif (not(cursor[1] in xRange)):
		cursor[1] = xRange[-1]
	
	if (key == "KEY_RIGHT") and (cursor[1] in xRange):
		cursor[1] += 1
	
	elif (not(cursor[1] in xRange)):
		cursor[1] = xRange[0]
	

	return cursor

def updateCursor(cmd, lenCMD, cursor, cursorLimits):

	if (cmd != ""):

		if (cmd == "delete"):
			cursor[0] = 0

		if ((lenCMD > 0) and (lenCMD < cursorLimits[1][1])):
				cursor[1] = lenCMD


		for y in range(0, (cursorLimits[1][0] - cursorLimits[0][0])):
			lenCMD -= cursorLimits[1][1] - cursorLimits[0][1] - 1

			if ((lenCMD > 0) and (lenCMD <= (cursorLimits[1][1] - cursorLimits[0][1] - 1))):

				cursor[0] = y + 1
				cursor[1] = 1

				if (lenCMD != 0):
					cursor[1] = lenCMD
				
				break			

	return cursor