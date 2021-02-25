#import dependencies

import keyboard
import mouse
from time import sleep

#key handler

def keyHandler(key):
	keyboard.press(key)
	sleep(0.05)
	keyboard.release(key)

#Joystick key handler

def processJoystick(spi, mouseMode, center, channels):
	data = []
	
	# gather joystick data
	for channel in channels:
		data.append(readChannel(spi, channel))

	# proccess joystick
	if not(mouseMode):
		if (data[0] < center[0]):
			keyboard.press("up")
		else:
			keyboard.release("up")


		if (data[0] > center[1]):
			keyboard.press("down")
		else:
			keyboard.release("down")
		

		if (data[1] < center[0]):
			keyboard.press("right")
		else:
			keyboard.release("right")
		

		if (data[1] > center[1]):
			keyboard.press("left")
		else:
			keyboard.release("left")
		

		if (data[2] > center[1]):
			keyboard.press("enter")
		else:
			keyboard.release("enter")


	if (mouseMode):
		if (data[1] < center[0]):
			mouse.move(1, 0, absolute=False)


		elif (data[1] > center[1]):
			mouse.move(-1, 0, absolute=False)
		

		if (data[0] < center[0]):
			mouse.move(0, 1, absolute=False)
		

		elif (data[0] > center[1]):
			mouse.move(0, -1, absolute=False)
		

		if (data[2] > center[1]):
			mouse.click()

# Function for reading the MCP3008 channel
def readChannel(spi, channel):
	val = spi.xfer2([1,(8+channel)<<4,0])
	data = ((val[1]&3) << 8) + val[2]
	return data
