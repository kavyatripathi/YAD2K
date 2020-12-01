import RPi.GPIO as GPIO
import time
from camera import *
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(50, True)
	p.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.output(50, False)
	p.ChangeDutyCycle(0)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

def steer() :
  try:
    while (Distance<10):
        SetAngle(60)
  except KeyboardInterrupt:
    
    GPIO.cleanup()      

