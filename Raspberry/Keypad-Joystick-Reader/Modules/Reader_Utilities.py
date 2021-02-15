#import dependencies

import keyboard
import mouse

#key handler

def keyHandler(key):
	keyboard.press_and_release(key)


#Joystick key handler
def processJoystick(spi, mouseMode, center, channels):
	data = []
	
	# gather joystick data
	for channel in channels:
		data.append(readChannel(spi, channel))

	# proccess joystick
	if not(mouseMode):
		if (data[1] > center[1]):
			keyboard.press_and_release("up")

		elif (data[1] < center[0]):
			keyboard.press_and_release("down")
		
		if (data[0] > center[1]):
			keyboard.press_and_release("right")
		
		elif (data[0] < center[0]):
			keyboard.press_and_release("left")
		
		if (data[2] > center[1]):
			keyboard.press_and_release("enter")

	if (mouseMode):
		if (data[0] > center[1]):
			mouse.move(1, 0, absolute=False)

		elif (data[0] < center[0]):
			mouse.move(-1, 0, absolute=False)
		
		if (data[1] > center[1]):
			mouse.move(0, 1, absolute=False)
		
		elif (data[1] < center[0]):
			mouse.move(0, -1, absolute=False)
		
		if (data[2] > center[1]):
			mouse.click()

# Function for reading the MCP3008 channel
def readChannel(spi, channel):
	val = spi.xfer2([1,(8+channel)<<4,0])
	data = ((val[1]&3) << 8) + val[2]
	return data