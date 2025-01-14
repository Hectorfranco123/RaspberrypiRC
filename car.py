from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=6, trigger = 5)
#while True:
#		print(ultrasonic.distance)
import RPi.GPIO as gpio
import time

def init():
		gpio.setmode(gpio.BCM)
		gpio.setup(17, gpio.OUT)
		gpio.setup(22, gpio.OUT)
		gpio.setup(23, gpio.OUT)
		gpio.setup(24, gpio.OUT) 

def forward(sec):
	init()
	gpio.output(17, True)
	gpio.output(22, False)
	gpio.output(23, False)
	gpio.output(24,	True)
	time.sleep(sec)
	gpio.cleanup()
	
def reverse(sec):
	init()
	gpio.output(17, False)
	gpio.output(22, True)
	gpio.output(23, True)
	gpio.output(24, False)
	time.sleep(sec)
	gpio.cleanup()
	
def left_turn(sec):
	init()
	gpio.output(17, True)
	gpio.output(22, False)
	gpio.output(23, True)
	gpio.output(24, False)
	time.sleep(sec)
	gpio.cleanup()
	
def right_turn(sec):
	init()
	gpio.output(17, False)
	gpio.output(22, True)
	gpio.output(23, False)
	gpio.output(24, True)
	time.sleep(sec)
	gpio.cleanup()
	
seconds = 3

#time.sleep(seconds)
#print("forward")
#forward(seconds)
#time.sleep(seconds-2)

#print("right")
#right_turn(seconds)
#time.sleep(seconds-2)

#time.sleep(seconds)
#print("forward")
#forward(seconds)
#time.sleep(seconds-2)

#print("right")
#right_turn(seconds)
#time.sleep(seconds-2)
time.sleep(15)

while True:
	while ultrasonic.distance > .5:
		print("forward")
		forward(1)
		if ultrasonic.distance < .1:
			print("reverse")
			reverse(2)
			break
	
	print("turning")
	right_turn(3) 
