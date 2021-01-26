#define whether the mouse or the arrow keys should be controlled

mouseMode = False

#import dependencies

from Modules.Reader_Utilities import *
from gpiozero import Button
from mouse import click
from pad4pi import rpi_gpio




#initialice pad4pi library

KEYPAD = [	
	#keyboard keys			#real keypad
	["1", "2", "3", "4"],		#[1, 2, 3, "A"]
	["q", "w", "e", "r"],		#[4, 5, 6, "B"]
	["a", "s", "d", "f"],		#[7, 8, 9, "C"]
	["z", "x", "c", "c"],		#["*", 0, "#","D"]
]

ROW_PINS = [6,13,19,26] # BCM numbering
COL_PINS = [12,16,20,21] # BCM numbering


factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

#register a handler to execute when a key is pressed

keypad.registerKeyPressHandler(keyHandler)

#prepare pins to be readed of the data bus

clk = Button(25,pull_up=True)
dat = Button(8, pull_up=True)
syn = Button(7, pull_up=True)

#prepare pins

clk.hold_time = 0
 
#Joystick data read utility


def joyDataread():
	data = ""

	while True:
		if (clk.is_pressed):
			if (dat.is_pressed):
				data = data + "1"
			
			else:
				data = data + "0"
			
		if (syn.is_pressed):
			break
	
	return str(data)


#main infinite loop execution

syn.wait_for_press()

center, axis_x, axis_y, button = False, 0, 0, False

while True:
	
	data = joyDataread()
	center, axis_x, axis_y, button = converttoval(data)
	joyHandler(center, axis_x, axis_y, button)