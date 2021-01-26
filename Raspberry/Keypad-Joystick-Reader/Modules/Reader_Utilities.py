#import dependencies

import keyboard
import mouse
from gpiozero import Button

#data conversion utility
def converttoval(data):
	center, axis_x, axis_y, button = False, 0, 0, False
	if (data == "0000"):
		center = True
	
	if (data == "1000"):
		axis_x, axis_y = -1, -1
	
	if (data == "0100"):
		axis_x, axis_y = -1, 0
	
	if (data == "1100"):
		axis_x, axis_y = -1, 1
	
	if (data == "0010"):
		axis_x, axis_y = 0, 1
	
	if (data == "1010"):
		axis_x, axis_y = 1, 1
	
	if (data == "0110"):
		axis_x, axis_y = 1, 0
	
	if (data == "1110"):
		axis_x, axis_y = 1, -1
	
	if (data == "0001"):
		axis_x, axis_y = 0, -1
		
	if (data == "1001"):
		button = True

	return center, axis_x, axis_y, button

#key handler

def keyHandler(key):
	keyboard.press_and_release(key)


#Joystick key handler
def joyHandler(center, axis_x, axis_y, button, mouseMode):
	if not(mouseMode):
		if (axis_y > 0):
			keyboard.press_and_release("up")

		elif (axis_y < 0):
			keyboard.press_and_release("down")
		
		if (axis_x > 0):
			keyboard.press_and_release("right")
		
		elif (axis_x < 0):
			keyboard.press_and_release("left")
		
		if (button):
			keyboard.press_and_release("enter")

	if (mouseMode):
		if (axis_x > 0):
			mouse.move(1, 0, absolute=False)

		elif (axis_x < 0):
			mouse.move(-1, 0, absolute=False)
		
		if (axis_y > 0):
			mouse.move(0, 1, absolute=False)
		
		elif (axis_y < 0):
			mouse.move(0, -1, absolute=False)
		
		if (button):
			mouse.click()
