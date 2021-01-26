#/usr/bin/python3
import os
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import CPUTemperature

fileDir = os.path.dirname(__file__)

min_temp = open('%s/min_temp' % fileDir, "r")
max_temp = open('%s/max_temp' % fileDir , "r")

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
cpu = CPUTemperature()

while True:
	
	temp = int(cpu.temperature)

	print(temp)

	act = int(min_temp.read(2))
	max = int(max_temp.read(2))

	min_temp.seek(0)
	max_temp.seek(0)
	
	if (temp >= act) and (temp >= max):

		GPIO.output(17, GPIO.LOW)
		GPIO.output(27, GPIO.LOW)
		sleep(60)

	if (temp >= act) and (temp <= max):

		GPIO.output(17, GPIO.LOW)
		GPIO.output(27, GPIO.HIGH)
		sleep(30)

	if (temp <= act) and (temp <= max):

		GPIO.output(17, GPIO.HIGH)
		GPIO.output(27, GPIO.HIGH)
		sleep(15)
