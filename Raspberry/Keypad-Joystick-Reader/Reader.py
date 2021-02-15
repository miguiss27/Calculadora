#define whether the mouse or the arrow keys should be controlled

mouseMode = False

#define some constants

delay =0.25 # seconds
center = [341, 682] # min, max values of the joystick center
channels = [0, 1, 2] # chanels of the MCP3008 to use as X, Y and button

#import dependencies

from Modules.Reader_Utilities import *
import spidev
from mouse import click
from pad4pi import rpi_gpio
import time

#prepare spi device
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

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


#main infinite loop execution

while True:
	
	processJoystick(spi, mouseMode, center, channels)
	time.sleep(delay)
