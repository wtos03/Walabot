import RPi.GPIO as GPIO
from time import sleep


aPort = 14
dPort = 15

on = GPIO.LOW
off = GPIO.HIGH


GPIO.setmode (GPIO.BCM) 
GPIO.setup (aPort,GPIO.OUT)
GPIO.setup (dPort,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(aPort, off)
GPIO.output(dPort, off)


def TurnOn(dev):
	if dev == "aport":
		GPIO.output(aPort, on)
	if dev == "dport":
		GPIO.output (dPort, on)
	print ('Trigger: Turn On :'+ dev)

def TurnOff(dev):
	if dev == "aport":
		GPIO.output(aPort, off)
	if dev == "dport":
		GPIO.output (dPort, off)
	print ('Trigger : Turn Off :'+ dev)
	
