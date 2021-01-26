#import dependencies

from .Constants import *
from math import fabs as abs

#import interface libraries

import curses

#menu print function

def showmenu(window, menu, comand, result, cursor, cursorLimits):

	#gather all data needed to show the menu

	windowHeight, windowWidth = window.getmaxyx()

	lngcmd=len(comand)
	lngres=len(result)

	#prepare the menu sizes

	menuHeight = 0
	menuWidth = 0

	if (((windowHeight - menuVerticalSeparators - (menuFrameMinHeight * 2)) // menuMinHeight) > 0):
		menuHeight = (menuMinHeight * ((windowHeight - menuVerticalSeparators - menuFrameMinHeight * 2) // menuMinHeight)) + menuVerticalSeparators
		
	if (((windowWidth - menuFrameMinWidth) // menuMinWidth) > 0):
		menuWidth = menuMinWidth * ((windowWidth - menuFrameMinWidth * 2) // menuMinWidth)
	
	menuFrameTotalHeight = windowHeight - menuHeight

	menuFrameTotalWidth = windowWidth - menuWidth

	#filling blank space

	for y in range(0, windowHeight):
		window.hline(y, 0, ' ', windowWidth)
		
	#build the menu frame

	for y in range(0, (menuFrameTotalHeight // 2)):
		window.hline(y, 0, '/', windowWidth)

	for x in range(0, (menuFrameTotalWidth // 2)):
		window.vline(0, x, '/', windowHeight)

	for y in range(0, (menuFrameTotalHeight // 2) + (menuFrameTotalHeight % 2)):
		window.hline(((menuFrameTotalHeight // 2) + menuHeight + y), 0, '/', windowWidth)

	for x in range(0, (menuFrameTotalWidth // 2) + (menuFrameTotalWidth % 2)):
		window.vline(0, ((menuFrameTotalWidth // 2) + menuWidth + x), '/', windowHeight)

	#build the menu horizontal lines

	for i in range(0, menuVerticalSeparators):
		window.hline(((menuFrameTotalHeight // 2) + ((windowHeight - menuVerticalSeparators - (menuFrameMinHeight * 2)) // menuMinHeight) + i + (i * ((windowHeight - menuVerticalSeparators - (menuFrameMinHeight * 2)) // menuMinHeight))), (menuFrameTotalWidth // 2), '/', menuWidth)

	#build the menu vertical lines

	window.vline((menuFrameTotalHeight // 2), (menuFrameTotalWidth // 2) + (menuWidth // 2), '/', menuHeight)
	window.vline((menuFrameTotalHeight // 2), (menuFrameTotalWidth // 2) - 1 + (menuWidth // 2), '/', menuHeight)

	window.vline(((menuFrameTotalHeight // 2) + (menuHeight // menuMinHeight)), (menuFrameTotalWidth // 2) - 1 + (menuWidth // 4), '/', menuHeight)
	window.vline(((menuFrameTotalHeight // 2) + (menuHeight // menuMinHeight)), (menuFrameTotalWidth // 2) + menuWidth - (menuWidth // 4), '/', menuHeight)
		
	#insert menu text

	stringSpace = (((menuWidth - menuVerticalSeparators) // 4) - 2)

	if ((((windowHeight - menuVerticalSeparators - (menuFrameMinHeight * 2)) // menuMinHeight) % 2) == 0):
		for y in range(0, menuVerticalSeparators):
			for x in range(1, (menuVerticalSeparators + 1)):

				menuHeigthNumber = ((windowHeight - menuVerticalSeparators - (menuFrameMinHeight * 2)) // menuMinHeight)

				menulng = len(menu[(x - 1) + (4 * y)])

				string = menu[(x - 1) + (4 * y)]

				if (menulng < (stringSpace)) and ((menuHeight > 0) and (menuWidth > 0)):
					window.addstr(((menuFrameTotalHeight // 2) + menuHeigthNumber + y + (menuHeigthNumber // 2) + (y * menuHeigthNumber)), ((menuFrameTotalWidth // 2) - ((x + 1) % 2) + (x // 2) + 2 * (x - 1) + x + ((x - 1) * stringSpace) + (stringSpace // 2) - (menulng // 2)), string)
					
	else:
		for y in range(0, menuVerticalSeparators):
			for x in range(1, (menuVerticalSeparators + 1)):

				menuHeigthNumber = ((windowHeight - menuVerticalSeparators - (menuFrameMinHeight * 2)) // menuMinHeight)

				menulng = len(menu[(x - 1) + (4 * y)])

				string = menu[(x - 1) + (4 * y)]

				if (menulng < (stringSpace)) and ((menuHeight > 0) and (menuWidth > 0)):
					window.addstr(((menuFrameTotalHeight // 2) + menuHeigthNumber + y + (menuHeigthNumber // 2) + (y * menuHeigthNumber) + 1), ((menuFrameTotalWidth // 2) - ((x + 1) % 2) + (x // 2) + 2 * (x - 1) + x + ((x - 1) * stringSpace) + (stringSpace // 2) - (menulng // 2)), string)




	#insert menu comand

	if ((menuHeight > 0) and (menuWidth > 0)):
		for i in range(0, ((menuHeight - menuVerticalSeparators) // menuMinHeight)):
			window.addstr(((menuFrameTotalHeight // 2) + i), ((menuFrameTotalWidth // 2) + 1), comand[(i * ((menuWidth // 2) - 2) - i):(((i + 1) * ((menuWidth // 2) - 2)) - 1 - i)])
			
			#print cursor in comand
			try:
				window.chgat(((menuFrameTotalHeight // 2) + cursor[0]), ((menuFrameTotalWidth // 2) + cursor[1]),1, curses.A_UNDERLINE)
			except:
				pass



	#insert menu result

	if ((menuHeight > 0) and (menuWidth > 0)):
		for i in range(0, ((menuHeight - menuVerticalSeparators) // menuMinHeight)):
			window.addstr((menuFrameTotalHeight // 2) + i, ((menuFrameTotalWidth // 2) + (menuWidth // 2) + 2), result[(i * ((menuWidth // 2) - 2) - i):(((i + 1) * ((menuWidth // 2) - 2)) - 1 - i)])
	
	#update cursor limits

	cursorLimits[0][0] = -1
	cursorLimits[0][1] = 0

	#update cursor y max limits

	cursorLimits[1][0] = ((menuHeight - menuVerticalSeparators) // menuMinHeight)
	
	#update cursor x max limits

	cursorLimits[1][1] = (menuWidth // 2) - 2


	#refresh the monitor

	window.refresh()

	return cursorLimits



#embedded menu helper(for tables, graphics...) 

def embedMenu(window, menu, cursor, cursorLimits):

	#gather all data needed to show the frame

	windowHeight, windowWidth = window.getmaxyx()


	#prepare the menu sizes


	menuHeight = 0
	menuWidth = 0

	if (((windowHeight - menuVerticalSeparators - (menuFrameMinHeight * 2)) // menuMinHeight) > 0):
		menuHeight = (menuMinHeight * ((windowHeight - menuVerticalSeparators - menuFrameMinHeight * 2) // menuMinHeight)) + menuVerticalSeparators
		
	if (((windowWidth - menuFrameMinWidth) // menuMinWidth) > 0):
		menuWidth = menuMinWidth * ((windowWidth - menuFrameMinWidth * 2) // menuMinWidth)
	
	menuFrameTotalHeight = windowHeight - menuHeight

	menuFrameTotalWidth = windowWidth - menuWidth

	#filling blank space

	for y in range(0, windowHeight):
		window.hline(y, 0, ' ', windowWidth)
		
	#build the menu frame

	for y in range(0, (menuFrameTotalHeight // 2)):
		window.hline(y, 0, '/', windowWidth)

	for x in range(0, (menuFrameTotalWidth // 2)):
		window.vline(0, x, '/', windowHeight)

	for y in range(0, (menuFrameTotalHeight // 2) + (menuFrameTotalHeight % 2)):
		window.hline(((menuFrameTotalHeight // 2) + menuHeight + y), 0, '/', windowWidth)

	for x in range(0, (menuFrameTotalWidth // 2) + (menuFrameTotalWidth % 2)):
		window.vline(0, ((menuFrameTotalWidth // 2) + menuWidth + x), '/', windowHeight)


	#segment menu

	menuArr = menu.split("\n")

	#create a curses window as the menu space (only if menu space exist)

	if ((menuHeight > 0) and (menuWidth > 0)):
		menuWindow = window.derwin(menuHeight, menuWidth, (menuFrameTotalHeight // 2), (menuFrameTotalWidth // 2))
		
		#insert menu in new window
		
		for y in range(cursor[0],(menuHeight + cursor[0])):
			try:
				menuWindow.addnstr((y - cursor[0]), cursor[1], menuArr[(y)], (menuWidth - cursor[1]))
			except:
				pass
		
	#update cursor min limits

	cursorLimits[0][0] = -1
	cursorLimits[0][1] = -1

	#update cursor y max limits

	if (menuHeight > len(menuArr)):
		cursorLimits[1][0] = (menuHeight - len(menuArr)) + 1

	elif (menuHeight < len(menuArr)):
		cursorLimits[1][0] = (len(menuArr) - menuHeight) + 1
	
	else:
		cursorLimits[1][0] = 1
	
	#update cursor x max limits

	if (menuWidth > len(menuArr[0])):
		cursorLimits[1][1] = (menuWidth - len(menuArr[0])) + 1

	elif (menuHeight < len(menuArr)):
		cursorLimits[1][1] = (len(menuArr[0]) - menuWidth) + 1
	
	else:
		cursorLimits[1][1] = 1



	#refresh the monitor

	window.refresh()


	return cursorLimits