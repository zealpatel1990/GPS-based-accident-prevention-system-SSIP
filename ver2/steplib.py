from time import sleep
import RPi.GPIO as gpio
class stepper:
	def __init__(self, pins):
		self.pins = pins
		self.stepPin = self.pins[0]
		self.directionPin = self.pins[1]
		self.enablePin = self.pins[2]
		gpio.setmode(gpio.BOARD)
		gpio.setup(self.stepPin, gpio.OUT)
		gpio.setup(self.directionPin, gpio.OUT)
		gpio.setup(self.enablePin, gpio.OUT)
		gpio.output(self.enablePin, True)
	
	def cleanGPIO(self):
		gpio.cleanup()
	
	def step(self, steps, dir, speed=1, stayOn=False):
		gpio.output(self.enablePin, False)
		turnLeft = True
		if (dir == 'r'):
			turnLeft = False;
		elif (dir != 'l'):
			print("STEPPER ERROR: no direction supplied")
			return False
		gpio.output(self.directionPin, turnLeft)

		stepCounter = 0
		waitTime = 0.005

		while stepCounter < steps:
			gpio.output(self.stepPin, True)
			sleep(0.0001)
			gpio.output(self.stepPin, False)
			stepCounter += 1
			sleep(waitTime)
		
		if (stayOn == False):
			gpio.output(self.enablePin, True)

		print("stepperDriver complete (turned " + dir + " " + str(steps) + " steps)")
	gpio.cleanup()		
"""
my calculations: 1.25mm per revolution
16rps  2cm(linear motion)  3200steps/s-- time diff bet step=0.0003125
8rps   1cm(linear motion)  1600steps/s-- time diff bet step=0.000625
4rps  0.5cm(linear motion)  800steps/s-- time diff bet step=0.00125
2rps   0.25cm(linear motion)  400steps/s-- time diff bet step=0.0025
 """
