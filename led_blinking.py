import RPi.GPIO as GPIO #to interface with Led
import time #import time 
GPIO.setmode(GPIO.BCM) #for BCM interfacing
GPIO.setup(22,GPIO.OUT) #for difine pin 
while True:
    GPIO.output(22,GPIO.HIGH) #for high
    time.sleep(0.5) #time delay
    GPIO.output(22,GPIO.LOW) #for low
    time.sleep(0.5)